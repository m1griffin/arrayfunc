#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for compare operations.
# Language: Python 3.5
# Date:     03-Feb-2018
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


# ==============================================================================

import itertools
import codegen_common

# ==============================================================================


# This template is for compare operations.
test_template_comp = ''' 

##############################################################################
class %(funcname)s_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typecode)s_%(count)s(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if '%(arrayevenodd)s' == 'even':
			testdatasize = 512
		if '%(arrayevenodd)s' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if '%(typecode)s' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif '%(typecode)s' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.%(typecode)s_min
			maxval = arrayfunc.arraylimits.%(typecode)s_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if '%(typecode)s' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in %(param_array_num_pass)s]
			vals_param_array_num_fail = [float(x) for x in %(param_array_num_fail)s]
			vals_param_num_array_pass = [float(x) for x in %(param_num_array_pass)s]
			vals_param_num_array_fail = [float(x) for x in %(param_num_array_fail)s]
		else:
			vals_param_array_num_pass = %(param_array_num_pass)s
			vals_param_array_num_fail = %(param_array_num_fail)s
			vals_param_num_array_pass = %(param_num_array_pass)s
			vals_param_num_array_fail = %(param_num_array_fail)s


		# Now create the arrays and lists.
		self.data_array_num = array.array('%(typecode)s', list(itertools.islice(itertools.cycle(%(data_array_num)s), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('%(typecode)s', list(itertools.islice(itertools.cycle(%(data_num_array)s), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('%(typecode)s', list(itertools.islice(itertools.cycle(%(data_array_array)s), testdatasize)))
		self.data_array_array_pass = array.array('%(typecode)s', list(itertools.islice(itertools.cycle(%(data_array_array_pass)s), testdatasize)))
		self.data_array_array_fail = array.array('%(typecode)s', list(itertools.islice(itertools.cycle(%(data_array_array_fail)s), testdatasize)))


	########################################################
	def test_%(funcname)s_basic_array_num_a1(self):
		"""Test %(funcname)s as *array-num* for basic function - Array code %(typecode)s.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x %(pyoperator)s testval for x in self.data_array_num])

				result = arrayfunc.%(funcname)s(self.data_array_num, testval %(nosimd)s)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_array_num_a2(self):
		"""Test %(funcname)s as *array-num* for basic function - Array code %(typecode)s.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x %(pyoperator)s testval for x in self.data_array_num])

				result = arrayfunc.%(funcname)s(self.data_array_num, testval %(nosimd)s)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_array_num_a3(self):
		"""Test %(funcname)s as *array-num* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x %(pyoperator)s testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.%(funcname)s(self.data_array_num, testval, maxlen=limited %(nosimd)s)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_num_array_b1(self):
		"""Test %(funcname)s as *num-array* for basic function - Array code %(typecode)s.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval %(pyoperator)s x for x in self.data_num_array])

				result = arrayfunc.%(funcname)s(testval, self.data_num_array %(nosimd)s)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_num_array_b2(self):
		"""Test %(funcname)s as *num-array* for basic function - Array code %(typecode)s.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval %(pyoperator)s x for x in self.data_num_array])

				result = arrayfunc.%(funcname)s(testval, self.data_num_array %(nosimd)s)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_num_array_b3(self):
		"""Test %(funcname)s as *num-array* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval %(pyoperator)s x for x in self.data_num_array[0:limited]])

				result = arrayfunc.%(funcname)s(testval, self.data_num_array, maxlen=limited %(nosimd)s)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_array_array_c1(self):
		"""Test %(funcname)s as *array-array* for basic function - Array code %(typecode)s.
		"""
		expected = all([x %(pyoperator)s y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.%(funcname)s(self.data_array_array, self.data_array_array_pass %(nosimd)s)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_array_array_c2(self):
		"""Test %(funcname)s as *array-array* for basic function - Array code %(typecode)s.
		"""
		expected = all([x %(pyoperator)s y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.%(funcname)s(self.data_array_array, self.data_array_array_fail %(nosimd)s)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funcname)s_basic_array_array_c3(self):
		"""Test %(funcname)s as *array-array* for basic function with array limit - Array code %(typecode)s.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x %(pyoperator)s y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.%(funcname)s(self.data_array_array, self.data_array_array_pass, maxlen=limited %(nosimd)s)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

'''


# ==============================================================================


# ==============================================================================

