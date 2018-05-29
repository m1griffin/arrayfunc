#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_fabs.py
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
"""This conducts unit tests for fabs.
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
class fabs_general_f(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs to output array - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('f', [0]*len(data))


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data, dataout)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_outputarray_ov(self):
		"""Test fabs to output array with matherrors=True  - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('f', [0]*len(data))


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_outputarray_lim(self):
		"""Test fabs to output array with array limit  - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('f', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.fabs(data, dataout, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_outputarray_ov_lim(self):
		"""Test fabs to output array with matherrors=True and array limit - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('f', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.fabs(data, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_inplace_ov(self):
		"""Test fabs in place with matherrors=True  - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_inplace_lim(self):
		"""Test fabs in place with array limit  - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.fabs(data, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_inplace_ov_lim(self):
		"""Test fabs in place with matherrors=True and array limit  - Array code f.
		"""
		data = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.fabs(data, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class fabs_param_errors_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('f', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_fabs_array_none_a1(self):
		"""Test fabs as *array-none* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.intarray)


	########################################################
	def test_fabs_array_none_b1(self):
		"""Test fabs as *array-none* for errors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.fabs(floatarray, matherrors=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(floatarray, errors='a')


	########################################################
	def test_fabs_array_none_b2(self):
		"""Test fabs as *array-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)
		testmaxlen = len(floatarray) // 2

		# This version is expected to pass.
		arrayfunc.fabs(floatarray, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(floatarray, maxlen='a')



	########################################################
	def test_fabs_array_array_c1(self):
		"""Test fabs as *array-array* for integer array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.intarray, self.dataout)


	########################################################
	def test_fabs_array_array_c2(self):
		"""Test fabs as *array-array* for integer output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.floatarray, self.intdataout)


	########################################################
	def test_fabs_array_array_c3(self):
		"""Test fabs as *array-array* for integer input and output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.intarray, self.intdataout)


	########################################################
	def test_fabs_array_num_array_d1(self):
		"""Test fabs as *array-num-array* for errors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.floatarray, self.dataout, errors='a')


	########################################################
	def test_fabs_array_array_d2(self):
		"""Test fabs as *array-array* for maxlen='a' - Array code f.
		"""
		testmaxlen = len(self.floatarray) // 2

		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.floatarray, self.dataout, maxlen='a')



	########################################################
	def test_fabs_no_params_e1(self):
		"""Test fabs with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fabs()


##############################################################################



##############################################################################
class fabs_general_d(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs to output array - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('d', [0]*len(data))


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data, dataout)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_outputarray_ov(self):
		"""Test fabs to output array with matherrors=True  - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('d', [0]*len(data))


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_outputarray_lim(self):
		"""Test fabs to output array with array limit  - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('d', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.fabs(data, dataout, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_outputarray_ov_lim(self):
		"""Test fabs to output array with matherrors=True and array limit - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		dataout = array.array('d', [0]*len(data))

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.fabs(data, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_inplace_ov(self):
		"""Test fabs in place with matherrors=True  - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])


		expected = [math.fabs(x) for x in data]
		arrayfunc.fabs(data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_inplace_lim(self):
		"""Test fabs in place with array limit  - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.fabs(data, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_inplace_ov_lim(self):
		"""Test fabs in place with matherrors=True and array limit  - Array code d.
		"""
		data = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		limited = len(data) // 2

		pydataout = [math.fabs(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.fabs(data, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class fabs_param_errors_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray = array.array('d', [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_fabs_array_none_a1(self):
		"""Test fabs as *array-none* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.intarray)


	########################################################
	def test_fabs_array_none_b1(self):
		"""Test fabs as *array-none* for errors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.fabs(floatarray, matherrors=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(floatarray, errors='a')


	########################################################
	def test_fabs_array_none_b2(self):
		"""Test fabs as *array-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)
		testmaxlen = len(floatarray) // 2

		# This version is expected to pass.
		arrayfunc.fabs(floatarray, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(floatarray, maxlen='a')



	########################################################
	def test_fabs_array_array_c1(self):
		"""Test fabs as *array-array* for integer array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.intarray, self.dataout)


	########################################################
	def test_fabs_array_array_c2(self):
		"""Test fabs as *array-array* for integer output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.floatarray, self.intdataout)


	########################################################
	def test_fabs_array_array_c3(self):
		"""Test fabs as *array-array* for integer input and output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.intarray, self.intdataout)


	########################################################
	def test_fabs_array_num_array_d1(self):
		"""Test fabs as *array-num-array* for errors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.floatarray, self.dataout, errors='a')


	########################################################
	def test_fabs_array_array_d2(self):
		"""Test fabs as *array-array* for maxlen='a' - Array code d.
		"""
		testmaxlen = len(self.floatarray) // 2

		# This version is expected to pass.
		arrayfunc.fabs(self.floatarray, self.dataout, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fabs(self.floatarray, self.dataout, maxlen='a')



	########################################################
	def test_fabs_no_params_e1(self):
		"""Test fabs with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fabs()


##############################################################################


##############################################################################
class fabs_nandata_exceptions_nan_f(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datanan, self.dataout)


	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datanan)


	########################################################
	def test_fabs_ov_outputarray(self):
		"""Test fabs for data of nan with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.fabs(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_ov_inplace(self):
		"""Test fabs in place for data of nan with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.fabs(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class fabs_nandata_exceptions_nan_d(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datanan, self.dataout)


	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datanan)


	########################################################
	def test_fabs_ov_outputarray(self):
		"""Test fabs for data of nan with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.fabs(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_ov_inplace(self):
		"""Test fabs in place for data of nan with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.fabs(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class fabs_nandata_exceptions_inf_f(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datainf, self.dataout)


	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datainf)


	########################################################
	def test_fabs_ov_outputarray(self):
		"""Test fabs for data of inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.fabs(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_ov_inplace(self):
		"""Test fabs in place for data of inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.fabs(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class fabs_nandata_exceptions_inf_d(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datainf, self.dataout)


	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.datainf)


	########################################################
	def test_fabs_ov_outputarray(self):
		"""Test fabs for data of inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.fabs(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_ov_inplace(self):
		"""Test fabs in place for data of inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.fabs(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class fabs_nandata_exceptions_ninf_f(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.dataninf, self.dataout)


	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.dataninf)


	########################################################
	def test_fabs_ov_outputarray(self):
		"""Test fabs for data of -inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.fabs(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_ov_inplace(self):
		"""Test fabs in place for data of -inf with matherrors checking off and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.fabs(self.dataninf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataninf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class fabs_nandata_exceptions_ninf_d(unittest.TestCase):
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
	def test_fabs_outputarray(self):
		"""Test fabs for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.dataninf, self.dataout)


	########################################################
	def test_fabs_inplace(self):
		"""Test fabs in place for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.fabs(self.dataninf)


	########################################################
	def test_fabs_ov_outputarray(self):
		"""Test fabs for data of -inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.fabs(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fabs_ov_inplace(self):
		"""Test fabs in place for data of -inf with matherrors checking off and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [math.fabs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.fabs(self.dataninf, matherrors=True)

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

		with open('arrayfunc_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('fabs\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
