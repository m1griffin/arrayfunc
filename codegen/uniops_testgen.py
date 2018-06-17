#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for math operators with one variable.
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
test_template_uniop = '''

##############################################################################
class %(funclabel)s_general_%(typelabel)s(unittest.TestCase):
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.data = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataout = array.array('%(typecode)s', [0]*len(self.data))

		self.expected = [%(pyoperator)s(x) for x in self.data]

		self.limited = len(self.data) // 2


	########################################################
	def test_%(funclabel)s_inplace_a1(self):
		"""Test %(funclabel)s in place - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x) for x in self.data]

		arrayfunc.%(funcname)s(self.data)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace_ov_a2(self):
		"""Test %(funclabel)s in place with matherrors=True  - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x) for x in self.data]
		arrayfunc.%(funcname)s(self.data, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace_lim_a3(self):
		"""Test %(funclabel)s in place with array limit  - Array code %(typelabel)s.
		"""
		pydataout = [%(pyoperator)s(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.%(funcname)s(self.data, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace_ov_lim_a4(self):
		"""Test %(funclabel)s in place with matherrors=True and array limit  - Array code %(typelabel)s.
		"""
		pydataout = [%(pyoperator)s(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.data)[self.limited:]

		arrayfunc.%(funcname)s(self.data, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_outputarray_a5(self):
		"""Test %(funclabel)s to output array - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x) for x in self.data]
		arrayfunc.%(funcname)s(self.data, self.dataout)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray_ov_a6(self):
		"""Test %(funclabel)s to output array with matherrors=True  - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x) for x in self.data]
		arrayfunc.%(funcname)s(self.data, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray_lim_a7(self):
		"""Test %(funclabel)s to output array with array limit  - Array code %(typelabel)s.
		"""
		pydataout = [%(pyoperator)s(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.%(funcname)s(self.data, self.dataout, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray_ov_lim_a8(self):
		"""Test %(funclabel)s to output array with matherrors=True and array limit - Array code %(typelabel)s.
		"""
		pydataout = [%(pyoperator)s(x) for x in self.data]
		expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

		arrayfunc.%(funcname)s(self.data, self.dataout, matherrors=True, maxlen=self.limited)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================



# ==============================================================================


# The template used to generate the tests for testing invalid parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(%(zero_const)s, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('%(badcode)s', [%(badconv)s(x) for x in self.testarray1])

		self.baddataout = array.array('%(badcode)s', [%(badconv)s(x) for x in self.dataout])



	########################################################
	def test_%(funclabel)s_array_array_a1(self):
		"""Test %(funclabel)s as *array-array* for invalid type of input array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for invalid type of output array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray2, self.baddataout)


	########################################################
	def test_%(funclabel)s_no_params_b1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()


##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for errors flag and maxlen.
param_invalid_opt_template = '''

