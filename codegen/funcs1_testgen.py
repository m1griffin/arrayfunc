#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for math functions which use one input parameter.
# Language: Python 3.5
# Date:     08-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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


# This template is for operators which do not use a second parameter.
test_template_noparams = '''

##############################################################################
class %(funclabel)s_general_%(typelabel)s(unittest.TestCase):
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_%(funclabel)s_outputarray(self):
		"""Test %(funclabel)s to output array - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])

		dataout = array.array('%(typecode)s', [0]*len(data))


		expected = [%(pyoperator)s(x) for x in data]
		arrayfunc.%(funcname)s(data, dataout)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray_ov(self):
		"""Test %(funclabel)s to output array with matherrors=True  - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])

		dataout = array.array('%(typecode)s', [0]*len(data))


		expected = [%(pyoperator)s(x) for x in data]
		arrayfunc.%(funcname)s(data, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray_lim(self):
		"""Test %(funclabel)s to output array with array limit  - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])

		dataout = array.array('%(typecode)s', [0]*len(data))

		limited = len(data) // 2

		pydataout = [%(pyoperator)s(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.%(funcname)s(data, dataout, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray_ov_lim(self):
		"""Test %(funclabel)s to output array with matherrors=True and array limit - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])

		dataout = array.array('%(typecode)s', [0]*len(data))

		limited = len(data) // 2

		pydataout = [%(pyoperator)s(x) for x in data]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.%(funcname)s(data, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_inplace(self):
		"""Test %(funclabel)s in place - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])


		expected = [%(pyoperator)s(x) for x in data]
		arrayfunc.%(funcname)s(data)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace_ov(self):
		"""Test %(funclabel)s in place with matherrors=True  - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])


		expected = [%(pyoperator)s(x) for x in data]
		arrayfunc.%(funcname)s(data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace_lim(self):
		"""Test %(funclabel)s in place with array limit  - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])

		limited = len(data) // 2

		pydataout = [%(pyoperator)s(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.%(funcname)s(data, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace_ov_lim(self):
		"""Test %(funclabel)s in place with matherrors=True and array limit  - Array code %(typelabel)s.
		"""
		data = array.array('%(typecode)s', [%(test_op_x)s])

		limited = len(data) // 2

		pydataout = [%(pyoperator)s(x) for x in data]
		expected = pydataout[0:limited] + list(data)[limited:]

		arrayfunc.%(funcname)s(data, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(list(data), expected):
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

		self.floatarray = array.array('%(typecode)s', [%(test_op_x)s])

		arraysize =  len(self.floatarray)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in self.floatarray])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.intarray)


	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for errors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray, matherrors=True)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray, errors='a')


	########################################################
	def test_%(funclabel)s_array_none_b2(self):
		"""Test %(funclabel)s as *array-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray = copy.copy(self.floatarray)
		testmaxlen = len(floatarray) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray, maxlen='a')



	########################################################
	def test_%(funclabel)s_array_array_c1(self):
		"""Test %(funclabel)s as *array-array* for integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.intarray, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for integer output array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_array_c3(self):
		"""Test %(funclabel)s as *array-array* for integer input and output array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.intarray, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_num_array_d1(self):
		"""Test %(funclabel)s as *array-num-array* for errors='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray, self.dataout, errors='a')


	########################################################
	def test_%(funclabel)s_array_array_d2(self):
		"""Test %(funclabel)s as *array-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.floatarray) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray, self.dataout, maxlen=testmaxlen)

		floatarray = copy.copy(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray, self.dataout, maxlen='a')



	########################################################
	def test_%(funclabel)s_no_params_e1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()


##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected and no second parameter is present.
nan_data_error_noparam_template = '''
##############################################################################
class %(funclabel)s_nandata_exceptions_%(testarray)s_%(typelabel)s(unittest.TestCase):
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, 10))

		self.datainf = array.array('%(typecode)s', [math.inf] * 10)
		self.datanan = array.array('%(typecode)s', [math.nan] * 10)
		self.dataninf = array.array('%(typecode)s', [-math.inf] * 10)


	########################################################
	def test_%(funclabel)s_outputarray(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout)


	########################################################
	def test_%(funclabel)s_inplace(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.data%(testarray)s)


	########################################################
	def test_%(funclabel)s_ov_outputarray(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors checking off and single parameter functions  - Array code %(typelabel)s.
		"""
		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout, matherrors=True)


	########################################################
	def test_%(funclabel)s_ov_inplace(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors checking off and single parameter functions  - Array code %(typelabel)s.
		"""
		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, matherrors=True)



