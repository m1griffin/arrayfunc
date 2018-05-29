#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_factorial.py
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
"""This conducts unit tests for factorial.
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
class factorial_general_b(unittest.TestCase):
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

		self.data = array.array('b', [0,1,2,3,4,5])
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code b.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code b.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code b.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code b.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code b.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code b.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code b.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code b.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_b(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('b', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_b(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('b', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_B(unittest.TestCase):
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

		self.data = array.array('B', [0,1,2,3,4,5])
		self.dataout = array.array('B', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code B.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code B.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code B.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code B.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code B.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code B.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code B.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code B.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_B(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('B', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_B(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('B', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_h(unittest.TestCase):
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

		self.data = array.array('h', [0,1,2,3,4,5])
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code h.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code h.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code h.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code h.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code h.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code h.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code h.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code h.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_h(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('h', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_h(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('h', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_H(unittest.TestCase):
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

		self.data = array.array('H', [0,1,2,3,4,5])
		self.dataout = array.array('H', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code H.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code H.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code H.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code H.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code H.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code H.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code H.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code H.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_H(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('H', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_H(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('H', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_i(unittest.TestCase):
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

		self.data = array.array('i', [0,1,2,3,4,5])
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code i.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code i.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code i.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code i.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code i.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code i.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code i.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code i.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_i(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('i', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_i(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('i', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_I(unittest.TestCase):
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

		self.data = array.array('I', [0,1,2,3,4,5])
		self.dataout = array.array('I', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code I.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code I.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code I.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code I.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code I.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code I.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code I.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code I.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_I(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('I', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_I(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('I', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_l(unittest.TestCase):
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

		self.data = array.array('l', [0,1,2,3,4,5])
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code l.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code l.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code l.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code l.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code l.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code l.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code l.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code l.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_l(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('l', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_l(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('l', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_L(unittest.TestCase):
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

		self.data = array.array('L', [0,1,2,3,4,5])
		self.dataout = array.array('L', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code L.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code L.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code L.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code L.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code L.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code L.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code L.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code L.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_L(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('L', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_L(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('L', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_q(unittest.TestCase):
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

		self.data = array.array('q', [0,1,2,3,4,5])
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code q.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code q.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code q.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code q.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_q(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('q', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_q(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('q', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_general_Q(unittest.TestCase):
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

		self.data = array.array('Q', [0,1,2,3,4,5])
		self.dataout = array.array('Q', [0]*len(self.data))

		self.expected = [math.factorial(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace_a1(self):
		"""Test factorial in place - Array code Q.
		"""
		expected = [math.factorial(x) for x in self.data]

		arrayfunc.factorial(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_a2(self):
		"""Test factorial in place with matherrors=True  - Array code Q.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_lim_a3(self):
		"""Test factorial in place with array limit  - Array code Q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_inplace_ov_lim_a4(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code Q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_factorial_outputarray_a5(self):
		"""Test factorial to output array - Array code Q.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_a6(self):
		"""Test factorial to output array with matherrors=True  - Array code Q.
		"""
		expected = [math.factorial(x) for x in self.data]
		arrayfunc.factorial(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_lim_a7(self):
		"""Test factorial to output array with array limit  - Array code Q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_factorial_outputarray_ov_lim_a8(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code Q.
		"""
		pydataout = [math.factorial(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class factorial_param_errors_Q(unittest.TestCase):
	"""Test factorial for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('Q', [0,1,2,3,4,5])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_factorial_array_array_a1(self):
		"""Test factorial as *array-array* for invalid type of input array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.badarray1, self.dataout)


	########################################################
	def test_factorial_array_array_a2(self):
		"""Test factorial as *array-array* for invalid type of output array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.testarray2, self.baddataout)


	########################################################
	def test_factorial_no_params_b1(self):
		"""Test factorial with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial()


##############################################################################



##############################################################################
class factorial_opt_param_errors_Q(unittest.TestCase):
	"""Test factorial for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('Q', [0,1,2,3,4,5])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for errors='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, errors='a')


	########################################################
	def test_factorial_array_none_a2(self):
		"""Test factorial as *array-none* for maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, maxlen='a')


	########################################################
	def test_factorial_array_array_b1(self):
		"""Test factorial as *array-array* for errors='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_factorial_array_array_b2(self):
		"""Test factorial as *array-array* for maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.inparray1b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class factorial_invalidarray_d(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0])
		self.dataout = array.array('d', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace(self):
		"""Test factorial in place - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data)


	########################################################
	def test_factorial_inplace_ov_a1(self):
		"""Test factorial in place with matherrors=True  - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, matherrors=True)


	########################################################
	def test_factorial_inplace_lim_a2(self):
		"""Test factorial in place with array limit  - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, maxlen=self.limited)


	########################################################
	def test_factorial_inplace_ov_lim_a3(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_factorial_outputarray_a4(self):
		"""Test factorial to output array - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout)


	########################################################
	def test_factorial_outputarray_ov_a4(self):
		"""Test factorial to output array with matherrors=True  - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout, matherrors=True)


	########################################################
	def test_factorial_outputarray_lim_a5(self):
		"""Test factorial to output array with array limit  - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_factorial_outputarray_ov_lim_a6(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class factorial_invalidarray_f(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0])
		self.dataout = array.array('f', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_factorial_inplace(self):
		"""Test factorial in place - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data)


	########################################################
	def test_factorial_inplace_ov_a1(self):
		"""Test factorial in place with matherrors=True  - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, matherrors=True)


	########################################################
	def test_factorial_inplace_lim_a2(self):
		"""Test factorial in place with array limit  - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, maxlen=self.limited)


	########################################################
	def test_factorial_inplace_ov_lim_a3(self):
		"""Test factorial in place with matherrors=True and array limit  - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_factorial_outputarray_a4(self):
		"""Test factorial to output array - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout)


	########################################################
	def test_factorial_outputarray_ov_a4(self):
		"""Test factorial to output array with matherrors=True  - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout, matherrors=True)


	########################################################
	def test_factorial_outputarray_lim_a5(self):
		"""Test factorial to output array with array limit  - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_factorial_outputarray_ov_lim_a6(self):
		"""Test factorial to output array with matherrors=True and array limit - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.factorial(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class factorial_error_neg_b(unittest.TestCase):
	"""Test factorial for errors in negative factorials in signed integer arrays.
	factorial_negative_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200

		self.negarray = array.array('b', itertools.repeat(-1, arraysize))
		self.goodarray = array.array('b', itertools.repeat(1, arraysize))

		self.dataout = array.array('b', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for negative factorial - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for negative factorial - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for negative factorial with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for negative factorial with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_neg_h(unittest.TestCase):
	"""Test factorial for errors in negative factorials in signed integer arrays.
	factorial_negative_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200

		self.negarray = array.array('h', itertools.repeat(-1, arraysize))
		self.goodarray = array.array('h', itertools.repeat(1, arraysize))

		self.dataout = array.array('h', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for negative factorial - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for negative factorial - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for negative factorial with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for negative factorial with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_neg_i(unittest.TestCase):
	"""Test factorial for errors in negative factorials in signed integer arrays.
	factorial_negative_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200

		self.negarray = array.array('i', itertools.repeat(-1, arraysize))
		self.goodarray = array.array('i', itertools.repeat(1, arraysize))

		self.dataout = array.array('i', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for negative factorial - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for negative factorial - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for negative factorial with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for negative factorial with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_neg_l(unittest.TestCase):
	"""Test factorial for errors in negative factorials in signed integer arrays.
	factorial_negative_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200

		self.negarray = array.array('l', itertools.repeat(-1, arraysize))
		self.goodarray = array.array('l', itertools.repeat(1, arraysize))

		self.dataout = array.array('l', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for negative factorial - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for negative factorial - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for negative factorial with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for negative factorial with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_neg_q(unittest.TestCase):
	"""Test factorial for errors in negative factorials in signed integer arrays.
	factorial_negative_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200

		self.negarray = array.array('q', itertools.repeat(-1, arraysize))
		self.goodarray = array.array('q', itertools.repeat(1, arraysize))

		self.dataout = array.array('q', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for negative factorial - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for negative factorial - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.negarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for negative factorial with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for negative factorial with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.goodarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.negarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_b(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('b', itertools.repeat(maxfactorials['b'], arraysize))
		self.ovflfacarray = array.array('b', itertools.repeat(maxfactorials['b'] + 1, arraysize))

		self.dataout = array.array('b', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_B(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('B', itertools.repeat(maxfactorials['B'], arraysize))
		self.ovflfacarray = array.array('B', itertools.repeat(maxfactorials['B'] + 1, arraysize))

		self.dataout = array.array('B', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_h(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('h', itertools.repeat(maxfactorials['h'], arraysize))
		self.ovflfacarray = array.array('h', itertools.repeat(maxfactorials['h'] + 1, arraysize))

		self.dataout = array.array('h', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_H(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('H', itertools.repeat(maxfactorials['H'], arraysize))
		self.ovflfacarray = array.array('H', itertools.repeat(maxfactorials['H'] + 1, arraysize))

		self.dataout = array.array('H', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_i(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('i', itertools.repeat(maxfactorials['i'], arraysize))
		self.ovflfacarray = array.array('i', itertools.repeat(maxfactorials['i'] + 1, arraysize))

		self.dataout = array.array('i', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_I(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('I', itertools.repeat(maxfactorials['I'], arraysize))
		self.ovflfacarray = array.array('I', itertools.repeat(maxfactorials['I'] + 1, arraysize))

		self.dataout = array.array('I', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_l(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('l', itertools.repeat(maxfactorials['l'], arraysize))
		self.ovflfacarray = array.array('l', itertools.repeat(maxfactorials['l'] + 1, arraysize))

		self.dataout = array.array('l', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_L(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('L', itertools.repeat(maxfactorials['L'], arraysize))
		self.ovflfacarray = array.array('L', itertools.repeat(maxfactorials['L'] + 1, arraysize))

		self.dataout = array.array('L', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_q(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('q', itertools.repeat(maxfactorials['q'], arraysize))
		self.ovflfacarray = array.array('q', itertools.repeat(maxfactorials['q'] + 1, arraysize))

		self.dataout = array.array('q', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class factorial_error_Q(unittest.TestCase):
	"""Test factorial for oversized factorial parameters in signed integer arrays.
	factorial_ovfl_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# These are the largest acceptable numbers to use in factorials for
		# each array type.
		maxfactorials = {'b' : 5, 
				'B' : 5, 
				'h' : 7, 
				'H' : 8, 
				'i' : 12, 
				'I' : 12, 
				'l' : 20, 
				'L' : 20, 
				'q' : 20, 
				'Q' : 20
				}

		arraysize = 200

		self.maxfacarray = array.array('Q', itertools.repeat(maxfactorials['Q'], arraysize))
		self.ovflfacarray = array.array('Q', itertools.repeat(maxfactorials['Q'] + 1, arraysize))

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))



	########################################################
	def test_factorial_array_none_a1(self):
		"""Test factorial as *array-none* for oversized factorial parameters - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray)


	########################################################
	def test_factorial_array_num_array_a2(self):
		"""Test factorial as *array-array* for oversized factorial parameters - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.factorial(self.ovflfacarray, self.dataout)


	########################################################
	def test_factorial_array_none_b1(self):
		"""Test factorial as *array-none* for oversized factorial parameters with matherrors=True - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, matherrors=True)


	########################################################
	def test_factorial_array_num_array_b2(self):
		"""Test factorial as *array-array* for oversized factorial parameters with matherrors=True - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.factorial(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.factorial(self.ovflfacarray, self.dataout, matherrors=True)



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
			f.write('factorial\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
