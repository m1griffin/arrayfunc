#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_truediv.py
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
"""This conducts unit tests for truediv.
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
class truediv_general_even_arraysize_b(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'b' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'b' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'b' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code b.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)
		dataout = array.array('b', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)
		dataout = array.array('b', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)
		dataout = array.array('b', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_b(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'b' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'b' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'b' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code b.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datax_an)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('b', self.datay_na)
				dataout = array.array('b', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)
		dataout = array.array('b', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)
		dataout = array.array('b', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code b.
		"""
		data1 = array.array('b', self.datax_aa)
		data2 = array.array('b', self.datay_aa)
		dataout = array.array('b', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_b(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('b', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('b', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code b.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code b.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code b.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_b(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('b', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('b', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code b.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_b(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.inparray1amax = array.array('b', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('b', [0] * arraysize)
		self.plus1array = array.array('b', [1] * arraysize)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_b(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.inparray1amax = array.array('b', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('b', [0] * arraysize)
		self.plus1array = array.array('b', [1] * arraysize)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_mindivminus1_b(unittest.TestCase):
	"""Test truediv for value overflow for min values divided by -1.
	param_overflow_truediv_mindivminus1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.b_max
		self.MinLimit = arrayfunc.arraylimits.b_min


		self.inparray1amin = array.array('b', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('b', [0] * arraysize)
		self.plus1array = array.array('b', [1] * arraysize)
		self.minus1array = array.array('b', [-1] * arraysize)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))



	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for min value / -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for min value / -1 matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for min value / -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for min value / -1 matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for min value / -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for min value / -1 matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for min value / -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for min value / -1 matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_num_none_e1(self):
		"""Test truediv as *array-array-none* for min value / -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array)


	########################################################
	def test_truediv_array_num_none_e2(self):
		"""Test truediv as *array-array-none* for min value / -1 matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_array_num_none_f1(self):
		"""Test truediv as *array-array-array* for min value / -1 - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout)


	########################################################
	def test_truediv_array_num_none_f2(self):
		"""Test truediv as *array-array-array* for min value / -1 matherrors=True - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_B(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'B' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'B' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'B' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code B.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)
		dataout = array.array('B', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)
		dataout = array.array('B', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)
		dataout = array.array('B', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_B(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'B' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'B' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'B' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code B.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datax_an)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('B', self.datay_na)
				dataout = array.array('B', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)
		dataout = array.array('B', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)
		dataout = array.array('B', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code B.
		"""
		data1 = array.array('B', self.datax_aa)
		data2 = array.array('B', self.datay_aa)
		dataout = array.array('B', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_B(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('B', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('B', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code B.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code B.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code B.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_B(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('B', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('B', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code B.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_B(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.B_max
		self.MinLimit = arrayfunc.arraylimits.B_min


		self.inparray1amax = array.array('B', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('B', [0] * arraysize)
		self.plus1array = array.array('B', [1] * arraysize)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_B(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.B_max
		self.MinLimit = arrayfunc.arraylimits.B_min


		self.inparray1amax = array.array('B', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('B', [0] * arraysize)
		self.plus1array = array.array('B', [1] * arraysize)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_h(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'h' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'h' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'h' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code h.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)
		dataout = array.array('h', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)
		dataout = array.array('h', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)
		dataout = array.array('h', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_h(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'h' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'h' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'h' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code h.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datax_an)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('h', self.datay_na)
				dataout = array.array('h', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)
		dataout = array.array('h', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)
		dataout = array.array('h', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code h.
		"""
		data1 = array.array('h', self.datax_aa)
		data2 = array.array('h', self.datay_aa)
		dataout = array.array('h', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_h(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('h', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('h', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code h.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code h.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code h.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_h(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('h', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('h', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code h.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_h(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.inparray1amax = array.array('h', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('h', [0] * arraysize)
		self.plus1array = array.array('h', [1] * arraysize)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_h(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.inparray1amax = array.array('h', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('h', [0] * arraysize)
		self.plus1array = array.array('h', [1] * arraysize)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_mindivminus1_h(unittest.TestCase):
	"""Test truediv for value overflow for min values divided by -1.
	param_overflow_truediv_mindivminus1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.h_max
		self.MinLimit = arrayfunc.arraylimits.h_min


		self.inparray1amin = array.array('h', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('h', [0] * arraysize)
		self.plus1array = array.array('h', [1] * arraysize)
		self.minus1array = array.array('h', [-1] * arraysize)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))



	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for min value / -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for min value / -1 matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for min value / -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for min value / -1 matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for min value / -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for min value / -1 matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for min value / -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for min value / -1 matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_num_none_e1(self):
		"""Test truediv as *array-array-none* for min value / -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array)


	########################################################
	def test_truediv_array_num_none_e2(self):
		"""Test truediv as *array-array-none* for min value / -1 matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_array_num_none_f1(self):
		"""Test truediv as *array-array-array* for min value / -1 - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout)


	########################################################
	def test_truediv_array_num_none_f2(self):
		"""Test truediv as *array-array-array* for min value / -1 matherrors=True - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_H(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'H' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'H' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'H' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code H.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)
		dataout = array.array('H', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)
		dataout = array.array('H', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)
		dataout = array.array('H', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_H(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'H' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'H' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'H' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code H.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datax_an)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('H', self.datay_na)
				dataout = array.array('H', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)
		dataout = array.array('H', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)
		dataout = array.array('H', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code H.
		"""
		data1 = array.array('H', self.datax_aa)
		data2 = array.array('H', self.datay_aa)
		dataout = array.array('H', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_H(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('H', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('H', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code H.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code H.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code H.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_H(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('H', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('H', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code H.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_H(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.H_max
		self.MinLimit = arrayfunc.arraylimits.H_min


		self.inparray1amax = array.array('H', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('H', [0] * arraysize)
		self.plus1array = array.array('H', [1] * arraysize)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_H(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.H_max
		self.MinLimit = arrayfunc.arraylimits.H_min


		self.inparray1amax = array.array('H', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('H', [0] * arraysize)
		self.plus1array = array.array('H', [1] * arraysize)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_i(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'i' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'i' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'i' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code i.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)
		dataout = array.array('i', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)
		dataout = array.array('i', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)
		dataout = array.array('i', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_i(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'i' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'i' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'i' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code i.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datax_an)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('i', self.datay_na)
				dataout = array.array('i', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)
		dataout = array.array('i', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)
		dataout = array.array('i', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code i.
		"""
		data1 = array.array('i', self.datax_aa)
		data2 = array.array('i', self.datay_aa)
		dataout = array.array('i', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_i(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('i', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('i', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code i.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code i.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code i.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_i(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('i', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('i', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code i.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_i(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.inparray1amax = array.array('i', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('i', [0] * arraysize)
		self.plus1array = array.array('i', [1] * arraysize)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_i(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.inparray1amax = array.array('i', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('i', [0] * arraysize)
		self.plus1array = array.array('i', [1] * arraysize)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_mindivminus1_i(unittest.TestCase):
	"""Test truediv for value overflow for min values divided by -1.
	param_overflow_truediv_mindivminus1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.i_max
		self.MinLimit = arrayfunc.arraylimits.i_min


		self.inparray1amin = array.array('i', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('i', [0] * arraysize)
		self.plus1array = array.array('i', [1] * arraysize)
		self.minus1array = array.array('i', [-1] * arraysize)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))



	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for min value / -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for min value / -1 matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for min value / -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for min value / -1 matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for min value / -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for min value / -1 matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for min value / -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for min value / -1 matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_num_none_e1(self):
		"""Test truediv as *array-array-none* for min value / -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array)


	########################################################
	def test_truediv_array_num_none_e2(self):
		"""Test truediv as *array-array-none* for min value / -1 matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_array_num_none_f1(self):
		"""Test truediv as *array-array-array* for min value / -1 - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout)


	########################################################
	def test_truediv_array_num_none_f2(self):
		"""Test truediv as *array-array-array* for min value / -1 matherrors=True - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_I(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'I' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'I' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'I' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code I.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)
		dataout = array.array('I', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)
		dataout = array.array('I', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)
		dataout = array.array('I', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_I(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'I' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'I' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'I' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code I.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datax_an)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('I', self.datay_na)
				dataout = array.array('I', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)
		dataout = array.array('I', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)
		dataout = array.array('I', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code I.
		"""
		data1 = array.array('I', self.datax_aa)
		data2 = array.array('I', self.datay_aa)
		dataout = array.array('I', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_I(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('I', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('I', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code I.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code I.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code I.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_I(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('I', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('I', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code I.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_I(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.I_max
		self.MinLimit = arrayfunc.arraylimits.I_min


		self.inparray1amax = array.array('I', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('I', [0] * arraysize)
		self.plus1array = array.array('I', [1] * arraysize)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_I(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.I_max
		self.MinLimit = arrayfunc.arraylimits.I_min


		self.inparray1amax = array.array('I', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('I', [0] * arraysize)
		self.plus1array = array.array('I', [1] * arraysize)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_l(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'l' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'l' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'l' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code l.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)
		dataout = array.array('l', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)
		dataout = array.array('l', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)
		dataout = array.array('l', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_l(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'l' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'l' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'l' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code l.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datax_an)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('l', self.datay_na)
				dataout = array.array('l', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)
		dataout = array.array('l', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)
		dataout = array.array('l', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code l.
		"""
		data1 = array.array('l', self.datax_aa)
		data2 = array.array('l', self.datay_aa)
		dataout = array.array('l', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_l(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('l', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('l', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code l.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code l.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code l.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_l(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('l', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('l', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code l.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_l(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.inparray1amax = array.array('l', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('l', [0] * arraysize)
		self.plus1array = array.array('l', [1] * arraysize)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_l(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.inparray1amax = array.array('l', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('l', [0] * arraysize)
		self.plus1array = array.array('l', [1] * arraysize)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_mindivminus1_l(unittest.TestCase):
	"""Test truediv for value overflow for min values divided by -1.
	param_overflow_truediv_mindivminus1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.l_max
		self.MinLimit = arrayfunc.arraylimits.l_min


		self.inparray1amin = array.array('l', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('l', [0] * arraysize)
		self.plus1array = array.array('l', [1] * arraysize)
		self.minus1array = array.array('l', [-1] * arraysize)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))



	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for min value / -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for min value / -1 matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for min value / -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for min value / -1 matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for min value / -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for min value / -1 matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for min value / -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for min value / -1 matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_num_none_e1(self):
		"""Test truediv as *array-array-none* for min value / -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array)


	########################################################
	def test_truediv_array_num_none_e2(self):
		"""Test truediv as *array-array-none* for min value / -1 matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_array_num_none_f1(self):
		"""Test truediv as *array-array-array* for min value / -1 - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout)


	########################################################
	def test_truediv_array_num_none_f2(self):
		"""Test truediv as *array-array-array* for min value / -1 matherrors=True - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_L(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'L' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'L' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'L' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code L.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)
		dataout = array.array('L', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)
		dataout = array.array('L', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)
		dataout = array.array('L', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_L(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'L' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'L' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'L' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code L.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datax_an)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('L', self.datay_na)
				dataout = array.array('L', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)
		dataout = array.array('L', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)
		dataout = array.array('L', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code L.
		"""
		data1 = array.array('L', self.datax_aa)
		data2 = array.array('L', self.datay_aa)
		dataout = array.array('L', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_L(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('L', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('L', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code L.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code L.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code L.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_L(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('L', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('L', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code L.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_L(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.L_max
		self.MinLimit = arrayfunc.arraylimits.L_min


		self.inparray1amax = array.array('L', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('L', [0] * arraysize)
		self.plus1array = array.array('L', [1] * arraysize)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_L(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.L_max
		self.MinLimit = arrayfunc.arraylimits.L_min


		self.inparray1amax = array.array('L', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('L', [0] * arraysize)
		self.plus1array = array.array('L', [1] * arraysize)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_q(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'q' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'q' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'q' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)
		dataout = array.array('q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)
		dataout = array.array('q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)
		dataout = array.array('q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_q(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'q' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'q' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'q' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datax_an)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('q', self.datay_na)
				dataout = array.array('q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)
		dataout = array.array('q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)
		dataout = array.array('q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code q.
		"""
		data1 = array.array('q', self.datax_aa)
		data2 = array.array('q', self.datay_aa)
		dataout = array.array('q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_q(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('q', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('q', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_q(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('q', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('q', [x for (x,y) in zip(itertools.cycle([-3,-2,-1,1,2,3,4]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_q(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.inparray1amax = array.array('q', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('q', [0] * arraysize)
		self.plus1array = array.array('q', [1] * arraysize)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_q(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.inparray1amax = array.array('q', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('q', [0] * arraysize)
		self.plus1array = array.array('q', [1] * arraysize)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################




##############################################################################
class overflow_signed_mindivminus1_q(unittest.TestCase):
	"""Test truediv for value overflow for min values divided by -1.
	param_overflow_truediv_mindivminus1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.q_max
		self.MinLimit = arrayfunc.arraylimits.q_min


		self.inparray1amin = array.array('q', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('q', [0] * arraysize)
		self.plus1array = array.array('q', [1] * arraysize)
		self.minus1array = array.array('q', [-1] * arraysize)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))



	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for min value / -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for min value / -1 matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for min value / -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for min value / -1 matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, -1, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for min value / -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for min value / -1 matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for min value / -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for min value / -1 matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_num_none_e1(self):
		"""Test truediv as *array-array-none* for min value / -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array)


	########################################################
	def test_truediv_array_num_none_e2(self):
		"""Test truediv as *array-array-none* for min value / -1 matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_array_num_none_f1(self):
		"""Test truediv as *array-array-array* for min value / -1 - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout)


	########################################################
	def test_truediv_array_num_none_f2(self):
		"""Test truediv as *array-array-array* for min value / -1 matherrors=True - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_Q(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'Q' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'Q' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'Q' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code Q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)
		dataout = array.array('Q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)
		dataout = array.array('Q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)
		dataout = array.array('Q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_Q(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'Q' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'Q' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'Q' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code Q.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datax_an)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('Q', self.datay_na)
				dataout = array.array('Q', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)
		dataout = array.array('Q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)
		dataout = array.array('Q', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code Q.
		"""
		data1 = array.array('Q', self.datax_aa)
		data2 = array.array('Q', self.datay_aa)
		dataout = array.array('Q', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_Q(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('Q', [0,1,2,3,4,5,6,7,8,9])
		self.testarray2 = array.array('Q', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])
		self.badarray2 = array.array('d', [float(x) for x in self.testarray2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code Q.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code Q.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_Q(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('Q', [0,1,2,3,4,5,6,7,8,9])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('Q', [x for (x,y) in zip(itertools.cycle([1,2,4,5,6,7]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_Q(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.Q_max
		self.MinLimit = arrayfunc.arraylimits.Q_min


		self.inparray1amax = array.array('Q', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('Q', [0] * arraysize)
		self.plus1array = array.array('Q', [1] * arraysize)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################




##############################################################################
class overflow_signed_divzero_errors_Q(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.Q_max
		self.MinLimit = arrayfunc.arraylimits.Q_min


		self.inparray1amax = array.array('Q', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('Q', [0] * arraysize)
		self.plus1array = array.array('Q', [1] * arraysize)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0 - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_f(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'f' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'f' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'f' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)
		dataout = array.array('f', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)
		dataout = array.array('f', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_f(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'f' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'f' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'f' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code f.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datax_an)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', self.datay_na)
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)
		dataout = array.array('f', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)
		dataout = array.array('f', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		data1 = array.array('f', self.datax_aa)
		data2 = array.array('f', self.datay_aa)
		dataout = array.array('f', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_f(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.testarray2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])
		self.badarray2 = array.array('i', [int(x) for x in self.testarray2])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code f.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code f.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code f.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code f.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_f(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code f.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_f(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.f_max
		self.MinLimit = arrayfunc.arraylimits.f_min


		self.inparray1amax = array.array('f', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('f', [0.0] * arraysize)
		self.plus1array = array.array('f', [1.0] * arraysize)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1.0)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0.0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0.0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0.0 - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################



##############################################################################
class truediv_NaN_errors_f(unittest.TestCase):
	"""Test truediv for basic general function operation using parameter nan.
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



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('nan')] * arraysize)



	########################################################
	def test_truediv_NaN_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for nan - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval)


	########################################################
	def test_truediv_NaN_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for nan with error check off - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for nan - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval, self.dataout)


	########################################################
	def test_truediv_NaN_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for nan with error check off - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for nan - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(testval, errordata)


	########################################################
	def test_truediv_NaN_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for nan with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for nan - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.truediv(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(testval, self.errordata, self.dataout)


	########################################################
	def test_truediv_NaN_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for nan with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for nan - Array code f.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.truediv(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.truediv(dataok1, self.errordata)


	########################################################
	def test_truediv_NaN_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for nan with error check off - Array code f.
		"""
		expected = [y / x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.truediv(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for nan - Array code f.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.truediv(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_truediv_NaN_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for nan with error check off - Array code f.
		"""
		expected = [y / x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.truediv(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class truediv_div_inf_errors_f(unittest.TestCase):
	"""Test truediv for basic general function operation using parameter inf.
	This version is for division operations where division by inf and -inf 
	results in zero.
	nan_div_data_error_template
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

		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('inf')] * arraysize)



	########################################################
	def test_truediv_inf_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for inf - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval)


	########################################################
	def test_truediv_inf_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for inf with error check off - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for inf - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval, self.dataout)


	########################################################
	def test_truediv_inf_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for inf with error check off - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for inf with error check off - Array code f.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for inf with error check off - Array code f.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class truediv_div_ninf_errors_f(unittest.TestCase):
	"""Test truediv for basic general function operation using parameter -inf.
	This version is for division operations where division by inf and -inf 
	results in zero.
	nan_div_data_error_template
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

		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('-inf')] * arraysize)



	########################################################
	def test_truediv_ninf_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for -inf - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval)


	########################################################
	def test_truediv_ninf_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for -inf with error check off - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for -inf - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval, self.dataout)


	########################################################
	def test_truediv_ninf_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for -inf with error check off - Array code f.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for -inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for -inf with error check off - Array code f.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for -inf with error check off - Array code f.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for -inf with error check off - Array code f.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

 

##############################################################################
class truediv_general_even_arraysize_d(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'd' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'd' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'd' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)
		dataout = array.array('d', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)
		dataout = array.array('d', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

 

##############################################################################
class truediv_general_odd_arraysize_d(unittest.TestCase):
	"""Test truediv for basic general function operation using numeric data.
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
	def expectop(self, x, y):
		"""Perform the math operation. This needs to be specially handled
		for truediv on large signed integer arrays. This is because of a 
		combination of factors. Python will produce a floating point result, 
		but we we want an integer result when using integer arrays. If we 
		simply convert the result back to integer then we lose precision on
		large integers, introducing errors. If we try to emulate it using
		floor division, then when using mixed positive and negative inputs
		the result is rounded away from zero, producing an incorrect result.
		So, we need to take the absolute value, then do floor division, then
		put the correct sign back into the result.
		"""
		# For true division on integer arrays.
		if ('/' == '/') and 'd' not in ('f', 'd'):
			# For when signs are opposite in signed arrays.
			if ((x < 0) ^ (y < 0)):
				return -(abs(x) // abs(y))
			else:
				return x // y
		else:
			return x / y



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

		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# The tests are created using a common template. The data used
		# in the tests varies depending on the operator.

		# Addition.
		if '/' == '+':
			# Data for two arrays.
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval, -10), (maxval - 12, 10), (maxval -12, -10), (0, 0), 
					(0, 1), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			# Data for an array and a number.
			arr_num1a = [minval + 12, minval + 15, 0, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests - expect an empty set.
			# [(x,y) for x,y in arr_arr if ((x + y) < minval) or ((x + y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x + y) < minval) or ((x + y) > maxval)]

		# Subtraction.
		elif '/' == '-':
			arr_arr = [(minval + 1, 1), (minval , -1), (minval +12, 10), (minval +12, -10),  
					(maxval, 0), (maxval - 10, -10), (maxval - 12, 10), (maxval -12, -10), 
					(0, 0), (1, 0), (0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), 
					((minval // 2) + 11, 10), (minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [0, 1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x - y) < minval) or ((x - y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x - y) < minval) or ((x - y) > maxval)]

		# Division.
		elif '/' in ('/', '//'):
			arr_arr = [(minval, 1), (minval + 1, -1), (minval +12, 10), (minval +12, -10), 
					(maxval, 10), (maxval , -10), (maxval -12, -10), (0, 1), (0, -1), 
					(10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 2, 10), 
					(minval //2, -10), (maxval // 2, 10), (maxval // 2, -10)]

			arr_num1a = [minval + 12, minval + 15, -1, 1, 10, -10, maxval // 2, (maxval // 2) + 10, maxval -12]
			arr_num1b = [1, -1, 2, -2, 10, -10]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x // y) < minval) or ((x // y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x // y) < minval) or ((x // y) > maxval)]


		# Multiplication.
		elif '/' == '*':
			arr_arr = [(minval, 1), (minval + 1, -1), (minval // 4, 2), (minval // 4, -2), 
					(maxval, 0), (maxval // 15, -10), (maxval // 15, 10), (0, 0), (0, 1), 
					(0, -1), (10, 5), (10, -5), (-10, 5), (-10, -5), (minval // 15, 10), 
					(minval // 15, -10), (maxval // 15, 10), (maxval // 15, -10)]

			arr_num1a = [minval // 4, minval // 5, 0, -1, 1, 10, -10, maxval // 4, maxval // 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]
			arr_num1b = [0, 1, -1, 2, -2, 3, -3]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x * y) < minval) or ((x * y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x * y) < minval) or ((x * y) > maxval)]

		# Modulo.
		elif '/' == '%':
			arr_arr = [(10, 3), (-10, 3), (10, -3), (-10, -3), (minval // 4, 3), (maxval // 4, 3), (0, 3), (0, -3), 
						(10, 2), (-10, 2), (10, -2), (-10, -2), (minval // 4, 2), (maxval // 4, 2), (0, 2), (0, -2),
						(59, 3), (59, 4), (59, 5), (59, 6)]

			arr_num1a = [x for x,y in arr_arr]
			arr_num1b = [y for x,y in arr_arr]

			# Data tests. Note in the template the symbols are doubled.
			# [(x,y) for x,y in arr_arr if ((x % y) < minval) or ((x % y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x % y) < minval) or ((x % y) > maxval)]


		# Raise to power. This requires a different approach to prevent
		# data from rapidly going out of range.
		elif '/' == '**':

			# Reduce the large value so that very large integers don't overflow
			# when losing resolution when converting integers to floating point. 
			powerval = (maxval / 4) * 3

			arr_arr = [ (9, 2), (7, 2), (3, 3), (3, 4), (2, 5), (int(math.sqrt(powerval)), 2), (int(powerval ** (1/3)), 3), (int(powerval ** (1/4)), 4)]

			arr_num1a = [9, 7, 3, 2, int(math.sqrt(powerval)), int(math.sqrt(powerval // 2)), int(math.sqrt(powerval // 10))]
			arr_num1b = [2, 2, 2, 2, 2, 2, 2]

			# Data tests:
			# [(x,y) for x,y in arr_arr if ((x ** y) < minval) or ((x ** y) > maxval)]
			# [(x,y) for x,y in zip(arr_num1a, itertools.cycle(arr_num1b)) if ((x ** y) < minval) or ((x ** y) > maxval)]


		else:
			print('Unknown operator.', '/')


		# If we are dealing with an unsigned array, filter the test data to remove negative values.
		if 'd' in ('B', 'H', 'I', 'L', 'Q'):
			tdata_arr_arr = [(x,y) for x,y in arr_arr if (x >= 0) and (y >= 0)]
			tdata_arr_num1a = [x for x in arr_num1a if x >= 0]
			tdata_arr_num1b = [x for x in arr_num1b if x >= 0]
		# If floating point, convert the data to the correct type.
		elif 'd' in ('f', 'd'):
			tdata_arr_arr = [(float(x), float(y)) for x,y in arr_arr]
			tdata_arr_num1a = [float(x) for x in arr_num1a]
			tdata_arr_num1b = [float(x) for x in arr_num1b]
		# No conversion is required for signed integers.
		else:
			tdata_arr_arr = arr_arr
			tdata_arr_num1a = arr_num1a
			tdata_arr_num1b = arr_num1b

		self.datacheck1 = tdata_arr_arr
		self.datacheck2 = tdata_arr_num1a
		self.datacheck3 = tdata_arr_num1b

		# Expand the data out to the desired length by repeating it.
		ttdata = list(itertools.islice(itertools.cycle(tdata_arr_arr), 0, testdatasize))

		# And separate the data pairs. These are used for tests with two arrays.
		self.datax_aa = [x for x,y in ttdata]
		self.datay_aa = [y for x,y in ttdata]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		# First when we have an array then a number.
		self.datax_an = list(itertools.islice(itertools.cycle(tdata_arr_num1a), 0, testdatasize))
		self.datay_an = tdata_arr_num1b

		# And for a number as the first parameter and an array as the second.
		self.datax_na = tdata_arr_num1a
		self.datay_na = list(itertools.islice(itertools.cycle(tdata_arr_num1b), 0, testdatasize))



	########################################################
	def test_truediv_check_test_data(self):
		"""Test truediv to ensure we have valid data present - Array code d.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datacheck1) > 2)
		self.assertTrue(len(self.datacheck2) > 2)
		self.assertTrue(len(self.datacheck3) > 2)



	########################################################
	def test_truediv_basic_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for basic function - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a3(self):
		"""Test truediv as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_none_a4(self):
		"""Test truediv as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for basic function - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(x, testval) for x in data1]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_num_array_b4(self):
		"""Test truediv as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datay_an:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datax_an)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for basic function - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c3(self):
		"""Test truediv as *num-array-none* for basic function with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_none_c4(self):
		"""Test truediv as *num-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.truediv(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for basic function - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				expected = [self.expectop(testval, x) for x in data1]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for basic function with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_num_array_array_d4(self):
		"""Test truediv as *num-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in self.datax_na:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', self.datay_na)
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [self.expectop(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.truediv(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e3(self):
		"""Test truediv as *array-array-none* for basic function with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_none_e4(self):
		"""Test truediv as *array-array-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.truediv(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for basic function - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)
		dataout = array.array('d', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_basic_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)
		dataout = array.array('d', [0]*len(data1))

		expected = [self.expectop(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_truediv_basic_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		data1 = array.array('d', self.datax_aa)
		data2 = array.array('d', self.datay_aa)
		dataout = array.array('d', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [self.expectop(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.truediv(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class truediv_param_errors_d(unittest.TestCase):
	"""Test truediv for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.testarray1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.testarray2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('i', [int(x) for x in self.testarray1])
		self.badarray2 = array.array('i', [int(x) for x in self.testarray2])

		self.baddataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, badvalue)



	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badarray1, testvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.truediv(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_truediv_array_num_array_b3(self):
		"""Test truediv as *array-num-array* for invalid type of output array - Array code d.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.truediv(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testarray1, testvalue, self.baddataout)



	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, badarray2)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for invalid type of number - Array code d.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(badvalue, testarray2)



	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for invalid type of array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for invalid type of number - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_truediv_num_array_array_d3(self):
		"""Test truediv as *num-array-array* for invalid type of output array - Array code d.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.truediv(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.truediv(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code d.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.truediv(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(testarray1, self.badarray2)


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2)



	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for invalid type of array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_truediv_array_array_array_f3(self):
		"""Test truediv as *array-array-array* for invalid type of output array - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_truediv_no_params_g1(self):
		"""Test truediv with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.truediv()



##############################################################################



##############################################################################
class truediv_opt_param_errors_d(unittest.TestCase):
	"""Test truediv for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for matherrors='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.truediv(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_truediv_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for matherrors='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_truediv_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for maxlen='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_truediv_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for matherrors='a' - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_truediv_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for maxlen='a' - Array code d.
		"""

		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.truediv(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################



##############################################################################
class overflow_signed_divzero_d(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.d_max
		self.MinLimit = arrayfunc.arraylimits.d_min


		self.inparray1amax = array.array('d', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('d', [0.0] * arraysize)
		self.plus1array = array.array('d', [1.0] * arraysize)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1.0)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0.0)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1.0, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0.0, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0.0 - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################



##############################################################################
class truediv_NaN_errors_d(unittest.TestCase):
	"""Test truediv for basic general function operation using parameter nan.
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



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('nan')] * arraysize)



	########################################################
	def test_truediv_NaN_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for nan - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval)


	########################################################
	def test_truediv_NaN_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for nan with error check off - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for nan - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval, self.dataout)


	########################################################
	def test_truediv_NaN_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for nan with error check off - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for nan - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(testval, errordata)


	########################################################
	def test_truediv_NaN_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for nan with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for nan - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.truediv(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(testval, self.errordata, self.dataout)


	########################################################
	def test_truediv_NaN_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for nan with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_array_array_none_e1(self):
		"""Test truediv as *array-array-none* for nan - Array code d.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.truediv(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.truediv(dataok1, self.errordata)


	########################################################
	def test_truediv_NaN_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for nan with error check off - Array code d.
		"""
		expected = [y / x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.truediv(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_NaN_array_array_array_f1(self):
		"""Test truediv as *array-array-array* for nan - Array code d.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.truediv(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_truediv_NaN_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for nan with error check off - Array code d.
		"""
		expected = [y / x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.truediv(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class truediv_div_inf_errors_d(unittest.TestCase):
	"""Test truediv for basic general function operation using parameter inf.
	This version is for division operations where division by inf and -inf 
	results in zero.
	nan_div_data_error_template
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

		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('inf')] * arraysize)



	########################################################
	def test_truediv_inf_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for inf - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval)


	########################################################
	def test_truediv_inf_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for inf with error check off - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for inf - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval, self.dataout)


	########################################################
	def test_truediv_inf_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for inf with error check off - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for inf with error check off - Array code d.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_inf_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for inf with error check off - Array code d.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################



##############################################################################
class truediv_div_ninf_errors_d(unittest.TestCase):
	"""Test truediv for basic general function operation using parameter -inf.
	This version is for division operations where division by inf and -inf 
	results in zero.
	nan_div_data_error_template
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

		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.dataok2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('-inf')] * arraysize)



	########################################################
	def test_truediv_ninf_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for -inf - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval)


	########################################################
	def test_truediv_ninf_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for -inf with error check off - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for -inf - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.truediv(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.truediv(errordata, testval, self.dataout)


	########################################################
	def test_truediv_ninf_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for -inf with error check off - Array code d.
		"""
		for testval in [-3.0,-2.0,-1.0,1.0,2.0,3.0,4.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x / testval for x in self.errordata]

				arrayfunc.truediv(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for -inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for -inf with error check off - Array code d.
		"""
		for testval in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval / x for x in self.errordata]

				arrayfunc.truediv(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_array_array_none_e2(self):
		"""Test truediv as *array-array-none* for -inf with error check off - Array code d.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_truediv_ninf_array_array_array_f2(self):
		"""Test truediv as *array-array-array* for -inf with error check off - Array code d.
		"""
		expected = [x / y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.truediv(self.dataok1, self.errordata, self.dataout, matherrors=True)

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

		with open('af_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('truediv\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