##############################################################################

'''


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected and no second parameter is present. When 
# matherrors checking is turned off, the results are checked.
nan_data_errorchecked_noparam_template = '''
##############################################################################
class %(funclabel)s_nandata_exceptions_%(testarray)s_%(typelabel)s(unittest.TestCase):
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, 10))

		self.datainf = array.array('%(typecode)s', [math.inf] * 10)
		self.datanan = array.array('%(typecode)s', [math.nan] * 10)
		self.dataninf = array.array('%(typecode)s', [-math.inf] * 10)


	########################################################
	def test_%(funclabel)s_outputarray(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout)


	########################################################
	def test_%(funclabel)s_inplace(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.data%(testarray)s)


	########################################################
	def test_%(funclabel)s_ov_outputarray(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors checking off and single parameter functions  - Array code %(typelabel)s.
		"""
		# Calculate the expected result.
		expected = [%(pyoperator)s(x) for x in self.data%(testarray)s]

		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_ov_inplace(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors checking off and single parameter functions  - Array code %(typelabel)s.
		"""
		# Calculate the expected result.
		expected = [%(pyoperator)s(x) for x in self.data%(testarray)s]

		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data%(testarray)s), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are not expected. 
nan_data_noerror_noparam_template = '''
##############################################################################
class %(funclabel)s_nandata_errorchecked_%(testarray)s_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation.
	nan_data_noerror_noparam_template
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

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, 10))

		self.datainf = array.array('%(typecode)s', [math.inf] * 10)
		self.datanan = array.array('%(typecode)s', [math.nan] * 10)
		self.dataninf = array.array('%(typecode)s', [-math.inf] * 10)


	########################################################
	def test_%(funclabel)s_outputarray(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		# Calculate the expected result.
		expected = [%(pyoperator)s(x) for x in self.data%(testarray)s]

		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		# Calculate the expected result.
		expected = [%(pyoperator)s(x) for x in self.data%(testarray)s]

		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s)

		for dataoutitem, expecteditem in zip(list(self.data%(testarray)s), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_ov_outputarray(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors checking off and single parameter functions  - Array code %(typelabel)s.
		"""
		# Calculate the expected result.
		expected = [%(pyoperator)s(x) for x in self.data%(testarray)s]

		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_ov_inplace(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors checking off and single parameter functions  - Array code %(typelabel)s.
		"""
		# Calculate the expected result.
		expected = [%(pyoperator)s(x) for x in self.data%(testarray)s]

		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data%(testarray)s), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for isnan and isinf only
nan_data_isnanisinftest_template = '''

