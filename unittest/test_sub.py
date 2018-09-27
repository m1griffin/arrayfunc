#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_sub.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      19-Jun-2018.
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
"""This conducts unit tests for sub.
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
class sub_general_b(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data -2,-1,0,1,2.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_b(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('b', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('b', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code b.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_b(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('b', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('b', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code b.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_max1_b(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.inparray1amax = array.array('b', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('b', [0] * arraysize)
		self.minus1array = array.array('b', [-1] * arraysize)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_min1_b(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.inparray1amin = array.array('b', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('b', [0] * arraysize)
		self.plus1array = array.array('b', [1] * arraysize)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1max_b(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.inparray2amax = array.array('b', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('b', [0] * arraysize)
		self.minus1array = array.array('b', [-1] * arraysize)
		self.minus2array = array.array('b', [-2] * arraysize)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2 - max value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2 - max value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2 - max value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2 - max value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2 - max value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2 - max value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1min_b(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_1min_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.inparray1amin = array.array('b', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('b', [0] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_d1(self):
		"""Test sub as *array-num-none* for 1 - min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit)


	########################################################
	def test_sub_array_num_array_d2(self):
		"""Test sub as *array-num-array* for 1 - min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_d3(self):
		"""Test sub as *num-array-none* for 1 - min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin)


	########################################################
	def test_sub_num_array_array_d4(self):
		"""Test sub as *num-array-array* for 1 - min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin, self.dataout)


	########################################################
	def test_sub_array_array_none_d5(self):
		"""Test sub as *array-array-none* for 1 - min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin)


	########################################################
	def test_sub_array_array_array_d6(self):
		"""Test sub as *array-array-array* for 1 - min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_B(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data 0,1,2,3,4.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_B(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('B', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('B', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code B.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_B(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('B', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('B', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code B.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_min1_B(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.B_max
		self.MinLimit = arrayfunc.arraylimits.B_min


		self.inparray1amin = array.array('B', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('B', [0] * arraysize)
		self.plus1array = array.array('B', [1] * arraysize)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_h(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data -2,-1,0,1,2.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_h(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('h', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('h', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code h.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_h(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('h', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('h', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code h.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_max1_h(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.inparray1amax = array.array('h', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('h', [0] * arraysize)
		self.minus1array = array.array('h', [-1] * arraysize)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_min1_h(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.inparray1amin = array.array('h', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('h', [0] * arraysize)
		self.plus1array = array.array('h', [1] * arraysize)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1max_h(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.inparray2amax = array.array('h', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('h', [0] * arraysize)
		self.minus1array = array.array('h', [-1] * arraysize)
		self.minus2array = array.array('h', [-2] * arraysize)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2 - max value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2 - max value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2 - max value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2 - max value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2 - max value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2 - max value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1min_h(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_1min_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.inparray1amin = array.array('h', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('h', [0] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_d1(self):
		"""Test sub as *array-num-none* for 1 - min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit)


	########################################################
	def test_sub_array_num_array_d2(self):
		"""Test sub as *array-num-array* for 1 - min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_d3(self):
		"""Test sub as *num-array-none* for 1 - min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin)


	########################################################
	def test_sub_num_array_array_d4(self):
		"""Test sub as *num-array-array* for 1 - min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin, self.dataout)


	########################################################
	def test_sub_array_array_none_d5(self):
		"""Test sub as *array-array-none* for 1 - min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin)


	########################################################
	def test_sub_array_array_array_d6(self):
		"""Test sub as *array-array-array* for 1 - min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_H(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data 0,1,2,3,4.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_H(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('H', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('H', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code H.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_H(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('H', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('H', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code H.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_min1_H(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.H_max
		self.MinLimit = arrayfunc.arraylimits.H_min


		self.inparray1amin = array.array('H', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('H', [0] * arraysize)
		self.plus1array = array.array('H', [1] * arraysize)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_i(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data -2,-1,0,1,2.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_i(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('i', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('i', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code i.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_i(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('i', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('i', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code i.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_max1_i(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.inparray1amax = array.array('i', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('i', [0] * arraysize)
		self.minus1array = array.array('i', [-1] * arraysize)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_min1_i(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.inparray1amin = array.array('i', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('i', [0] * arraysize)
		self.plus1array = array.array('i', [1] * arraysize)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1max_i(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.inparray2amax = array.array('i', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('i', [0] * arraysize)
		self.minus1array = array.array('i', [-1] * arraysize)
		self.minus2array = array.array('i', [-2] * arraysize)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2 - max value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2 - max value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2 - max value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2 - max value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2 - max value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2 - max value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1min_i(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_1min_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.inparray1amin = array.array('i', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('i', [0] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_d1(self):
		"""Test sub as *array-num-none* for 1 - min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit)


	########################################################
	def test_sub_array_num_array_d2(self):
		"""Test sub as *array-num-array* for 1 - min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_d3(self):
		"""Test sub as *num-array-none* for 1 - min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin)


	########################################################
	def test_sub_num_array_array_d4(self):
		"""Test sub as *num-array-array* for 1 - min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin, self.dataout)


	########################################################
	def test_sub_array_array_none_d5(self):
		"""Test sub as *array-array-none* for 1 - min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin)


	########################################################
	def test_sub_array_array_array_d6(self):
		"""Test sub as *array-array-array* for 1 - min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_I(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data 0,1,2,3,4.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_I(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('I', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('I', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code I.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_I(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('I', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('I', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code I.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_min1_I(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.I_max
		self.MinLimit = arrayfunc.arraylimits.I_min


		self.inparray1amin = array.array('I', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('I', [0] * arraysize)
		self.plus1array = array.array('I', [1] * arraysize)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_l(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data -2,-1,0,1,2.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_l(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('l', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('l', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code l.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_l(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('l', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('l', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code l.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_max1_l(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.inparray1amax = array.array('l', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('l', [0] * arraysize)
		self.minus1array = array.array('l', [-1] * arraysize)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_min1_l(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.inparray1amin = array.array('l', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('l', [0] * arraysize)
		self.plus1array = array.array('l', [1] * arraysize)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1max_l(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.inparray2amax = array.array('l', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('l', [0] * arraysize)
		self.minus1array = array.array('l', [-1] * arraysize)
		self.minus2array = array.array('l', [-2] * arraysize)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2 - max value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2 - max value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2 - max value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2 - max value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2 - max value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2 - max value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1min_l(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_1min_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.inparray1amin = array.array('l', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('l', [0] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_d1(self):
		"""Test sub as *array-num-none* for 1 - min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit)


	########################################################
	def test_sub_array_num_array_d2(self):
		"""Test sub as *array-num-array* for 1 - min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_d3(self):
		"""Test sub as *num-array-none* for 1 - min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin)


	########################################################
	def test_sub_num_array_array_d4(self):
		"""Test sub as *num-array-array* for 1 - min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin, self.dataout)


	########################################################
	def test_sub_array_array_none_d5(self):
		"""Test sub as *array-array-none* for 1 - min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin)


	########################################################
	def test_sub_array_array_array_d6(self):
		"""Test sub as *array-array-array* for 1 - min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_L(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data 0,1,2,3,4.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_L(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('L', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('L', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code L.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_L(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('L', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('L', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code L.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_min1_L(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.L_max
		self.MinLimit = arrayfunc.arraylimits.L_min


		self.inparray1amin = array.array('L', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('L', [0] * arraysize)
		self.plus1array = array.array('L', [1] * arraysize)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_q(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data -2,-1,0,1,2.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_q(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('q', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('q', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_q(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('q', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('q', [x for (x,y) in zip(itertools.cycle([-2,-1,0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_max1_q(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.inparray1amax = array.array('q', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('q', [0] * arraysize)
		self.minus1array = array.array('q', [-1] * arraysize)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, -1, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_min1_q(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.inparray1amin = array.array('q', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('q', [0] * arraysize)
		self.plus1array = array.array('q', [1] * arraysize)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1max_q(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.inparray2amax = array.array('q', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('q', [0] * arraysize)
		self.minus1array = array.array('q', [-1] * arraysize)
		self.minus2array = array.array('q', [-2] * arraysize)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2 - max value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2 - max value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2 - max value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2 - max value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(-2, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2 - max value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2 - max value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1min_q(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_1min_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.inparray1amin = array.array('q', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('q', [0] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_d1(self):
		"""Test sub as *array-num-none* for 1 - min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit)


	########################################################
	def test_sub_array_num_array_d2(self):
		"""Test sub as *array-num-array* for 1 - min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.MinLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_d3(self):
		"""Test sub as *num-array-none* for 1 - min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin)


	########################################################
	def test_sub_num_array_array_d4(self):
		"""Test sub as *num-array-array* for 1 - min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(0, self.inparray1bmin, self.dataout)


	########################################################
	def test_sub_array_array_none_d5(self):
		"""Test sub as *array-array-none* for 1 - min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin)


	########################################################
	def test_sub_array_array_array_d6(self):
		"""Test sub as *array-array-array* for 1 - min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.zero2array, self.inparray1bmin, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_Q(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data 0,1,2,3,4.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100,101,102,103,104,105,106,107,108,109]
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_Q(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('Q', [100,101,102,103,104,105,106,107,108,109])
		self.testarray2 = array.array('Q', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_Q(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('Q', [100,101,102,103,104,105,106,107,108,109])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('Q', [x for (x,y) in zip(itertools.cycle([0,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_min1_Q(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.Q_max
		self.MinLimit = arrayfunc.arraylimits.Q_min


		self.inparray1amin = array.array('Q', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('Q', [0] * arraysize)
		self.plus1array = array.array('Q', [1] * arraysize)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, 1, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################

 

##############################################################################
class sub_general_f(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data -2.0,-1.0,0.0,1.0,2.0.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]
		self.datay = [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_f(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.testarray2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])
		self.badarray2 = array.array('i', [int(x) for x in self.testarray2])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code f.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_f(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_max1_f(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.f_max
		self.MinLimit = arrayfunc.arraylimits.f_min


		self.inparray1amax = array.array('f', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('f', [0.0] * arraysize)
		self.minus1array = array.array('f', [-1.0e37] * arraysize)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, -1.0e37)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, -1.0e37, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_min1_f(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.f_max
		self.MinLimit = arrayfunc.arraylimits.f_min


		self.inparray1amin = array.array('f', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('f', [0.0] * arraysize)
		self.plus1array = array.array('f', [1.0e37] * arraysize)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, 1.0e37)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, 1.0e37, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1.0e37 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1max_f(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.f_max
		self.MinLimit = arrayfunc.arraylimits.f_min


		self.inparray2amax = array.array('f', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('f', [0.0] * arraysize)
		self.minus1array = array.array('f', [-1.0e37] * arraysize)
		self.minus2array = array.array('f', [-2.0e37] * arraysize)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2.0e37 - max value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2.0e37 - max value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2.0e37 - max value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2.0e37, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(-2.0e37, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2.0e37 - max value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2.0e37, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(-2.0e37, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2.0e37 - max value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2.0e37 - max value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################



##############################################################################
class sub_NaN_errors_f(unittest.TestCase):
	"""Test sub for basic general function operation using parameter nan.
	nan_data_error_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('nan')] * arraysize)



	########################################################
	def test_sub_NaN_array_num_none_a1(self):
		"""Test sub as *array-num-none* for nan - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval)


	########################################################
	def test_sub_NaN_array_num_none_a2(self):
		"""Test sub as *array-num-none* for nan with error check off - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_array_num_array_b1(self):
		"""Test sub as *array-num-array* for nan - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval, self.dataout)


	########################################################
	def test_sub_NaN_array_num_array_b2(self):
		"""Test sub as *array-num-array* for nan with error check off - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_num_array_none_c1(self):
		"""Test sub as *num-array-none* for nan - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, errordata)


	########################################################
	def test_sub_NaN_num_array_none_c2(self):
		"""Test sub as *num-array-none* for nan with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_num_array_array_d1(self):
		"""Test sub as *num-array-array* for nan - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.sub(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, self.errordata, self.dataout)


	########################################################
	def test_sub_NaN_num_array_array_d2(self):
		"""Test sub as *num-array-array* for nan with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_array_array_none_e1(self):
		"""Test sub as *array-array-none* for nan - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.sub(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(dataok1, self.errordata)


	########################################################
	def test_sub_NaN_array_array_none_e2(self):
		"""Test sub as *array-array-none* for nan with error check off - Array code f.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_array_array_array_f1(self):
		"""Test sub as *array-array-array* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_sub_NaN_array_array_array_f2(self):
		"""Test sub as *array-array-array* for nan with error check off - Array code f.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class sub_inf_errors_f(unittest.TestCase):
	"""Test sub for basic general function operation using parameter inf.
	nan_data_error_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('inf')] * arraysize)



	########################################################
	def test_sub_inf_array_num_none_a1(self):
		"""Test sub as *array-num-none* for inf - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval)


	########################################################
	def test_sub_inf_array_num_none_a2(self):
		"""Test sub as *array-num-none* for inf with error check off - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_array_num_array_b1(self):
		"""Test sub as *array-num-array* for inf - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval, self.dataout)


	########################################################
	def test_sub_inf_array_num_array_b2(self):
		"""Test sub as *array-num-array* for inf with error check off - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_num_array_none_c1(self):
		"""Test sub as *num-array-none* for inf - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, errordata)


	########################################################
	def test_sub_inf_num_array_none_c2(self):
		"""Test sub as *num-array-none* for inf with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_num_array_array_d1(self):
		"""Test sub as *num-array-array* for inf - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.sub(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, self.errordata, self.dataout)


	########################################################
	def test_sub_inf_num_array_array_d2(self):
		"""Test sub as *num-array-array* for inf with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_array_array_none_e1(self):
		"""Test sub as *array-array-none* for inf - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.sub(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(dataok1, self.errordata)


	########################################################
	def test_sub_inf_array_array_none_e2(self):
		"""Test sub as *array-array-none* for inf with error check off - Array code f.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_array_array_array_f1(self):
		"""Test sub as *array-array-array* for inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_sub_inf_array_array_array_f2(self):
		"""Test sub as *array-array-array* for inf with error check off - Array code f.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class sub_ninf_errors_f(unittest.TestCase):
	"""Test sub for basic general function operation using parameter -inf.
	nan_data_error_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('-inf')] * arraysize)



	########################################################
	def test_sub_ninf_array_num_none_a1(self):
		"""Test sub as *array-num-none* for -inf - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval)


	########################################################
	def test_sub_ninf_array_num_none_a2(self):
		"""Test sub as *array-num-none* for -inf with error check off - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_array_num_array_b1(self):
		"""Test sub as *array-num-array* for -inf - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval, self.dataout)


	########################################################
	def test_sub_ninf_array_num_array_b2(self):
		"""Test sub as *array-num-array* for -inf with error check off - Array code f.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_num_array_none_c1(self):
		"""Test sub as *num-array-none* for -inf - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, errordata)


	########################################################
	def test_sub_ninf_num_array_none_c2(self):
		"""Test sub as *num-array-none* for -inf with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_num_array_array_d1(self):
		"""Test sub as *num-array-array* for -inf - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.sub(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, self.errordata, self.dataout)


	########################################################
	def test_sub_ninf_num_array_array_d2(self):
		"""Test sub as *num-array-array* for -inf with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_array_array_none_e1(self):
		"""Test sub as *array-array-none* for -inf - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.sub(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(dataok1, self.errordata)


	########################################################
	def test_sub_ninf_array_array_none_e2(self):
		"""Test sub as *array-array-none* for -inf with error check off - Array code f.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_array_array_array_f1(self):
		"""Test sub as *array-array-array* for -inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_sub_ninf_array_array_array_f2(self):
		"""Test sub as *array-array-array* for -inf with error check off - Array code f.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

 

