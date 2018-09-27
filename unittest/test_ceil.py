#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_ceil.py
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
"""This conducts unit tests for ceil.
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
class ceil_general_f(unittest.TestCase):
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


	########################################################
	def test_ceil_outputarray(self):
		"""Test ceil to output array - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('f', [0]*len(data))


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data, dataout)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_outputarray_ov(self):
		"""Test ceil to output array with matherrors=True  - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('f', [0]*len(data))


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_outputarray_lim(self):
		"""Test ceil to output array with array limit  - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('f', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.ceil(data, dataout, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_outputarray_ov_lim(self):
		"""Test ceil to output array with matherrors=True and array limit - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('f', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.ceil(data, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_inplace_ov(self):
		"""Test ceil in place with matherrors=True  - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_inplace_lim(self):
		"""Test ceil in place with array limit  - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.ceil(data, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_inplace_ov_lim(self):
		"""Test ceil in place with matherrors=True and array limit  - Array code f.
		"""
		data = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.ceil(data, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class ceil_param_errors_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('f', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_ceil_array_none_a1(self):
		"""Test ceil as *array-none* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.intarray)


	########################################################
	def test_ceil_array_none_b1(self):
		"""Test ceil as *array-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.ceil(floatarray, matherrors=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(floatarray, errors='a')


	########################################################
	def test_ceil_array_none_b2(self):
		"""Test ceil as *array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)
		testmaxlen = len(floatarray) // 2

		# This version is expected to pass.
		arrayfunc.ceil(floatarray, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(floatarray, maxlen='a')



	########################################################
	def test_ceil_array_array_c1(self):
		"""Test ceil as *array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.intarray, self.dataout)


	########################################################
	def test_ceil_array_array_c2(self):
		"""Test ceil as *array-array* for integer output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.floatarray, self.intdataout)


	########################################################
	def test_ceil_array_array_c3(self):
		"""Test ceil as *array-array* for integer input and output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.intarray, self.intdataout)


	########################################################
	def test_ceil_array_num_array_d1(self):
		"""Test ceil as *array-num-array* for errors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.floatarray, self.dataout, errors='a')


	########################################################
	def test_ceil_array_array_d2(self):
		"""Test ceil as *array-array* for maxlen='a' - Array code f.
		"""
		testmaxlen = len(self.floatarray) // 2

		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.floatarray, self.dataout, maxlen='a')



	########################################################
	def test_ceil_no_params_e1(self):
		"""Test ceil with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.ceil()


##############################################################################



##############################################################################
class ceil_general_d(unittest.TestCase):
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


	########################################################
	def test_ceil_outputarray(self):
		"""Test ceil to output array - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('d', [0]*len(data))


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data, dataout)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_outputarray_ov(self):
		"""Test ceil to output array with matherrors=True  - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('d', [0]*len(data))


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_outputarray_lim(self):
		"""Test ceil to output array with array limit  - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('d', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.ceil(data, dataout, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_outputarray_ov_lim(self):
		"""Test ceil to output array with matherrors=True and array limit - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		dataout = array.array('d', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.ceil(data, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_inplace_ov(self):
		"""Test ceil in place with matherrors=True  - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])


		expected = [math.ceil(x) for x in data]
		arrayfunc.ceil(data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_inplace_lim(self):
		"""Test ceil in place with array limit  - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.ceil(data, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ceil_inplace_ov_lim(self):
		"""Test ceil in place with matherrors=True and array limit  - Array code d.
		"""
		data = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		limited = len(data) // 2

		pydataout = [math.ceil(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.ceil(data, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class ceil_param_errors_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('d', [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_ceil_array_none_a1(self):
		"""Test ceil as *array-none* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.intarray)


	########################################################
	def test_ceil_array_none_b1(self):
		"""Test ceil as *array-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.ceil(floatarray, matherrors=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(floatarray, errors='a')


	########################################################
	def test_ceil_array_none_b2(self):
		"""Test ceil as *array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)
		testmaxlen = len(floatarray) // 2

		# This version is expected to pass.
		arrayfunc.ceil(floatarray, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(floatarray, maxlen='a')



	########################################################
	def test_ceil_array_array_c1(self):
		"""Test ceil as *array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.intarray, self.dataout)


	########################################################
	def test_ceil_array_array_c2(self):
		"""Test ceil as *array-array* for integer output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.floatarray, self.intdataout)


	########################################################
	def test_ceil_array_array_c3(self):
		"""Test ceil as *array-array* for integer input and output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.intarray, self.intdataout)


	########################################################
	def test_ceil_array_num_array_d1(self):
		"""Test ceil as *array-num-array* for errors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.floatarray, self.dataout, errors='a')


	########################################################
	def test_ceil_array_array_d2(self):
		"""Test ceil as *array-array* for maxlen='a' - Array code d.
		"""
		testmaxlen = len(self.floatarray) // 2

		# This version is expected to pass.
		arrayfunc.ceil(self.floatarray, self.dataout, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ceil(self.floatarray, self.dataout, maxlen='a')



	########################################################
	def test_ceil_no_params_e1(self):
		"""Test ceil with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.ceil()


##############################################################################


##############################################################################
class ceil_nandata_exceptions_nan_f(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_error_noparam_template
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
	def test_ceil_outputarray(self):
		"""Test ceil for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datanan, self.dataout)


	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datanan)


	########################################################
	def test_ceil_ov_outputarray(self):
		"""Test ceil for data of nan with matherrors checking off and single parameter functions  - Array code f.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datanan, self.dataout, matherrors=True)


	########################################################
	def test_ceil_ov_inplace(self):
		"""Test ceil in place for data of nan with matherrors checking off and single parameter functions  - Array code f.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datanan, matherrors=True)