##############################################################################
class %(funclabel)s_opt_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('%(typecode)s', [%(test_op_x)s])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('%(typecode)s', itertools.repeat(%(zero_const)s, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for errors='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, errors='a')


	########################################################
	def test_%(funclabel)s_array_none_a2(self):
		"""Test %(funclabel)s as *array-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_b1(self):
		"""Test %(funclabel)s as *array-array* for errors='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.dataout, errors='a')


	########################################################
	def test_%(funclabel)s_array_array_b2(self):
		"""Test %(funclabel)s as *array-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.dataout, maxlen='a')



##############################################################################

'''

# ==============================================================================

# Test to see that invalid arrays are rejected.
test_template_invalidarray = '''

##############################################################################
class %(funclabel)s_invalidarray_%(typelabel)s(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataout = array.array('%(typecode)s', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_%(funclabel)s_inplace(self):
		"""Test %(funclabel)s in place - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data)


	########################################################
	def test_%(funclabel)s_inplace_ov_a1(self):
		"""Test %(funclabel)s in place with matherrors=True  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, matherrors=True)


	########################################################
	def test_%(funclabel)s_inplace_lim_a2(self):
		"""Test %(funclabel)s in place with array limit  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, maxlen=self.limited)


	########################################################
	def test_%(funclabel)s_inplace_ov_lim_a3(self):
		"""Test %(funclabel)s in place with matherrors=True and array limit  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, matherrors=True, maxlen=self.limited)


	########################################################
	def test_%(funclabel)s_outputarray_a4(self):
		"""Test %(funclabel)s to output array - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, self.dataout)


	########################################################
	def test_%(funclabel)s_outputarray_ov_a4(self):
		"""Test %(funclabel)s to output array with matherrors=True  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, self.dataout, matherrors=True)


	########################################################
	def test_%(funclabel)s_outputarray_lim_a5(self):
		"""Test %(funclabel)s to output array with array limit  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, self.dataout, maxlen=self.limited)


	########################################################
	def test_%(funclabel)s_outputarray_ov_lim_a6(self):
		"""Test %(funclabel)s to output array with matherrors=True and array limit - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, self.dataout, matherrors=True, maxlen=self.limited)


##############################################################################

'''


# ==============================================================================



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
	def test_%(funclabel)s_outputarray_a1(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout)


	########################################################
	def test_%(funclabel)s_inplace_a2(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors checking on and single parameter functions  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.data%(testarray)s)


	########################################################
	def test_%(funclabel)s_ov_outputarray_a3(self):
		"""Test %(funclabel)s for data of %(testlabel)s with matherrors=True and single parameter functions  - Array code %(typelabel)s.
		"""
		# Calculate the expected result.
		expected = [%(pyoperator)s(x) for x in self.data%(testarray)s]

		# This is the actual test.
		arrayfunc.%(funcname)s(self.data%(testarray)s, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_ov_inplace_a4(self):
		"""Test %(funclabel)s in place for data of %(testlabel)s with matherrors=True and single parameter functions  - Array code %(typelabel)s.
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

# The template used to generate the tests for overflows using minimum value.
param_overflow_minval_template = '''

##############################################################################
class overflow_signed_ovflmin_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for value overflow for negating or taking absolute 
	values of min values in signed arrays.
	param_overflow_minval_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.maxarray = array.array('%(typecode)s', itertools.repeat(self.MaxLimit, arraysize))
		self.minarray = array.array('%(typecode)s', itertools.repeat(self.MinLimit, arraysize))

		self.dataout = array.array('%(typecode)s', itertools.repeat(0, arraysize))



	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for overflow of min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.%(funcname)s(self.minarray)


	########################################################
	def test_%(funclabel)s_array_num_array_a2(self):
		"""Test %(funclabel)s as *array-array* for overflow of min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.%(funcname)s(self.minarray, self.dataout)


	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for overflow of min value with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxarray, matherrors=True)

		# This is the actual test.
		arrayfunc.%(funcname)s(self.minarray, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-array* for overflow of min value with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.%(funcname)s(self.minarray, self.dataout, matherrors=True)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for negative factorial parameters.
factorial_negative_template = '''

##############################################################################
class factorial_error_neg_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for errors in negative factorials in signed integer arrays.
	factorial_negative_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200

		self.negarray = array.array('%(typecode)s', itertools.repeat(-1, arraysize))
		self.goodarray = array.array('%(typecode)s', itertools.repeat(1, arraysize))

		self.dataout = array.array('%(typecode)s', itertools.repeat(0, arraysize))



	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for negative factorial - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.goodarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.%(funcname)s(self.negarray)


	########################################################
	def test_%(funclabel)s_array_num_array_a2(self):
		"""Test %(funclabel)s as *array-array* for negative factorial - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.goodarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.%(funcname)s(self.negarray, self.dataout)


	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for negative factorial with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.goodarray, matherrors=True)

		# This is the actual test.
		arrayfunc.%(funcname)s(self.negarray, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-array* for negative factorial with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.goodarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.%(funcname)s(self.negarray, self.dataout, matherrors=True)



##############################################################################

'''
# ==============================================================================

# ==============================================================================

# The template used to generate the tests for oversized factorial parameters.
factorial_ovfl_template = '''

##############################################################################
class factorial_error_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for oversized factorial parameters in signed integer arrays.
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

		# Check if long integer (l and L) is 8 bytes or only 4.
		# If it is the smaller size, we must revise the maximum factorial size.
		if arrayfunc.arraylimits.L_max < 18446744073709551615:
			maxfactorials['l'] = 12
			maxfactorials['L'] = 12


		arraysize = 200

		self.maxfacarray = array.array('%(typecode)s', itertools.repeat(maxfactorials['%(typecode)s'], arraysize))
		self.ovflfacarray = array.array('%(typecode)s', itertools.repeat(maxfactorials['%(typecode)s'] + 1, arraysize))

		self.dataout = array.array('%(typecode)s', itertools.repeat(0, arraysize))



	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for oversized factorial parameters - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxfacarray)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.%(funcname)s(self.ovflfacarray)


	########################################################
	def test_%(funclabel)s_array_num_array_a2(self):
		"""Test %(funclabel)s as *array-array* for oversized factorial parameters - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxfacarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(OverflowError):
			arrayfunc.%(funcname)s(self.ovflfacarray, self.dataout)


	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for oversized factorial parameters with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxfacarray, matherrors=True)

		# This is the actual test.
		arrayfunc.%(funcname)s(self.ovflfacarray, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-array* for oversized factorial parameters with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.maxfacarray, self.dataout, matherrors=True)

		# This is the actual test.
		arrayfunc.%(funcname)s(self.ovflfacarray, self.dataout, matherrors=True)



