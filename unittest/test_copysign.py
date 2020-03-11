#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_copysign.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      06-Mar-2020.
#
###############################################################################
#
#   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for copysign.
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
class copysign_general_f(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -3.0, -1.0, 0.0, 1.0, 3.0.
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
	def test_copysign_basic_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for basic function - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_none_a3(self):
		"""Test copysign as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_none_a4(self):
		"""Test copysign as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for basic function - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_array_b3(self):
		"""Test copysign as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_array_b4(self):
		"""Test copysign as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for basic function - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_none_c3(self):
		"""Test copysign as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_none_c4(self):
		"""Test copysign as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for basic function - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_array_d3(self):
		"""Test copysign as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_array_d4(self):
		"""Test copysign as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_none_e3(self):
		"""Test copysign as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.copysign(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_none_e4(self):
		"""Test copysign as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.copysign(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_array_e5(self):
		"""Test copysign as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_array_array_array_e6(self):
		"""Test copysign as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_array_e7(self):
		"""Test copysign as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.copysign(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class copysign_param_errors_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.floatarray2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_copysign_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(intarray1, testfloat)


	########################################################
	def test_copysign_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(floatarray1, testint)


	########################################################
	def test_copysign_array_num_none_a3(self):
		"""Test copysign as *array-num-none* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(intarray1, testint)


	########################################################
	def test_copysign_array_num_none_a4(self):
		"""Test copysign as *array-num-none* for matherrors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, matherrors='a')


	########################################################
	def test_copysign_array_num_none_a5(self):
		"""Test copysign as *array-num-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, maxlen='a')



	########################################################
	def test_copysign_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(intarray1, testfloat, self.dataout)


	########################################################
	def test_copysign_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(self.floatarray1, testint, self.dataout)


	########################################################
	def test_copysign_array_num_array_b3(self):
		"""Test copysign as *array-num-array* for integer output array - Array code f.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(floatarray1, testfloat, self.intdataout)


	########################################################
	def test_copysign_array_num_array_b4(self):
		"""Test copysign as *array-num-array* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(self.intarray1, testint, self.intdataout)


	########################################################
	def test_copysign_array_num_array_b5(self):
		"""Test copysign as *array-num-array* for matherrors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, self.dataout, matherrors='a')


	########################################################
	def test_copysign_array_num_array_b6(self):
		"""Test copysign as *array-num-array* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, self.dataout, maxlen='a')



	########################################################
	def test_copysign_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, intarray1)


	########################################################
	def test_copysign_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, floatarray1)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testint, floatarray1)


	########################################################
	def test_copysign_num_array_none_c3(self):
		"""Test copysign as *num-array-none* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testint, intarray1)


	########################################################
	def test_copysign_num_array_none_c4(self):
		"""Test copysign as *num-array-none* for matherrors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, floatarray1, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, floatarray1, matherrors='a')


	########################################################
	def test_copysign_num_array_none_c5(self):
		"""Test copysign as *num-array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, floatarray1, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, floatarray1, maxlen='a')



	########################################################
	def test_copysign_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_copysign_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_copysign_num_array_array_d3(self):
		"""Test copysign as *num-array-array* for integer output array - Array code f.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, self.floatarray1, self.intdataout)


	########################################################
	def test_copysign_num_array_array_d4(self):
		"""Test copysign as *num-array-array* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testint, self.intarray1, self.intdataout)


	########################################################
	def test_copysign_num_array_array_d5(self):
		"""Test copysign as *num-array-array* for matherrors='a' - Array code f.
		"""
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, self.floatarray1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, self.intarray1, self.dataout, matherrors='a')


	########################################################
	def test_copysign_num_array_array_d6(self):
		"""Test copysign as *num-array-array* for maxlen='a' - Array code f.
		"""
		testfloat = self.floatarray2[0]
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, self.floatarray1, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, self.intarray1, self.dataout, maxlen='a')



	########################################################
	def test_copysign_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for integer array - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, self.floatarray2)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, self.intarray2)


	########################################################
	def test_copysign_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.floatarray2)


	########################################################
	def test_copysign_array_array_none_e3(self):
		"""Test copysign as *array-array-none* for all integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.intarray2)


	########################################################
	def test_copysign_array_array_none_e4(self):
		"""Test copysign as *array-array-none* for matherrors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, self.floatarray2, matherrors=True)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, self.floatarray2, matherrors='a')


	########################################################
	def test_copysign_array_array_none_e5(self):
		"""Test copysign as *array-array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, self.floatarray2, maxlen=testmaxlen)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, self.floatarray2, maxlen='a')



	########################################################
	def test_copysign_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.intarray2, self.dataout)


	########################################################
	def test_copysign_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.floatarray2, self.dataout)


	########################################################
	def test_copysign_array_array_array_f3(self):
		"""Test copysign as *array-array-array* for integer output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.floatarray2, self.intdataout)


	########################################################
	def test_copysign_array_array_array_f4(self):
		"""Test copysign as *array-array-array* for all integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.intarray2, self.intdataout)


	########################################################
	def test_copysign_array_array_array_f5(self):
		"""Test copysign as *array-array-array* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, matherrors='a')


	########################################################
	def test_copysign_array_array_array_f6(self):
		"""Test copysign as *array-array-array* for maxlen='a' - Array code f.
		"""
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, maxlen='a')


	########################################################
	def test_copysign_no_params_g1(self):
		"""Test copysign with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.copysign()



