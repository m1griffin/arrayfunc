#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_pow.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      01-Jul-2019.
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
"""This conducts unit tests for pow.
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
class pow_general_even_arraysize_b(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('b', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_b(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('b', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax)
		data2 = array.array('b', self.datay)
		dataout = array.array('b', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_b(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('b', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('b', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code b.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_b(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('b', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('b', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code b.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_negy_b(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_negy_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.datax1 = array.array('b', [0,1,2,3,4,5,6,7,8,9])
		self.datax2 = copy.copy(self.datax1)
		self.datay1 = array.array('b', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax1)])
		self.datay2 = copy.copy(self.datay1)

		self.minus1 = array.array('b', [-1] * len(self.datax1))

		self.dataout = array.array('b', itertools.repeat(0, len(self.datax1)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** -1 with matherrors=True  - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2, -1, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** -1 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, -1, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** -1 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** -1 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** -1 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** -1 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_pow_error_b(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('b', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('b', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('b', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('b', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_B(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('B', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_B(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('B', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax)
		data2 = array.array('B', self.datay)
		dataout = array.array('B', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_B(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('B', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('B', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code B.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_B(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('B', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('B', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code B.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_pow_error_B(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('B', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('B', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('B', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('B', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_h(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('h', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_h(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('h', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax)
		data2 = array.array('h', self.datay)
		dataout = array.array('h', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_h(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('h', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('h', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code h.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_h(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('h', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('h', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code h.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_negy_h(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_negy_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.datax1 = array.array('h', [0,1,2,3,4,5,6,7,8,9])
		self.datax2 = copy.copy(self.datax1)
		self.datay1 = array.array('h', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax1)])
		self.datay2 = copy.copy(self.datay1)

		self.minus1 = array.array('h', [-1] * len(self.datax1))

		self.dataout = array.array('h', itertools.repeat(0, len(self.datax1)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** -1 with matherrors=True  - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2, -1, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** -1 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, -1, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** -1 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** -1 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** -1 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** -1 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_pow_error_h(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('h', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('h', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('h', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('h', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_H(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('H', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_H(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('H', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax)
		data2 = array.array('H', self.datay)
		dataout = array.array('H', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_H(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('H', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('H', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code H.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_H(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('H', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('H', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code H.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_pow_error_H(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('H', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('H', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('H', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('H', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_i(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('i', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_i(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('i', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax)
		data2 = array.array('i', self.datay)
		dataout = array.array('i', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_i(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('i', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('i', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code i.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_i(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('i', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('i', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code i.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_negy_i(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_negy_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.datax1 = array.array('i', [0,1,2,3,4,5,6,7,8,9])
		self.datax2 = copy.copy(self.datax1)
		self.datay1 = array.array('i', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax1)])
		self.datay2 = copy.copy(self.datay1)

		self.minus1 = array.array('i', [-1] * len(self.datax1))

		self.dataout = array.array('i', itertools.repeat(0, len(self.datax1)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** -1 with matherrors=True  - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2, -1, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** -1 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, -1, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** -1 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** -1 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** -1 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** -1 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_pow_error_i(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('i', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('i', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('i', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('i', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_I(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('I', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_I(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('I', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax)
		data2 = array.array('I', self.datay)
		dataout = array.array('I', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_I(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('I', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('I', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code I.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_I(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('I', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('I', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code I.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_pow_error_I(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('I', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('I', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('I', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('I', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_l(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('l', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_l(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('l', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax)
		data2 = array.array('l', self.datay)
		dataout = array.array('l', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_l(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('l', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('l', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code l.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_l(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('l', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('l', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code l.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_negy_l(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_negy_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.datax1 = array.array('l', [0,1,2,3,4,5,6,7,8,9])
		self.datax2 = copy.copy(self.datax1)
		self.datay1 = array.array('l', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax1)])
		self.datay2 = copy.copy(self.datay1)

		self.minus1 = array.array('l', [-1] * len(self.datax1))

		self.dataout = array.array('l', itertools.repeat(0, len(self.datax1)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** -1 with matherrors=True  - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2, -1, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** -1 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, -1, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** -1 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** -1 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** -1 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** -1 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_pow_error_l(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('l', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('l', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('l', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('l', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_L(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('L', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_L(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('L', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax)
		data2 = array.array('L', self.datay)
		dataout = array.array('L', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_L(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('L', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('L', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code L.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_L(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('L', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('L', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code L.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_pow_error_L(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('L', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('L', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('L', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('L', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_q(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('q', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_q(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('q', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax)
		data2 = array.array('q', self.datay)
		dataout = array.array('q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_q(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('q', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('q', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_q(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('q', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('q', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_negy_q(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_negy_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.datax1 = array.array('q', [0,1,2,3,4,5,6,7,8,9])
		self.datax2 = copy.copy(self.datax1)
		self.datay1 = array.array('q', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax1)])
		self.datay2 = copy.copy(self.datay1)

		self.minus1 = array.array('q', [-1] * len(self.datax1))

		self.dataout = array.array('q', itertools.repeat(0, len(self.datax1)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** -1 with matherrors=True  - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2, -1, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, -1, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** -1 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, -1, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** -1 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.minus1, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** -1 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** -1 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2, self.minus1, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** -1 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_pow_error_q(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('q', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('q', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('q', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('q', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_Q(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('Q', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_Q(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0,1,2.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		self.datax = array.array('Q', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax)
		data2 = array.array('Q', self.datay)
		dataout = array.array('Q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_Q(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('Q', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('Q', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_Q(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('Q', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('Q', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_pow_error_Q(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('Q', range(0, 127, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('Q', [x for (x,y) in zip(itertools.cycle([0,1,2]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('Q', [2] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('Q', itertools.repeat(0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 127 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 127 with matherrors=True  - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 127 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, 127, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 127 with matherrors=True - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 127, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 127 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 127 with matherrors=True - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 127 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(2, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 127 with matherrors=True - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 127 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 127 with matherrors=True - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 127 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 127 with matherrors=True - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class pow_general_even_arraysize_f(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0.0,1.0,2.0.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.datax = array.array('f', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_f(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0.0,1.0,2.0.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.datax = array.array('f', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax)
		data2 = array.array('f', self.datay)
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_f(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.testarray2 = array.array('f', [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])
		self.badarray2 = array.array('i', [int(x) for x in self.testarray2])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code f.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_f(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('f', [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_pow_error_f(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('f', range(0, 1100, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('f', [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('f', [2.0] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('f', itertools.repeat(0.0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 1100.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, 1100.0)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 1100.0 with matherrors=True  - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 1100.0, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 1100.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, 1100.0, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 1100.0 with matherrors=True - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 1100.0, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 1100.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(2.0, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 1100.0 with matherrors=True - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2.0, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 1100.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(2.0, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 1100.0 with matherrors=True - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2.0, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 1100.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 1100.0 with matherrors=True - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 1100.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 1100.0 with matherrors=True - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class pow_NaN_pow_f(unittest.TestCase):
	"""Test pow for basic general function operation using parameter nan.
	nan_data_pow_template
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

		self.dataok1 = array.array('f', [-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0])
		self.dataok2 = array.array('f', [-2.0, 3.0, -4.0, 5.0, 5.0, 4.0, -3.0, 2.0])

		arraysize = len(self.dataok1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('nan')] * arraysize)



	########################################################
	def test_pow_NaN_array_num_none_a1(self):
		"""Test pow as *array-num-none* for nan - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval)
				else:
					arrayfunc.pow(errordata, testval)
					for dataoutitem, expecteditem in zip(errordata, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_num_none_a2(self):
		"""Test pow as *array-num-none* for nan with error check off - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.pow(x, testval) for x in errordata]

				arrayfunc.pow(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_array_num_array_b1(self):
		"""Test pow as *array-num-array* for nan - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval, self.dataout)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval, self.dataout)
				else:
					arrayfunc.pow(errordata, testval, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_num_array_b2(self):
		"""Test pow as *array-num-array* for nan with error check off - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(x, testval) for x in self.errordata]

				arrayfunc.pow(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_num_array_none_c1(self):
		"""Test pow as *num-array-none* for nan - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(testval, dataok2)

				expected = [math.pow(testval, x) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, errordata)
				else:
					arrayfunc.pow(testval, errordata)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_num_array_none_c2(self):
		"""Test pow as *num-array-none* for nan with error check off - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_num_array_array_d1(self):
		"""Test pow as *num-array-array* for nan - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.pow(testval, self.dataok2, self.dataout)

				expected = [math.pow(testval, x) for x in self.errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, self.errordata, self.dataout)
				else:
					arrayfunc.pow(testval, self.errordata, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_num_array_array_d2(self):
		"""Test pow as *num-array-array* for nan with error check off - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_array_array_none_e1(self):
		"""Test pow as *array-array-none* for nan - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.pow(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		expected = [math.pow(x, y) for x,y in zip(dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(dataok1, self.errordata)
		else:
			arrayfunc.pow(dataok1, self.errordata)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_array_none_e2(self):
		"""Test pow as *array-array-none* for nan with error check off - Array code f.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok2, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok2, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_array_array_array_f1(self):
		"""Test pow as *array-array-array* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.dataok1, self.dataok2, self.dataout)

		expected = [math.pow(x, y) for x,y in zip(self.dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
		else:
			arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_array_array_f2(self):
		"""Test pow as *array-array-array* for nan with error check off - Array code f.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class pow_inf_pow_f(unittest.TestCase):
	"""Test pow for basic general function operation using parameter inf.
	nan_data_pow_template
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

		self.dataok1 = array.array('f', [-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0])
		self.dataok2 = array.array('f', [-2.0, 3.0, -4.0, 5.0, 5.0, 4.0, -3.0, 2.0])

		arraysize = len(self.dataok1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('inf')] * arraysize)



	########################################################
	def test_pow_inf_array_num_none_a1(self):
		"""Test pow as *array-num-none* for inf - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval)
				else:
					arrayfunc.pow(errordata, testval)
					for dataoutitem, expecteditem in zip(errordata, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_num_none_a2(self):
		"""Test pow as *array-num-none* for inf with error check off - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.pow(x, testval) for x in errordata]

				arrayfunc.pow(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_array_num_array_b1(self):
		"""Test pow as *array-num-array* for inf - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval, self.dataout)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval, self.dataout)
				else:
					arrayfunc.pow(errordata, testval, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_num_array_b2(self):
		"""Test pow as *array-num-array* for inf with error check off - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(x, testval) for x in self.errordata]

				arrayfunc.pow(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_num_array_none_c1(self):
		"""Test pow as *num-array-none* for inf - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(testval, dataok2)

				expected = [math.pow(testval, x) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, errordata)
				else:
					arrayfunc.pow(testval, errordata)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_num_array_none_c2(self):
		"""Test pow as *num-array-none* for inf with error check off - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_num_array_array_d1(self):
		"""Test pow as *num-array-array* for inf - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.pow(testval, self.dataok2, self.dataout)

				expected = [math.pow(testval, x) for x in self.errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, self.errordata, self.dataout)
				else:
					arrayfunc.pow(testval, self.errordata, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_num_array_array_d2(self):
		"""Test pow as *num-array-array* for inf with error check off - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_array_array_none_e1(self):
		"""Test pow as *array-array-none* for inf - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.pow(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		expected = [math.pow(x, y) for x,y in zip(dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(dataok1, self.errordata)
		else:
			arrayfunc.pow(dataok1, self.errordata)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_array_none_e2(self):
		"""Test pow as *array-array-none* for inf with error check off - Array code f.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok2, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok2, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_array_array_array_f1(self):
		"""Test pow as *array-array-array* for inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.dataok1, self.dataok2, self.dataout)

		expected = [math.pow(x, y) for x,y in zip(self.dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
		else:
			arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_array_array_f2(self):
		"""Test pow as *array-array-array* for inf with error check off - Array code f.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class pow_ninf_pow_f(unittest.TestCase):
	"""Test pow for basic general function operation using parameter -inf.
	nan_data_pow_template
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

		self.dataok1 = array.array('f', [-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0])
		self.dataok2 = array.array('f', [-2.0, 3.0, -4.0, 5.0, 5.0, 4.0, -3.0, 2.0])

		arraysize = len(self.dataok1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('-inf')] * arraysize)



	########################################################
	def test_pow_ninf_array_num_none_a1(self):
		"""Test pow as *array-num-none* for -inf - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval)
				else:
					arrayfunc.pow(errordata, testval)
					for dataoutitem, expecteditem in zip(errordata, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_num_none_a2(self):
		"""Test pow as *array-num-none* for -inf with error check off - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.pow(x, testval) for x in errordata]

				arrayfunc.pow(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_array_num_array_b1(self):
		"""Test pow as *array-num-array* for -inf - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval, self.dataout)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval, self.dataout)
				else:
					arrayfunc.pow(errordata, testval, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_num_array_b2(self):
		"""Test pow as *array-num-array* for -inf with error check off - Array code f.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(x, testval) for x in self.errordata]

				arrayfunc.pow(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_num_array_none_c1(self):
		"""Test pow as *num-array-none* for -inf - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(testval, dataok2)

				expected = [math.pow(testval, x) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, errordata)
				else:
					arrayfunc.pow(testval, errordata)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_num_array_none_c2(self):
		"""Test pow as *num-array-none* for -inf with error check off - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_num_array_array_d1(self):
		"""Test pow as *num-array-array* for -inf - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.pow(testval, self.dataok2, self.dataout)

				expected = [math.pow(testval, x) for x in self.errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, self.errordata, self.dataout)
				else:
					arrayfunc.pow(testval, self.errordata, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_num_array_array_d2(self):
		"""Test pow as *num-array-array* for -inf with error check off - Array code f.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_array_array_none_e1(self):
		"""Test pow as *array-array-none* for -inf - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.pow(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		expected = [math.pow(x, y) for x,y in zip(dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(dataok1, self.errordata)
		else:
			arrayfunc.pow(dataok1, self.errordata)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_array_none_e2(self):
		"""Test pow as *array-array-none* for -inf with error check off - Array code f.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok2, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok2, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_array_array_array_f1(self):
		"""Test pow as *array-array-array* for -inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.dataok1, self.dataok2, self.dataout)

		expected = [math.pow(x, y) for x,y in zip(self.dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
		else:
			arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_array_array_f2(self):
		"""Test pow as *array-array-array* for -inf with error check off - Array code f.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

 

##############################################################################
class pow_general_even_arraysize_d(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0.0,1.0,2.0.
	test_op_templ
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.datax = array.array('d', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class pow_general_odd_arraysize_d(unittest.TestCase):
	"""Test pow for basic general function operation using numeric 
	data 0.0,1.0,2.0.
	test_op_templ
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.datax = array.array('d', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_pow_basic_array_num_none_a1(self):
		"""Test pow as *array-num-none* for basic function - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a2(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a3(self):
		"""Test pow as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_none_a4(self):
		"""Test pow as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_num_array_b1(self):
		"""Test pow as *array-num-array* for basic function - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b2(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				expected =  [x ** testval for x in data1] 

				arrayfunc.pow(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b3(self):
		"""Test pow as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_num_array_b4(self):
		"""Test pow as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [x ** testval for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_none_c1(self):
		"""Test pow as *num-array-none* for basic function - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c2(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c3(self):
		"""Test pow as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_none_c4(self):
		"""Test pow as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.pow(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_num_array_array_d1(self):
		"""Test pow as *num-array-array* for basic function - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d2(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				expected =  [testval ** x for x in data1] 

				arrayfunc.pow(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d3(self):
		"""Test pow as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_num_array_array_d4(self):
		"""Test pow as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout =  [testval ** x for x in data1] 
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.pow(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_none_e1(self):
		"""Test pow as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e2(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e3(self):
		"""Test pow as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_none_e4(self):
		"""Test pow as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.pow(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f1(self):
		"""Test pow as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_basic_array_array_array_f2(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		expected =  [x ** y for (x, y) in zip(data1, data2)] 
		arrayfunc.pow(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_basic_array_array_array_f3(self):
		"""Test pow as *array-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax)
		data2 = array.array('d', self.datay)
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout =  [x ** y for (x, y) in zip(data1, data2)] 
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.pow(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class pow_param_errors_d(unittest.TestCase):
	"""Test pow for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.testarray2 = array.array('d', [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])
		self.badarray2 = array.array('i', [int(x) for x in self.testarray2])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, badvalue)



	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badarray1, testvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.pow(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_pow_array_num_array_b3(self):
		"""Test pow as *array-num-array* for invalid type of output array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.pow(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testarray1, testvalue, self.baddataout)



	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, badarray2)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.pow(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(badvalue, testarray2)



	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for invalid type of number - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_pow_num_array_array_d3(self):
		"""Test pow as *num-array-array* for invalid type of output array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.pow(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.pow(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code d.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.pow(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(testarray1, self.badarray2)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2)



	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_pow_array_array_array_f3(self):
		"""Test pow as *array-array-array* for invalid type of output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_pow_no_params_g1(self):
		"""Test pow with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow()



##############################################################################



##############################################################################
class pow_opt_param_errors_d(unittest.TestCase):
	"""Test pow for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('d', [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.pow(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for matherrors='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for maxlen='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for maxlen='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.pow(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_pow_error_d(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('d', range(0, 1100, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('d', [x for (x,y) in zip(itertools.cycle([0.0,1.0,2.0]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('d', [2.0] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('d', itertools.repeat(0.0, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** 1100.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, 1100.0)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** 1100.0 with matherrors=True  - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 1100.0, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** 1100.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, 1100.0, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** 1100.0 with matherrors=True - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2.0, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, 1100.0, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** 1100.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(2.0, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** 1100.0 with matherrors=True - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2.0, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** 1100.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(2.0, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** 1100.0 with matherrors=True - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2.0, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2.0, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** 1100.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** 1100.0 with matherrors=True - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** 1100.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** 1100.0 with matherrors=True - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class pow_NaN_pow_d(unittest.TestCase):
	"""Test pow for basic general function operation using parameter nan.
	nan_data_pow_template
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

		self.dataok1 = array.array('d', [-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0])
		self.dataok2 = array.array('d', [-2.0, 3.0, -4.0, 5.0, 5.0, 4.0, -3.0, 2.0])

		arraysize = len(self.dataok1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('nan')] * arraysize)



	########################################################
	def test_pow_NaN_array_num_none_a1(self):
		"""Test pow as *array-num-none* for nan - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval)
				else:
					arrayfunc.pow(errordata, testval)
					for dataoutitem, expecteditem in zip(errordata, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_num_none_a2(self):
		"""Test pow as *array-num-none* for nan with error check off - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.pow(x, testval) for x in errordata]

				arrayfunc.pow(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_array_num_array_b1(self):
		"""Test pow as *array-num-array* for nan - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval, self.dataout)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval, self.dataout)
				else:
					arrayfunc.pow(errordata, testval, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_num_array_b2(self):
		"""Test pow as *array-num-array* for nan with error check off - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(x, testval) for x in self.errordata]

				arrayfunc.pow(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_num_array_none_c1(self):
		"""Test pow as *num-array-none* for nan - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(testval, dataok2)

				expected = [math.pow(testval, x) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, errordata)
				else:
					arrayfunc.pow(testval, errordata)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_num_array_none_c2(self):
		"""Test pow as *num-array-none* for nan with error check off - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_num_array_array_d1(self):
		"""Test pow as *num-array-array* for nan - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.pow(testval, self.dataok2, self.dataout)

				expected = [math.pow(testval, x) for x in self.errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, self.errordata, self.dataout)
				else:
					arrayfunc.pow(testval, self.errordata, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_num_array_array_d2(self):
		"""Test pow as *num-array-array* for nan with error check off - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_array_array_none_e1(self):
		"""Test pow as *array-array-none* for nan - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.pow(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		expected = [math.pow(x, y) for x,y in zip(dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(dataok1, self.errordata)
		else:
			arrayfunc.pow(dataok1, self.errordata)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_array_none_e2(self):
		"""Test pow as *array-array-none* for nan with error check off - Array code d.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok2, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok2, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_NaN_array_array_array_f1(self):
		"""Test pow as *array-array-array* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.dataok1, self.dataok2, self.dataout)

		expected = [math.pow(x, y) for x,y in zip(self.dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
		else:
			arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_NaN_array_array_array_f2(self):
		"""Test pow as *array-array-array* for nan with error check off - Array code d.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class pow_inf_pow_d(unittest.TestCase):
	"""Test pow for basic general function operation using parameter inf.
	nan_data_pow_template
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

		self.dataok1 = array.array('d', [-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0])
		self.dataok2 = array.array('d', [-2.0, 3.0, -4.0, 5.0, 5.0, 4.0, -3.0, 2.0])

		arraysize = len(self.dataok1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('inf')] * arraysize)



	########################################################
	def test_pow_inf_array_num_none_a1(self):
		"""Test pow as *array-num-none* for inf - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval)
				else:
					arrayfunc.pow(errordata, testval)
					for dataoutitem, expecteditem in zip(errordata, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_num_none_a2(self):
		"""Test pow as *array-num-none* for inf with error check off - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.pow(x, testval) for x in errordata]

				arrayfunc.pow(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_array_num_array_b1(self):
		"""Test pow as *array-num-array* for inf - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval, self.dataout)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval, self.dataout)
				else:
					arrayfunc.pow(errordata, testval, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_num_array_b2(self):
		"""Test pow as *array-num-array* for inf with error check off - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(x, testval) for x in self.errordata]

				arrayfunc.pow(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_num_array_none_c1(self):
		"""Test pow as *num-array-none* for inf - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(testval, dataok2)

				expected = [math.pow(testval, x) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, errordata)
				else:
					arrayfunc.pow(testval, errordata)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_num_array_none_c2(self):
		"""Test pow as *num-array-none* for inf with error check off - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_num_array_array_d1(self):
		"""Test pow as *num-array-array* for inf - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.pow(testval, self.dataok2, self.dataout)

				expected = [math.pow(testval, x) for x in self.errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, self.errordata, self.dataout)
				else:
					arrayfunc.pow(testval, self.errordata, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_num_array_array_d2(self):
		"""Test pow as *num-array-array* for inf with error check off - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_array_array_none_e1(self):
		"""Test pow as *array-array-none* for inf - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.pow(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		expected = [math.pow(x, y) for x,y in zip(dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(dataok1, self.errordata)
		else:
			arrayfunc.pow(dataok1, self.errordata)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_array_none_e2(self):
		"""Test pow as *array-array-none* for inf with error check off - Array code d.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok2, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok2, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_inf_array_array_array_f1(self):
		"""Test pow as *array-array-array* for inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.dataok1, self.dataok2, self.dataout)

		expected = [math.pow(x, y) for x,y in zip(self.dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
		else:
			arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_inf_array_array_array_f2(self):
		"""Test pow as *array-array-array* for inf with error check off - Array code d.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class pow_ninf_pow_d(unittest.TestCase):
	"""Test pow for basic general function operation using parameter -inf.
	nan_data_pow_template
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

		self.dataok1 = array.array('d', [-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0])
		self.dataok2 = array.array('d', [-2.0, 3.0, -4.0, 5.0, 5.0, 4.0, -3.0, 2.0])

		arraysize = len(self.dataok1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('-inf')] * arraysize)



	########################################################
	def test_pow_ninf_array_num_none_a1(self):
		"""Test pow as *array-num-none* for -inf - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval)
				else:
					arrayfunc.pow(errordata, testval)
					for dataoutitem, expecteditem in zip(errordata, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_num_none_a2(self):
		"""Test pow as *array-num-none* for -inf with error check off - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.pow(x, testval) for x in errordata]

				arrayfunc.pow(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_array_num_array_b1(self):
		"""Test pow as *array-num-array* for -inf - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(dataok1, testval, self.dataout)

				expected = [math.pow(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(errordata, testval, self.dataout)
				else:
					arrayfunc.pow(errordata, testval, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_num_array_b2(self):
		"""Test pow as *array-num-array* for -inf with error check off - Array code d.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(x, testval) for x in self.errordata]

				arrayfunc.pow(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_num_array_none_c1(self):
		"""Test pow as *num-array-none* for -inf - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.pow(testval, dataok2)

				expected = [math.pow(testval, x) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, errordata)
				else:
					arrayfunc.pow(testval, errordata)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_num_array_none_c2(self):
		"""Test pow as *num-array-none* for -inf with error check off - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_num_array_array_d1(self):
		"""Test pow as *num-array-array* for -inf - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.pow(testval, self.dataok2, self.dataout)

				expected = [math.pow(testval, x) for x in self.errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.pow(testval, self.errordata, self.dataout)
				else:
					arrayfunc.pow(testval, self.errordata, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_num_array_array_d2(self):
		"""Test pow as *num-array-array* for -inf with error check off - Array code d.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.pow(testval, x) for x in self.errordata]

				arrayfunc.pow(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_array_array_none_e1(self):
		"""Test pow as *array-array-none* for -inf - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.pow(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		expected = [math.pow(x, y) for x,y in zip(dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(dataok1, self.errordata)
		else:
			arrayfunc.pow(dataok1, self.errordata)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_array_none_e2(self):
		"""Test pow as *array-array-none* for -inf with error check off - Array code d.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok2, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok2, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_pow_ninf_array_array_array_f1(self):
		"""Test pow as *array-array-array* for -inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.dataok1, self.dataok2, self.dataout)

		expected = [math.pow(x, y) for x,y in zip(self.dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
		else:
			arrayfunc.pow(self.dataok1, self.errordata, self.dataout)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_pow_ninf_array_array_array_f2(self):
		"""Test pow as *array-array-array* for -inf with error check off - Array code d.
		"""
		expected = [math.pow(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.pow(self.dataok1, self.errordata, self.dataout, matherrors=True)

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
			f.write('pow\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