##############################################################################

'''




# ==============================================================================

# These are all the test code templates. 
test_templates = {'test_template_uniop' : test_template_uniop,
	'nan_data_errorchecked_noparam_template' : nan_data_errorchecked_noparam_template,
}


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['test_op_templ'] == 'test_template_uniop']


# ==============================================================================


nantemplates = ['test_nan_data_template', 'test_inf_data_template', 'test_ninf_data_template']
nanfunclabel = ['nan', 'inf', 'ninf']
nantestlabel = ['nan', 'inf', '-inf']


# The types of arrays which this operator or function uses.
supportedarrays = {'neg' : (codegen_common.signedint + codegen_common.floatarrays),
			'abs_' : (codegen_common.signedint + codegen_common.floatarrays),
			'factorial' : (codegen_common.intarrays),
	}

# The types of arrays which this operator or function does not support.
unsupportedarrays = dict([(x,tuple(set(codegen_common.arraycodes) - set(y))) for x,y in supportedarrays.items()])



# ==============================================================================


for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '09-Dec-2017', funcname)

	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)

		testtemplate = test_templates[func['test_op_templ']]


		for functype in supportedarrays[funcname]:
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : func['test_op_x']}
			f.write(testtemplate % funcdata)

			# Convert the numeric literals to the appropriate type for the array.
			if functype in codegen_common.floatarrays:
				funcdata['zero_const'] = '0.0'
				funcdata['badcode'] = 'i'
				funcdata['badconv'] = 'int'
			else:
				funcdata['zero_const'] = '0'
				funcdata['badcode'] = 'd'
				funcdata['badconv'] = 'float'

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			# Test for invalid optional parameters such as matherrors and maxlen.
			f.write(param_invalid_opt_template % funcdata)

		# Test to see that calls using unsupported arrays fail.
		for functype in unsupportedarrays[funcname]:
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 
				'typelabel' : functype, 'typecode' : functype}
			# Make sure we don't send negative numbers to unsigned arrays.
			# For signed arrays, we don't care what the sign is because the
			# test will simply raise an exception based on array type anyway.
			if functype in codegen_common.floatarrays:
				funcdata['test_op_x'] = ','.join([str(abs(float(x))) for x in func['test_op_x'].split(',')])
			else:
				funcdata['test_op_x'] = ','.join([str(abs(int(x))) for x in func['test_op_x'].split(',')])

			f.write(test_template_invalidarray % funcdata)


		# Do function specific additional tests.
		if funcname in ('neg', 'abs_'):
			for functype in codegen_common.signedint:
				funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 
					'typelabel' : functype, 'typecode' : functype}
				f.write(param_overflow_minval_template % funcdata)
			

		# Do function specific additional tests.
		if funcname == 'factorial':
			for functype in codegen_common.signedint:
				funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 
					'typelabel' : functype, 'typecode' : functype}
				f.write(factorial_negative_template % funcdata)

			for functype in codegen_common.intarrays:
				funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 
					'typelabel' : functype, 'typecode' : functype}
				f.write(factorial_ovfl_template % funcdata)



		# Tests involving NaN, inf, and -inf.
		if not set(codegen_common.floatarrays).isdisjoint(supportedarrays[funcname]):
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

