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

# This template is for compare operators (e.g. ==, !=, <, <=, >, >=).
test_template_comp = ''' 

##############################################################################
class %(funclabel)s_general_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data %(test_op_y)s.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.data2 = array.array('%(typecode)s', [%(test_op_y)s])
		self.data2fail = array.array('%(typecode)s', [%(test_op_y_fail)s])


	########################################################
	def test_%(funclabel)s_basic_array_num_a1(self):
		"""Test %(funclabel)s as *array-num* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x %(pyoperator)s testval for x in self.data1])

				result = arrayfunc.%(funcname)s(self.data1, testval)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_array_num_a2(self):
		"""Test %(funclabel)s as *array-num* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.data2fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x %(pyoperator)s testval for x in self.data1])

				result = arrayfunc.%(funcname)s(self.data1, testval)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_array_num_a3(self):
		"""Test %(funclabel)s as *array-num* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x %(pyoperator)s testval for x in self.data1[0:limited]])

				result = arrayfunc.%(funcname)s(self.data1, testval, maxlen=limited)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_num_array_b1(self):
		"""Test %(funclabel)s as *num-array* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.data1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval %(pyoperator)s x for x in self.data2])

				result = arrayfunc.%(funcname)s(testval, self.data2)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_num_array_b2(self):
		"""Test %(funclabel)s as *num-array* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.data1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval %(pyoperator)s x for x in self.data2fail])

				result = arrayfunc.%(funcname)s(testval, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_num_array_b3(self):
		"""Test %(funclabel)s as *num-array* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in self.data1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval %(pyoperator)s x for x in self.data2[0:limited]])

				result = arrayfunc.%(funcname)s(testval, self.data2, maxlen=limited)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_array_array_c1(self):
		"""Test %(funclabel)s as *array-array* for basic function - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.%(funcname)s(self.data1, self.data2)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for basic function - Array code %(typelabel)s.
		"""
		expected = all([x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.%(funcname)s(self.data1, self.data2fail)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_%(funclabel)s_basic_array_array_c3(self):
		"""Test %(funclabel)s as *array-array* for basic function with array limit - Array code %(typelabel)s.
		"""
		limited = len(self.data1) // 2

		expected = all([x %(pyoperator)s y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.%(funcname)s(self.data1, self.data2, maxlen=limited)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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

		self.nanvalue = float('NaN')
		self.infvalue = float('inf')
		self.ninfvalue = float('-inf')

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


# ==============================================================================

# These are all the test code templates. 
test_templates = {'test_template_comp' : test_template_comp}


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['test_op_templ'] == 'test_template_comp']


# ==============================================================================


for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '14-Feb-2018', funcname)

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		# Check each array type.
		for functype in codegen_common.arraycodes:
			testtemplate = test_templates[func['test_op_templ']]

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



			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 
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
				

			f.write(testtemplate % funcdata)

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			# Test for invalid optional parameters such as errors and maxlen.
			f.write(param_invalid_opt_template % funcdata)



			# NaN, Inf tests are for floating point only.
			if functype in codegen_common.floatarrays:

				# NaN, inf, -inf tests.
				funcdata = {'funclabel' : func['funcname'], 
					'funcname' : funcname, 
					'pyoperator' : func['pyoperator'],
					'typelabel' : functype, 
					'typecode' : functype, 
					}

				f.write(nan_data_template % funcdata)


		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

