#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_radians.py
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
"""This conducts unit tests for radians.
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
class radians_general_even_arraysize_with_simd_f(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_noparams
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.data = array.array('f', xdata)
		self.dataout = array.array('f', [0]*len(self.data))

		self.limited = len(self.data) // 2

		# The expected results.
		self.expected = [math.radians(x) for x in self.data]

		# The expected results when the maxlen parameter is used.
		self.expectedlimiteddata = self.expected[0:self.limited] + list(self.data)[self.limited:]

		# The same, but where dataout is used as one of the sources.
		self.expectedlimiteddataout = self.expected[0:self.limited] + list(self.dataout)[self.limited:]



	########################################################
	def test_radians_basic_array_none_a1(self):
		"""Test radians as *array-none* for basic function - Array code f.
		"""
		arrayfunc.radians(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a2(self):
		"""Test radians as *array-none* for basic function with matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a3(self):
		"""Test radians as *array-none* for basic function with maxlen - Array code f.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a4(self):
		"""Test radians as *array-none* for basic function with maxlen and matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b1(self):
		"""Test radians as *array-array* for basic function - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b2(self):
		"""Test radians as *array-array* for basic function with matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b3(self):
		"""Test radians as *array-array* for basic function with maxlen - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b4(self):
		"""Test radians as *array-array* for basic function with maxlen and matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class radians_general_odd_arraysize_with_simd_f(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_noparams
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.data = array.array('f', xdata)
		self.dataout = array.array('f', [0]*len(self.data))

		self.limited = len(self.data) // 2

		# The expected results.
		self.expected = [math.radians(x) for x in self.data]

		# The expected results when the maxlen parameter is used.
		self.expectedlimiteddata = self.expected[0:self.limited] + list(self.data)[self.limited:]

		# The same, but where dataout is used as one of the sources.
		self.expectedlimiteddataout = self.expected[0:self.limited] + list(self.dataout)[self.limited:]



	########################################################
	def test_radians_basic_array_none_a1(self):
		"""Test radians as *array-none* for basic function - Array code f.
		"""
		arrayfunc.radians(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a2(self):
		"""Test radians as *array-none* for basic function with matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a3(self):
		"""Test radians as *array-none* for basic function with maxlen - Array code f.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a4(self):
		"""Test radians as *array-none* for basic function with maxlen and matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b1(self):
		"""Test radians as *array-array* for basic function - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b2(self):
		"""Test radians as *array-array* for basic function with matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b3(self):
		"""Test radians as *array-array* for basic function with maxlen - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b4(self):
		"""Test radians as *array-array* for basic function with maxlen and matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class radians_general_even_arraysize_without_simd_f(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_noparams
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.data = array.array('f', xdata)
		self.dataout = array.array('f', [0]*len(self.data))

		self.limited = len(self.data) // 2

		# The expected results.
		self.expected = [math.radians(x) for x in self.data]

		# The expected results when the maxlen parameter is used.
		self.expectedlimiteddata = self.expected[0:self.limited] + list(self.data)[self.limited:]

		# The same, but where dataout is used as one of the sources.
		self.expectedlimiteddataout = self.expected[0:self.limited] + list(self.dataout)[self.limited:]



	########################################################
	def test_radians_basic_array_none_a1(self):
		"""Test radians as *array-none* for basic function - Array code f.
		"""
		arrayfunc.radians(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a2(self):
		"""Test radians as *array-none* for basic function with matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a3(self):
		"""Test radians as *array-none* for basic function with maxlen - Array code f.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a4(self):
		"""Test radians as *array-none* for basic function with maxlen and matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b1(self):
		"""Test radians as *array-array* for basic function - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b2(self):
		"""Test radians as *array-array* for basic function with matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b3(self):
		"""Test radians as *array-array* for basic function with maxlen - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b4(self):
		"""Test radians as *array-array* for basic function with maxlen and matherrors=True - Array code f.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class radians_param_errors_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_radians_array_none_a1(self):
		"""Test radians as *array-none* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.intarray)


	########################################################
	def test_radians_array_none_b1(self):
		"""Test radians as *array-none* for matherrors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.radians(floatarray, matherrors=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(floatarray, matherrors='a')


	########################################################
	def test_radians_array_none_b2(self):
		"""Test radians as *array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)
		testmaxlen = len(floatarray) // 2

		# This version is expected to pass.
		arrayfunc.radians(floatarray, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(floatarray, maxlen='a')



	########################################################
	def test_radians_array_array_c1(self):
		"""Test radians as *array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.intarray, self.dataout)


	########################################################
	def test_radians_array_array_c2(self):
		"""Test radians as *array-array* for integer output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.intdataout)


	########################################################
	def test_radians_array_array_c3(self):
		"""Test radians as *array-array* for integer input and output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.intarray, self.intdataout)


	########################################################
	def test_radians_array_num_array_d1(self):
		"""Test radians as *array-num-array* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.dataout, matherrors='a')


	########################################################
	def test_radians_array_array_d2(self):
		"""Test radians as *array-array* for maxlen='a' - Array code f.
		"""
		testmaxlen = len(self.floatarray) // 2

		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.dataout, maxlen='a')



	########################################################
	def test_radians_no_params_e1(self):
		"""Test radians with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.radians()


##############################################################################



##############################################################################
class radians_param_nosimd_errors_f(unittest.TestCase):
	"""Test for invalid nosimd parameters.
	param_nosimd_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])



	########################################################
	def test_radians_array_none_b1(self):
		"""Test radians as *array-none* for nosimd='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.radians(floatarray, nosimd=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(floatarray, nosimd='a')


	########################################################
	def test_radians_array_num_array_d1(self):
		"""Test radians as *array-num-array* for nosimd='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.dataout, nosimd='a')



##############################################################################



##############################################################################
class radians_general_even_arraysize_with_simd_d(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_noparams
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.data = array.array('d', xdata)
		self.dataout = array.array('d', [0]*len(self.data))

		self.limited = len(self.data) // 2

		# The expected results.
		self.expected = [math.radians(x) for x in self.data]

		# The expected results when the maxlen parameter is used.
		self.expectedlimiteddata = self.expected[0:self.limited] + list(self.data)[self.limited:]

		# The same, but where dataout is used as one of the sources.
		self.expectedlimiteddataout = self.expected[0:self.limited] + list(self.dataout)[self.limited:]



	########################################################
	def test_radians_basic_array_none_a1(self):
		"""Test radians as *array-none* for basic function - Array code d.
		"""
		arrayfunc.radians(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a2(self):
		"""Test radians as *array-none* for basic function with matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a3(self):
		"""Test radians as *array-none* for basic function with maxlen - Array code d.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a4(self):
		"""Test radians as *array-none* for basic function with maxlen and matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b1(self):
		"""Test radians as *array-array* for basic function - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b2(self):
		"""Test radians as *array-array* for basic function with matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b3(self):
		"""Test radians as *array-array* for basic function with maxlen - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b4(self):
		"""Test radians as *array-array* for basic function with maxlen and matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class radians_general_odd_arraysize_with_simd_d(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_noparams
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.data = array.array('d', xdata)
		self.dataout = array.array('d', [0]*len(self.data))

		self.limited = len(self.data) // 2

		# The expected results.
		self.expected = [math.radians(x) for x in self.data]

		# The expected results when the maxlen parameter is used.
		self.expectedlimiteddata = self.expected[0:self.limited] + list(self.data)[self.limited:]

		# The same, but where dataout is used as one of the sources.
		self.expectedlimiteddataout = self.expected[0:self.limited] + list(self.dataout)[self.limited:]



	########################################################
	def test_radians_basic_array_none_a1(self):
		"""Test radians as *array-none* for basic function - Array code d.
		"""
		arrayfunc.radians(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a2(self):
		"""Test radians as *array-none* for basic function with matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a3(self):
		"""Test radians as *array-none* for basic function with maxlen - Array code d.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a4(self):
		"""Test radians as *array-none* for basic function with maxlen and matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b1(self):
		"""Test radians as *array-array* for basic function - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b2(self):
		"""Test radians as *array-array* for basic function with matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b3(self):
		"""Test radians as *array-array* for basic function with maxlen - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b4(self):
		"""Test radians as *array-array* for basic function with maxlen and matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class radians_general_even_arraysize_without_simd_d(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_noparams
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), range(testdatasize))]
		self.data = array.array('d', xdata)
		self.dataout = array.array('d', [0]*len(self.data))

		self.limited = len(self.data) // 2

		# The expected results.
		self.expected = [math.radians(x) for x in self.data]

		# The expected results when the maxlen parameter is used.
		self.expectedlimiteddata = self.expected[0:self.limited] + list(self.data)[self.limited:]

		# The same, but where dataout is used as one of the sources.
		self.expectedlimiteddataout = self.expected[0:self.limited] + list(self.dataout)[self.limited:]



	########################################################
	def test_radians_basic_array_none_a1(self):
		"""Test radians as *array-none* for basic function - Array code d.
		"""
		arrayfunc.radians(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a2(self):
		"""Test radians as *array-none* for basic function with matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a3(self):
		"""Test radians as *array-none* for basic function with maxlen - Array code d.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_none_a4(self):
		"""Test radians as *array-none* for basic function with maxlen and matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, maxlen=self.limited, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimiteddata):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b1(self):
		"""Test radians as *array-array* for basic function - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b2(self):
		"""Test radians as *array-array* for basic function with matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b3(self):
		"""Test radians as *array-array* for basic function with maxlen - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_basic_array_array_b4(self):
		"""Test radians as *array-array* for basic function with maxlen and matherrors=True - Array code d.
		"""
		arrayfunc.radians(self.data, self.dataout, maxlen=self.limited, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimiteddataout):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class radians_param_errors_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_radians_array_none_a1(self):
		"""Test radians as *array-none* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.intarray)


	########################################################
	def test_radians_array_none_b1(self):
		"""Test radians as *array-none* for matherrors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.radians(floatarray, matherrors=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(floatarray, matherrors='a')


	########################################################
	def test_radians_array_none_b2(self):
		"""Test radians as *array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)
		testmaxlen = len(floatarray) // 2

		# This version is expected to pass.
		arrayfunc.radians(floatarray, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(floatarray, maxlen='a')



	########################################################
	def test_radians_array_array_c1(self):
		"""Test radians as *array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.intarray, self.dataout)


	########################################################
	def test_radians_array_array_c2(self):
		"""Test radians as *array-array* for integer output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.intdataout)


	########################################################
	def test_radians_array_array_c3(self):
		"""Test radians as *array-array* for integer input and output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.intarray, self.intdataout)


	########################################################
	def test_radians_array_num_array_d1(self):
		"""Test radians as *array-num-array* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.dataout, matherrors='a')


	########################################################
	def test_radians_array_array_d2(self):
		"""Test radians as *array-array* for maxlen='a' - Array code d.
		"""
		testmaxlen = len(self.floatarray) // 2

		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.dataout, maxlen='a')



	########################################################
	def test_radians_no_params_e1(self):
		"""Test radians with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.radians()


##############################################################################



##############################################################################
class radians_param_nosimd_errors_d(unittest.TestCase):
	"""Test for invalid nosimd parameters.
	param_nosimd_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])



	########################################################
	def test_radians_array_none_b1(self):
		"""Test radians as *array-none* for nosimd='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.radians(floatarray, nosimd=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(floatarray, nosimd='a')


	########################################################
	def test_radians_array_num_array_d1(self):
		"""Test radians as *array-num-array* for nosimd='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.radians(self.floatarray, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.radians(self.floatarray, self.dataout, nosimd='a')