# This template tests with numbers in various positions.
test_template_numpos = ''' 


##############################################################################
class %(funclabel)s_numpos_%(typelabel)s(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('%(typecode)s', [%(test_data1)s] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('%(typecode)s', list(self.data1))
		self.data1fail[-1] = %(test_data1fail)s

		self.data2 = array.array('%(typecode)s', [%(test_data2)s] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('%(typecode)s', list(self.data2))
		self.data2fail[-1] = %(test_data2fail)s



	########################################################
	def test_%(funclabel)s_numpos_array_num_a1(self):
		"""Test %(funclabel)s as *array-num* for failing with different data positions in array - Array code %(typelabel)s.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x %(pyoperator)s self.testval2 for x in self.data1fail])

				result = arrayfunc.%(funcname)s(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_%(funclabel)s_numpos_num_array_b1(self):
		"""Test %(funclabel)s as *num-array* for failing with different data positions in array - Array code %(typelabel)s.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 %(pyoperator)s x for x in self.data2fail])

				result = arrayfunc.%(funcname)s(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_%(funclabel)s_numpos_array_array_c1(self):
		"""Test %(funclabel)s as *array-array* for failing with different data positions in array 1 - Array code %(typelabel)s.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x %(pyoperator)s y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.%(funcname)s(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_%(funclabel)s_numpos_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for failing with different data positions in array 2 - Array code %(typelabel)s.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x %(pyoperator)s y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.%(funcname)s(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################

'''



# ==============================================================================


