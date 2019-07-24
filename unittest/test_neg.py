#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_neg.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      06-Jul-2019.
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
"""This conducts unit tests for neg.
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
class neg_general_even_arraysize_with_simd_b(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('b', xdata)
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code b.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_odd_arraysize_with_simd_b(unittest.TestCase):
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('b', xdata)
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code b.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_even_arraysize_without_simd_b(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('b', xdata)
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code b.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code b.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code b.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_param_errors_b(unittest.TestCase):
	"""Test neg for invalid array and numeric parameters.
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
	def test_neg_array_array_a1(self):
		"""Test neg as *array-array* for invalid type of input array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.badarray1, self.dataout)


	########################################################
	def test_neg_array_array_a2(self):
		"""Test neg as *array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.testarray2, self.baddataout)


	########################################################
	def test_neg_no_params_b1(self):
		"""Test neg with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg()


##############################################################################



##############################################################################
class neg_opt_param_errors_b(unittest.TestCase):
	"""Test neg for invalid errors flag and maxlen parameters.
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for matherrors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, matherrors='a')


	########################################################
	def test_neg_array_none_a2(self):
		"""Test neg as *array-none* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, maxlen='a')


	########################################################
	def test_neg_array_none_a3(self):
		"""Test neg as *array-none* for nosimd='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, nosimd='a')



	########################################################
	def test_neg_array_array_b1(self):
		"""Test neg as *array-array* for matherrors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, matherrors='a')


	########################################################
	def test_neg_array_array_b2(self):
		"""Test neg as *array-array* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_neg_array_array_b3(self):
		"""Test neg as *array-array* for nosimd='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, nosimd='a')


##############################################################################



##############################################################################
class neg_general_even_arraysize_with_simd_h(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('h', xdata)
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code h.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_odd_arraysize_with_simd_h(unittest.TestCase):
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('h', xdata)
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code h.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_even_arraysize_without_simd_h(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('h', xdata)
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code h.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code h.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code h.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_param_errors_h(unittest.TestCase):
	"""Test neg for invalid array and numeric parameters.
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
	def test_neg_array_array_a1(self):
		"""Test neg as *array-array* for invalid type of input array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.badarray1, self.dataout)


	########################################################
	def test_neg_array_array_a2(self):
		"""Test neg as *array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.testarray2, self.baddataout)


	########################################################
	def test_neg_no_params_b1(self):
		"""Test neg with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg()


##############################################################################



##############################################################################
class neg_opt_param_errors_h(unittest.TestCase):
	"""Test neg for invalid errors flag and maxlen parameters.
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for matherrors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, matherrors='a')


	########################################################
	def test_neg_array_none_a2(self):
		"""Test neg as *array-none* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, maxlen='a')


	########################################################
	def test_neg_array_none_a3(self):
		"""Test neg as *array-none* for nosimd='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, nosimd='a')



	########################################################
	def test_neg_array_array_b1(self):
		"""Test neg as *array-array* for matherrors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, matherrors='a')


	########################################################
	def test_neg_array_array_b2(self):
		"""Test neg as *array-array* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_neg_array_array_b3(self):
		"""Test neg as *array-array* for nosimd='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, nosimd='a')


##############################################################################



##############################################################################
class neg_general_even_arraysize_with_simd_i(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('i', xdata)
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code i.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_odd_arraysize_with_simd_i(unittest.TestCase):
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('i', xdata)
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code i.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_even_arraysize_without_simd_i(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('i', xdata)
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code i.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code i.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code i.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_param_errors_i(unittest.TestCase):
	"""Test neg for invalid array and numeric parameters.
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
	def test_neg_array_array_a1(self):
		"""Test neg as *array-array* for invalid type of input array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.badarray1, self.dataout)


	########################################################
	def test_neg_array_array_a2(self):
		"""Test neg as *array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.testarray2, self.baddataout)


	########################################################
	def test_neg_no_params_b1(self):
		"""Test neg with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg()


##############################################################################



##############################################################################
class neg_opt_param_errors_i(unittest.TestCase):
	"""Test neg for invalid errors flag and maxlen parameters.
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for matherrors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, matherrors='a')


	########################################################
	def test_neg_array_none_a2(self):
		"""Test neg as *array-none* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, maxlen='a')


	########################################################
	def test_neg_array_none_a3(self):
		"""Test neg as *array-none* for nosimd='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, nosimd='a')



	########################################################
	def test_neg_array_array_b1(self):
		"""Test neg as *array-array* for matherrors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, matherrors='a')


	########################################################
	def test_neg_array_array_b2(self):
		"""Test neg as *array-array* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_neg_array_array_b3(self):
		"""Test neg as *array-array* for nosimd='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, nosimd='a')


##############################################################################



##############################################################################
class neg_general_even_arraysize_with_simd_l(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('l', xdata)
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code l.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_odd_arraysize_with_simd_l(unittest.TestCase):
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('l', xdata)
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code l.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_even_arraysize_without_simd_l(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('l', xdata)
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code l.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code l.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code l.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_param_errors_l(unittest.TestCase):
	"""Test neg for invalid array and numeric parameters.
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
	def test_neg_array_array_a1(self):
		"""Test neg as *array-array* for invalid type of input array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.badarray1, self.dataout)


	########################################################
	def test_neg_array_array_a2(self):
		"""Test neg as *array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.testarray2, self.baddataout)


	########################################################
	def test_neg_no_params_b1(self):
		"""Test neg with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg()


##############################################################################



##############################################################################
class neg_opt_param_errors_l(unittest.TestCase):
	"""Test neg for invalid errors flag and maxlen parameters.
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for matherrors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, matherrors='a')


	########################################################
	def test_neg_array_none_a2(self):
		"""Test neg as *array-none* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, maxlen='a')


	########################################################
	def test_neg_array_none_a3(self):
		"""Test neg as *array-none* for nosimd='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, nosimd='a')



	########################################################
	def test_neg_array_array_b1(self):
		"""Test neg as *array-array* for matherrors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, matherrors='a')


	########################################################
	def test_neg_array_array_b2(self):
		"""Test neg as *array-array* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_neg_array_array_b3(self):
		"""Test neg as *array-array* for nosimd='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, nosimd='a')


##############################################################################



##############################################################################
class neg_general_even_arraysize_with_simd_q(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('q', xdata)
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code q.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_odd_arraysize_with_simd_q(unittest.TestCase):
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('q', xdata)
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code q.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_even_arraysize_without_simd_q(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('q', xdata)
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code q.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code q.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code q.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_param_errors_q(unittest.TestCase):
	"""Test neg for invalid array and numeric parameters.
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
	def test_neg_array_array_a1(self):
		"""Test neg as *array-array* for invalid type of input array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.badarray1, self.dataout)


	########################################################
	def test_neg_array_array_a2(self):
		"""Test neg as *array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.testarray2, self.baddataout)


	########################################################
	def test_neg_no_params_b1(self):
		"""Test neg with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg()


##############################################################################



##############################################################################
class neg_opt_param_errors_q(unittest.TestCase):
	"""Test neg for invalid errors flag and maxlen parameters.
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for matherrors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, matherrors='a')


	########################################################
	def test_neg_array_none_a2(self):
		"""Test neg as *array-none* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, maxlen='a')


	########################################################
	def test_neg_array_none_a3(self):
		"""Test neg as *array-none* for nosimd='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, nosimd='a')



	########################################################
	def test_neg_array_array_b1(self):
		"""Test neg as *array-array* for matherrors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, matherrors='a')


	########################################################
	def test_neg_array_array_b2(self):
		"""Test neg as *array-array* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_neg_array_array_b3(self):
		"""Test neg as *array-array* for nosimd='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, nosimd='a')


##############################################################################



##############################################################################
class neg_general_even_arraysize_with_simd_f(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('f', xdata)
		self.dataout = array.array('f', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code f.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_odd_arraysize_with_simd_f(unittest.TestCase):
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('f', xdata)
		self.dataout = array.array('f', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code f.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_even_arraysize_without_simd_f(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('f', xdata)
		self.dataout = array.array('f', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code f.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code f.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code f.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_param_errors_f(unittest.TestCase):
	"""Test neg for invalid array and numeric parameters.
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
	def test_neg_array_array_a1(self):
		"""Test neg as *array-array* for invalid type of input array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.badarray1, self.dataout)


	########################################################
	def test_neg_array_array_a2(self):
		"""Test neg as *array-array* for invalid type of output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.testarray2, self.baddataout)


	########################################################
	def test_neg_no_params_b1(self):
		"""Test neg with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg()


##############################################################################



##############################################################################
class neg_opt_param_errors_f(unittest.TestCase):
	"""Test neg for invalid errors flag and maxlen parameters.
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, matherrors='a')


	########################################################
	def test_neg_array_none_a2(self):
		"""Test neg as *array-none* for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, maxlen='a')


	########################################################
	def test_neg_array_none_a3(self):
		"""Test neg as *array-none* for nosimd='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, nosimd='a')



	########################################################
	def test_neg_array_array_b1(self):
		"""Test neg as *array-array* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, matherrors='a')


	########################################################
	def test_neg_array_array_b2(self):
		"""Test neg as *array-array* for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_neg_array_array_b3(self):
		"""Test neg as *array-array* for nosimd='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, nosimd='a')


##############################################################################



##############################################################################
class neg_general_even_arraysize_with_simd_d(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('d', xdata)
		self.dataout = array.array('d', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code d.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_odd_arraysize_with_simd_d(unittest.TestCase):
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

		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('d', xdata)
		self.dataout = array.array('d', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code d.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_general_even_arraysize_without_simd_d(unittest.TestCase):
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

		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4,5]), range(testdatasize))]

		self.data = array.array('d', xdata)
		self.dataout = array.array('d', [0]*len(self.data))

		self.expected = [-(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_neg_inplace_a1(self):
		"""Test neg in place - Array code d.
		"""
		expected = [-(x) for x in self.data]

		arrayfunc.neg(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_a2(self):
		"""Test neg in place with matherrors=True  - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_maxlen_a3(self):
		"""Test neg in place with array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_inplace_ov_maxlen_a4(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_neg_outputarray_a5(self):
		"""Test neg to output array - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_a6(self):
		"""Test neg to output array with matherrors=True  - Array code d.
		"""
		expected = [-(x) for x in self.data]
		arrayfunc.neg(self.data, self.dataout, matherrors=True , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_maxlen_a7(self):
		"""Test neg to output array with array maxlen  - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_outputarray_ov_maxlen_a8(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code d.
		"""
		pydataout = [-(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class neg_param_errors_d(unittest.TestCase):
	"""Test neg for invalid array and numeric parameters.
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
	def test_neg_array_array_a1(self):
		"""Test neg as *array-array* for invalid type of input array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.badarray1, self.dataout)


	########################################################
	def test_neg_array_array_a2(self):
		"""Test neg as *array-array* for invalid type of output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.testarray2, self.baddataout)


	########################################################
	def test_neg_no_params_b1(self):
		"""Test neg with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg()


##############################################################################



##############################################################################
class neg_opt_param_errors_d(unittest.TestCase):
	"""Test neg for invalid errors flag and maxlen parameters.
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, matherrors='a')


	########################################################
	def test_neg_array_none_a2(self):
		"""Test neg as *array-none* for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, maxlen='a')


	########################################################
	def test_neg_array_none_a3(self):
		"""Test neg as *array-none* for nosimd='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, nosimd='a')



	########################################################
	def test_neg_array_array_b1(self):
		"""Test neg as *array-array* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, matherrors='a')


	########################################################
	def test_neg_array_array_b2(self):
		"""Test neg as *array-array* for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_neg_array_array_b3(self):
		"""Test neg as *array-array* for nosimd='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.inparray1a, self.dataout, nosimd=False)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.inparray1b, self.dataout, nosimd='a')