##############################################################################
class sub_general_d(unittest.TestCase):
	"""Test sub for basic general function operation using numeric 
	data -2.0,-1.0,0.0,1.0,2.0.
	test_template_op
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.datax = [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]
		self.datay = [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.datax)]


	########################################################
	def test_sub_basic_array_num_none_a1(self):
		"""Test sub as *array-num-none* for basic function - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a2(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a3(self):
		"""Test sub as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_none_a4(self):
		"""Test sub as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_num_array_b1(self):
		"""Test sub as *array-num-array* for basic function - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b2(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				expected =  [x - testval for x in data1] 

				arrayfunc.sub(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b3(self):
		"""Test sub as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_num_array_b4(self):
		"""Test sub as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datay:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x - testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_none_c1(self):
		"""Test sub as *num-array-none* for basic function - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c2(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c3(self):
		"""Test sub as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_none_c4(self):
		"""Test sub as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.sub(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_num_array_array_d1(self):
		"""Test sub as *num-array-array* for basic function - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d2(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				expected =  [testval - x for x in data1] 

				arrayfunc.sub(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d3(self):
		"""Test sub as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_num_array_array_d4(self):
		"""Test sub as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datax:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval - x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.sub(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_none_e1(self):
		"""Test sub as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e2(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e3(self):
		"""Test sub as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_none_e4(self):
		"""Test sub as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.sub(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e5(self):
		"""Test sub as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_basic_array_array_array_e6(self):
		"""Test sub as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		expected =  [x - y for (x, y) in zip(data1, data2)] 
		arrayfunc.sub(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_sub_basic_array_array_array_e7(self):
		"""Test sub as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x - y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.sub(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class sub_param_errors_d(unittest.TestCase):
	"""Test sub for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.testarray2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])
		self.badarray2 = array.array('i', [int(x) for x in self.testarray2])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue)


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, badvalue)



	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badarray1, testvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.sub(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_sub_array_num_array_b3(self):
		"""Test sub as *array-num-array* for invalid type of output array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.sub(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testarray1, testvalue, self.baddataout)



	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, badarray2)


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.sub(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(badvalue, testarray2)



	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for invalid type of number - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_sub_num_array_array_d3(self):
		"""Test sub as *num-array-array* for invalid type of output array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.sub(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.sub(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code d.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.sub(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(testarray1, self.badarray2)


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2)



	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_sub_array_array_array_f3(self):
		"""Test sub as *array-array-array* for invalid type of output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_sub_no_params_g1(self):
		"""Test sub with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.sub()



##############################################################################



##############################################################################
class sub_opt_param_errors_d(unittest.TestCase):
	"""Test sub for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for errors='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, errors='a')


	########################################################
	def test_sub_array_num_none_a2(self):
		"""Test sub as *array-num-none* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_sub_array_num_array_b1(self):
		"""Test sub as *array-num-array* for errors='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, errors='a')


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_sub_num_array_none_c1(self):
		"""Test sub as *num-array-none* for errors='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, errors='a')


	########################################################
	def test_sub_num_array_none_c2(self):
		"""Test sub as *num-array-none* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_num_array_array_d1(self):
		"""Test sub as *num-array-array* for errors='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_num_array_array_d2(self):
		"""Test sub as *num-array-array* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.sub(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_sub_array_array_none_e1(self):
		"""Test sub as *array-array-none* for errors='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, errors='a')


	########################################################
	def test_sub_array_array_none_e2(self):
		"""Test sub as *array-array-none* for maxlen='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_sub_array_array_array_f1(self):
		"""Test sub as *array-array-array* for errors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, errors='a')


	########################################################
	def test_sub_array_array_array_f2(self):
		"""Test sub as *array-array-array* for maxlen='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.sub(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.sub(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_max1_d(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.d_max
		self.MinLimit = arrayfunc.arraylimits.d_min


		self.inparray1amax = array.array('d', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('d', [0.0] * arraysize)
		self.minus1array = array.array('d', [-1.0e300] * arraysize)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, -1.0e300)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, -1.0e300, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_min1_d(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.d_max
		self.MinLimit = arrayfunc.arraylimits.d_min


		self.inparray1amin = array.array('d', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('d', [0.0] * arraysize)
		self.plus1array = array.array('d', [1.0e300] * arraysize)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, 1.0e300)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, 1.0e300, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1.0e300 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_1max_d(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.d_max
		self.MinLimit = arrayfunc.arraylimits.d_min


		self.inparray2amax = array.array('d', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('d', [0.0] * arraysize)
		self.minus1array = array.array('d', [-1.0e300] * arraysize)
		self.minus2array = array.array('d', [-2.0e300] * arraysize)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2.0e300 - max value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2.0e300 - max value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2.0e300 - max value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2.0e300, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(-2.0e300, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2.0e300 - max value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2.0e300, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(-2.0e300, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2.0e300 - max value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2.0e300 - max value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################



##############################################################################
class sub_NaN_errors_d(unittest.TestCase):
	"""Test sub for basic general function operation using parameter nan.
	nan_data_error_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('nan')] * arraysize)



	########################################################
	def test_sub_NaN_array_num_none_a1(self):
		"""Test sub as *array-num-none* for nan - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval)


	########################################################
	def test_sub_NaN_array_num_none_a2(self):
		"""Test sub as *array-num-none* for nan with error check off - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_array_num_array_b1(self):
		"""Test sub as *array-num-array* for nan - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval, self.dataout)


	########################################################
	def test_sub_NaN_array_num_array_b2(self):
		"""Test sub as *array-num-array* for nan with error check off - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_num_array_none_c1(self):
		"""Test sub as *num-array-none* for nan - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, errordata)


	########################################################
	def test_sub_NaN_num_array_none_c2(self):
		"""Test sub as *num-array-none* for nan with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_num_array_array_d1(self):
		"""Test sub as *num-array-array* for nan - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.sub(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, self.errordata, self.dataout)


	########################################################
	def test_sub_NaN_num_array_array_d2(self):
		"""Test sub as *num-array-array* for nan with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_array_array_none_e1(self):
		"""Test sub as *array-array-none* for nan - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.sub(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(dataok1, self.errordata)


	########################################################
	def test_sub_NaN_array_array_none_e2(self):
		"""Test sub as *array-array-none* for nan with error check off - Array code d.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_NaN_array_array_array_f1(self):
		"""Test sub as *array-array-array* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_sub_NaN_array_array_array_f2(self):
		"""Test sub as *array-array-array* for nan with error check off - Array code d.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class sub_inf_errors_d(unittest.TestCase):
	"""Test sub for basic general function operation using parameter inf.
	nan_data_error_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('inf')] * arraysize)



	########################################################
	def test_sub_inf_array_num_none_a1(self):
		"""Test sub as *array-num-none* for inf - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval)


	########################################################
	def test_sub_inf_array_num_none_a2(self):
		"""Test sub as *array-num-none* for inf with error check off - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_array_num_array_b1(self):
		"""Test sub as *array-num-array* for inf - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval, self.dataout)


	########################################################
	def test_sub_inf_array_num_array_b2(self):
		"""Test sub as *array-num-array* for inf with error check off - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_num_array_none_c1(self):
		"""Test sub as *num-array-none* for inf - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, errordata)


	########################################################
	def test_sub_inf_num_array_none_c2(self):
		"""Test sub as *num-array-none* for inf with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_num_array_array_d1(self):
		"""Test sub as *num-array-array* for inf - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.sub(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, self.errordata, self.dataout)


	########################################################
	def test_sub_inf_num_array_array_d2(self):
		"""Test sub as *num-array-array* for inf with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_array_array_none_e1(self):
		"""Test sub as *array-array-none* for inf - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.sub(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(dataok1, self.errordata)


	########################################################
	def test_sub_inf_array_array_none_e2(self):
		"""Test sub as *array-array-none* for inf with error check off - Array code d.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_inf_array_array_array_f1(self):
		"""Test sub as *array-array-array* for inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_sub_inf_array_array_array_f2(self):
		"""Test sub as *array-array-array* for inf with error check off - Array code d.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class sub_ninf_errors_d(unittest.TestCase):
	"""Test sub for basic general function operation using parameter -inf.
	nan_data_error_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0,-1.0,0.0,1.0,2.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('-inf')] * arraysize)



	########################################################
	def test_sub_ninf_array_num_none_a1(self):
		"""Test sub as *array-num-none* for -inf - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval)


	########################################################
	def test_sub_ninf_array_num_none_a2(self):
		"""Test sub as *array-num-none* for -inf with error check off - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_array_num_array_b1(self):
		"""Test sub as *array-num-array* for -inf - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(errordata, testval, self.dataout)


	########################################################
	def test_sub_ninf_array_num_array_b2(self):
		"""Test sub as *array-num-array* for -inf with error check off - Array code d.
		"""
		for testval in [-2.0,-1.0,0.0,1.0,2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x - testval for x in self.errordata]

				arrayfunc.sub(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_num_array_none_c1(self):
		"""Test sub as *num-array-none* for -inf - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.sub(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, errordata)


	########################################################
	def test_sub_ninf_num_array_none_c2(self):
		"""Test sub as *num-array-none* for -inf with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_num_array_array_d1(self):
		"""Test sub as *num-array-array* for -inf - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.sub(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.sub(testval, self.errordata, self.dataout)


	########################################################
	def test_sub_ninf_num_array_array_d2(self):
		"""Test sub as *num-array-array* for -inf with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval - x for x in self.errordata]

				arrayfunc.sub(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_array_array_none_e1(self):
		"""Test sub as *array-array-none* for -inf - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.sub(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(dataok1, self.errordata)


	########################################################
	def test_sub_ninf_array_array_none_e2(self):
		"""Test sub as *array-array-none* for -inf with error check off - Array code d.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_sub_ninf_array_array_array_f1(self):
		"""Test sub as *array-array-array* for -inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.sub(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_sub_ninf_array_array_array_f2(self):
		"""Test sub as *array-array-array* for -inf with error check off - Array code d.
		"""
		expected = [y - x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.sub(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
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
			f.write('sub\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################