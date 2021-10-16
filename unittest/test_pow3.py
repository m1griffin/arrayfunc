#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_pow3.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     10-Oct-2021.
# Ver:      14-Oct-2021.
#
###############################################################################
#
#   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for pow3.
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



SCHAR_POW3MAX = 5
SCHAR_POW3MIN = -5 
UCHAR_POW3MAX = 6

SSHORT_POW3MAX = 31
SSHORT_POW3MIN = -32 
USHORT_POW3MAX = 40

SINT_POW3MAX = 1290
SINT_POW3MIN = -1290
UINT_POW3MAX = 1625

# Account for 64 bit versus 32 bit word sizes.
if arrayfunc.arraylimits.l_max == arrayfunc.arraylimits.q_max:

	SLINT_POW3MAX = 2097151
	SLINT_POW3MIN = -2097152
	ULINT_POW3MAX = 2642245

else:

	SLINT_POW3MAX = 1290
	SLINT_POW3MIN = -1290
	ULINT_POW3MAX = 1625


SLLINT_POW3MAX = 2097151
SLLINT_POW3MIN = -2097152
ULLINT_POW3MAX = 2642245



##############################################################################
class pow3_general___arraysize_b(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SCHAR_POW3MAX
		powmindata = SCHAR_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'b' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'b' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('b', self.testdata)
		self.dataoutput = array.array('b', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code b.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code b.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code b.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code b.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code b.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code b.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_b(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SCHAR_POW3MAX
		powmindata = SCHAR_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'b' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'b' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('b', self.testdata)
		self.dataoutput = array.array('b', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code b.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code b.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code b.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code b.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code b.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_b(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SCHAR_POW3MAX
		powmindata = SCHAR_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'b' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'b' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('b', self.testdata)
		self.dataoutput = array.array('b', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code b.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_b(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.b_max
		else:
			limit = arrayfunc.arraylimits.b_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('b', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('b', [0] * arraysize)

		self.dataoutput = array.array('b', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('b', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_min_errors_b(unittest.TestCase):
	"""Test pow3 for value overflow for min value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'min' == 'max':
			limit = arrayfunc.arraylimits.b_max
		else:
			limit = arrayfunc.arraylimits.b_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('b', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('b', [0] * arraysize)

		self.dataoutput = array.array('b', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('b', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_b(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = SCHAR_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SCHAR_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('b', [limit] * arraysize)

		self.dataoutput = array.array('b', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('b', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('b', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_min_errors_b(unittest.TestCase):
	"""Test pow3 for marginal value overflow for min value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'min' == 'max':
			limit = SCHAR_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SCHAR_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('b', [limit] * arraysize)

		self.dataoutput = array.array('b', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('b', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('b', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_B(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = UCHAR_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'B' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'B' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('B', self.testdata)
		self.dataoutput = array.array('B', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code B.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code B.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code B.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code B.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code B.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code B.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_B(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = UCHAR_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'B' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'B' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('B', self.testdata)
		self.dataoutput = array.array('B', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code B.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code B.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code B.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code B.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code B.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_B(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = UCHAR_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'B' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'B' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('B', self.testdata)
		self.dataoutput = array.array('B', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code B.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_B(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.B_max
		else:
			limit = arrayfunc.arraylimits.B_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('B', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('B', [0] * arraysize)

		self.dataoutput = array.array('B', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('B', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_B(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = UCHAR_POW3MAX
			limitovfl = limit + 1
		else:
			limit = 0
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('B', [limit] * arraysize)

		self.dataoutput = array.array('B', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('B', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('B', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_h(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SSHORT_POW3MAX
		powmindata = SSHORT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'h' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'h' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('h', self.testdata)
		self.dataoutput = array.array('h', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code h.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code h.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code h.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code h.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code h.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code h.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_h(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SSHORT_POW3MAX
		powmindata = SSHORT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'h' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'h' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('h', self.testdata)
		self.dataoutput = array.array('h', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code h.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code h.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code h.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code h.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code h.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_h(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SSHORT_POW3MAX
		powmindata = SSHORT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'h' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'h' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('h', self.testdata)
		self.dataoutput = array.array('h', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code h.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_h(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.h_max
		else:
			limit = arrayfunc.arraylimits.h_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('h', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('h', [0] * arraysize)

		self.dataoutput = array.array('h', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('h', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_min_errors_h(unittest.TestCase):
	"""Test pow3 for value overflow for min value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'min' == 'max':
			limit = arrayfunc.arraylimits.h_max
		else:
			limit = arrayfunc.arraylimits.h_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('h', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('h', [0] * arraysize)

		self.dataoutput = array.array('h', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('h', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_h(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = SSHORT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SSHORT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('h', [limit] * arraysize)

		self.dataoutput = array.array('h', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('h', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('h', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_min_errors_h(unittest.TestCase):
	"""Test pow3 for marginal value overflow for min value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'min' == 'max':
			limit = SSHORT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SSHORT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('h', [limit] * arraysize)

		self.dataoutput = array.array('h', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('h', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('h', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_H(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = USHORT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'H' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'H' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('H', self.testdata)
		self.dataoutput = array.array('H', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code H.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code H.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code H.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code H.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code H.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code H.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_H(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = USHORT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'H' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'H' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('H', self.testdata)
		self.dataoutput = array.array('H', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code H.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code H.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code H.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code H.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code H.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_H(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = USHORT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'H' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'H' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('H', self.testdata)
		self.dataoutput = array.array('H', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code H.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_H(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.H_max
		else:
			limit = arrayfunc.arraylimits.H_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('H', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('H', [0] * arraysize)

		self.dataoutput = array.array('H', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('H', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_H(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = USHORT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = 0
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('H', [limit] * arraysize)

		self.dataoutput = array.array('H', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('H', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('H', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_i(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SINT_POW3MAX
		powmindata = SINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'i' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'i' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('i', self.testdata)
		self.dataoutput = array.array('i', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code i.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code i.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code i.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code i.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code i.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code i.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_i(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SINT_POW3MAX
		powmindata = SINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'i' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'i' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('i', self.testdata)
		self.dataoutput = array.array('i', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code i.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code i.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code i.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code i.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code i.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_i(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SINT_POW3MAX
		powmindata = SINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'i' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'i' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('i', self.testdata)
		self.dataoutput = array.array('i', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code i.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_i(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.i_max
		else:
			limit = arrayfunc.arraylimits.i_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('i', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('i', [0] * arraysize)

		self.dataoutput = array.array('i', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('i', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_min_errors_i(unittest.TestCase):
	"""Test pow3 for value overflow for min value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'min' == 'max':
			limit = arrayfunc.arraylimits.i_max
		else:
			limit = arrayfunc.arraylimits.i_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('i', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('i', [0] * arraysize)

		self.dataoutput = array.array('i', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('i', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_i(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = SINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SINT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('i', [limit] * arraysize)

		self.dataoutput = array.array('i', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('i', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('i', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_min_errors_i(unittest.TestCase):
	"""Test pow3 for marginal value overflow for min value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'min' == 'max':
			limit = SINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SINT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('i', [limit] * arraysize)

		self.dataoutput = array.array('i', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('i', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('i', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_I(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = UINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'I' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'I' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('I', self.testdata)
		self.dataoutput = array.array('I', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code I.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code I.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code I.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code I.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code I.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code I.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_I(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = UINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'I' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'I' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('I', self.testdata)
		self.dataoutput = array.array('I', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code I.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code I.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code I.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code I.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code I.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_I(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = UINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'I' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'I' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('I', self.testdata)
		self.dataoutput = array.array('I', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code I.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_I(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.I_max
		else:
			limit = arrayfunc.arraylimits.I_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('I', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('I', [0] * arraysize)

		self.dataoutput = array.array('I', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('I', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_I(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = UINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = 0
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('I', [limit] * arraysize)

		self.dataoutput = array.array('I', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('I', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('I', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_l(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLINT_POW3MAX
		powmindata = SLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'l' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'l' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('l', self.testdata)
		self.dataoutput = array.array('l', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code l.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code l.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code l.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code l.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code l.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code l.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_l(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLINT_POW3MAX
		powmindata = SLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'l' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'l' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('l', self.testdata)
		self.dataoutput = array.array('l', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code l.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code l.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code l.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code l.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code l.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_l(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLINT_POW3MAX
		powmindata = SLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'l' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'l' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('l', self.testdata)
		self.dataoutput = array.array('l', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code l.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_l(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.l_max
		else:
			limit = arrayfunc.arraylimits.l_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('l', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('l', [0] * arraysize)

		self.dataoutput = array.array('l', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('l', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_min_errors_l(unittest.TestCase):
	"""Test pow3 for value overflow for min value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'min' == 'max':
			limit = arrayfunc.arraylimits.l_max
		else:
			limit = arrayfunc.arraylimits.l_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('l', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('l', [0] * arraysize)

		self.dataoutput = array.array('l', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('l', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_l(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = SLINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SLINT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('l', [limit] * arraysize)

		self.dataoutput = array.array('l', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('l', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('l', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_min_errors_l(unittest.TestCase):
	"""Test pow3 for marginal value overflow for min value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'min' == 'max':
			limit = SLINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SLINT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('l', [limit] * arraysize)

		self.dataoutput = array.array('l', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('l', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('l', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_L(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = ULINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'L' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'L' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('L', self.testdata)
		self.dataoutput = array.array('L', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code L.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code L.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code L.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code L.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code L.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code L.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_L(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = ULINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'L' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'L' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('L', self.testdata)
		self.dataoutput = array.array('L', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code L.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code L.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code L.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code L.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code L.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_L(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = ULINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'L' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'L' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('L', self.testdata)
		self.dataoutput = array.array('L', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code L.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_L(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.L_max
		else:
			limit = arrayfunc.arraylimits.L_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('L', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('L', [0] * arraysize)

		self.dataoutput = array.array('L', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('L', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_L(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = ULINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = 0
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('L', [limit] * arraysize)

		self.dataoutput = array.array('L', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('L', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('L', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_q(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'q' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'q' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('q', self.testdata)
		self.dataoutput = array.array('q', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_q(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'q' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'q' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('q', self.testdata)
		self.dataoutput = array.array('q', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_q(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'q' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'q' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('q', self.testdata)
		self.dataoutput = array.array('q', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_q(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.q_max
		else:
			limit = arrayfunc.arraylimits.q_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('q', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('q', [0] * arraysize)

		self.dataoutput = array.array('q', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('q', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_min_errors_q(unittest.TestCase):
	"""Test pow3 for value overflow for min value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'min' == 'max':
			limit = arrayfunc.arraylimits.q_max
		else:
			limit = arrayfunc.arraylimits.q_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('q', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('q', [0] * arraysize)

		self.dataoutput = array.array('q', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('q', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_q(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = SLLINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SLLINT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('q', [limit] * arraysize)

		self.dataoutput = array.array('q', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('q', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('q', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_min_errors_q(unittest.TestCase):
	"""Test pow3 for marginal value overflow for min value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'min' == 'max':
			limit = SLLINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = SLLINT_POW3MIN
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('q', [limit] * arraysize)

		self.dataoutput = array.array('q', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('q', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('q', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_Q(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = ULLINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'Q' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'Q' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('Q', self.testdata)
		self.dataoutput = array.array('Q', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code Q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code Q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code Q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code Q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code Q.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_Q(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = ULLINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'Q' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'Q' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('Q', self.testdata)
		self.dataoutput = array.array('Q', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code Q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code Q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code Q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code Q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code Q.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_Q(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = ULLINT_POW3MAX
		powmindata = 0
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'Q' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'Q' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('Q', self.testdata)
		self.dataoutput = array.array('Q', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code Q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_overflow_max_errors_Q(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.Q_max
		else:
			limit = arrayfunc.arraylimits.Q_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('Q', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('Q', [0] * arraysize)

		self.dataoutput = array.array('Q', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('Q', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_margin_max_errors_Q(unittest.TestCase):
	"""Test pow3 for marginal value overflow for max value.
	param_overflow_margin_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		# These reflect the largest input values which can be used before 
		# integer overflow occurs.
		# Minimum values can only be used for signed data types.
		if 'max' == 'max':
			limit = ULLINT_POW3MAX
			limitovfl = limit + 1
		else:
			limit = 0
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('Q', [limit] * arraysize)

		self.dataoutput = array.array('Q', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('Q', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('Q', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.dataovfl1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow margin value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow margin value - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.dataovfl1, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow margin value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow margin value with error check off - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except OverflowError:
			self.fail('Exception OverflowError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_f(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'f' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'f' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('f', self.testdata)
		self.dataoutput = array.array('f', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code f.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code f.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code f.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code f.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code f.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_f(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'f' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'f' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('f', self.testdata)
		self.dataoutput = array.array('f', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code f.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code f.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code f.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code f.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_f(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'f' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'f' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('f', self.testdata)
		self.dataoutput = array.array('f', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_NaN_errors_f(unittest.TestCase):
	"""Test pow3 for basic general function operation using parameter nan.
	nan_data_error_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()


		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'f' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'f' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('f', self.testdata)

		arraysize = len(self.data1)

		self.dataoutput = array.array('f', [0] * arraysize)

		self.errordata = array.array('f', [float('nan')] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('f', self.testdata)
		self.errordataend[-1] = float('nan')



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_NaN_array_none_a1(self):
		"""Test pow3 as *array-none* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata)


	########################################################
	def test_pow3_NaN_array_array_a2(self):
		"""Test pow3 as *array-array* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata, self.dataoutput)



	########################################################
	def test_pow3_NaN_array_none_b1(self):
		"""Test pow3 as *array-none* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_NaN_array_array_b2(self):
		"""Test pow3 as *array-array* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_NaN_array_none_c1(self):
		"""Test pow3 as *array-none* for nan with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordata), expected)


	########################################################
	def test_pow3_NaN_array_array_c2(self):
		"""Test pow3 as *array-array* for nan with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)



	########################################################
	def test_pow3_NaN_array_none_d1(self):
		"""Test pow3 as *array-none* for nan with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordataend), expected)


	########################################################
	def test_pow3_NaN_array_array_d2(self):
		"""Test pow3 as *array-array* for nan with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


##############################################################################



##############################################################################
class pow3_inf_errors_f(unittest.TestCase):
	"""Test pow3 for basic general function operation using parameter inf.
	nan_data_error_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()


		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'f' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'f' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('f', self.testdata)

		arraysize = len(self.data1)

		self.dataoutput = array.array('f', [0] * arraysize)

		self.errordata = array.array('f', [float('inf')] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('f', self.testdata)
		self.errordataend[-1] = float('inf')



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_inf_array_none_a1(self):
		"""Test pow3 as *array-none* for inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata)


	########################################################
	def test_pow3_inf_array_array_a2(self):
		"""Test pow3 as *array-array* for inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata, self.dataoutput)



	########################################################
	def test_pow3_inf_array_none_b1(self):
		"""Test pow3 as *array-none* for inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_inf_array_array_b2(self):
		"""Test pow3 as *array-array* for inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_inf_array_none_c1(self):
		"""Test pow3 as *array-none* for inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordata), expected)


	########################################################
	def test_pow3_inf_array_array_c2(self):
		"""Test pow3 as *array-array* for inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)



	########################################################
	def test_pow3_inf_array_none_d1(self):
		"""Test pow3 as *array-none* for inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordataend), expected)


	########################################################
	def test_pow3_inf_array_array_d2(self):
		"""Test pow3 as *array-array* for inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


##############################################################################



##############################################################################
class pow3_ninf_errors_f(unittest.TestCase):
	"""Test pow3 for basic general function operation using parameter -inf.
	nan_data_error_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()


		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'f' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'f' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('f', self.testdata)

		arraysize = len(self.data1)

		self.dataoutput = array.array('f', [0] * arraysize)

		self.errordata = array.array('f', [float('-inf')] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('f', self.testdata)
		self.errordataend[-1] = float('-inf')



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_ninf_array_none_a1(self):
		"""Test pow3 as *array-none* for -inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata)


	########################################################
	def test_pow3_ninf_array_array_a2(self):
		"""Test pow3 as *array-array* for -inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata, self.dataoutput)



	########################################################
	def test_pow3_ninf_array_none_b1(self):
		"""Test pow3 as *array-none* for -inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_ninf_array_array_b2(self):
		"""Test pow3 as *array-array* for -inf - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_ninf_array_none_c1(self):
		"""Test pow3 as *array-none* for -inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordata), expected)


	########################################################
	def test_pow3_ninf_array_array_c2(self):
		"""Test pow3 as *array-array* for -inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)



	########################################################
	def test_pow3_ninf_array_none_d1(self):
		"""Test pow3 as *array-none* for -inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordataend), expected)


	########################################################
	def test_pow3_ninf_array_array_d2(self):
		"""Test pow3 as *array-array* for -inf with error check off - Array code f.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


##############################################################################



##############################################################################
class pow3_overflow_max_errors_f(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.f_max
		else:
			limit = arrayfunc.arraylimits.f_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('f', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('f', [0] * arraysize)

		self.dataoutput = array.array('f', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('f', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_min_errors_f(unittest.TestCase):
	"""Test pow3 for value overflow for min value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'min' == 'max':
			limit = arrayfunc.arraylimits.f_max
		else:
			limit = arrayfunc.arraylimits.f_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('f', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('f', [0] * arraysize)

		self.dataoutput = array.array('f', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('f', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_general___arraysize_d(unittest.TestCase):
	"""Test pow3 for basic general function operation using numeric data.
	test_general_templ
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'd' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'd' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('d', self.testdata)
		self.dataoutput = array.array('d', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_basic_array_none_a1(self):
		"""Test pow3 as *array-none* for basic function - Array code d.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_a2(self):
		"""Test pow3 as *array-array* for basic function - Array code d.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_b1(self):
		"""Test pow3 as *array-none* for basic function with array limit - Array code d.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_b2(self):
		"""Test pow3 as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_c1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True - Array code d.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_c2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True - Array code d.
		"""
		expected = self.pyexpected

		arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_pow3_basic_array_none_d1(self):
		"""Test pow3 as *array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.pow3(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_pow3_basic_array_array_d2(self):
		"""Test pow3 as *array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.pow3(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################



##############################################################################
class pow3_param_errors_d(unittest.TestCase):
	"""Test pow3 for invalid array and numeric parameters.
	param_invalid_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'd' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'd' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('d', self.testdata)
		self.dataoutput = array.array('d', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for invalid type of array - Array code d.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytes([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code d.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_pow3_array_array_a3(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code d.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_pow3_array_array_a4(self):
		"""Test pow3 as *array-array* for invalid type of array - Array code d.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_pow3_no_params_b1(self):
		"""Test pow3 with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.pow3()



##############################################################################



##############################################################################
class pow3_opt_param_errors_d(unittest.TestCase):
	"""Test pow3 for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()

		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]


		# If floating point, convert the data to the correct type.
		if 'd' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'd' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('d', self.testdata)
		self.dataoutput = array.array('d', [0] * len(self.data1))



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_array_num_none_a1(self):
		"""Test pow3 as *array-none* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a')


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, maxlen='a')


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_pow3_array_num_none_c1(self):
		"""Test pow3 as *array-none* for matherrors='a' and maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for matherrors='a' and maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################



##############################################################################
class pow3_NaN_errors_d(unittest.TestCase):
	"""Test pow3 for basic general function operation using parameter nan.
	nan_data_error_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()


		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'd' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'd' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('d', self.testdata)

		arraysize = len(self.data1)

		self.dataoutput = array.array('d', [0] * arraysize)

		self.errordata = array.array('d', [float('nan')] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('d', self.testdata)
		self.errordataend[-1] = float('nan')



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_NaN_array_none_a1(self):
		"""Test pow3 as *array-none* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata)


	########################################################
	def test_pow3_NaN_array_array_a2(self):
		"""Test pow3 as *array-array* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata, self.dataoutput)



	########################################################
	def test_pow3_NaN_array_none_b1(self):
		"""Test pow3 as *array-none* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_NaN_array_array_b2(self):
		"""Test pow3 as *array-array* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_NaN_array_none_c1(self):
		"""Test pow3 as *array-none* for nan with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordata), expected)


	########################################################
	def test_pow3_NaN_array_array_c2(self):
		"""Test pow3 as *array-array* for nan with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)



	########################################################
	def test_pow3_NaN_array_none_d1(self):
		"""Test pow3 as *array-none* for nan with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordataend), expected)


	########################################################
	def test_pow3_NaN_array_array_d2(self):
		"""Test pow3 as *array-array* for nan with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


##############################################################################



##############################################################################
class pow3_inf_errors_d(unittest.TestCase):
	"""Test pow3 for basic general function operation using parameter inf.
	nan_data_error_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()


		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'd' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'd' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('d', self.testdata)

		arraysize = len(self.data1)

		self.dataoutput = array.array('d', [0] * arraysize)

		self.errordata = array.array('d', [float('inf')] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('d', self.testdata)
		self.errordataend[-1] = float('inf')



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_inf_array_none_a1(self):
		"""Test pow3 as *array-none* for inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata)


	########################################################
	def test_pow3_inf_array_array_a2(self):
		"""Test pow3 as *array-array* for inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata, self.dataoutput)



	########################################################
	def test_pow3_inf_array_none_b1(self):
		"""Test pow3 as *array-none* for inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_inf_array_array_b2(self):
		"""Test pow3 as *array-array* for inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_inf_array_none_c1(self):
		"""Test pow3 as *array-none* for inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordata), expected)


	########################################################
	def test_pow3_inf_array_array_c2(self):
		"""Test pow3 as *array-array* for inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)



	########################################################
	def test_pow3_inf_array_none_d1(self):
		"""Test pow3 as *array-none* for inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordataend), expected)


	########################################################
	def test_pow3_inf_array_array_d2(self):
		"""Test pow3 as *array-array* for inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


##############################################################################



##############################################################################
class pow3_ninf_errors_d(unittest.TestCase):
	"""Test pow3 for basic general function operation using parameter -inf.
	nan_data_error_template
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


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%0.3f != %0.3f at index %d' % (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%d != %d at index %d' % (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):
		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		cls.testdatasize = cls.simdincr * 4


		# Generate the data test set.
		powmaxdata = SLLINT_POW3MAX
		powmindata = SLLINT_POW3MIN
		# Divide by an odd number so we get odd and even numbers.
		# With b and B arrays we will get all possible values.
		dataincr = (powmaxdata - powmindata) // 251
		if dataincr < 1:
			dataincr = 1
		tdata = list(range(powmindata, powmaxdata + 1, dataincr))
		tdata.extend([powmindata, powmindata + 1, powmaxdata, powmaxdata - 1, 0, 1])
		if powmindata < 0:
			tdata.append(-1)
		# Eliminate duplicates and sort.
		tdata = list(set(tdata))
		tdata.sort()


		# If the sequence is short, repeat it to make it longer.
		if len(tdata) < cls.testdatasize:
			tdata = [x for x,y in zip(itertools.cycle(tdata), range(cls.testdatasize))]

		# If floating point, convert the data to the correct type.
		if 'd' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, 3) for x in cls.testdata]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if 'd' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('d', self.testdata)

		arraysize = len(self.data1)

		self.dataoutput = array.array('d', [0] * arraysize)

		self.errordata = array.array('d', [float('-inf')] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('d', self.testdata)
		self.errordataend[-1] = float('-inf')



	########################################################
	def test_pow3_check_test_data(self):
		"""Test pow3 to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_pow3_ninf_array_none_a1(self):
		"""Test pow3 as *array-none* for -inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata)


	########################################################
	def test_pow3_ninf_array_array_a2(self):
		"""Test pow3 as *array-array* for -inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordata, self.dataoutput)



	########################################################
	def test_pow3_ninf_array_none_b1(self):
		"""Test pow3 as *array-none* for -inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_ninf_array_array_b2(self):
		"""Test pow3 as *array-array* for -inf - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_ninf_array_none_c1(self):
		"""Test pow3 as *array-none* for -inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordata), expected)


	########################################################
	def test_pow3_ninf_array_array_c2(self):
		"""Test pow3 as *array-array* for -inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordata]

		arrayfunc.pow3(self.errordata, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)



	########################################################
	def test_pow3_ninf_array_none_d1(self):
		"""Test pow3 as *array-none* for -inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordataend), expected)


	########################################################
	def test_pow3_ninf_array_array_d2(self):
		"""Test pow3 as *array-array* for -inf with error check off - Array code d.
		"""
		expected = [pow(x, 3) for x in self.errordataend]

		arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


##############################################################################



##############################################################################
class pow3_overflow_max_errors_d(unittest.TestCase):
	"""Test pow3 for value overflow for max value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'max' == 'max':
			limit = arrayfunc.arraylimits.d_max
		else:
			limit = arrayfunc.arraylimits.d_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('d', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('d', [0] * arraysize)

		self.dataoutput = array.array('d', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('d', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


##############################################################################



##############################################################################
class pow3_overflow_min_errors_d(unittest.TestCase):
	"""Test pow3 for value overflow for min value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if 'min' == 'max':
			limit = arrayfunc.arraylimits.d_max
		else:
			limit = arrayfunc.arraylimits.d_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('d', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('d', [0] * arraysize)

		self.dataoutput = array.array('d', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('d', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_pow3_array_none_a1(self):
		"""Test pow3 as *array-none* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1)


	########################################################
	def test_pow3_array_array_a2(self):
		"""Test pow3 as *array-array* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.data1, self.dataoutput)



	########################################################
	def test_pow3_array_none_b1(self):
		"""Test pow3 as *array-none* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend)


	########################################################
	def test_pow3_array_array_b2(self):
		"""Test pow3 as *array-array* for overflow value - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.pow3(self.errordataend, self.dataoutput)



	########################################################
	def test_pow3_array_none_c1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_c2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.data1, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')



	########################################################
	def test_pow3_array_none_d1(self):
		"""Test pow3 as *array-none* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


	########################################################
	def test_pow3_array_array_d2(self):
		"""Test pow3 as *array-array* for overflow value with error check off - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.pow3(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.pow3(self.errordataend, self.dataoutput, matherrors=True)
		except ArithmeticError:
			self.fail('Exception ArithmeticError raised unexpectedly.')


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
			f.write('pow3\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
