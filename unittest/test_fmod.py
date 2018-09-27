#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_fmod.py
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
"""This conducts unit tests for fmod.
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
class fmod_general_f(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -2.0, -1.0, 1.0, 2.0.
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
	def test_fmod_basic_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_none_a3(self):
		"""Test fmod as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_none_a4(self):
		"""Test fmod as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_array_num_array_b1(self):
		"""Test fmod as *array-num-array* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_array_b2(self):
		"""Test fmod as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_array_b3(self):
		"""Test fmod as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_array_b4(self):
		"""Test fmod as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_num_array_none_c1(self):
		"""Test fmod as *num-array-none* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_none_c2(self):
		"""Test fmod as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_none_c3(self):
		"""Test fmod as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_none_c4(self):
		"""Test fmod as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_num_array_array_d1(self):
		"""Test fmod as *num-array-array* for basic function - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_array_d2(self):
		"""Test fmod as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_array_d3(self):
		"""Test fmod as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_array_d4(self):
		"""Test fmod as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_array_array_none_e1(self):
		"""Test fmod as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_none_e2(self):
		"""Test fmod as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_none_e3(self):
		"""Test fmod as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.fmod(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_none_e4(self):
		"""Test fmod as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.fmod(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_array_e5(self):
		"""Test fmod as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_array_array_array_e6(self):
		"""Test fmod as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_array_e7(self):
		"""Test fmod as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.fmod(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class fmod_param_errors_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.floatarray2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_fmod_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(intarray1, testfloat)


	########################################################
	def test_fmod_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(floatarray1, testint)


	########################################################
	def test_fmod_array_num_none_a3(self):
		"""Test fmod as *array-num-none* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(intarray1, testint)


	########################################################
	def test_fmod_array_num_none_a4(self):
		"""Test fmod as *array-num-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, errors='a')


	########################################################
	def test_fmod_array_num_none_a5(self):
		"""Test fmod as *array-num-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, maxlen='a')



	########################################################
	def test_fmod_array_num_array_b1(self):
		"""Test fmod as *array-num-array* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(intarray1, testfloat, self.dataout)


	########################################################
	def test_fmod_array_num_array_b2(self):
		"""Test fmod as *array-num-array* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(self.floatarray1, testint, self.dataout)


	########################################################
	def test_fmod_array_num_array_b3(self):
		"""Test fmod as *array-num-array* for integer output array - Array code f.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(floatarray1, testfloat, self.intdataout)


	########################################################
	def test_fmod_array_num_array_b4(self):
		"""Test fmod as *array-num-array* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(self.intarray1, testint, self.intdataout)


	########################################################
	def test_fmod_array_num_array_b5(self):
		"""Test fmod as *array-num-array* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, self.dataout, errors='a')


	########################################################
	def test_fmod_array_num_array_b6(self):
		"""Test fmod as *array-num-array* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, self.dataout, maxlen='a')



	########################################################
	def test_fmod_num_array_none_c1(self):
		"""Test fmod as *num-array-none* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, intarray1)


	########################################################
	def test_fmod_num_array_none_c2(self):
		"""Test fmod as *num-array-none* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, floatarray1)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testint, floatarray1)


	########################################################
	def test_fmod_num_array_none_c3(self):
		"""Test fmod as *num-array-none* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testint, intarray1)


	########################################################
	def test_fmod_num_array_none_c4(self):
		"""Test fmod as *num-array-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, floatarray1, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, floatarray1, errors='a')


	########################################################
	def test_fmod_num_array_none_c5(self):
		"""Test fmod as *num-array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, floatarray1, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, floatarray1, maxlen='a')



	########################################################
	def test_fmod_num_array_array_d1(self):
		"""Test fmod as *num-array-array* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_fmod_num_array_array_d2(self):
		"""Test fmod as *num-array-array* for integer number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_fmod_num_array_array_d3(self):
		"""Test fmod as *num-array-array* for integer output array - Array code f.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, self.floatarray1, self.intdataout)


	########################################################
	def test_fmod_num_array_array_d4(self):
		"""Test fmod as *num-array-array* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testint, self.intarray1, self.intdataout)


	########################################################
	def test_fmod_num_array_array_d5(self):
		"""Test fmod as *num-array-array* for errors='a' - Array code f.
		"""
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, self.floatarray1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, self.intarray1, self.dataout, errors='a')


	########################################################
	def test_fmod_num_array_array_d6(self):
		"""Test fmod as *num-array-array* for maxlen='a' - Array code f.
		"""
		testfloat = self.floatarray2[0]
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, self.floatarray1, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, self.intarray1, self.dataout, maxlen='a')



	########################################################
	def test_fmod_array_array_none_e1(self):
		"""Test fmod as *array-array-none* for integer array - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, self.floatarray2)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, self.intarray2)


	########################################################
	def test_fmod_array_array_none_e2(self):
		"""Test fmod as *array-array-none* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.floatarray2)


	########################################################
	def test_fmod_array_array_none_e3(self):
		"""Test fmod as *array-array-none* for all integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.intarray2)


	########################################################
	def test_fmod_array_array_none_e4(self):
		"""Test fmod as *array-array-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, self.floatarray2, matherrors=True)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, self.floatarray2, errors='a')


	########################################################
	def test_fmod_array_array_none_e5(self):
		"""Test fmod as *array-array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, self.floatarray2, maxlen=testmaxlen)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, self.floatarray2, maxlen='a')



	########################################################
	def test_fmod_array_array_array_f1(self):
		"""Test fmod as *array-array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.intarray2, self.dataout)


	########################################################
	def test_fmod_array_array_array_f2(self):
		"""Test fmod as *array-array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.floatarray2, self.dataout)


	########################################################
	def test_fmod_array_array_array_f3(self):
		"""Test fmod as *array-array-array* for integer output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.floatarray2, self.intdataout)


	########################################################
	def test_fmod_array_array_array_f4(self):
		"""Test fmod as *array-array-array* for all integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.intarray2, self.intdataout)


	########################################################
	def test_fmod_array_array_array_f5(self):
		"""Test fmod as *array-array-array* for errors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, errors='a')


	########################################################
	def test_fmod_array_array_array_f6(self):
		"""Test fmod as *array-array-array* for maxlen='a' - Array code f.
		"""
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, maxlen='a')


	########################################################
	def test_fmod_no_params_g1(self):
		"""Test fmod with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fmod()



##############################################################################



##############################################################################
class fmod_NaN_errors_f(unittest.TestCase):
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
			return math.fmod(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('nan')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('nan')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('nan')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_fmod_NaN_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.fmod(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errordata, testval)


	########################################################
	def test_fmod_NaN_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for nan with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [self.PyOp(x, testval, float('nan')) for x in self.errordata]

				arrayfunc.fmod(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_array_num_array_b1(self):
		"""Test fmod as *array-num-array* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.fmod(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errordata, testval, self.dataout)


	########################################################
	def test_fmod_NaN_array_num_array_b2(self):
		"""Test fmod as *array-num-array* for nan with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [self.PyOp(x, testval, float('nan')) for x in self.errordata]

				arrayfunc.fmod(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_num_array_none_c1(self):
		"""Test fmod as *num-array-none* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.fmod(testval, dataok1)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(testval, errordata)


	########################################################
	def test_fmod_NaN_num_array_none_c2(self):
		"""Test fmod as *num-array-none* for nan with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expectedpe = [self.PyOp(testval, x, float('nan')) for x in self.errordata]

				arrayfunc.fmod(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_num_array_array_d1(self):
		"""Test fmod as *num-array-array* for nan - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.fmod(testval, self.dataok1, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(testval, self.errordata, self.dataout)


	########################################################
	def test_fmod_NaN_num_array_array_d2(self):
		"""Test fmod as *num-array-array* for nan with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedpe = [self.PyOp(testval, x, float('nan')) for x in self.errordata]

				arrayfunc.fmod(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_array_array_none_e1(self):
		"""Test fmod as *array-array-none* for nan - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.fmod(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(dataok1, self.errordata)


	########################################################
	def test_fmod_NaN_array_array_none_e2(self):
		"""Test fmod as *array-array-none* for nan with error check off - Array code f.
		"""
		arrayfunc.fmod(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_array_array_array_f1(self):
		"""Test fmod as *array-array-array* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_fmod_NaN_array_array_array_f2(self):
		"""Test fmod as *array-array-array* for nan with error check off - Array code f.
		"""
		arrayfunc.fmod(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class fmod_inf_noerrors_f(unittest.TestCase):
	"""Test for fmod(x, y) operation using parameter inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# A "1" suffix means the data is meant for the first parameter. 
		# A "2" suffix means the data is meant for the second parameter.
		self.okarray1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.okarray2 = array.array('f', [x for x,y in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.okarray1)])


		# This is how long the test arrays should be.
		testarraysize = len(self.okarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, testarraysize))

		self.errorarray = array.array('f', [float('inf')] * testarraysize)
		self.errorparam = float('inf')

		# When error data is calculated with error checking off, the result is
		# always NaN.
		self.nanresult = [float('nan')] * testarraysize



	########################################################
	def test_fmod_inf_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for error array with error check on - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval)


	########################################################
	def test_fmod_inf_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for error array with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				# The output goes into the first array.
				arrayfunc.fmod(errorarray, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_array_a3(self):
		"""Test fmod as *array-num-array* for error array with error check on - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval, self.dataout)


	########################################################
	def test_fmod_inf_array_num_array_a4(self):
		"""Test fmod as *array-num-array* for error array with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.fmod(self.errorarray, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_none_a5(self):
		"""Test fmod as *array-num-none* for error number with error check on - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_none_a6(self):
		"""Test fmod as *array-num-none* for error number with error check off - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_array_a7(self):
		"""Test fmod as *array-num-array* for error number with error check on - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_array_a8(self):
		"""Test fmod as *array-num-array* for error number with error check off - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_inf_num_array_none_b1(self):
		"""Test fmod as *num-array-none* for error number with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray2 = copy.copy(self.okarray2)

				# This version is expected to pass.
				arrayfunc.fmod(testval, okarray2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, okarray2)


	########################################################
	def test_fmod_inf_num_array_none_b2(self):
		"""Test fmod as *num-array-none* for error number with error check off - Array code f.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorparam, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray2, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_array_b3(self):
		"""Test fmod as *num-array-array* for error number with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.fmod(testval, self.okarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout)


	########################################################
	def test_fmod_inf_num_array_array_b4(self):
		"""Test fmod as *num-array-array* for error number with error check off - Array code f.
		"""
		arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_inf_num_array_none_b5(self):
		"""Test fmod as *num-array-none* for error array with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_none_b6(self):
		"""Test fmod as *num-array-none* for error array with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_array_b7(self):
		"""Test fmod as *num-array-array* for error array with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_array_b8(self):
		"""Test fmod as *num-array-array* for error array with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_inf_array_array_none_c1(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2)


	########################################################
	def test_fmod_inf_array_array_none_c2(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code f.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorarray, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.errorarray, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_array_c3(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout)


	########################################################
	def test_fmod_inf_array_array_array_c4(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code f.
		"""
		arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_none_c5(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_none_c6(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_array_c7(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_array_c8(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class fmod_ninf_noerrors_f(unittest.TestCase):
	"""Test for fmod(x, y) operation using parameter -inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# A "1" suffix means the data is meant for the first parameter. 
		# A "2" suffix means the data is meant for the second parameter.
		self.okarray1 = array.array('f', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.okarray2 = array.array('f', [x for x,y in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.okarray1)])


		# This is how long the test arrays should be.
		testarraysize = len(self.okarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, testarraysize))

		self.errorarray = array.array('f', [float('-inf')] * testarraysize)
		self.errorparam = float('-inf')

		# When error data is calculated with error checking off, the result is
		# always NaN.
		self.nanresult = [float('nan')] * testarraysize



	########################################################
	def test_fmod_ninf_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for error array with error check on - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval)


	########################################################
	def test_fmod_ninf_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for error array with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				# The output goes into the first array.
				arrayfunc.fmod(errorarray, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_array_a3(self):
		"""Test fmod as *array-num-array* for error array with error check on - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval, self.dataout)


	########################################################
	def test_fmod_ninf_array_num_array_a4(self):
		"""Test fmod as *array-num-array* for error array with error check off - Array code f.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.fmod(self.errorarray, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_none_a5(self):
		"""Test fmod as *array-num-none* for error number with error check on - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_none_a6(self):
		"""Test fmod as *array-num-none* for error number with error check off - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_array_a7(self):
		"""Test fmod as *array-num-array* for error number with error check on - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_array_a8(self):
		"""Test fmod as *array-num-array* for error number with error check off - Array code f.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_ninf_num_array_none_b1(self):
		"""Test fmod as *num-array-none* for error number with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray2 = copy.copy(self.okarray2)

				# This version is expected to pass.
				arrayfunc.fmod(testval, okarray2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, okarray2)


	########################################################
	def test_fmod_ninf_num_array_none_b2(self):
		"""Test fmod as *num-array-none* for error number with error check off - Array code f.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorparam, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray2, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_array_b3(self):
		"""Test fmod as *num-array-array* for error number with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.fmod(testval, self.okarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout)


	########################################################
	def test_fmod_ninf_num_array_array_b4(self):
		"""Test fmod as *num-array-array* for error number with error check off - Array code f.
		"""
		arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_ninf_num_array_none_b5(self):
		"""Test fmod as *num-array-none* for error array with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_none_b6(self):
		"""Test fmod as *num-array-none* for error array with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_array_b7(self):
		"""Test fmod as *num-array-array* for error array with error check on - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_array_b8(self):
		"""Test fmod as *num-array-array* for error array with error check off - Array code f.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_ninf_array_array_none_c1(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2)


	########################################################
	def test_fmod_ninf_array_array_none_c2(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code f.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorarray, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.errorarray, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_array_c3(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout)


	########################################################
	def test_fmod_ninf_array_array_array_c4(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code f.
		"""
		arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_none_c5(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_none_c6(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_array_c7(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_array_c8(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code f.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class fmod_general_d(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -2.0, -1.0, 1.0, 2.0.
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
	def test_fmod_basic_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_none_a3(self):
		"""Test fmod as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_none_a4(self):
		"""Test fmod as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_array_num_array_b1(self):
		"""Test fmod as *array-num-array* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_array_b2(self):
		"""Test fmod as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.fmod(x, testval) for x in data1]

				arrayfunc.fmod(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_array_b3(self):
		"""Test fmod as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_num_array_b4(self):
		"""Test fmod as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_num_array_none_c1(self):
		"""Test fmod as *num-array-none* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_none_c2(self):
		"""Test fmod as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_none_c3(self):
		"""Test fmod as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_none_c4(self):
		"""Test fmod as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.fmod(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_num_array_array_d1(self):
		"""Test fmod as *num-array-array* for basic function - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_array_d2(self):
		"""Test fmod as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.fmod(testval, x) for x in data1]

				arrayfunc.fmod(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_array_d3(self):
		"""Test fmod as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_num_array_array_d4(self):
		"""Test fmod as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.fmod(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.fmod(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_array_array_none_e1(self):
		"""Test fmod as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_none_e2(self):
		"""Test fmod as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_none_e3(self):
		"""Test fmod as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.fmod(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_none_e4(self):
		"""Test fmod as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])

		limited = len(data1) // 2

		pydataout = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.fmod(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_array_e5(self):
		"""Test fmod as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_basic_array_array_array_e6(self):
		"""Test fmod as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		expected = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.fmod(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_basic_array_array_array_e7(self):
		"""Test fmod as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		data2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), data1)])
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [math.fmod(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.fmod(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class fmod_param_errors_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.floatarray2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_fmod_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(intarray1, testfloat)


	########################################################
	def test_fmod_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(floatarray1, testint)


	########################################################
	def test_fmod_array_num_none_a3(self):
		"""Test fmod as *array-num-none* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(intarray1, testint)


	########################################################
	def test_fmod_array_num_none_a4(self):
		"""Test fmod as *array-num-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, errors='a')


	########################################################
	def test_fmod_array_num_none_a5(self):
		"""Test fmod as *array-num-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, maxlen='a')



	########################################################
	def test_fmod_array_num_array_b1(self):
		"""Test fmod as *array-num-array* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(intarray1, testfloat, self.dataout)


	########################################################
	def test_fmod_array_num_array_b2(self):
		"""Test fmod as *array-num-array* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(self.floatarray1, testint, self.dataout)


	########################################################
	def test_fmod_array_num_array_b3(self):
		"""Test fmod as *array-num-array* for integer output array - Array code d.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(floatarray1, testfloat, self.intdataout)


	########################################################
	def test_fmod_array_num_array_b4(self):
		"""Test fmod as *array-num-array* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(self.intarray1, testint, self.intdataout)


	########################################################
	def test_fmod_array_num_array_b5(self):
		"""Test fmod as *array-num-array* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, self.dataout, errors='a')


	########################################################
	def test_fmod_array_num_array_b6(self):
		"""Test fmod as *array-num-array* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, testfloat, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, testfloat, self.dataout, maxlen='a')



	########################################################
	def test_fmod_num_array_none_c1(self):
		"""Test fmod as *num-array-none* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, intarray1)


	########################################################
	def test_fmod_num_array_none_c2(self):
		"""Test fmod as *num-array-none* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, floatarray1)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testint, floatarray1)


	########################################################
	def test_fmod_num_array_none_c3(self):
		"""Test fmod as *num-array-none* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testint, intarray1)


	########################################################
	def test_fmod_num_array_none_c4(self):
		"""Test fmod as *num-array-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, floatarray1, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, floatarray1, errors='a')


	########################################################
	def test_fmod_num_array_none_c5(self):
		"""Test fmod as *num-array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, floatarray1, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, floatarray1, maxlen='a')



	########################################################
	def test_fmod_num_array_array_d1(self):
		"""Test fmod as *num-array-array* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_fmod_num_array_array_d2(self):
		"""Test fmod as *num-array-array* for integer number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_fmod_num_array_array_d3(self):
		"""Test fmod as *num-array-array* for integer output array - Array code d.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testfloat, self.floatarray1, self.intdataout)


	########################################################
	def test_fmod_num_array_array_d4(self):
		"""Test fmod as *num-array-array* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.fmod(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.fmod(testint, self.intarray1, self.intdataout)


	########################################################
	def test_fmod_num_array_array_d5(self):
		"""Test fmod as *num-array-array* for errors='a' - Array code d.
		"""
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, self.floatarray1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, self.intarray1, self.dataout, errors='a')


	########################################################
	def test_fmod_num_array_array_d6(self):
		"""Test fmod as *num-array-array* for maxlen='a' - Array code d.
		"""
		testfloat = self.floatarray2[0]
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(testfloat, self.floatarray1, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(testfloat, self.intarray1, self.dataout, maxlen='a')



	########################################################
	def test_fmod_array_array_none_e1(self):
		"""Test fmod as *array-array-none* for integer array - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, self.floatarray2)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, self.intarray2)


	########################################################
	def test_fmod_array_array_none_e2(self):
		"""Test fmod as *array-array-none* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.floatarray2)


	########################################################
	def test_fmod_array_array_none_e3(self):
		"""Test fmod as *array-array-none* for all integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.intarray2)


	########################################################
	def test_fmod_array_array_none_e4(self):
		"""Test fmod as *array-array-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, self.floatarray2, matherrors=True)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, self.floatarray2, errors='a')


	########################################################
	def test_fmod_array_array_none_e5(self):
		"""Test fmod as *array-array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(floatarray1, self.floatarray2, maxlen=testmaxlen)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(floatarray1, self.floatarray2, maxlen='a')



	########################################################
	def test_fmod_array_array_array_f1(self):
		"""Test fmod as *array-array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.intarray2, self.dataout)


	########################################################
	def test_fmod_array_array_array_f2(self):
		"""Test fmod as *array-array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.floatarray2, self.dataout)


	########################################################
	def test_fmod_array_array_array_f3(self):
		"""Test fmod as *array-array-array* for integer output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.floatarray2, self.intdataout)


	########################################################
	def test_fmod_array_array_array_f4(self):
		"""Test fmod as *array-array-array* for all integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.intarray1, self.intarray2, self.intdataout)


	########################################################
	def test_fmod_array_array_array_f5(self):
		"""Test fmod as *array-array-array* for errors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, errors='a')


	########################################################
	def test_fmod_array_array_array_f6(self):
		"""Test fmod as *array-array-array* for maxlen='a' - Array code d.
		"""
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fmod(self.floatarray1, self.floatarray2, self.dataout, maxlen='a')


	########################################################
	def test_fmod_no_params_g1(self):
		"""Test fmod with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fmod()



##############################################################################



##############################################################################
class fmod_NaN_errors_d(unittest.TestCase):
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
			return math.fmod(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.dataok1)])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('nan')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('nan')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('nan')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_fmod_NaN_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.fmod(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errordata, testval)


	########################################################
	def test_fmod_NaN_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for nan with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [self.PyOp(x, testval, float('nan')) for x in self.errordata]

				arrayfunc.fmod(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_array_num_array_b1(self):
		"""Test fmod as *array-num-array* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.fmod(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errordata, testval, self.dataout)


	########################################################
	def test_fmod_NaN_array_num_array_b2(self):
		"""Test fmod as *array-num-array* for nan with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [self.PyOp(x, testval, float('nan')) for x in self.errordata]

				arrayfunc.fmod(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_num_array_none_c1(self):
		"""Test fmod as *num-array-none* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.fmod(testval, dataok1)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(testval, errordata)


	########################################################
	def test_fmod_NaN_num_array_none_c2(self):
		"""Test fmod as *num-array-none* for nan with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expectedpe = [self.PyOp(testval, x, float('nan')) for x in self.errordata]

				arrayfunc.fmod(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_num_array_array_d1(self):
		"""Test fmod as *num-array-array* for nan - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.fmod(testval, self.dataok1, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(testval, self.errordata, self.dataout)


	########################################################
	def test_fmod_NaN_num_array_array_d2(self):
		"""Test fmod as *num-array-array* for nan with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedpe = [self.PyOp(testval, x, float('nan')) for x in self.errordata]

				arrayfunc.fmod(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_array_array_none_e1(self):
		"""Test fmod as *array-array-none* for nan - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.fmod(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(dataok1, self.errordata)


	########################################################
	def test_fmod_NaN_array_array_none_e2(self):
		"""Test fmod as *array-array-none* for nan with error check off - Array code d.
		"""
		arrayfunc.fmod(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_NaN_array_array_array_f1(self):
		"""Test fmod as *array-array-array* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_fmod_NaN_array_array_array_f2(self):
		"""Test fmod as *array-array-array* for nan with error check off - Array code d.
		"""
		arrayfunc.fmod(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class fmod_inf_noerrors_d(unittest.TestCase):
	"""Test for fmod(x, y) operation using parameter inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# A "1" suffix means the data is meant for the first parameter. 
		# A "2" suffix means the data is meant for the second parameter.
		self.okarray1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.okarray2 = array.array('d', [x for x,y in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.okarray1)])


		# This is how long the test arrays should be.
		testarraysize = len(self.okarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, testarraysize))

		self.errorarray = array.array('d', [float('inf')] * testarraysize)
		self.errorparam = float('inf')

		# When error data is calculated with error checking off, the result is
		# always NaN.
		self.nanresult = [float('nan')] * testarraysize



	########################################################
	def test_fmod_inf_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for error array with error check on - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval)


	########################################################
	def test_fmod_inf_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for error array with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				# The output goes into the first array.
				arrayfunc.fmod(errorarray, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_array_a3(self):
		"""Test fmod as *array-num-array* for error array with error check on - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval, self.dataout)


	########################################################
	def test_fmod_inf_array_num_array_a4(self):
		"""Test fmod as *array-num-array* for error array with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.fmod(self.errorarray, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_none_a5(self):
		"""Test fmod as *array-num-none* for error number with error check on - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_none_a6(self):
		"""Test fmod as *array-num-none* for error number with error check off - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_array_a7(self):
		"""Test fmod as *array-num-array* for error number with error check on - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_num_array_a8(self):
		"""Test fmod as *array-num-array* for error number with error check off - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_inf_num_array_none_b1(self):
		"""Test fmod as *num-array-none* for error number with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray2 = copy.copy(self.okarray2)

				# This version is expected to pass.
				arrayfunc.fmod(testval, okarray2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, okarray2)


	########################################################
	def test_fmod_inf_num_array_none_b2(self):
		"""Test fmod as *num-array-none* for error number with error check off - Array code d.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorparam, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray2, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_array_b3(self):
		"""Test fmod as *num-array-array* for error number with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.fmod(testval, self.okarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout)


	########################################################
	def test_fmod_inf_num_array_array_b4(self):
		"""Test fmod as *num-array-array* for error number with error check off - Array code d.
		"""
		arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_inf_num_array_none_b5(self):
		"""Test fmod as *num-array-none* for error array with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_none_b6(self):
		"""Test fmod as *num-array-none* for error array with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_array_b7(self):
		"""Test fmod as *num-array-array* for error array with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_num_array_array_b8(self):
		"""Test fmod as *num-array-array* for error array with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_inf_array_array_none_c1(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2)


	########################################################
	def test_fmod_inf_array_array_none_c2(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code d.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorarray, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.errorarray, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_array_c3(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout)


	########################################################
	def test_fmod_inf_array_array_array_c4(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code d.
		"""
		arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_none_c5(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_none_c6(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_array_c7(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_inf_array_array_array_c8(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class fmod_ninf_noerrors_d(unittest.TestCase):
	"""Test for fmod(x, y) operation using parameter -inf.
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# A "1" suffix means the data is meant for the first parameter. 
		# A "2" suffix means the data is meant for the second parameter.
		self.okarray1 = array.array('d', [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0])
		self.okarray2 = array.array('d', [x for x,y in zip(itertools.cycle([-2.0, -1.0, 1.0, 2.0]), self.okarray1)])


		# This is how long the test arrays should be.
		testarraysize = len(self.okarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, testarraysize))

		self.errorarray = array.array('d', [float('-inf')] * testarraysize)
		self.errorparam = float('-inf')

		# When error data is calculated with error checking off, the result is
		# always NaN.
		self.nanresult = [float('nan')] * testarraysize



	########################################################
	def test_fmod_ninf_array_num_none_a1(self):
		"""Test fmod as *array-num-none* for error array with error check on - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval)


	########################################################
	def test_fmod_ninf_array_num_none_a2(self):
		"""Test fmod as *array-num-none* for error array with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				# The output goes into the first array.
				arrayfunc.fmod(errorarray, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_array_a3(self):
		"""Test fmod as *array-num-array* for error array with error check on - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.fmod(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(errorarray, testval, self.dataout)


	########################################################
	def test_fmod_ninf_array_num_array_a4(self):
		"""Test fmod as *array-num-array* for error array with error check off - Array code d.
		"""
		for testval in [-2.0, -1.0, 1.0, 2.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.fmod(self.errorarray, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_none_a5(self):
		"""Test fmod as *array-num-none* for error number with error check on - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_none_a6(self):
		"""Test fmod as *array-num-none* for error number with error check off - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorparam, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_array_a7(self):
		"""Test fmod as *array-num-array* for error number with error check on - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_num_array_a8(self):
		"""Test fmod as *array-num-array* for error number with error check off - Array code d.
		"""
		expected = [math.fmod(x, self.errorparam) for x in self.okarray1]

		arrayfunc.fmod(self.okarray1, self.errorparam, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_ninf_num_array_none_b1(self):
		"""Test fmod as *num-array-none* for error number with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray2 = copy.copy(self.okarray2)

				# This version is expected to pass.
				arrayfunc.fmod(testval, okarray2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, okarray2)


	########################################################
	def test_fmod_ninf_num_array_none_b2(self):
		"""Test fmod as *num-array-none* for error number with error check off - Array code d.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorparam, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray2, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_array_b3(self):
		"""Test fmod as *num-array-array* for error number with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.fmod(testval, self.okarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout)


	########################################################
	def test_fmod_ninf_num_array_array_b4(self):
		"""Test fmod as *num-array-array* for error number with error check off - Array code d.
		"""
		arrayfunc.fmod(self.errorparam, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_ninf_num_array_none_b5(self):
		"""Test fmod as *num-array-none* for error array with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_none_b6(self):
		"""Test fmod as *num-array-none* for error array with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [math.fmod(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.fmod(testval, errorarray, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_array_b7(self):
		"""Test fmod as *num-array-array* for error array with error check on - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_num_array_array_b8(self):
		"""Test fmod as *num-array-array* for error array with error check off - Array code d.
		"""
		for testval in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.fmod(testval, x) for x in self.errorarray]

				arrayfunc.fmod(testval, self.errorarray, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fmod_ninf_array_array_none_c1(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2)


	########################################################
	def test_fmod_ninf_array_array_none_c2(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code d.
		"""
		# The output goes into the first array.
		arrayfunc.fmod(self.errorarray, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.errorarray, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_array_c3(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fmod(self.okarray1, self.okarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout)


	########################################################
	def test_fmod_ninf_array_array_array_c4(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code d.
		"""
		arrayfunc.fmod(self.errorarray, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_none_c5(self):
		"""Test fmod as *array-array-none* for error array with error check on - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_none_c6(self):
		"""Test fmod as *array-array-none* for error array with error check off - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.fmod(self.okarray1, self.errorarray, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_array_c7(self):
		"""Test fmod as *array-array-array* for error array with error check on - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fmod_ninf_array_array_array_c8(self):
		"""Test fmod as *array-array-array* for error array with error check off - Array code d.
		"""
		expected = [math.fmod(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.fmod(self.okarray1, self.errorarray, self.dataout, matherrors=True)

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
			f.write('fmod\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