##############################################################################


##############################################################################
class radians_nandata_exceptions_nan_f(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_errorchecked_noparam_template
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

		self.dataout = array.array('f', itertools.repeat(0.0, 10))

		self.datainf = array.array('f', [math.inf] * 10)
		self.datanan = array.array('f', [math.nan] * 10)
		self.dataninf = array.array('f', [-math.inf] * 10)


	########################################################
	def test_radians_outputarray(self):
		"""Test radians for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datanan, self.dataout)


	########################################################
	def test_radians_inplace(self):
		"""Test radians in place for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datanan)


	########################################################
	def test_radians_ov_outputarray(self):
		"""Test radians for data of nan with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.radians(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_ov_inplace(self):
		"""Test radians in place for data of nan with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.radians(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class radians_nandata_exceptions_nan_d(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_errorchecked_noparam_template
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

		self.dataout = array.array('d', itertools.repeat(0.0, 10))

		self.datainf = array.array('d', [math.inf] * 10)
		self.datanan = array.array('d', [math.nan] * 10)
		self.dataninf = array.array('d', [-math.inf] * 10)


	########################################################
	def test_radians_outputarray(self):
		"""Test radians for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datanan, self.dataout)


	########################################################
	def test_radians_inplace(self):
		"""Test radians in place for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datanan)


	########################################################
	def test_radians_ov_outputarray(self):
		"""Test radians for data of nan with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.radians(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_ov_inplace(self):
		"""Test radians in place for data of nan with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.radians(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class radians_nandata_exceptions_inf_f(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_errorchecked_noparam_template
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

		self.dataout = array.array('f', itertools.repeat(0.0, 10))

		self.datainf = array.array('f', [math.inf] * 10)
		self.datanan = array.array('f', [math.nan] * 10)
		self.dataninf = array.array('f', [-math.inf] * 10)


	########################################################
	def test_radians_outputarray(self):
		"""Test radians for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datainf, self.dataout)


	########################################################
	def test_radians_inplace(self):
		"""Test radians in place for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datainf)


	########################################################
	def test_radians_ov_outputarray(self):
		"""Test radians for data of inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.radians(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_ov_inplace(self):
		"""Test radians in place for data of inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.radians(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class radians_nandata_exceptions_inf_d(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_errorchecked_noparam_template
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

		self.dataout = array.array('d', itertools.repeat(0.0, 10))

		self.datainf = array.array('d', [math.inf] * 10)
		self.datanan = array.array('d', [math.nan] * 10)
		self.dataninf = array.array('d', [-math.inf] * 10)


	########################################################
	def test_radians_outputarray(self):
		"""Test radians for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datainf, self.dataout)


	########################################################
	def test_radians_inplace(self):
		"""Test radians in place for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.datainf)


	########################################################
	def test_radians_ov_outputarray(self):
		"""Test radians for data of inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.radians(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_ov_inplace(self):
		"""Test radians in place for data of inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.radians(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class radians_nandata_exceptions_ninf_f(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_errorchecked_noparam_template
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

		self.dataout = array.array('f', itertools.repeat(0.0, 10))

		self.datainf = array.array('f', [math.inf] * 10)
		self.datanan = array.array('f', [math.nan] * 10)
		self.dataninf = array.array('f', [-math.inf] * 10)


	########################################################
	def test_radians_outputarray(self):
		"""Test radians for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.dataninf, self.dataout)


	########################################################
	def test_radians_inplace(self):
		"""Test radians in place for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.dataninf)


	########################################################
	def test_radians_ov_outputarray(self):
		"""Test radians for data of -inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.radians(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_ov_inplace(self):
		"""Test radians in place for data of -inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.radians(self.dataninf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataninf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class radians_nandata_exceptions_ninf_d(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_errorchecked_noparam_template
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

		self.dataout = array.array('d', itertools.repeat(0.0, 10))

		self.datainf = array.array('d', [math.inf] * 10)
		self.datanan = array.array('d', [math.nan] * 10)
		self.dataninf = array.array('d', [-math.inf] * 10)


	########################################################
	def test_radians_outputarray(self):
		"""Test radians for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.dataninf, self.dataout)


	########################################################
	def test_radians_inplace(self):
		"""Test radians in place for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.radians(self.dataninf)


	########################################################
	def test_radians_ov_outputarray(self):
		"""Test radians for data of -inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.radians(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_radians_ov_inplace(self):
		"""Test radians in place for data of -inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.radians(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.radians(self.dataninf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataninf), expected):
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
			f.write('radians\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