# The template used to generate the tests for testing invalid array and
# numeric parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.data2 = array.array('%(typecode)s', [%(test_op_y)s])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('%(badtypecode)s', [%(bad_test_op_x)s])
		self.badarray2 = array.array('%(badtypecode)s', [%(bad_test_op_y)s])


	########################################################
	def test_%(funclabel)s_array_num_a1(self):
		"""Test %(funclabel)s as *array-num* for incompatible array - Array code %(typelabel)s.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.%(funcname)s(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.%(funcname)s(badarray1, testval)


	########################################################
	def test_%(funclabel)s_array_num_a2(self):
		"""Test %(funclabel)s as *array-num* for incompatible number - Array code %(typelabel)s.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.%(funcname)s(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.%(funcname)s(data1, badval)


	########################################################
	def test_%(funclabel)s_num_array_c1(self):
		"""Test %(funclabel)s as *num-array* for incompatible array - Array code %(typelabel)s.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.%(funcname)s(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.%(funcname)s(testval, badarray1)


	########################################################
	def test_%(funclabel)s_num_array_c2(self):
		"""Test %(funclabel)s as *num-array* for incompatible number - Array code %(typelabel)s.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.%(funcname)s(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.%(funcname)s(badval, data1)


	########################################################
	def test_%(funclabel)s_array_array_e1(self):
		"""Test %(funclabel)s as *array-array* for incompatible second array - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(data1, self.badarray2)


	########################################################
	def test_%(funclabel)s_array_array_e2(self):
		"""Test %(funclabel)s as *array-array* for incompatible first array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.badarray1, self.data2)


	########################################################
	def test_%(funclabel)s_no_params_f1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s()



##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for errors flag and maxlen.
param_invalid_opt_template = '''

##############################################################################
class %(funclabel)s_param_errors_opt_%(typelabel)s(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('%(typecode)s', [%(test_op_x)s])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('%(typecode)s', [%(test_op_y)s])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_%(funclabel)s_array_num_a1(self):
		"""Test %(funclabel)s as *array-num* for matherrors=True - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_num_a2(self):
		"""Test %(funclabel)s as *array-num* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_num_a3(self):
		"""Test %(funclabel)s as *array-num* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_%(funclabel)s_num_array_c1(self):
		"""Test %(funclabel)s as *num-array* for matherrors=True - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_%(funclabel)s_num_array_c2(self):
		"""Test %(funclabel)s as *num-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_%(funclabel)s_num_array_c3(self):
		"""Test %(funclabel)s as *num-array* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_%(funclabel)s_array_array_e1(self):
		"""Test %(funclabel)s as *array-array* for matherrors=True - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_array_e2(self):
		"""Test %(funclabel)s as *array-array* for maxlen='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_e3(self):
		"""Test %(funclabel)s as *array-array* for nosimd='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected.
nan_data_template = '''

##############################################################################
class %(funclabel)s_errors_nf_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using parameter NaN, inf, and -inf.
	nan_data_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testvalue = 10.5
		self.testdata = array.array('%(typecode)s', [self.testvalue] * 20)

		self.nanvalue = math.nan
		self.infvalue = math.inf
		self.ninfvalue = -math.inf

		self.nandata = array.array('%(typecode)s', [float(self.nanvalue)] * len(self.testdata))
		self.infdata = array.array('%(typecode)s', [float(self.infvalue)] * len(self.testdata))
		self.ninfdata = array.array('%(typecode)s', [float(self.ninfvalue)] * len(self.testdata))


	########################################################
	def test_%(funclabel)s_nan_data_array_num_a1(self):
		"""Test %(funclabel)s as *array-num* for NaN value - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s self.nanvalue for x in self.testdata])

		result = arrayfunc.%(funcname)s(self.testdata, self.nanvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_num_a2(self):
		"""Test %(funclabel)s as *array-num* for NaN array - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s self.testvalue for x in self.nandata])

		result = arrayfunc.%(funcname)s(self.nandata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_num_array_a3(self):
		"""Test %(funclabel)s as *num-array* for NaN value - Array code %(typelabel)s.
		"""
		expected = all([self.nanvalue %(pyoperator)s x for x in self.testdata])

		result = arrayfunc.%(funcname)s(self.nanvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_num_array_a4(self):
		"""Test %(funclabel)s as *num-array* for NaN array - Array code %(typelabel)s.
		"""
		expected = all([self.testvalue %(pyoperator)s x for x in self.nandata])

		result = arrayfunc.%(funcname)s(self.testvalue, self.nandata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_array_a5(self):
		"""Test %(funclabel)s as *array-array* for NaN array 1 - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x,y) in zip(self.nandata, self.testdata)])

		result = arrayfunc.%(funcname)s(self.nandata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_array_a6(self):
		"""Test %(funclabel)s as *array-array* for NaN array 2 - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x,y) in zip(self.testdata, self.nandata)])

		result = arrayfunc.%(funcname)s(self.testdata, self.nandata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_num_b1(self):
		"""Test %(funclabel)s as *array-num* for inf value - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s self.infvalue for x in self.testdata])

		result = arrayfunc.%(funcname)s(self.testdata, self.infvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_num_b2(self):
		"""Test %(funclabel)s as *array-num* for inf array - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s self.testvalue for x in self.infdata])

		result = arrayfunc.%(funcname)s(self.infdata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_num_array_b3(self):
		"""Test %(funclabel)s as *num-array* for inf value - Array code %(typelabel)s.
		"""
		expected = all([self.infvalue %(pyoperator)s x for x in self.testdata])

		result = arrayfunc.%(funcname)s(self.infvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_num_array_b4(self):
		"""Test %(funclabel)s as *num-array* for inf array - Array code %(typelabel)s.
		"""
		expected = all([self.testvalue %(pyoperator)s x for x in self.infdata])

		result = arrayfunc.%(funcname)s(self.testvalue, self.infdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_array_b5(self):
		"""Test %(funclabel)s as *array-array* for inf array 1 - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x,y) in zip(self.infdata, self.testdata)])

		result = arrayfunc.%(funcname)s(self.infdata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_array_b6(self):
		"""Test %(funclabel)s as *array-array* for inf array 2 - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x,y) in zip(self.testdata, self.infdata)])

		result = arrayfunc.%(funcname)s(self.testdata, self.infdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_num_c1(self):
		"""Test %(funclabel)s as *array-num* for -inf value - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s self.ninfvalue for x in self.testdata])

		result = arrayfunc.%(funcname)s(self.testdata, self.ninfvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_num_c2(self):
		"""Test %(funclabel)s as *array-num* for -inf array - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s self.testvalue for x in self.ninfdata])

		result = arrayfunc.%(funcname)s(self.ninfdata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_num_array_c3(self):
		"""Test %(funclabel)s as *num-array* for -inf value - Array code %(typelabel)s.
		"""
		expected = all([self.ninfvalue %(pyoperator)s x for x in self.testdata])

		result = arrayfunc.%(funcname)s(self.ninfvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_num_array_c4(self):
		"""Test %(funclabel)s as *num-array* for -inf array - Array code %(typelabel)s.
		"""
		expected = all([self.testvalue %(pyoperator)s x for x in self.ninfdata])

		result = arrayfunc.%(funcname)s(self.testvalue, self.ninfdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_array_c5(self):
		"""Test %(funclabel)s as *array-array* for -inf array 1 - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x,y) in zip(self.ninfdata, self.testdata)])

		result = arrayfunc.%(funcname)s(self.ninfdata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_nan_data_array_array_c6(self):
		"""Test %(funclabel)s as *array-array* for -inf array 2 - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x,y) in zip(self.testdata, self.ninfdata)])

		result = arrayfunc.%(funcname)s(self.testdata, self.ninfdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

'''

# ==============================================================================

# This data is used to create tests for test_template_numpos.

# First parameter.
numposdata1 = {
	'eq' : '5',
	'gt' : '6',
	'ge' : '6',
	'lt' : '5',
	'le' : '6',
	'ne' : '5',
}

# First parameter to cause no match.
numposdata1fail = {
	'eq' : '4',
	'gt' : '5',
	'ge' : '4',
	'lt' : '7',
	'le' : '8',
	'ne' : '6',
}


# Second parameter.
numposdata2 = {
	'eq' : '5',
	'gt' : '5',
	'ge' : '5',
	'lt' : '6',
	'le' : '7',
	'ne' : '6',
}

# Second parameter to cause no match.
numposdata2fail = {
	'eq' : '4',
	'gt' : '7',
	'ge' : '7',
	'lt' : '4',
	'le' : '5',
	'ne' : '5',
}


# ==============================================================================

# ==============================================================================

pyoperator = {
	'eq' : '==',
	'gt' : '>',
	'ge' : '>=',
	'lt' : '<',
	'le' : '<=',
	'ne' : '!=',
}


# Test data for the template test_template_comp.
# This contains lists of test values to allow multiple tests sets
# with the same template. This allows a broader range of data to
# be tested.
# This is in a format which is easier to view in an editor, rather than
# easier to extract.

testdata = {
	'eq' : 
	{
	'data_array_num' :        ('[baseval, baseval, baseval]',  '[topval, topval, topval]'),
	'param_array_num_pass' :  ('[baseval, baseval, baseval]',  '[topval, topval, topval]'),
	'param_array_num_fail' :  ('[midval1, 0, midval2]',        '[0, midval1, midval3]'),

	'param_num_array_pass' :  ('[baseval, baseval, baseval]',   '[topval, topval, topval]'),
	'param_num_array_fail' :  ('[midval3, 0, maxint]',          '[midval3, 0, maxint]'),
	'data_num_array' :        ('[baseval, baseval, baseval]',   '[topval, topval, topval]'),

	'data_array_array' :      ('[baseval, baseval, baseval]',   '[topval, topval, topval]'),
	'data_array_array_pass' : ('[baseval, baseval, baseval]',   '[topval, topval, topval]'),
	'data_array_array_fail' : ('[midval2, midval3, midval1]',   '[midval1, 0, midval3]'),
	},

	'gt' : 
	{
	'data_array_num' :        ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]'),
	'param_array_num_pass' :  ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]'),
	'param_array_num_fail' :  ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]'),

	'param_num_array_pass' :  ('[baseval + 20, baseval + 30, baseval + 40]', '[topval + 5, topval, maxint]'),
	'param_num_array_fail' :  ('[baseval + 0, baseval + 1, baseval + 4]',    '[topval - 25, topval - 30, topval - 35]'),
	'data_num_array' :        ('[baseval + 10, baseval + 15, baseval + 17]', '[topval - 10, topval - 15, topval - 20]'),

	'data_array_array' :      ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]'),
	'data_array_array_pass' : ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]'),
	'data_array_array_fail' : ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]'),
	},

	'ge' : 
	{
	'data_array_num' :        ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]', '[baseval, baseval, baseval]'),
	'param_array_num_pass' :  ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]', '[baseval, baseval, baseval]'),
	'param_array_num_fail' :  ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]',            '[baseval + 1, baseval + 2, baseval + 3]'),

	'param_num_array_pass' :  ('[baseval + 20, baseval + 30, baseval + 40]', '[topval + 5, topval, maxint]',            '[baseval, baseval, baseval]'),
	'param_num_array_fail' :  ('[baseval + 0, baseval + 1, baseval + 4]',    '[topval - 25, topval - 30, topval - 35]', '[baseval - 1, baseval - 2, baseval - 3]'),
	'data_num_array' :        ('[baseval + 10, baseval + 15, baseval + 17]', '[topval - 10, topval - 15, topval - 20]', '[baseval, baseval, baseval]'),

	'data_array_array' :      ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]', '[baseval, baseval, baseval]'),
	'data_array_array_pass' : ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]', '[baseval, baseval, baseval]'),
	'data_array_array_fail' : ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]',            '[baseval + 1, baseval + 2, baseval + 3]'),
	},

	'lt' : 
	{
	'data_array_num' :        ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]'),
	'param_array_num_pass' :  ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]'),
	'param_array_num_fail' :  ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]'),

	'param_num_array_pass' :  ('[baseval + 0, baseval + 1, baseval + 4]',    '[topval - 25, topval - 30, topval - 35]'),
	'param_num_array_fail' :  ('[baseval + 20, baseval + 30, baseval + 40]', '[topval + 5, topval, maxint]'),
	'data_num_array' :        ('[baseval + 10, baseval + 15, baseval + 17]', '[topval - 10, topval - 15, topval - 20]'),

	'data_array_array' :      ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]'),
	'data_array_array_pass' : ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]'),
	'data_array_array_fail' : ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]'),
	},

	'le' : 
	{
	'data_array_num' :        ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]', '[baseval, baseval, baseval]'),
	'param_array_num_pass' :  ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]',            '[baseval, baseval, baseval]'),
	'param_array_num_fail' :  ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]', '[baseval - 1, baseval - 2, baseval - 3]'),

	'param_num_array_pass' :  ('[baseval + 0, baseval + 1, baseval + 4]',    '[topval - 25, topval - 30, topval - 35]', '[baseval, baseval, baseval]'),
	'param_num_array_fail' :  ('[baseval + 20, baseval + 30, baseval + 40]', '[topval + 5, topval, maxint]',            '[baseval + 1, baseval + 2, baseval + 3]'),
	'data_num_array' :        ('[baseval + 10, baseval + 15, baseval + 17]', '[topval - 10, topval - 15, topval - 20]', '[baseval, baseval, baseval]'),

	'data_array_array' :      ('[baseval + 10, baseval + 20, baseval + 30]', '[topval - 10, topval - 15, topval - 20]', '[baseval, baseval, baseval]'),
	'data_array_array_pass' : ('[baseval + 31, baseval + 35, topval]',       '[topval + 5, topval, maxint]',            '[baseval, baseval, baseval]'),
	'data_array_array_fail' : ('[baseval + 1, baseval + 2, baseval + 3]',    '[topval - 25, topval - 30, topval - 35]', '[baseval - 1, baseval - 2, baseval - 3]'),
	},

	'ne' : 
	{
	'data_array_num' :        ('[baseval, baseval, baseval]', '[topval, topval, topval]'),
	'param_array_num_pass' :  ('[midval1, 0, midval3]',       '[midval3, midval2, 0]'),
	'param_array_num_fail' :  ('[baseval, baseval, baseval]', '[topval, topval, topval]'),

	'param_num_array_pass' :  ('[midval1, midval3, 0]',       '[midval3, midval1, 0]'),
	'param_num_array_fail' :  ('[baseval, baseval, baseval]', '[topval, topval, topval]'),
	'data_num_array' :        ('[baseval, baseval, baseval]', '[topval, topval, topval]'),

	'data_array_array' :      ('[baseval, baseval, baseval]', '[topval, topval, topval]'),
	'data_array_array_pass' : ('[midval2, midval3, midval1]', '[midval1, 0, midval3]'),
	'data_array_array_fail' : ('[baseval, baseval, baseval]', '[topval, topval, topval]'),
	},

}


def makedata(funcname):
	'''Make the combinations of data options for tests.
	'''
	# Get the data for one specific op.
	op = testdata[funcname]

	# Get how many tests are present. These should all be the same, so
	# we look for the maximum in order to detect errors.
	numtests = max([len(op[x]) for x in op])
	mintests = min([len(op[x]) for x in op])
	if numtests != mintests:
		print('Error! This is a mismatch in the number of data sets for ', funcname)

	count = tuple([('count', x) for x in range(0, numtests)])
	typecode = [('typecode', x) for x in codegen_common.arraycodes]
	arrayevenodd = (('arrayevenodd', 'even'), ('arrayevenodd', 'odd'))
	simdpresent = (('simdpresent', 'nosimd'), ('simdpresent', 'withsimd'))

	# This creates all the combinations of test data.
	combos = [dict(x) for x in itertools.product(typecode, arrayevenodd, simdpresent, count)]

	opdata = {}
	# Cycle through the sets of test data.
	for testnum in range(numtests):
		# Get the data for one set of tests.
		opdata[testnum] = dict([(x, op[x][testnum]) for x in op])

	nosimd = {'nosimd' : {'nosimd' : ', nosimd=True'}, 'withsimd' : {'nosimd' : ''}}

	# Update with the test data. These values don't represent independent combinations,
	# but rather just additional data that goes along with other items already present.
	for x in combos:
		x.update(nosimd[x['simdpresent']])
		x.update(opdata[x['count']])
		x['funcname'] = funcname
		x['pyoperator'] = pyoperator[funcname]

	return combos



# ==============================================================================




# ==============================================================================

# Read in the op codes.
opdata = codegen_common.ReadINI('affuncdata.ini')

# Filter out the desired math functions.
funclist = [(x,dict(y)) for x,y in opdata.items() if y.get('test_op_templ') == 'test_template_comp']

# ==============================================================================

# This defines the module name.
modulename = 'arrayfunc'
# Import the array module for testing.
arrayimport = 'import array'


for funcname, func in funclist:

	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '14-Feb-2018', funcname)

	# Add additional header data.
	headerdate['modulename'] = modulename
	headerdate['arrayimport'] = arrayimport

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)

		# Tests for detailed functionality of operations.
		for funcdata in makedata(funcname):
			f.write(test_template_comp % funcdata)



		# Check each array type.
		for functype in codegen_common.arraycodes:

			# Convert the numeric literals to the appropriate type for the array.
			if functype in codegen_common.floatarrays:
				fmtconvert = lambda y: ','.join([str(float(x)) for x in y.split(',')])

				test_op_x = fmtconvert(func['test_op_x'])
				test_op_y = fmtconvert(func['test_op_y'])
				test_op_y_fail = fmtconvert(func['test_op_y_fail'])
			else:
				test_op_x = func['test_op_x']
				test_op_y = func['test_op_y']
				test_op_y_fail = func['test_op_y_fail']



			funcdata = {'funclabel' : funcname, 'funcname' : funcname, 
					'pyoperator' : func['pyoperator'], 
					'typelabel' : functype, 'typecode' : functype, 
					'test_op_x' : test_op_x, 'test_op_y' : test_op_y,
					'test_op_y_fail' : test_op_y_fail}

			# Basic tests.

			# Create an array of data which is incompatible with the actual test type.
			if functype in codegen_common.floatarrays:
				funcdata['badtypecode'] = 'i'
				badfmtconvert = lambda y: ','.join([str(int(x)) for x in y.split(',')])
				funcdata['bad_test_op_x'] = badfmtconvert(func['test_op_x'])
				funcdata['bad_test_op_y'] = badfmtconvert(func['test_op_y'])
			else:
				funcdata['badtypecode'] = 'd'
				badfmtconvert = lambda y: ','.join([str(float(x)) for x in y.split(',')])
				funcdata['bad_test_op_x'] = badfmtconvert(func['test_op_x'])
				funcdata['bad_test_op_y'] = badfmtconvert(func['test_op_y'])
				
			# Test for basic operation.
			# With SIMD, even data arra size.
			funcdata['simdpresent'] = 'with'
			funcdata['nosimd'] = ''
			funcdata['arrayevenodd'] = 'even'
			#f.write(test_template_comp % funcdata)

			# With SIMD, odd data array size.
			funcdata['simdpresent'] = 'with'
			funcdata['nosimd'] = ''
			funcdata['arrayevenodd'] = 'odd'
			#f.write(test_template_comp % funcdata)

			# Without SIMD.
			funcdata['simdpresent'] = 'without'
			funcdata['nosimd'] = ', nosimd=True'
			funcdata['arrayevenodd'] = 'even'
			#f.write(test_template_comp % funcdata)


			#####

			# Test for function with data in different array positions.
			funcdata['test_data1'] = numposdata1[funcname]
			funcdata['test_data1fail'] = numposdata1fail[funcname]
			funcdata['test_data2'] = numposdata2[funcname]
			funcdata['test_data2fail'] = numposdata2fail[funcname]
			f.write(test_template_numpos % funcdata)


			#####

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			# Test for invalid optional parameters such as errors and maxlen.
			f.write(param_invalid_opt_template % funcdata)

			#####

			# NaN, Inf tests are for floating point only.
			if functype in codegen_common.floatarrays:

				# NaN, inf, -inf tests.
				funcdata = {'funclabel' : funcname, 
					'funcname' : funcname, 
					'pyoperator' : func['pyoperator'],
					'typelabel' : functype, 
					'typecode' : functype, 
					}

				f.write(nan_data_template % funcdata)


		f.write(codegen_common.testendtemplate % {'funcname' : funcname, 'testprefix' : 'af'})

# ==============================================================================

