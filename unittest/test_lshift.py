#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_lshift.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     05-Apr-2018.
# Ver:      19-Oct-2019.
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
"""This conducts unit tests for lshift.
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
class lshift_general_even_arraysize_with_simd_b(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('b', xdata)
		self.data2 = array.array('b', ydata)
		self.dataout = array.array('b', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code b.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code b.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code b.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_b(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('b', xdata)
		self.data2 = array.array('b', ydata)
		self.dataout = array.array('b', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code b.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code b.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code b.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_b(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('b', xdata)
		self.data2 = array.array('b', ydata)
		self.dataout = array.array('b', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code b.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code b.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code b.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_b(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('b', testdata1)
		self.testarray2 = array.array('b', testdata2)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code b.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_b(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('b', self.inpdata1a)
		self.inparray2a = array.array('b', self.inpdata2a)
		self.dataout = array.array('b', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code b.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code b.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_b(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('b', self.inpdata1a)
		self.inparray2a = array.array('b', self.inpdata2a)
		self.dataout = array.array('b', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code b.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_B(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('B', xdata)
		self.data2 = array.array('B', ydata)
		self.dataout = array.array('B', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code B.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code B.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code B.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_B(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('B', xdata)
		self.data2 = array.array('B', ydata)
		self.dataout = array.array('B', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code B.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code B.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code B.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_B(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('B', xdata)
		self.data2 = array.array('B', ydata)
		self.dataout = array.array('B', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code B.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code B.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code B.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_B(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('B', testdata1)
		self.testarray2 = array.array('B', testdata2)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code B.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_B(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('B', self.inpdata1a)
		self.inparray2a = array.array('B', self.inpdata2a)
		self.dataout = array.array('B', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code B.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code B.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_B(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('B', self.inpdata1a)
		self.inparray2a = array.array('B', self.inpdata2a)
		self.dataout = array.array('B', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code B.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_h(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('h', xdata)
		self.data2 = array.array('h', ydata)
		self.dataout = array.array('h', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code h.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code h.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code h.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_h(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('h', xdata)
		self.data2 = array.array('h', ydata)
		self.dataout = array.array('h', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code h.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code h.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code h.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_h(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('h', xdata)
		self.data2 = array.array('h', ydata)
		self.dataout = array.array('h', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code h.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code h.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code h.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_h(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('h', testdata1)
		self.testarray2 = array.array('h', testdata2)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code h.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_h(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('h', self.inpdata1a)
		self.inparray2a = array.array('h', self.inpdata2a)
		self.dataout = array.array('h', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code h.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code h.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_h(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('h', self.inpdata1a)
		self.inparray2a = array.array('h', self.inpdata2a)
		self.dataout = array.array('h', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code h.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_H(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('H', xdata)
		self.data2 = array.array('H', ydata)
		self.dataout = array.array('H', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code H.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code H.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code H.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_H(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('H', xdata)
		self.data2 = array.array('H', ydata)
		self.dataout = array.array('H', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code H.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code H.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code H.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_H(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('H', xdata)
		self.data2 = array.array('H', ydata)
		self.dataout = array.array('H', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code H.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code H.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code H.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_H(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('H', testdata1)
		self.testarray2 = array.array('H', testdata2)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code H.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_H(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('H', self.inpdata1a)
		self.inparray2a = array.array('H', self.inpdata2a)
		self.dataout = array.array('H', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code H.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code H.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_H(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('H', self.inpdata1a)
		self.inparray2a = array.array('H', self.inpdata2a)
		self.dataout = array.array('H', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code H.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_i(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('i', xdata)
		self.data2 = array.array('i', ydata)
		self.dataout = array.array('i', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code i.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code i.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code i.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_i(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('i', xdata)
		self.data2 = array.array('i', ydata)
		self.dataout = array.array('i', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code i.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code i.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code i.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_i(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('i', xdata)
		self.data2 = array.array('i', ydata)
		self.dataout = array.array('i', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code i.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code i.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code i.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_i(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('i', testdata1)
		self.testarray2 = array.array('i', testdata2)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code i.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_i(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('i', self.inpdata1a)
		self.inparray2a = array.array('i', self.inpdata2a)
		self.dataout = array.array('i', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code i.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code i.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_i(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('i', self.inpdata1a)
		self.inparray2a = array.array('i', self.inpdata2a)
		self.dataout = array.array('i', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code i.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_I(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('I', xdata)
		self.data2 = array.array('I', ydata)
		self.dataout = array.array('I', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code I.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code I.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code I.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_I(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('I', xdata)
		self.data2 = array.array('I', ydata)
		self.dataout = array.array('I', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code I.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code I.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code I.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_I(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('I', xdata)
		self.data2 = array.array('I', ydata)
		self.dataout = array.array('I', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code I.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code I.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code I.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_I(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('I', testdata1)
		self.testarray2 = array.array('I', testdata2)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code I.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_I(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('I', self.inpdata1a)
		self.inparray2a = array.array('I', self.inpdata2a)
		self.dataout = array.array('I', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code I.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code I.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_I(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('I', self.inpdata1a)
		self.inparray2a = array.array('I', self.inpdata2a)
		self.dataout = array.array('I', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code I.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_l(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('l', xdata)
		self.data2 = array.array('l', ydata)
		self.dataout = array.array('l', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code l.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code l.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code l.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_l(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('l', xdata)
		self.data2 = array.array('l', ydata)
		self.dataout = array.array('l', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code l.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code l.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code l.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_l(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('l', xdata)
		self.data2 = array.array('l', ydata)
		self.dataout = array.array('l', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code l.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code l.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code l.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_l(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('l', testdata1)
		self.testarray2 = array.array('l', testdata2)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code l.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_l(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('l', self.inpdata1a)
		self.inparray2a = array.array('l', self.inpdata2a)
		self.dataout = array.array('l', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code l.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code l.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_l(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('l', self.inpdata1a)
		self.inparray2a = array.array('l', self.inpdata2a)
		self.dataout = array.array('l', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code l.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_L(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('L', xdata)
		self.data2 = array.array('L', ydata)
		self.dataout = array.array('L', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code L.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code L.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code L.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_L(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('L', xdata)
		self.data2 = array.array('L', ydata)
		self.dataout = array.array('L', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code L.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code L.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code L.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_L(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('L', xdata)
		self.data2 = array.array('L', ydata)
		self.dataout = array.array('L', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code L.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code L.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code L.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_L(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('L', testdata1)
		self.testarray2 = array.array('L', testdata2)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code L.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_L(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('L', self.inpdata1a)
		self.inparray2a = array.array('L', self.inpdata2a)
		self.dataout = array.array('L', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code L.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code L.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_L(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('L', self.inpdata1a)
		self.inparray2a = array.array('L', self.inpdata2a)
		self.dataout = array.array('L', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code L.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_q(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('q', xdata)
		self.data2 = array.array('q', ydata)
		self.dataout = array.array('q', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code q.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_q(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('q', xdata)
		self.data2 = array.array('q', ydata)
		self.dataout = array.array('q', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code q.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_q(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('q', xdata)
		self.data2 = array.array('q', ydata)
		self.dataout = array.array('q', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code q.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_q(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('q', testdata1)
		self.testarray2 = array.array('q', testdata2)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_q(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('q', self.inpdata1a)
		self.inparray2a = array.array('q', self.inpdata2a)
		self.dataout = array.array('q', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_q(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('q', self.inpdata1a)
		self.inparray2a = array.array('q', self.inpdata2a)
		self.dataout = array.array('q', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_with_simd_Q(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('Q', xdata)
		self.data2 = array.array('Q', ydata)
		self.dataout = array.array('Q', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code Q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code Q.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code Q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_odd_arraysize_with_simd_Q(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('Q', xdata)
		self.data2 = array.array('Q', ydata)
		self.dataout = array.array('Q', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited )

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code Q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code Q.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code Q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout )

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class lshift_general_even_arraysize_without_simd_Q(unittest.TestCase):
	"""Test lshift for basic general function operation using numeric 
	data 0, 1, 2.
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
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([0, 1, 2]), range(testdatasize))]

		self.data1 = array.array('Q', xdata)
		self.data2 = array.array('Q', ydata)
		self.dataout = array.array('Q', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_lshift_basic_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.lshift(datax, testval, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_lshift_basic_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x << testval for x in datax]

				arrayfunc.lshift(datax, testval, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x << testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(datax, testval, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.lshift(testval, datay, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval << x for x in datay]

				arrayfunc.lshift(testval, datay, self.dataout , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval << x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.lshift(testval, datay, self.dataout, maxlen=self.limited , nosimd=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for basic function - Array code Q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.lshift(self.data1, self.data2 , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for basic function with array limit - Array code Q.
		"""
		pydataout = [x << y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.lshift(self.data1, self.data2, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_lshift_basic_array_array_array_e3(self):
		"""Test lshift as *array-array-array* for basic function - Array code Q.
		"""
		expected = [x << y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.lshift(self.data1, self.data2, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class lshift_param_errors_Q(unittest.TestCase):
	"""Test lshift for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [0,1,2,3,4,5,6,7,8,9]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('Q', testdata1)
		self.testarray2 = array.array('Q', testdata2)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue)


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, badvalue)



	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badarray1, testvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.lshift(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_lshift_array_num_array_b3(self):
		"""Test lshift as *array-num-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.lshift(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testarray1, testvalue, self.baddataout)



	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, badarray2)


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(badvalue, testarray2)



	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for invalid type of number - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_lshift_num_array_array_d3(self):
		"""Test lshift as *num-array-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.lshift(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.lshift(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.lshift(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(testarray1, self.badarray2)


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2)



	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_lshift_array_array_array_f3(self):
		"""Test lshift as *array-array-array* for invalid type of output array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.lshift(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_lshift_no_params_g1(self):
		"""Test lshift with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.lshift()


##############################################################################



##############################################################################
class lshift_opt_param_errors_Q(unittest.TestCase):
	"""Test lshift for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('Q', self.inpdata1a)
		self.inparray2a = array.array('Q', self.inpdata2a)
		self.dataout = array.array('Q', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_lshift_array_num_none_a2(self):
		"""Test lshift as *array-num-none* for matherrors=True (unsupported option) - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for maxlen='a' - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_num_array_b2(self):
		"""Test lshift as *array-num-array* for matherrors=True (unsupported option) - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_num_array_none_c2(self):
		"""Test lshift as *num-array-none* for matherrors=True (unsupported option) - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_num_array_array_d2(self):
		"""Test lshift as *num-array-array* for matherrors=True (unsupported option) - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_lshift_array_array_none_e2(self):
		"""Test lshift as *array-array-none* for matherrors=True (unsupported option) - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_lshift_array_array_array_f2(self):
		"""Test lshift as *array-array-array* for matherrors=True (unsupported option) - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class lshift_opt_nosimd_param_errors_Q(unittest.TestCase):
	"""Test lshift for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [0,1,2,3,4,5,6,7,8,9]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0, 1, 2]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('Q', self.inpdata1a)
		self.inparray2a = array.array('Q', self.inpdata2a)
		self.dataout = array.array('Q', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_lshift_array_num_none_a1(self):
		"""Test lshift as *array-num-none* for nosimd='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_lshift_array_num_array_b1(self):
		"""Test lshift as *array-num-array* for nosimd='a' - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_lshift_num_array_none_c1(self):
		"""Test lshift as *num-array-none* for nosimd='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_num_array_array_d1(self):
		"""Test lshift as *num-array-array* for nosimd='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.lshift(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_lshift_array_array_none_e1(self):
		"""Test lshift as *array-array-none* for nosimd='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_lshift_array_array_array_f1(self):
		"""Test lshift as *array-array-array* for nosimd='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.lshift(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.lshift(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



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
			f.write('lshift\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