##############################################################################
class %(funclabel)s_isnanisinftest_%(typelabel)s(unittest.TestCase):
	"""Test for invalid parameters.
	nan_data_isnanisinftest_template
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

		self.floatarray = array.array('%(typecode)s', [%(test_op_x)s])

		floatarraysize =  len(self.floatarray)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, floatarraysize))

		# This interleaves ordinaray float data with nan, inf, and -inf.
		self.testarray = array.array('%(typecode)s', itertools.chain.from_iterable([(x,y) for (x,y) in zip(itertools.cycle([float('nan'), float('inf'), float('-inf')]), self.floatarray)]))


		# These are the expected results from tests.
		self.floatexpected = [float(%(pyoperator)s(x)) for x in self.floatarray]
		self.testexpected = [float(%(pyoperator)s(x)) for x in self.testarray]

		testarraysize =  len(self.testexpected)

		self.testdataout = array.array('%(typecode)s', itertools.repeat(0.0, testarraysize))


	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for float data - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.floatarray)

		for dataoutitem, expecteditem in zip(list(self.floatarray), self.floatexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_none_a2(self):
		"""Test %(funclabel)s as *array-none* for mixed float, nan, inf array - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.testarray)

		for dataoutitem, expecteditem in zip(list(self.testarray), self.testexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for float data with matherrors=True - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.floatarray, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.floatarray), self.floatexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_none_b2(self):
		"""Test %(funclabel)s as *array-none* for mixed float, nan, inf data with matherrors=True - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.testarray, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.testarray), self.testexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_none_c1(self):
		"""Test %(funclabel)s as *array-none* for float data with maxlen=length//2 - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.floatarray) // 2
		floathalfexpected = copy.copy(self.floatexpected[0: testmaxlen] + list(self.floatarray)[testmaxlen :])

		arrayfunc.%(funcname)s(self.floatarray, maxlen=testmaxlen)

		for dataoutitem, expecteditem in zip(list(self.floatarray), floathalfexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_none_c2(self):
		"""Test %(funclabel)s as *array-none* for mixed float, nan, inf with maxlen=length//2 - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.testarray) // 2
		testhalfexpected = self.testexpected[0: testmaxlen] + list(self.testarray)[testmaxlen :]

		arrayfunc.%(funcname)s(self.testarray, maxlen=testmaxlen)

		for dataoutitem, expecteditem in zip(list(self.testarray), testhalfexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_array_d1(self):
		"""Test %(funclabel)s as *array-array* for float data with output array - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.floatarray, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.floatexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_array_d2(self):
		"""Test %(funclabel)s as *array-array* for mixed float, nan, inf with output array - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.testarray, self.testdataout)

		for dataoutitem, expecteditem in zip(list(self.testdataout), self.testexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_array_e1(self):
		"""Test %(funclabel)s as *array-array* for float data with output array with matherrors=True - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.floatarray, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.floatexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_array_e2(self):
		"""Test %(funclabel)s as *array-array* for mixed float, nan, inf with output array with matherrors=True - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.testarray, self.testdataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.testdataout), self.testexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_array_f1(self):
		"""Test %(funclabel)s as *array-array* for float data with output array with maxlen=length//2 - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.floatarray) // 2
		floathalfexpected = self.floatexpected[0: testmaxlen] + list(self.dataout)[testmaxlen :]

		arrayfunc.%(funcname)s(self.floatarray, self.dataout, maxlen=testmaxlen)

		for dataoutitem, expecteditem in zip(list(self.dataout), floathalfexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_array_array_f2(self):
		"""Test %(funclabel)s as *array-array* for mixed float, nan, inf with output array with maxlen=length//2 - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.testarray) // 2
		testhalfexpected = self.testexpected[0: testmaxlen] + list(self.testdataout)[testmaxlen :]

		arrayfunc.%(funcname)s(self.testarray, self.testdataout, maxlen=testmaxlen)

		for dataoutitem, expecteditem in zip(list(self.testdataout), testhalfexpected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================



# ==============================================================================

# These are all the test code templates. 
test_templates = {'test_template_noparams' : test_template_noparams,
	'nan_data_error_noparam_template' : nan_data_error_noparam_template,
	'nan_data_errorchecked_noparam_template' : nan_data_errorchecked_noparam_template,
	'nan_data_noerror_noparam_template' : nan_data_noerror_noparam_template,
	'nan_data_isnanisinftest_template' : nan_data_isnanisinftest_template,
}


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['test_op_templ'] == 'test_template_noparams']


# ==============================================================================


nantemplates = ['test_nan_data_template', 'test_inf_data_template', 'test_ninf_data_template']
nanfunclabel = ['nan', 'inf', 'ninf']
nantestlabel = ['nan', 'inf', '-inf']


for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '09-Dec-2017', funcname)

	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)

		testtemplate = test_templates[func['test_op_templ']]

		for functype in codegen_common.floatarrays:
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : func['test_op_x']}
			f.write(testtemplate % funcdata)

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

		# Tests involving NaN, inf, and -inf.
		for templatename, testarray, testlabel  in zip(nantemplates, nanfunclabel, nantestlabel) :

			testtemplate = test_templates[func[templatename]]

			for functype in codegen_common.floatarrays:
				funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 
						'pyoperator' : func['pyoperator'], 'typelabel' : functype, 
						'typecode' : functype, 'test_op_x' : func['test_op_x'],
						'testarray' : testarray, 'testlabel' : testlabel}
				f.write(testtemplate % funcdata)


		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