##############################################################################



##############################################################################
class neg_invalidarray_B(unittest.TestCase):
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
	def test_neg_inplace(self):
		"""Test neg in place - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data)


	########################################################
	def test_neg_inplace_ov_a1(self):
		"""Test neg in place with matherrors=True  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True)


	########################################################
	def test_neg_inplace_maxlen_a2(self):
		"""Test neg in place with array maxlen  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, maxlen=self.limited)


	########################################################
	def test_neg_inplace_ov_maxlen_a3(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_a4(self):
		"""Test neg to output array - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout)


	########################################################
	def test_neg_outputarray_ov_a4(self):
		"""Test neg to output array with matherrors=True  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True)


	########################################################
	def test_neg_outputarray_maxlen_a5(self):
		"""Test neg to output array with array maxlen  - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_ov_maxlen_a6(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class neg_invalidarray_H(unittest.TestCase):
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
	def test_neg_inplace(self):
		"""Test neg in place - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data)


	########################################################
	def test_neg_inplace_ov_a1(self):
		"""Test neg in place with matherrors=True  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True)


	########################################################
	def test_neg_inplace_maxlen_a2(self):
		"""Test neg in place with array maxlen  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, maxlen=self.limited)


	########################################################
	def test_neg_inplace_ov_maxlen_a3(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_a4(self):
		"""Test neg to output array - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout)


	########################################################
	def test_neg_outputarray_ov_a4(self):
		"""Test neg to output array with matherrors=True  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True)


	########################################################
	def test_neg_outputarray_maxlen_a5(self):
		"""Test neg to output array with array maxlen  - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_ov_maxlen_a6(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class neg_invalidarray_I(unittest.TestCase):
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
	def test_neg_inplace(self):
		"""Test neg in place - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data)


	########################################################
	def test_neg_inplace_ov_a1(self):
		"""Test neg in place with matherrors=True  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True)


	########################################################
	def test_neg_inplace_maxlen_a2(self):
		"""Test neg in place with array maxlen  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, maxlen=self.limited)


	########################################################
	def test_neg_inplace_ov_maxlen_a3(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_a4(self):
		"""Test neg to output array - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout)


	########################################################
	def test_neg_outputarray_ov_a4(self):
		"""Test neg to output array with matherrors=True  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True)


	########################################################
	def test_neg_outputarray_maxlen_a5(self):
		"""Test neg to output array with array maxlen  - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_ov_maxlen_a6(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class neg_invalidarray_L(unittest.TestCase):
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
	def test_neg_inplace(self):
		"""Test neg in place - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data)


	########################################################
	def test_neg_inplace_ov_a1(self):
		"""Test neg in place with matherrors=True  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True)


	########################################################
	def test_neg_inplace_maxlen_a2(self):
		"""Test neg in place with array maxlen  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, maxlen=self.limited)


	########################################################
	def test_neg_inplace_ov_maxlen_a3(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_a4(self):
		"""Test neg to output array - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout)


	########################################################
	def test_neg_outputarray_ov_a4(self):
		"""Test neg to output array with matherrors=True  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True)


	########################################################
	def test_neg_outputarray_maxlen_a5(self):
		"""Test neg to output array with array maxlen  - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_ov_maxlen_a6(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class neg_invalidarray_Q(unittest.TestCase):
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
	def test_neg_inplace(self):
		"""Test neg in place - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data)


	########################################################
	def test_neg_inplace_ov_a1(self):
		"""Test neg in place with matherrors=True  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True)


	########################################################
	def test_neg_inplace_maxlen_a2(self):
		"""Test neg in place with array maxlen  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, maxlen=self.limited)


	########################################################
	def test_neg_inplace_ov_maxlen_a3(self):
		"""Test neg in place with matherrors=True and array maxlen  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_a4(self):
		"""Test neg to output array - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout)


	########################################################
	def test_neg_outputarray_ov_a4(self):
		"""Test neg to output array with matherrors=True  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True)


	########################################################
	def test_neg_outputarray_maxlen_a5(self):
		"""Test neg to output array with array maxlen  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_neg_outputarray_ov_maxlen_a6(self):
		"""Test neg to output array with matherrors=True and array maxlen - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.neg(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################



##############################################################################
class overflow_signed_ovflmin_b(unittest.TestCase):
	"""Test neg for value overflow for negating or taking absolute 
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for overflow of min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray)


	########################################################
	def test_neg_array_num_array_a2(self):
		"""Test neg as *array-array* for overflow of min value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray, self.dataout)


	########################################################
	def test_neg_array_none_b1(self):
		"""Test neg as *array-none* for overflow of min value with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, matherrors=True)


	########################################################
	def test_neg_array_num_array_b2(self):
		"""Test neg as *array-array* for overflow of min value with matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_h(unittest.TestCase):
	"""Test neg for value overflow for negating or taking absolute 
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for overflow of min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray)


	########################################################
	def test_neg_array_num_array_a2(self):
		"""Test neg as *array-array* for overflow of min value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray, self.dataout)


	########################################################
	def test_neg_array_none_b1(self):
		"""Test neg as *array-none* for overflow of min value with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, matherrors=True)


	########################################################
	def test_neg_array_num_array_b2(self):
		"""Test neg as *array-array* for overflow of min value with matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_i(unittest.TestCase):
	"""Test neg for value overflow for negating or taking absolute 
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for overflow of min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray)


	########################################################
	def test_neg_array_num_array_a2(self):
		"""Test neg as *array-array* for overflow of min value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray, self.dataout)


	########################################################
	def test_neg_array_none_b1(self):
		"""Test neg as *array-none* for overflow of min value with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, matherrors=True)


	########################################################
	def test_neg_array_num_array_b2(self):
		"""Test neg as *array-array* for overflow of min value with matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_l(unittest.TestCase):
	"""Test neg for value overflow for negating or taking absolute 
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for overflow of min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray)


	########################################################
	def test_neg_array_num_array_a2(self):
		"""Test neg as *array-array* for overflow of min value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray, self.dataout)


	########################################################
	def test_neg_array_none_b1(self):
		"""Test neg as *array-none* for overflow of min value with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, matherrors=True)


	########################################################
	def test_neg_array_num_array_b2(self):
		"""Test neg as *array-array* for overflow of min value with matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, self.dataout, matherrors=True)



