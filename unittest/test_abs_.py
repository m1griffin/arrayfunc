#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_abs_.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      13-Jun-2018.
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
"""This conducts unit tests for abs_.
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
class abs__general_b(unittest.TestCase):
	"""Test for basic general tests.
	test_template_uniop
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

		self.data = array.array('b', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [abs(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace_a1(self):
		"""Test abs_ in place - Array code b.
		"""
		expected = [abs(x) for x in self.data]

		arrayfunc.abs_(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_a2(self):
		"""Test abs_ in place with matherrors=True  - Array code b.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_lim_a3(self):
		"""Test abs_ in place with array limit  - Array code b.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_lim_a4(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code b.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_abs__outputarray_a5(self):
		"""Test abs_ to output array - Array code b.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_a6(self):
		"""Test abs_ to output array with matherrors=True  - Array code b.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_lim_a7(self):
		"""Test abs_ to output array with array limit  - Array code b.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_lim_a8(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code b.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class abs__param_errors_b(unittest.TestCase):
	"""Test abs_ for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('b', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_abs__array_array_a1(self):
		"""Test abs_ as *array-array* for invalid type of input array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.badarray1, self.dataout)


	########################################################
	def test_abs__array_array_a2(self):
		"""Test abs_ as *array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.testarray2, self.baddataout)


	########################################################
	def test_abs__no_params_b1(self):
		"""Test abs_ with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_()


##############################################################################



##############################################################################
class abs__opt_param_errors_b(unittest.TestCase):
	"""Test abs_ for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('b', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for errors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, errors='a')


	########################################################
	def test_abs__array_none_a2(self):
		"""Test abs_ as *array-none* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, maxlen='a')


	########################################################
	def test_abs__array_array_b1(self):
		"""Test abs_ as *array-array* for errors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_abs__array_array_b2(self):
		"""Test abs_ as *array-array* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class abs__general_h(unittest.TestCase):
	"""Test for basic general tests.
	test_template_uniop
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

		self.data = array.array('h', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [abs(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace_a1(self):
		"""Test abs_ in place - Array code h.
		"""
		expected = [abs(x) for x in self.data]

		arrayfunc.abs_(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_a2(self):
		"""Test abs_ in place with matherrors=True  - Array code h.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_lim_a3(self):
		"""Test abs_ in place with array limit  - Array code h.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_lim_a4(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code h.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_abs__outputarray_a5(self):
		"""Test abs_ to output array - Array code h.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_a6(self):
		"""Test abs_ to output array with matherrors=True  - Array code h.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_lim_a7(self):
		"""Test abs_ to output array with array limit  - Array code h.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_lim_a8(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code h.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class abs__param_errors_h(unittest.TestCase):
	"""Test abs_ for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('h', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_abs__array_array_a1(self):
		"""Test abs_ as *array-array* for invalid type of input array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.badarray1, self.dataout)


	########################################################
	def test_abs__array_array_a2(self):
		"""Test abs_ as *array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.testarray2, self.baddataout)


	########################################################
	def test_abs__no_params_b1(self):
		"""Test abs_ with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_()


##############################################################################



##############################################################################
class abs__opt_param_errors_h(unittest.TestCase):
	"""Test abs_ for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('h', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for errors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, errors='a')


	########################################################
	def test_abs__array_none_a2(self):
		"""Test abs_ as *array-none* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, maxlen='a')


	########################################################
	def test_abs__array_array_b1(self):
		"""Test abs_ as *array-array* for errors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_abs__array_array_b2(self):
		"""Test abs_ as *array-array* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class abs__general_i(unittest.TestCase):
	"""Test for basic general tests.
	test_template_uniop
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

		self.data = array.array('i', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [abs(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace_a1(self):
		"""Test abs_ in place - Array code i.
		"""
		expected = [abs(x) for x in self.data]

		arrayfunc.abs_(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_a2(self):
		"""Test abs_ in place with matherrors=True  - Array code i.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_lim_a3(self):
		"""Test abs_ in place with array limit  - Array code i.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_lim_a4(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code i.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_abs__outputarray_a5(self):
		"""Test abs_ to output array - Array code i.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_a6(self):
		"""Test abs_ to output array with matherrors=True  - Array code i.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_lim_a7(self):
		"""Test abs_ to output array with array limit  - Array code i.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_lim_a8(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code i.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class abs__param_errors_i(unittest.TestCase):
	"""Test abs_ for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('i', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_abs__array_array_a1(self):
		"""Test abs_ as *array-array* for invalid type of input array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.badarray1, self.dataout)


	########################################################
	def test_abs__array_array_a2(self):
		"""Test abs_ as *array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.testarray2, self.baddataout)


	########################################################
	def test_abs__no_params_b1(self):
		"""Test abs_ with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_()


##############################################################################



##############################################################################
class abs__opt_param_errors_i(unittest.TestCase):
	"""Test abs_ for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('i', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for errors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, errors='a')


	########################################################
	def test_abs__array_none_a2(self):
		"""Test abs_ as *array-none* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, maxlen='a')


	########################################################
	def test_abs__array_array_b1(self):
		"""Test abs_ as *array-array* for errors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_abs__array_array_b2(self):
		"""Test abs_ as *array-array* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class abs__general_l(unittest.TestCase):
	"""Test for basic general tests.
	test_template_uniop
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

		self.data = array.array('l', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [abs(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace_a1(self):
		"""Test abs_ in place - Array code l.
		"""
		expected = [abs(x) for x in self.data]

		arrayfunc.abs_(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_a2(self):
		"""Test abs_ in place with matherrors=True  - Array code l.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_lim_a3(self):
		"""Test abs_ in place with array limit  - Array code l.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_lim_a4(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code l.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_abs__outputarray_a5(self):
		"""Test abs_ to output array - Array code l.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_a6(self):
		"""Test abs_ to output array with matherrors=True  - Array code l.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_lim_a7(self):
		"""Test abs_ to output array with array limit  - Array code l.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_lim_a8(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code l.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class abs__param_errors_l(unittest.TestCase):
	"""Test abs_ for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('l', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_abs__array_array_a1(self):
		"""Test abs_ as *array-array* for invalid type of input array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.badarray1, self.dataout)


	########################################################
	def test_abs__array_array_a2(self):
		"""Test abs_ as *array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.testarray2, self.baddataout)


	########################################################
	def test_abs__no_params_b1(self):
		"""Test abs_ with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_()


##############################################################################



##############################################################################
class abs__opt_param_errors_l(unittest.TestCase):
	"""Test abs_ for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('l', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for errors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, errors='a')


	########################################################
	def test_abs__array_none_a2(self):
		"""Test abs_ as *array-none* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, maxlen='a')


	########################################################
	def test_abs__array_array_b1(self):
		"""Test abs_ as *array-array* for errors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_abs__array_array_b2(self):
		"""Test abs_ as *array-array* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class abs__general_q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_uniop
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

		self.data = array.array('q', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [abs(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace_a1(self):
		"""Test abs_ in place - Array code q.
		"""
		expected = [abs(x) for x in self.data]

		arrayfunc.abs_(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_a2(self):
		"""Test abs_ in place with matherrors=True  - Array code q.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_lim_a3(self):
		"""Test abs_ in place with array limit  - Array code q.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_lim_a4(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code q.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_abs__outputarray_a5(self):
		"""Test abs_ to output array - Array code q.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_a6(self):
		"""Test abs_ to output array with matherrors=True  - Array code q.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_lim_a7(self):
		"""Test abs_ to output array with array limit  - Array code q.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_lim_a8(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code q.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class abs__param_errors_q(unittest.TestCase):
	"""Test abs_ for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('q', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_abs__array_array_a1(self):
		"""Test abs_ as *array-array* for invalid type of input array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.badarray1, self.dataout)


	########################################################
	def test_abs__array_array_a2(self):
		"""Test abs_ as *array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.testarray2, self.baddataout)


	########################################################
	def test_abs__no_params_b1(self):
		"""Test abs_ with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_()


##############################################################################



##############################################################################
class abs__opt_param_errors_q(unittest.TestCase):
	"""Test abs_ for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('q', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for errors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, errors='a')


	########################################################
	def test_abs__array_none_a2(self):
		"""Test abs_ as *array-none* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, maxlen='a')


	########################################################
	def test_abs__array_array_b1(self):
		"""Test abs_ as *array-array* for errors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_abs__array_array_b2(self):
		"""Test abs_ as *array-array* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class abs__general_f(unittest.TestCase):
	"""Test for basic general tests.
	test_template_uniop
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

		self.data = array.array('f', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.dataout = array.array('f', [0]*len(self.data))

		self.expected = [abs(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace_a1(self):
		"""Test abs_ in place - Array code f.
		"""
		expected = [abs(x) for x in self.data]

		arrayfunc.abs_(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_a2(self):
		"""Test abs_ in place with matherrors=True  - Array code f.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_lim_a3(self):
		"""Test abs_ in place with array limit  - Array code f.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_lim_a4(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code f.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_abs__outputarray_a5(self):
		"""Test abs_ to output array - Array code f.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_a6(self):
		"""Test abs_ to output array with matherrors=True  - Array code f.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_lim_a7(self):
		"""Test abs_ to output array with array limit  - Array code f.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_lim_a8(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code f.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class abs__param_errors_f(unittest.TestCase):
	"""Test abs_ for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('f', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])



	########################################################
	def test_abs__array_array_a1(self):
		"""Test abs_ as *array-array* for invalid type of input array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.badarray1, self.dataout)


	########################################################
	def test_abs__array_array_a2(self):
		"""Test abs_ as *array-array* for invalid type of output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.testarray2, self.baddataout)


	########################################################
	def test_abs__no_params_b1(self):
		"""Test abs_ with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_()


##############################################################################



##############################################################################
class abs__opt_param_errors_f(unittest.TestCase):
	"""Test abs_ for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('f', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for errors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, errors='a')


	########################################################
	def test_abs__array_none_a2(self):
		"""Test abs_ as *array-none* for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, maxlen='a')


	########################################################
	def test_abs__array_array_b1(self):
		"""Test abs_ as *array-array* for errors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_abs__array_array_b2(self):
		"""Test abs_ as *array-array* for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class abs__general_d(unittest.TestCase):
	"""Test for basic general tests.
	test_template_uniop
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

		self.data = array.array('d', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.dataout = array.array('d', [0]*len(self.data))

		self.expected = [abs(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace_a1(self):
		"""Test abs_ in place - Array code d.
		"""
		expected = [abs(x) for x in self.data]

		arrayfunc.abs_(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_a2(self):
		"""Test abs_ in place with matherrors=True  - Array code d.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_lim_a3(self):
		"""Test abs_ in place with array limit  - Array code d.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__inplace_ov_lim_a4(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code d.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_abs__outputarray_a5(self):
		"""Test abs_ to output array - Array code d.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_a6(self):
		"""Test abs_ to output array with matherrors=True  - Array code d.
		"""
		expected = [abs(x) for x in self.data]
		arrayfunc.abs_(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_lim_a7(self):
		"""Test abs_ to output array with array limit  - Array code d.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__outputarray_ov_lim_a8(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code d.
		"""
		pydataout = [abs(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class abs__param_errors_d(unittest.TestCase):
	"""Test abs_ for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('d', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])



	########################################################
	def test_abs__array_array_a1(self):
		"""Test abs_ as *array-array* for invalid type of input array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.badarray1, self.dataout)


	########################################################
	def test_abs__array_array_a2(self):
		"""Test abs_ as *array-array* for invalid type of output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.testarray2, self.baddataout)


	########################################################
	def test_abs__no_params_b1(self):
		"""Test abs_ with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_()


##############################################################################



##############################################################################
class abs__opt_param_errors_d(unittest.TestCase):
	"""Test abs_ for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('d', [-5,-4,-3,-2,-1,0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for errors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, errors='a')


	########################################################
	def test_abs__array_none_a2(self):
		"""Test abs_ as *array-none* for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, maxlen='a')


	########################################################
	def test_abs__array_array_b1(self):
		"""Test abs_ as *array-array* for errors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_abs__array_array_b2(self):
		"""Test abs_ as *array-array* for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class abs__invalidarray_Q(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('Q', [5,4,3,2,1,0,1,2,3,4,5])
		self.dataout = array.array('Q', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace(self):
		"""Test abs_ in place - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data)


	########################################################
	def test_abs__inplace_ov_a1(self):
		"""Test abs_ in place with matherrors=True  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True)


	########################################################
	def test_abs__inplace_lim_a2(self):
		"""Test abs_ in place with array limit  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, maxlen=self.limited)


	########################################################
	def test_abs__inplace_ov_lim_a3(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_a4(self):
		"""Test abs_ to output array - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout)


	########################################################
	def test_abs__outputarray_ov_a4(self):
		"""Test abs_ to output array with matherrors=True  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True)


	########################################################
	def test_abs__outputarray_lim_a5(self):
		"""Test abs_ to output array with array limit  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_ov_lim_a6(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class abs__invalidarray_H(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('H', [5,4,3,2,1,0,1,2,3,4,5])
		self.dataout = array.array('H', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace(self):
		"""Test abs_ in place - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data)


	########################################################
	def test_abs__inplace_ov_a1(self):
		"""Test abs_ in place with matherrors=True  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True)


	########################################################
	def test_abs__inplace_lim_a2(self):
		"""Test abs_ in place with array limit  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, maxlen=self.limited)


	########################################################
	def test_abs__inplace_ov_lim_a3(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_a4(self):
		"""Test abs_ to output array - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout)


	########################################################
	def test_abs__outputarray_ov_a4(self):
		"""Test abs_ to output array with matherrors=True  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True)


	########################################################
	def test_abs__outputarray_lim_a5(self):
		"""Test abs_ to output array with array limit  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_ov_lim_a6(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class abs__invalidarray_L(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('L', [5,4,3,2,1,0,1,2,3,4,5])
		self.dataout = array.array('L', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace(self):
		"""Test abs_ in place - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data)


	########################################################
	def test_abs__inplace_ov_a1(self):
		"""Test abs_ in place with matherrors=True  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True)


	########################################################
	def test_abs__inplace_lim_a2(self):
		"""Test abs_ in place with array limit  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, maxlen=self.limited)


	########################################################
	def test_abs__inplace_ov_lim_a3(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_a4(self):
		"""Test abs_ to output array - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout)


	########################################################
	def test_abs__outputarray_ov_a4(self):
		"""Test abs_ to output array with matherrors=True  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True)


	########################################################
	def test_abs__outputarray_lim_a5(self):
		"""Test abs_ to output array with array limit  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_ov_lim_a6(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class abs__invalidarray_I(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('I', [5,4,3,2,1,0,1,2,3,4,5])
		self.dataout = array.array('I', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace(self):
		"""Test abs_ in place - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data)


	########################################################
	def test_abs__inplace_ov_a1(self):
		"""Test abs_ in place with matherrors=True  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True)


	########################################################
	def test_abs__inplace_lim_a2(self):
		"""Test abs_ in place with array limit  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, maxlen=self.limited)


	########################################################
	def test_abs__inplace_ov_lim_a3(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_a4(self):
		"""Test abs_ to output array - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout)


	########################################################
	def test_abs__outputarray_ov_a4(self):
		"""Test abs_ to output array with matherrors=True  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True)


	########################################################
	def test_abs__outputarray_lim_a5(self):
		"""Test abs_ to output array with array limit  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_ov_lim_a6(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class abs__invalidarray_B(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', [5,4,3,2,1,0,1,2,3,4,5])
		self.dataout = array.array('B', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_abs__inplace(self):
		"""Test abs_ in place - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data)


	########################################################
	def test_abs__inplace_ov_a1(self):
		"""Test abs_ in place with matherrors=True  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True)


	########################################################
	def test_abs__inplace_lim_a2(self):
		"""Test abs_ in place with array limit  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, maxlen=self.limited)


	########################################################
	def test_abs__inplace_ov_lim_a3(self):
		"""Test abs_ in place with matherrors=True and array limit  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_a4(self):
		"""Test abs_ to output array - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout)


	########################################################
	def test_abs__outputarray_ov_a4(self):
		"""Test abs_ to output array with matherrors=True  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True)


	########################################################
	def test_abs__outputarray_lim_a5(self):
		"""Test abs_ to output array with array limit  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_abs__outputarray_ov_lim_a6(self):
		"""Test abs_ to output array with matherrors=True and array limit - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.abs_(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class overflow_signed_ovflmin_b(unittest.TestCase):
	"""Test abs_ for value overflow for negating or taking absolute 
	values of min values in signed arrays.
	param_overflow_minval_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.maxarray = array.array('b', itertools.repeat(self.MaxLimit, arraysize))
		self.minarray = array.array('b', itertools.repeat(self.MinLimit, arraysize))

		self.dataout = array.array('b', itertools.repeat(0, arraysize))



	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for overflow of min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray)


	########################################################
	def test_abs__array_num_array_a2(self):
		"""Test abs_ as *array-array* for overflow of min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray, self.dataout)


	########################################################
	def test_abs__array_none_b1(self):
		"""Test abs_ as *array-none* for overflow of min value with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, matherrors=True)


	########################################################
	def test_abs__array_num_array_b2(self):
		"""Test abs_ as *array-array* for overflow of min value with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_h(unittest.TestCase):
	"""Test abs_ for value overflow for negating or taking absolute 
	values of min values in signed arrays.
	param_overflow_minval_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.maxarray = array.array('h', itertools.repeat(self.MaxLimit, arraysize))
		self.minarray = array.array('h', itertools.repeat(self.MinLimit, arraysize))

		self.dataout = array.array('h', itertools.repeat(0, arraysize))



	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for overflow of min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray)


	########################################################
	def test_abs__array_num_array_a2(self):
		"""Test abs_ as *array-array* for overflow of min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray, self.dataout)


	########################################################
	def test_abs__array_none_b1(self):
		"""Test abs_ as *array-none* for overflow of min value with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, matherrors=True)


	########################################################
	def test_abs__array_num_array_b2(self):
		"""Test abs_ as *array-array* for overflow of min value with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_i(unittest.TestCase):
	"""Test abs_ for value overflow for negating or taking absolute 
	values of min values in signed arrays.
	param_overflow_minval_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.maxarray = array.array('i', itertools.repeat(self.MaxLimit, arraysize))
		self.minarray = array.array('i', itertools.repeat(self.MinLimit, arraysize))

		self.dataout = array.array('i', itertools.repeat(0, arraysize))



	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for overflow of min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray)


	########################################################
	def test_abs__array_num_array_a2(self):
		"""Test abs_ as *array-array* for overflow of min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray, self.dataout)


	########################################################
	def test_abs__array_none_b1(self):
		"""Test abs_ as *array-none* for overflow of min value with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, matherrors=True)


	########################################################
	def test_abs__array_num_array_b2(self):
		"""Test abs_ as *array-array* for overflow of min value with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_l(unittest.TestCase):
	"""Test abs_ for value overflow for negating or taking absolute 
	values of min values in signed arrays.
	param_overflow_minval_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.maxarray = array.array('l', itertools.repeat(self.MaxLimit, arraysize))
		self.minarray = array.array('l', itertools.repeat(self.MinLimit, arraysize))

		self.dataout = array.array('l', itertools.repeat(0, arraysize))



	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for overflow of min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray)


	########################################################
	def test_abs__array_num_array_a2(self):
		"""Test abs_ as *array-array* for overflow of min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray, self.dataout)


	########################################################
	def test_abs__array_none_b1(self):
		"""Test abs_ as *array-none* for overflow of min value with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, matherrors=True)


	########################################################
	def test_abs__array_num_array_b2(self):
		"""Test abs_ as *array-array* for overflow of min value with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_q(unittest.TestCase):
	"""Test abs_ for value overflow for negating or taking absolute 
	values of min values in signed arrays.
	param_overflow_minval_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.maxarray = array.array('q', itertools.repeat(self.MaxLimit, arraysize))
		self.minarray = array.array('q', itertools.repeat(self.MinLimit, arraysize))

		self.dataout = array.array('q', itertools.repeat(0, arraysize))



	########################################################
	def test_abs__array_none_a1(self):
		"""Test abs_ as *array-none* for overflow of min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray)


	########################################################
	def test_abs__array_num_array_a2(self):
		"""Test abs_ as *array-array* for overflow of min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.abs_(self.minarray, self.dataout)


	########################################################
	def test_abs__array_none_b1(self):
		"""Test abs_ as *array-none* for overflow of min value with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, matherrors=True)


	########################################################
	def test_abs__array_num_array_b2(self):
		"""Test abs_ as *array-array* for overflow of min value with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.abs_(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.abs_(self.minarray, self.dataout, matherrors=True)



##############################################################################


##############################################################################
class abs__nandata_exceptions_nan_f(unittest.TestCase):
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
	def test_abs__outputarray_a1(self):
		"""Test abs_ for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datanan, self.dataout)


	########################################################
	def test_abs__inplace_a2(self):
		"""Test abs_ in place for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datanan)


	########################################################
	def test_abs__ov_outputarray_a3(self):
		"""Test abs_ for data of nan with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.abs_(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__ov_inplace_a4(self):
		"""Test abs_ in place for data of nan with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.abs_(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class abs__nandata_exceptions_nan_d(unittest.TestCase):
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
	def test_abs__outputarray_a1(self):
		"""Test abs_ for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datanan, self.dataout)


	########################################################
	def test_abs__inplace_a2(self):
		"""Test abs_ in place for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datanan)


	########################################################
	def test_abs__ov_outputarray_a3(self):
		"""Test abs_ for data of nan with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.abs_(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__ov_inplace_a4(self):
		"""Test abs_ in place for data of nan with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.abs_(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class abs__nandata_exceptions_inf_f(unittest.TestCase):
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
	def test_abs__outputarray_a1(self):
		"""Test abs_ for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datainf, self.dataout)


	########################################################
	def test_abs__inplace_a2(self):
		"""Test abs_ in place for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datainf)


	########################################################
	def test_abs__ov_outputarray_a3(self):
		"""Test abs_ for data of inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.abs_(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__ov_inplace_a4(self):
		"""Test abs_ in place for data of inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.abs_(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class abs__nandata_exceptions_inf_d(unittest.TestCase):
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
	def test_abs__outputarray_a1(self):
		"""Test abs_ for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datainf, self.dataout)


	########################################################
	def test_abs__inplace_a2(self):
		"""Test abs_ in place for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.datainf)


	########################################################
	def test_abs__ov_outputarray_a3(self):
		"""Test abs_ for data of inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.abs_(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__ov_inplace_a4(self):
		"""Test abs_ in place for data of inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.abs_(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class abs__nandata_exceptions_ninf_f(unittest.TestCase):
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
	def test_abs__outputarray_a1(self):
		"""Test abs_ for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.dataninf, self.dataout)


	########################################################
	def test_abs__inplace_a2(self):
		"""Test abs_ in place for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.dataninf)


	########################################################
	def test_abs__ov_outputarray_a3(self):
		"""Test abs_ for data of -inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.abs_(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__ov_inplace_a4(self):
		"""Test abs_ in place for data of -inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.abs_(self.dataninf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataninf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class abs__nandata_exceptions_ninf_d(unittest.TestCase):
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
	def test_abs__outputarray_a1(self):
		"""Test abs_ for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.dataninf, self.dataout)


	########################################################
	def test_abs__inplace_a2(self):
		"""Test abs_ in place for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.abs_(self.dataninf)


	########################################################
	def test_abs__ov_outputarray_a3(self):
		"""Test abs_ for data of -inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.abs_(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_abs__ov_inplace_a4(self):
		"""Test abs_ in place for data of -inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [abs(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.abs_(self.dataninf, matherrors=True)

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
			f.write('abs_\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
