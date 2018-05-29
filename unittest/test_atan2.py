#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_atan2.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      28-May-2018.
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
"""This conducts unit tests for atan2.
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
class atan2_general_f(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -2.0, -1.0, 0.0, 1.0, 2.0.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_atan2_basic_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_none_a3(self):
		"""Test atan2 as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_none_a4(self):
		"""Test atan2 as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_array_b3(self):
		"""Test atan2 as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_array_b4(self):
		"""Test atan2 as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_none_c3(self):
		"""Test atan2 as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_none_c4(self):
		"""Test atan2 as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_array_d3(self):
		"""Test atan2 as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_array_d4(self):
		"""Test atan2 as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_none_e3(self):
		"""Test atan2 as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.atan2(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_none_e4(self):
		"""Test atan2 as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.atan2(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_array_e5(self):
		"""Test atan2 as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_array_array_array_e6(self):
		"""Test atan2 as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_array_e7(self):
		"""Test atan2 as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.atan2(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class atan2_param_errors_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.floatarray2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_atan2_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(intarray1, testfloat)


	########################################################
	def test_atan2_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(floatarray1, testint)


	########################################################
	def test_atan2_array_num_none_a3(self):
		"""Test atan2 as *array-num-none* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(intarray1, testint)


	########################################################
	def test_atan2_array_num_none_a4(self):
		"""Test atan2 as *array-num-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, errors='a')


	########################################################
	def test_atan2_array_num_none_a5(self):
		"""Test atan2 as *array-num-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, maxlen='a')



	########################################################
	def test_atan2_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(intarray1, testfloat, self.dataout)


	########################################################
	def test_atan2_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(self.floatarray1, testint, self.dataout)


	########################################################
	def test_atan2_array_num_array_b3(self):
		"""Test atan2 as *array-num-array* for integer output array - Array code f.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(floatarray1, testfloat, self.intdataout)


	########################################################
	def test_atan2_array_num_array_b4(self):
		"""Test atan2 as *array-num-array* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(self.intarray1, testint, self.intdataout)


	########################################################
	def test_atan2_array_num_array_b5(self):
		"""Test atan2 as *array-num-array* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, self.dataout, errors='a')


	########################################################
	def test_atan2_array_num_array_b6(self):
		"""Test atan2 as *array-num-array* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, self.dataout, maxlen='a')



	########################################################
	def test_atan2_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, intarray1)


	########################################################
	def test_atan2_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, floatarray1)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testint, floatarray1)


	########################################################
	def test_atan2_num_array_none_c3(self):
		"""Test atan2 as *num-array-none* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testint, intarray1)


	########################################################
	def test_atan2_num_array_none_c4(self):
		"""Test atan2 as *num-array-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, floatarray1, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, floatarray1, errors='a')


	########################################################
	def test_atan2_num_array_none_c5(self):
		"""Test atan2 as *num-array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, floatarray1, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, floatarray1, maxlen='a')



	########################################################
	def test_atan2_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_atan2_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_atan2_num_array_array_d3(self):
		"""Test atan2 as *num-array-array* for integer output array - Array code f.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, self.floatarray1, self.intdataout)


	########################################################
	def test_atan2_num_array_array_d4(self):
		"""Test atan2 as *num-array-array* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testint, self.intarray1, self.intdataout)


	########################################################
	def test_atan2_num_array_array_d5(self):
		"""Test atan2 as *num-array-array* for errors='a' - Array code f.
		"""
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, self.floatarray1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, self.intarray1, self.dataout, errors='a')


	########################################################
	def test_atan2_num_array_array_d6(self):
		"""Test atan2 as *num-array-array* for maxlen='a' - Array code f.
		"""
		testfloat = self.floatarray2[0]
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, self.floatarray1, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, self.intarray1, self.dataout, maxlen='a')



	########################################################
	def test_atan2_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for integer array - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, self.floatarray2)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, self.intarray2)


	########################################################
	def test_atan2_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.floatarray2)


	########################################################
	def test_atan2_array_array_none_e3(self):
		"""Test atan2 as *array-array-none* for all integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.intarray2)


	########################################################
	def test_atan2_array_array_none_e4(self):
		"""Test atan2 as *array-array-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, self.floatarray2, matherrors=True)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, self.floatarray2, errors='a')


	########################################################
	def test_atan2_array_array_none_e5(self):
		"""Test atan2 as *array-array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, self.floatarray2, maxlen=testmaxlen)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, self.floatarray2, maxlen='a')



	########################################################
	def test_atan2_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.intarray2, self.dataout)


	########################################################
	def test_atan2_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.floatarray2, self.dataout)


	########################################################
	def test_atan2_array_array_array_f3(self):
		"""Test atan2 as *array-array-array* for integer output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.floatarray2, self.intdataout)


	########################################################
	def test_atan2_array_array_array_f4(self):
		"""Test atan2 as *array-array-array* for all integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.intarray2, self.intdataout)


	########################################################
	def test_atan2_array_array_array_f5(self):
		"""Test atan2 as *array-array-array* for errors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, errors='a')


	########################################################
	def test_atan2_array_array_array_f6(self):
		"""Test atan2 as *array-array-array* for maxlen='a' - Array code f.
		"""
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, maxlen='a')


	########################################################
	def test_atan2_no_params_g1(self):
		"""Test atan2 with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.atan2()



##############################################################################



##############################################################################
class atan2_NaN_errors_f(unittest.TestCase):
	"""Test for basic general function operation using parameter nan.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return math.atan2(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('nan')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('inf')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('inf')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_atan2_NaN_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.atan2(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(errordata, testval)


	########################################################
	def test_atan2_NaN_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for nan with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [self.PyOp(x, testval, float('inf')) for x in self.errordata]

				arrayfunc.atan2(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.atan2(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(errordata, testval, self.dataout)


	########################################################
	def test_atan2_NaN_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for nan with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [self.PyOp(x, testval, float('inf')) for x in self.errordata]

				arrayfunc.atan2(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.atan2(testval, dataok1)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(testval, errordata)


	########################################################
	def test_atan2_NaN_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for nan with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expectedpe = [self.PyOp(testval, x, float('inf')) for x in self.errordata]

				arrayfunc.atan2(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.atan2(testval, self.dataok1, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(testval, self.errordata, self.dataout)


	########################################################
	def test_atan2_NaN_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for nan with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedpe = [self.PyOp(testval, x, float('inf')) for x in self.errordata]

				arrayfunc.atan2(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for nan - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.atan2(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.atan2(dataok1, self.errordata)


	########################################################
	def test_atan2_NaN_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for nan with error check off - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.atan2(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_atan2_NaN_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for nan with error check off - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class atan2_inf_noerrors_f(unittest.TestCase):
	"""Test for basic general function operation using parameter inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return math.atan2(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('inf')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('inf')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('inf')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_atan2_inf_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for inf - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for inf with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for inf - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for inf with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for inf - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for inf - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for inf - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for inf with error check off - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for inf - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for inf with error check off - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class atan2_ninf_noerrors_f(unittest.TestCase):
	"""Test for basic general function operation using parameter -inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return math.atan2(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('-inf')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('inf')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('inf')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_atan2_ninf_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for -inf - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for -inf with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for -inf - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for -inf with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for -inf - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for -inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for -inf - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for -inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for -inf - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for -inf with error check off - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for -inf - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for -inf with error check off - Array code f.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class atan2_general_d(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -2.0, -1.0, 0.0, 1.0, 2.0.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_atan2_basic_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_none_a3(self):
		"""Test atan2 as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_none_a4(self):
		"""Test atan2 as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.atan2(x, testval) for x in data1]

				arrayfunc.atan2(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_array_b3(self):
		"""Test atan2 as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_num_array_b4(self):
		"""Test atan2 as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_none_c3(self):
		"""Test atan2 as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_none_c4(self):
		"""Test atan2 as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.atan2(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.atan2(testval, x) for x in data1]

				arrayfunc.atan2(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_array_d3(self):
		"""Test atan2 as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_num_array_array_d4(self):
		"""Test atan2 as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.atan2(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.atan2(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_none_e3(self):
		"""Test atan2 as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.atan2(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_none_e4(self):
		"""Test atan2 as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.atan2(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_array_e5(self):
		"""Test atan2 as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_basic_array_array_array_e6(self):
		"""Test atan2 as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		expected = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.atan2(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_basic_array_array_array_e7(self):
		"""Test atan2 as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [math.atan2(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.atan2(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class atan2_param_errors_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.floatarray2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_atan2_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(intarray1, testfloat)


	########################################################
	def test_atan2_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(floatarray1, testint)


	########################################################
	def test_atan2_array_num_none_a3(self):
		"""Test atan2 as *array-num-none* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(intarray1, testint)


	########################################################
	def test_atan2_array_num_none_a4(self):
		"""Test atan2 as *array-num-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, errors='a')


	########################################################
	def test_atan2_array_num_none_a5(self):
		"""Test atan2 as *array-num-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, maxlen='a')



	########################################################
	def test_atan2_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(intarray1, testfloat, self.dataout)


	########################################################
	def test_atan2_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(self.floatarray1, testint, self.dataout)


	########################################################
	def test_atan2_array_num_array_b3(self):
		"""Test atan2 as *array-num-array* for integer output array - Array code d.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(floatarray1, testfloat, self.intdataout)


	########################################################
	def test_atan2_array_num_array_b4(self):
		"""Test atan2 as *array-num-array* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(self.intarray1, testint, self.intdataout)


	########################################################
	def test_atan2_array_num_array_b5(self):
		"""Test atan2 as *array-num-array* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, self.dataout, errors='a')


	########################################################
	def test_atan2_array_num_array_b6(self):
		"""Test atan2 as *array-num-array* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, testfloat, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, testfloat, self.dataout, maxlen='a')



	########################################################
	def test_atan2_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, intarray1)


	########################################################
	def test_atan2_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, floatarray1)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testint, floatarray1)


	########################################################
	def test_atan2_num_array_none_c3(self):
		"""Test atan2 as *num-array-none* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testint, intarray1)


	########################################################
	def test_atan2_num_array_none_c4(self):
		"""Test atan2 as *num-array-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, floatarray1, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, floatarray1, errors='a')


	########################################################
	def test_atan2_num_array_none_c5(self):
		"""Test atan2 as *num-array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, floatarray1, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, floatarray1, maxlen='a')



	########################################################
	def test_atan2_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_atan2_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_atan2_num_array_array_d3(self):
		"""Test atan2 as *num-array-array* for integer output array - Array code d.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testfloat, self.floatarray1, self.intdataout)


	########################################################
	def test_atan2_num_array_array_d4(self):
		"""Test atan2 as *num-array-array* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.atan2(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.atan2(testint, self.intarray1, self.intdataout)


	########################################################
	def test_atan2_num_array_array_d5(self):
		"""Test atan2 as *num-array-array* for errors='a' - Array code d.
		"""
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, self.floatarray1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, self.intarray1, self.dataout, errors='a')


	########################################################
	def test_atan2_num_array_array_d6(self):
		"""Test atan2 as *num-array-array* for maxlen='a' - Array code d.
		"""
		testfloat = self.floatarray2[0]
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(testfloat, self.floatarray1, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(testfloat, self.intarray1, self.dataout, maxlen='a')



	########################################################
	def test_atan2_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for integer array - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, self.floatarray2)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, self.intarray2)


	########################################################
	def test_atan2_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.floatarray2)


	########################################################
	def test_atan2_array_array_none_e3(self):
		"""Test atan2 as *array-array-none* for all integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.intarray2)


	########################################################
	def test_atan2_array_array_none_e4(self):
		"""Test atan2 as *array-array-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, self.floatarray2, matherrors=True)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, self.floatarray2, errors='a')


	########################################################
	def test_atan2_array_array_none_e5(self):
		"""Test atan2 as *array-array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(floatarray1, self.floatarray2, maxlen=testmaxlen)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(floatarray1, self.floatarray2, maxlen='a')



	########################################################
	def test_atan2_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.intarray2, self.dataout)


	########################################################
	def test_atan2_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.floatarray2, self.dataout)


	########################################################
	def test_atan2_array_array_array_f3(self):
		"""Test atan2 as *array-array-array* for integer output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.floatarray2, self.intdataout)


	########################################################
	def test_atan2_array_array_array_f4(self):
		"""Test atan2 as *array-array-array* for all integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.intarray1, self.intarray2, self.intdataout)


	########################################################
	def test_atan2_array_array_array_f5(self):
		"""Test atan2 as *array-array-array* for errors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, errors='a')


	########################################################
	def test_atan2_array_array_array_f6(self):
		"""Test atan2 as *array-array-array* for maxlen='a' - Array code d.
		"""
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.atan2(self.floatarray1, self.floatarray2, self.dataout, maxlen='a')


	########################################################
	def test_atan2_no_params_g1(self):
		"""Test atan2 with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.atan2()



##############################################################################



##############################################################################
class atan2_NaN_errors_d(unittest.TestCase):
	"""Test for basic general function operation using parameter nan.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return math.atan2(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('nan')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('inf')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('inf')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_atan2_NaN_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.atan2(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(errordata, testval)


	########################################################
	def test_atan2_NaN_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for nan with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [self.PyOp(x, testval, float('inf')) for x in self.errordata]

				arrayfunc.atan2(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.atan2(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(errordata, testval, self.dataout)


	########################################################
	def test_atan2_NaN_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for nan with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [self.PyOp(x, testval, float('inf')) for x in self.errordata]

				arrayfunc.atan2(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.atan2(testval, dataok1)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(testval, errordata)


	########################################################
	def test_atan2_NaN_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for nan with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expectedpe = [self.PyOp(testval, x, float('inf')) for x in self.errordata]

				arrayfunc.atan2(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.atan2(testval, self.dataok1, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.atan2(testval, self.errordata, self.dataout)


	########################################################
	def test_atan2_NaN_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for nan with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedpe = [self.PyOp(testval, x, float('inf')) for x in self.errordata]

				arrayfunc.atan2(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for nan - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.atan2(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.atan2(dataok1, self.errordata)


	########################################################
	def test_atan2_NaN_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for nan with error check off - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_NaN_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.atan2(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.atan2(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_atan2_NaN_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for nan with error check off - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class atan2_inf_noerrors_d(unittest.TestCase):
	"""Test for basic general function operation using parameter inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return math.atan2(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('inf')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('inf')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('inf')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_atan2_inf_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for inf - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for inf with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for inf - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for inf with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for inf - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for inf - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for inf - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for inf with error check off - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_inf_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for inf - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_inf_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for inf with error check off - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class atan2_ninf_noerrors_d(unittest.TestCase):
	"""Test for basic general function operation using parameter -inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return math.atan2(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 0.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('-inf')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('inf')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('inf')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_atan2_ninf_array_num_none_a1(self):
		"""Test atan2 as *array-num-none* for -inf - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_num_none_a2(self):
		"""Test atan2 as *array-num-none* for -inf with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_array_num_array_b1(self):
		"""Test atan2 as *array-num-array* for -inf - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_num_array_b2(self):
		"""Test atan2 as *array-num-array* for -inf with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 0.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_num_array_none_c1(self):
		"""Test atan2 as *num-array-none* for -inf - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_num_array_none_c2(self):
		"""Test atan2 as *num-array-none* for -inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.atan2(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_num_array_array_d1(self):
		"""Test atan2 as *num-array-array* for -inf - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_num_array_array_d2(self):
		"""Test atan2 as *num-array-array* for -inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.atan2(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_array_array_none_e1(self):
		"""Test atan2 as *array-array-none* for -inf - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_array_none_e2(self):
		"""Test atan2 as *array-array-none* for -inf with error check off - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_atan2_ninf_array_array_array_f1(self):
		"""Test atan2 as *array-array-array* for -inf - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_atan2_ninf_array_array_array_f2(self):
		"""Test atan2 as *array-array-array* for -inf with error check off - Array code d.
		"""
		arrayfunc.atan2(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
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
			f.write('atan2\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