##############################################################################



##############################################################################
class overflow_signed_ovflmin_q(unittest.TestCase):
	"""Test neg for value overflow for negating or taking absolute 
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
	def test_neg_array_none_a1(self):
		"""Test neg as *array-none* for overflow of min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray)


	########################################################
	def test_neg_array_num_array_a2(self):
		"""Test neg as *array-array* for overflow of min value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.neg(self.minarray, self.dataout)


	########################################################
	def test_neg_array_none_b1(self):
		"""Test neg as *array-none* for overflow of min value with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, matherrors=True)


	########################################################
	def test_neg_array_num_array_b2(self):
		"""Test neg as *array-array* for overflow of min value with matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.neg(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.neg(self.minarray, self.dataout, matherrors=True)



##############################################################################


##############################################################################
class neg_nandata_exceptions_nan_f(unittest.TestCase):
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
	def test_neg_outputarray_a1(self):
		"""Test neg for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datanan, self.dataout)


	########################################################
	def test_neg_inplace_a2(self):
		"""Test neg in place for data of nan with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datanan)


	########################################################
	def test_neg_ov_outputarray_a3(self):
		"""Test neg for data of nan with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.neg(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_ov_inplace_a4(self):
		"""Test neg in place for data of nan with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.neg(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class neg_nandata_exceptions_nan_d(unittest.TestCase):
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
	def test_neg_outputarray_a1(self):
		"""Test neg for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datanan, self.dataout)


	########################################################
	def test_neg_inplace_a2(self):
		"""Test neg in place for data of nan with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datanan)


	########################################################
	def test_neg_ov_outputarray_a3(self):
		"""Test neg for data of nan with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.neg(self.datanan, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_ov_inplace_a4(self):
		"""Test neg in place for data of nan with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datanan]

		# This is the actual test.
		arrayfunc.neg(self.datanan, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datanan), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class neg_nandata_exceptions_inf_f(unittest.TestCase):
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
	def test_neg_outputarray_a1(self):
		"""Test neg for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datainf, self.dataout)


	########################################################
	def test_neg_inplace_a2(self):
		"""Test neg in place for data of inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datainf)


	########################################################
	def test_neg_ov_outputarray_a3(self):
		"""Test neg for data of inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.neg(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_ov_inplace_a4(self):
		"""Test neg in place for data of inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.neg(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class neg_nandata_exceptions_inf_d(unittest.TestCase):
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
	def test_neg_outputarray_a1(self):
		"""Test neg for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datainf, self.dataout)


	########################################################
	def test_neg_inplace_a2(self):
		"""Test neg in place for data of inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.datainf)


	########################################################
	def test_neg_ov_outputarray_a3(self):
		"""Test neg for data of inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.neg(self.datainf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_ov_inplace_a4(self):
		"""Test neg in place for data of inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.datainf]

		# This is the actual test.
		arrayfunc.neg(self.datainf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.datainf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class neg_nandata_exceptions_ninf_f(unittest.TestCase):
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
	def test_neg_outputarray_a1(self):
		"""Test neg for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.dataninf, self.dataout)


	########################################################
	def test_neg_inplace_a2(self):
		"""Test neg in place for data of -inf with matherrors checking on and single parameter functions  - Array code f.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.dataninf)


	########################################################
	def test_neg_ov_outputarray_a3(self):
		"""Test neg for data of -inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.neg(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_ov_inplace_a4(self):
		"""Test neg in place for data of -inf with matherrors=True and single parameter functions  - Array code f.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.neg(self.dataninf, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataninf), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class neg_nandata_exceptions_ninf_d(unittest.TestCase):
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
	def test_neg_outputarray_a1(self):
		"""Test neg for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.dataninf, self.dataout)


	########################################################
	def test_neg_inplace_a2(self):
		"""Test neg in place for data of -inf with matherrors checking on and single parameter functions  - Array code d.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.neg(self.dataninf)


	########################################################
	def test_neg_ov_outputarray_a3(self):
		"""Test neg for data of -inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.neg(self.dataninf, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_neg_ov_inplace_a4(self):
		"""Test neg in place for data of -inf with matherrors=True and single parameter functions  - Array code d.
		"""
		# Calculate the expected result.
		expected = [-(x) for x in self.dataninf]

		# This is the actual test.
		arrayfunc.neg(self.dataninf, matherrors=True)

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
			f.write('neg\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
