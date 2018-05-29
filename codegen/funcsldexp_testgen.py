#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for the ldexp math function.
# Language: Python 3.5
# Date:     28-Jan-2018
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



# ==============================================================================

# This template is for the basic tests.
test_template_ldexp = '''

##############################################################################
class %(funclabel)s_general_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data %(test_op_y)s.
	test_template_ldexp
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for basic function - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a3(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a4(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_basic_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for basic function - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b4(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for testing invalid parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.floatarray2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for integer array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testint)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(intarray1, testint)


	########################################################
	def test_%(funclabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for float number - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testint)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(floatarray1, testfloat)


	########################################################
	def test_%(funclabel)s_array_num_none_a3(self):
		"""Test %(funclabel)s as *array-num-none* for integer number and array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testint)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(intarray1, testint)


	########################################################
	def test_%(funclabel)s_array_num_none_a4(self):
		"""Test %(funclabel)s as *array-num-none* for errors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray1[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testint, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testint, errors='a')


	########################################################
	def test_%(funclabel)s_array_num_none_a5(self):
		"""Test %(funclabel)s as *array-num-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray1[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testint, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testint, maxlen='a')



	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for integer array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(intarray1, testint, self.dataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for float number - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(self.floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(self.floatarray1, testfloat, self.dataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for integer output array - Array code %(typelabel)s.
		"""
		for testint in self.intarray2:
			with self.subTest(msg='Failed with parameter', testint = testint):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(floatarray1, testint, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b4(self):
		"""Test %(funclabel)s as *array-num-array* for integer number and array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(self.floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(self.intarray1, testint, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b5(self):
		"""Test %(funclabel)s as *array-num-array* for errors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray2[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testint, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testint, self.dataout, errors='a')


	########################################################
	def test_%(funclabel)s_array_num_array_b6(self):
		"""Test %(funclabel)s as *array-num-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testint, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testint, self.dataout, maxlen='a')



	########################################################
	def test_%(funclabel)s_array_num_array_c1(self):
		"""Test %(funclabel)s as *array* for missing numeric parameter - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray1)


	########################################################
	def test_%(funclabel)s_array_num_array_c2(self):
		"""Test %(funclabel)s as *num* for missing array parameter - Array code %(typelabel)s.
		"""
		testint = self.intarray2[0]
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testint)


	########################################################
	def test_%(funclabel)s_array_num_array_c3(self):
		"""Test %(funclabel)s as *array* for missing numeric parameter with maxlen - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.floatarray1) // 2
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray1, maxlen=testmaxlen)


	########################################################
	def test_%(funclabel)s_array_num_array_c4(self):
		"""Test %(funclabel)s as *num* for missing array parameter with maxlen - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.floatarray1) // 2
		testint = self.intarray2[0]
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testint, maxlen=testmaxlen)



	########################################################
	def test_%(funclabel)s_no_params_d1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()



##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected.
nan_data_error_ldexp_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using parameter %(errordata)s.
	nan_data_error_ldexp_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)


		self.expectedep = [%(pyoperator)s(x, y) for x,y in zip(self.errordata, itertools.cycle([%(test_op_y)s]))]


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [%(pyoperator)s(x, testval) for x in self.errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [%(pyoperator)s(x, testval) for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# These are all the test code templates. 
test_templates = {'test_template_ldexp' : test_template_ldexp,
			'nan_data_error_ldexp_template' : nan_data_error_ldexp_template,
}


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.
funclist = [x for x in oplist if x['test_op_templ'] == 'test_template_ldexp']

# ==============================================================================



for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '09-Dec-2017', funcname)

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		# Check each array type.
		for functype in codegen_common.floatarrays:
			testtemplate = test_templates[func['test_op_templ']]
			# Basic tests.
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y']}

			f.write(testtemplate % funcdata)

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			# NaN, inf, -inf tests.
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y'],
				'test_nan_default' : func['test_nan_default']
				}

			# NaN
			testtemplate = test_templates[func['test_nan_data_template']]
			funcdata['errorlabel'] = 'NaN'
			funcdata['errordata'] = 'nan'
			f.write(testtemplate % funcdata)

			# inf
			testtemplate = test_templates[func['test_inf_data_template']]
			funcdata['errorlabel'] = 'inf'
			funcdata['errordata'] = 'inf'
			f.write(testtemplate % funcdata)

			# -inf
			testtemplate = test_templates[func['test_ninf_data_template']]
			funcdata['errorlabel'] = 'ninf'
			funcdata['errordata'] = '-inf'
			f.write(testtemplate % funcdata)


		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