##############################################################################



##############################################################################
class copysign_NaN_errors_f(unittest.TestCase):
	"""Test for copysign function operation using parameter nan.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.okarray1 = array.array('f', [-3.0, -1.0, 0.0, 1.0, 3.0])
		# This is the same data, but with signs reversed.
		self.okarray2 = array.array('f', [-x for x in [-3.0, -1.0, 0.0, 1.0, 3.0]])

		arraysize =  len(self.okarray1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('nan')] * arraysize)


	########################################################
	def test_copysign_NaN_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for nan - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval)


	########################################################
	def test_copysign_NaN_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for nan with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(x, testval) for x in errordata]

				arrayfunc.copysign(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for nan - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval, self.dataout)


	########################################################
	def test_copysign_NaN_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for nan with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(x, testval) for x in self.errordata]

				arrayfunc.copysign(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for nan - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for nan with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for nan - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for nan with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for nan - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for nan with error check off - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for nan - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for nan with error check off - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class copysign_inf_errors_f(unittest.TestCase):
	"""Test for copysign function operation using parameter inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.okarray1 = array.array('f', [-3.0, -1.0, 0.0, 1.0, 3.0])
		# This is the same data, but with signs reversed.
		self.okarray2 = array.array('f', [-x for x in [-3.0, -1.0, 0.0, 1.0, 3.0]])

		arraysize =  len(self.okarray1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('inf')] * arraysize)


	########################################################
	def test_copysign_inf_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval)


	########################################################
	def test_copysign_inf_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(x, testval) for x in errordata]

				arrayfunc.copysign(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval, self.dataout)


	########################################################
	def test_copysign_inf_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(x, testval) for x in self.errordata]

				arrayfunc.copysign(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for inf - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for inf with error check off - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for inf - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for inf with error check off - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class copysign_ninf_errors_f(unittest.TestCase):
	"""Test for copysign function operation using parameter -inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.okarray1 = array.array('f', [-3.0, -1.0, 0.0, 1.0, 3.0])
		# This is the same data, but with signs reversed.
		self.okarray2 = array.array('f', [-x for x in [-3.0, -1.0, 0.0, 1.0, 3.0]])

		arraysize =  len(self.okarray1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('-inf')] * arraysize)


	########################################################
	def test_copysign_ninf_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for -inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval)


	########################################################
	def test_copysign_ninf_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for -inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(x, testval) for x in errordata]

				arrayfunc.copysign(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for -inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval, self.dataout)


	########################################################
	def test_copysign_ninf_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for -inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(x, testval) for x in self.errordata]

				arrayfunc.copysign(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for -inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for -inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for -inf - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for -inf with error check off - Array code f.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for -inf - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for -inf with error check off - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for -inf - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for -inf with error check off - Array code f.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class copysign_general_d(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -3.0, -1.0, 0.0, 1.0, 3.0.
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
	def test_copysign_basic_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for basic function - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_none_a3(self):
		"""Test copysign as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_none_a4(self):
		"""Test copysign as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for basic function - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.copysign(x, testval) for x in data1]

				arrayfunc.copysign(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_array_b3(self):
		"""Test copysign as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_num_array_b4(self):
		"""Test copysign as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for basic function - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_none_c3(self):
		"""Test copysign as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_none_c4(self):
		"""Test copysign as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.copysign(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for basic function - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.copysign(testval, x) for x in data1]

				arrayfunc.copysign(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_array_d3(self):
		"""Test copysign as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_num_array_array_d4(self):
		"""Test copysign as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-3.0, -1.0, 0.0, 1.0, 3.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.copysign(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.copysign(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_none_e3(self):
		"""Test copysign as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.copysign(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_none_e4(self):
		"""Test copysign as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.copysign(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_array_e5(self):
		"""Test copysign as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_basic_array_array_array_e6(self):
		"""Test copysign as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		expected = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.copysign(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_basic_array_array_array_e7(self):
		"""Test copysign as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [math.copysign(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.copysign(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class copysign_param_errors_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.floatarray2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0, -1.0, 0.0, 1.0, 3.0]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_copysign_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(intarray1, testfloat)


	########################################################
	def test_copysign_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(floatarray1, testint)


	########################################################
	def test_copysign_array_num_none_a3(self):
		"""Test copysign as *array-num-none* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(intarray1, testint)


	########################################################
	def test_copysign_array_num_none_a4(self):
		"""Test copysign as *array-num-none* for matherrors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, matherrors='a')


	########################################################
	def test_copysign_array_num_none_a5(self):
		"""Test copysign as *array-num-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, maxlen='a')



	########################################################
	def test_copysign_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(intarray1, testfloat, self.dataout)


	########################################################
	def test_copysign_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(self.floatarray1, testint, self.dataout)


	########################################################
	def test_copysign_array_num_array_b3(self):
		"""Test copysign as *array-num-array* for integer output array - Array code d.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(floatarray1, testfloat, self.intdataout)


	########################################################
	def test_copysign_array_num_array_b4(self):
		"""Test copysign as *array-num-array* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(self.intarray1, testint, self.intdataout)


	########################################################
	def test_copysign_array_num_array_b5(self):
		"""Test copysign as *array-num-array* for matherrors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, self.dataout, matherrors='a')


	########################################################
	def test_copysign_array_num_array_b6(self):
		"""Test copysign as *array-num-array* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, testfloat, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, testfloat, self.dataout, maxlen='a')



	########################################################
	def test_copysign_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, intarray1)


	########################################################
	def test_copysign_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, floatarray1)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testint, floatarray1)


	########################################################
	def test_copysign_num_array_none_c3(self):
		"""Test copysign as *num-array-none* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testint, intarray1)


	########################################################
	def test_copysign_num_array_none_c4(self):
		"""Test copysign as *num-array-none* for matherrors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, floatarray1, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, floatarray1, matherrors='a')


	########################################################
	def test_copysign_num_array_none_c5(self):
		"""Test copysign as *num-array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, floatarray1, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, floatarray1, maxlen='a')



	########################################################
	def test_copysign_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_copysign_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_copysign_num_array_array_d3(self):
		"""Test copysign as *num-array-array* for integer output array - Array code d.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testfloat, self.floatarray1, self.intdataout)


	########################################################
	def test_copysign_num_array_array_d4(self):
		"""Test copysign as *num-array-array* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.copysign(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.copysign(testint, self.intarray1, self.intdataout)


	########################################################
	def test_copysign_num_array_array_d5(self):
		"""Test copysign as *num-array-array* for matherrors='a' - Array code d.
		"""
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, self.floatarray1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, self.intarray1, self.dataout, matherrors='a')


	########################################################
	def test_copysign_num_array_array_d6(self):
		"""Test copysign as *num-array-array* for maxlen='a' - Array code d.
		"""
		testfloat = self.floatarray2[0]
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(testfloat, self.floatarray1, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(testfloat, self.intarray1, self.dataout, maxlen='a')



	########################################################
	def test_copysign_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for integer array - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, self.floatarray2)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, self.intarray2)


	########################################################
	def test_copysign_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.floatarray2)


	########################################################
	def test_copysign_array_array_none_e3(self):
		"""Test copysign as *array-array-none* for all integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.intarray2)


	########################################################
	def test_copysign_array_array_none_e4(self):
		"""Test copysign as *array-array-none* for matherrors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, self.floatarray2, matherrors=True)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, self.floatarray2, matherrors='a')


	########################################################
	def test_copysign_array_array_none_e5(self):
		"""Test copysign as *array-array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(floatarray1, self.floatarray2, maxlen=testmaxlen)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(floatarray1, self.floatarray2, maxlen='a')



	########################################################
	def test_copysign_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.intarray2, self.dataout)


	########################################################
	def test_copysign_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.floatarray2, self.dataout)


	########################################################
	def test_copysign_array_array_array_f3(self):
		"""Test copysign as *array-array-array* for integer output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.floatarray2, self.intdataout)


	########################################################
	def test_copysign_array_array_array_f4(self):
		"""Test copysign as *array-array-array* for all integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.intarray1, self.intarray2, self.intdataout)


	########################################################
	def test_copysign_array_array_array_f5(self):
		"""Test copysign as *array-array-array* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, matherrors='a')


	########################################################
	def test_copysign_array_array_array_f6(self):
		"""Test copysign as *array-array-array* for maxlen='a' - Array code d.
		"""
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.copysign(self.floatarray1, self.floatarray2, self.dataout, maxlen='a')


	########################################################
	def test_copysign_no_params_g1(self):
		"""Test copysign with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.copysign()



##############################################################################



##############################################################################
class copysign_NaN_errors_d(unittest.TestCase):
	"""Test for copysign function operation using parameter nan.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.okarray1 = array.array('d', [-3.0, -1.0, 0.0, 1.0, 3.0])
		# This is the same data, but with signs reversed.
		self.okarray2 = array.array('d', [-x for x in [-3.0, -1.0, 0.0, 1.0, 3.0]])

		arraysize =  len(self.okarray1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('nan')] * arraysize)


	########################################################
	def test_copysign_NaN_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for nan - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval)


	########################################################
	def test_copysign_NaN_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for nan with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(x, testval) for x in errordata]

				arrayfunc.copysign(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for nan - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval, self.dataout)


	########################################################
	def test_copysign_NaN_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for nan with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(x, testval) for x in self.errordata]

				arrayfunc.copysign(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for nan - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for nan with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for nan - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for nan with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for nan - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for nan with error check off - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_NaN_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for nan - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_NaN_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for nan with error check off - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class copysign_inf_errors_d(unittest.TestCase):
	"""Test for copysign function operation using parameter inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.okarray1 = array.array('d', [-3.0, -1.0, 0.0, 1.0, 3.0])
		# This is the same data, but with signs reversed.
		self.okarray2 = array.array('d', [-x for x in [-3.0, -1.0, 0.0, 1.0, 3.0]])

		arraysize =  len(self.okarray1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('inf')] * arraysize)


	########################################################
	def test_copysign_inf_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval)


	########################################################
	def test_copysign_inf_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(x, testval) for x in errordata]

				arrayfunc.copysign(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval, self.dataout)


	########################################################
	def test_copysign_inf_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(x, testval) for x in self.errordata]

				arrayfunc.copysign(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for inf - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for inf with error check off - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_inf_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for inf - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_inf_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for inf with error check off - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class copysign_ninf_errors_d(unittest.TestCase):
	"""Test for copysign function operation using parameter -inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.okarray1 = array.array('d', [-3.0, -1.0, 0.0, 1.0, 3.0])
		# This is the same data, but with signs reversed.
		self.okarray2 = array.array('d', [-x for x in [-3.0, -1.0, 0.0, 1.0, 3.0]])

		arraysize =  len(self.okarray1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('-inf')] * arraysize)


	########################################################
	def test_copysign_ninf_array_num_none_a1(self):
		"""Test copysign as *array-num-none* for -inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval)


	########################################################
	def test_copysign_ninf_array_num_none_a2(self):
		"""Test copysign as *array-num-none* for -inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(x, testval) for x in errordata]

				arrayfunc.copysign(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_array_num_array_b1(self):
		"""Test copysign as *array-num-array* for -inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.copysign(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.copysign(errordata, testval, self.dataout)


	########################################################
	def test_copysign_ninf_array_num_array_b2(self):
		"""Test copysign as *array-num-array* for -inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(x, testval) for x in self.errordata]

				arrayfunc.copysign(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_num_array_none_c1(self):
		"""Test copysign as *num-array-none* for -inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_num_array_none_c2(self):
		"""Test copysign as *num-array-none* for -inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.copysign(testval, x) for x in errordata]

				arrayfunc.copysign(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_num_array_array_d1(self):
		"""Test copysign as *num-array-array* for -inf - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_num_array_array_d2(self):
		"""Test copysign as *num-array-array* for -inf with error check off - Array code d.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.copysign(testval, x) for x in self.errordata]

				arrayfunc.copysign(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_array_array_none_e1(self):
		"""Test copysign as *array-array-none* for -inf - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_array_array_none_e2(self):
		"""Test copysign as *array-array-none* for -inf with error check off - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_copysign_ninf_array_array_array_f1(self):
		"""Test copysign as *array-array-array* for -inf - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_copysign_ninf_array_array_array_f2(self):
		"""Test copysign as *array-array-array* for -inf with error check off - Array code d.
		"""
		expected = [math.copysign(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.copysign(self.okarray1, self.errordata, self.dataout, matherrors=True)

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

		with open('af_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('copysign\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