##############################################################################


##############################################################################
class ceil_nandata_exceptions_nan_d(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_error_noparam_template
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
	def test_ceil_outputarray(self):
		"""Test ceil for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datanan, self.dataout)


	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datanan)


	########################################################
	def test_ceil_ov_outputarray(self):
		"""Test ceil for data of nan with matherrors checking off and single parameter functions  - Array code d.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datanan, self.dataout, matherrors=True)


	########################################################
	def test_ceil_ov_inplace(self):
		"""Test ceil in place for data of nan with matherrors checking off and single parameter functions  - Array code d.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datanan, matherrors=True)



##############################################################################


##############################################################################
class ceil_nandata_exceptions_inf_f(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_error_noparam_template
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
	def test_ceil_outputarray(self):
		"""Test ceil for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datainf, self.dataout)


	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datainf)


	########################################################
	def test_ceil_ov_outputarray(self):
		"""Test ceil for data of inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datainf, self.dataout, matherrors=True)


	########################################################
	def test_ceil_ov_inplace(self):
		"""Test ceil in place for data of inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datainf, matherrors=True)



##############################################################################


##############################################################################
class ceil_nandata_exceptions_inf_d(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_error_noparam_template
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
	def test_ceil_outputarray(self):
		"""Test ceil for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datainf, self.dataout)


	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.datainf)


	########################################################
	def test_ceil_ov_outputarray(self):
		"""Test ceil for data of inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datainf, self.dataout, matherrors=True)


	########################################################
	def test_ceil_ov_inplace(self):
		"""Test ceil in place for data of inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.datainf, matherrors=True)



##############################################################################


##############################################################################
class ceil_nandata_exceptions_ninf_f(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_error_noparam_template
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
	def test_ceil_outputarray(self):
		"""Test ceil for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.dataninf, self.dataout)


	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.dataninf)


	########################################################
	def test_ceil_ov_outputarray(self):
		"""Test ceil for data of -inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.dataninf, self.dataout, matherrors=True)


	########################################################
	def test_ceil_ov_inplace(self):
		"""Test ceil in place for data of -inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.dataninf, matherrors=True)



##############################################################################


##############################################################################
class ceil_nandata_exceptions_ninf_d(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_error_noparam_template
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
	def test_ceil_outputarray(self):
		"""Test ceil for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.dataninf, self.dataout)


	########################################################
	def test_ceil_inplace(self):
		"""Test ceil in place for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.ceil(self.dataninf)


	########################################################
	def test_ceil_ov_outputarray(self):
		"""Test ceil for data of -inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.dataninf, self.dataout, matherrors=True)


	########################################################
	def test_ceil_ov_inplace(self):
		"""Test ceil in place for data of -inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# This is the actual test.
		arrayfunc.ceil(self.dataninf, matherrors=True)



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
			f.write('ceil\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################