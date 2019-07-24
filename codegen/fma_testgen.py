#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for the fma math function.
# Language: Python 3.5
# Date:     30-Nov-2018
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
test_template_fma = '''

##############################################################################
class fma_general_%(optlable)s_%(arrayevenodd)s_arraysize_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using %(optdescription)s.
	test_template_fma
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

		# The compare values are set by template. They are used to
		# set whether the array size is even or odd.
		if '%(arrayevenodd)s' == 'even':
			testdatasize = 160
		if '%(arrayevenodd)s' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([%(test_op_x)s]), range(testdatasize))]
		self.datax = array.array('%(typecode)s', xdata)

		ydata = [x for x,y in zip(itertools.cycle([%(test_op_y)s]), range(testdatasize))]
		self.datay = array.array('%(typecode)s', ydata)
		zdata = [x for x,y in zip(itertools.cycle([%(test_op_z)s]), range(testdatasize))]
		self.dataz = array.array('%(typecode)s', zdata)

		self.dataout = array.array('%(typecode)s', [0.0] * len(self.datax))

		self.limited = len(self.datax) // 2

		# These are used in parameter loops to avoid having too many tests.
		self.yiter = [%(test_op_y)s]
		self.ziter = [%(test_op_z)s]


	########################################################
	def test_fma_basic_arr_num_num_none_a1(self):
		"""Test fma as *arr_num_num_none* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		for y in self.yiter:
			for z in self.ziter:
				with self.subTest(msg='Failed with parameters', y = y, z = z):

					# Copy the array so the data doesn't get changed.
					datax = copy.copy(self.datax)

					expected = [x * y + z for x in datax]
					%(limexpected_a)s

					arrayfunc.fma(datax, y, z%(testoptions)s)

					for dataoutitem, expecteditem in zip(datax, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fma_basic_arr_num_num_arr_a2(self):
		"""Test fma as *arr_num_num_arr* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		for y in self.yiter:
			for z in self.ziter:
				with self.subTest(msg='Failed with parameters', y = y, z = z):
					expected = [x * y + z for x in self.datax]
					%(limexpected_b)s

					arrayfunc.fma(self.datax, y, z, self.dataout%(testoptions)s)

					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fma_basic_arr_arr_num_none_b1(self):
		"""Test fma as *arr_arr_num_none* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		for z in self.ziter:
			with self.subTest(msg='Failed with parameters', z = z):

				# Copy the array so the data doesn't get changed.
				datax = copy.copy(self.datax)

				expected = [x * y + z for x,y in zip(datax, self.datay)]
				%(limexpected_a)s

				arrayfunc.fma(datax, self.datay, z%(testoptions)s)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fma_basic_arr_arr_num_arr_b2(self):
		"""Test fma as *arr_arr_num_arr* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		for z in self.ziter:
			with self.subTest(msg='Failed with parameters', z = z):
				expected = [x * y + z for x,y in zip(self.datax, self.datay)]
				%(limexpected_b)s

				arrayfunc.fma(self.datax, self.datay, z, self.dataout%(testoptions)s)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fma_basic_arr_num_arr_none_c1(self):
		"""Test fma as *arr_num_arr_none* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		for y in self.yiter:
			with self.subTest(msg='Failed with parameters', y = y):

				# Copy the array so the data doesn't get changed.
				datax = copy.copy(self.datax)

				expected = [x * y + z for x,z in zip(datax, self.dataz)]
				%(limexpected_a)s

				arrayfunc.fma(datax, y, self.dataz%(testoptions)s)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fma_basic_arr_num_arr_arr_c2(self):
		"""Test fma as *arr_num_arr_arr* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		for y in self.yiter:
			with self.subTest(msg='Failed with parameters', y = y):
				expected = [x * y + z for x,z in zip(self.datax, self.dataz)]
				%(limexpected_b)s

				arrayfunc.fma(self.datax, y, self.dataz, self.dataout%(testoptions)s)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fma_basic_arr_arr_arr_none_d1(self):
		"""Test fma as *arr_arr_arr_none* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		expected = [x * y + z for x,y,z in zip(self.datax, self.datay, self.dataz)]
		%(limexpected_a)s

		arrayfunc.fma(self.datax, self.datay, self.dataz%(testoptions)s)

		for dataoutitem, expecteditem in zip(self.datax, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_fma_basic_arr_arr_arr_arr_d2(self):
		"""Test fma as *arr_arr_arr_arr* for basic function - %(optdescription)s - Array code %(typelabel)s.
		"""
		expected = [x * y + z for x,y,z in zip(self.datax, self.datay, self.dataz)]
		%(limexpected_b)s

		arrayfunc.fma(self.datax, self.datay, self.dataz, self.dataout%(testoptions)s)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================


# This is used to test parameters when inserting invalid integer arrays
# and values.
param_int_invalid_template = '''

##############################################################################
class fma_param_errors_types_%(typelabel)s(unittest.TestCase):
	"""Test for invalid parameters.
	param_int_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [%(test_op_x)s]
		arraysize = len(xdata)

		# Floating point test data.
		self.floatarrayx = array.array('%(typecode)s', xdata)
		self.floatarrayy = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), xdata)])
		self.floatarrayz = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_z)s]), xdata)])
		self.floatarrayout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		# Take an arbitrary value from each data array for when we need only a single value.
		self.floatnumx = self.floatarrayx[1]
		self.floatnumy = self.floatarrayy[1]
		self.floatnumz = self.floatarrayz[1]
		self.floatnumout = 0.0

		# Integer test data.
		self.intarrayx = array.array('i', [int(x) for x in self.floatarrayx])
		self.intarrayy = array.array('i', [int(x) for x in self.floatarrayy])
		self.intarrayz = array.array('i', [int(x) for x in self.floatarrayz])
		self.intarrayout = array.array('i', [int(x) for x in self.floatarrayout])
		self.intarrayout = array.array('i', [0] * arraysize)

		# Take an arbitrary value from each data array for when we need only a single value.
		self.intnumx = self.intarrayx[1]
		self.intnumy = self.intarrayy[1]
		self.intnumz = self.intarrayz[1]
		self.intnumout = 0

		# Bytes test data.
		self.bytesx = bytes([abs(int(x)) for x in self.floatarrayx])
		self.bytesy = bytes([abs(int(x)) for x in self.floatarrayy])
		self.bytesz = bytes([abs(int(x)) for x in self.floatarrayz])
		self.bytesout = bytes([abs(int(x)) for x in self.floatarrayout])

		# String data.
		self.strx = ''.join([str(x) for x in self.bytesx])
		self.stry = ''.join([str(x) for x in self.bytesy])
		self.strz = ''.join([str(x) for x in self.bytesz])
		self.strout = ''.join([str(x) for x in self.bytesout])


'''


# This is used to construct the individual tests.
param_int_invalid_template_tests = '''
	########################################################
	def test_fma_invalid_param_%(testlabel)s_%(testcount)s(self):
		"""Test fma as *%(testlabel)s* for invalid integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.fma(self.%(xpass)sx, self.%(ypass)sy, self.%(zpass)sz%(outpass)s)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fma(self.%(xtest)sx, self.%(ytest)sy, self.%(ztest)sz%(outtest)s)

'''


# ==============================================================================

# The template used to generate the tests for testing invalid numbers of parameters.
param_invalid_options_template = '''

##############################################################################
class fma_param_errors_numbers_%(typelabel)s(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_options_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [%(test_op_x)s]
		arraysize =  len(xdata)

		# Floating point test data.
		self.arrayx = array.array('%(typecode)s', xdata)
		self.arrayy = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), xdata)])
		self.arrayz = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_z)s]), xdata)])
		self.arrayout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		# Take an arbitrary value from each data array for when we need only a single value.
		self.numx = self.arrayx[1]
		self.numy = self.arrayy[1]
		self.numz = self.arrayz[1]



	########################################################
	def test_fma_array_num_num_none_a1(self):
		"""Test fma as *array_num_num_array* for matherrors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		arrayx = copy.copy(self.arrayx)

		# This version is expected to pass.
		arrayfunc.fma(arrayx, self.numy, self.numz, matherrors=True)

		arrayx = copy.copy(self.arrayx)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fma(arrayx, self.numy, self.numz, matherrors='a')


	########################################################
	def test_fma_array_num_num_array_a2(self):
		"""Test fma as *array_num_num_array* for matherrors='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.fma(self.arrayx, self.numy, self.numz, self.arrayout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fma(self.arrayx, self.numy, self.numz, self.arrayout, matherrors='a')



	########################################################
	def test_fma_array_num_num_none_b1(self):
		"""Test fma as *array_num_num_array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		arrayx = copy.copy(self.arrayx)

		# This version is expected to pass.
		arrayfunc.fma(arrayx, self.numy, self.numz, maxlen=True)

		arrayx = copy.copy(self.arrayx)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fma(arrayx, self.numy, self.numz, maxlen='a')


	########################################################
	def test_fma_array_num_num_array_b2(self):
		"""Test fma as *array_num_num_array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.fma(self.arrayx, self.numy, self.numz, self.arrayout, maxlen=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fma(self.arrayx, self.numy, self.numz, self.arrayout, maxlen='a')



	########################################################
	def test_fma_array_num_num_none_c1(self):
		"""Test fma as *array_num_num_array* for badparam=True - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		arrayx = copy.copy(self.arrayx)

		# This version is expected to pass.
		arrayfunc.fma(arrayx, self.numy, self.numz)

		arrayx = copy.copy(self.arrayx)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fma(arrayx, self.numy, self.numz, badparam=True)


	########################################################
	def test_fma_array_num_num_array_c2(self):
		"""Test fma as *array_num_num_array* for badparam=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.fma(self.arrayx, self.numy, self.numz, self.arrayout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.fma(self.arrayx, self.numy, self.numz, self.arrayout, badparam=True)



	########################################################
	def test_fma_array_num_array_d1(self):
		"""Test fma as *array_num* for missing numeric parameter - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fma(self.arrayx, self.numy)


	########################################################
	def test_fma_array_num_array_d2(self):
		"""Test fma as *array_num* for missing array parameter - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fma(self.arrayx, self.arrayy)


	########################################################
	def test_fma_array_num_array_e1(self):
		"""Test fma as *array_num* for two missing numeric parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fma(self.arrayx)


	########################################################
	def test_fma_no_params_f1(self):
		"""Test fma with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.fma()



##############################################################################

'''

# ==============================================================================



# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected.
nan_data_error_fma_template = '''

##############################################################################
class fma_finite_errors_%(typelabel)s(unittest.TestCase):
	"""Test for non-finite parameters, nan, inf, -inf.
	nan_data_error_fma_template
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

		xdata = [%(test_op_x)s]
		self.arraysize = len(xdata)

		# Floating point test data.
		self.okarrayx = array.array('%(typecode)s', xdata)
		self.okarrayy = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), xdata)])
		self.okarrayz = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_z)s]), xdata)])
		self.arrayout = array.array('%(typecode)s', itertools.repeat(0.0, self.arraysize))

		# Take an arbitrary value from each data array for when we need only a single value.
		self.oknumx = self.okarrayx[1]
		self.oknumy = self.okarrayy[1]
		self.oknumz = self.okarrayz[1]

		# NaN as array.
		self.nanarrayx = array.array('%(typecode)s', itertools.repeat(math.nan, self.arraysize))
		self.nanarrayy = array.array('%(typecode)s', itertools.repeat(math.nan, self.arraysize))
		self.nanarrayz = array.array('%(typecode)s', itertools.repeat(math.nan, self.arraysize))

		# NaN as individual value.
		self.nannumx = math.nan
		self.nannumy = math.nan
		self.nannumz = math.nan

		# inf as array.
		self.infarrayx = array.array('%(typecode)s', itertools.repeat(math.inf, self.arraysize))
		self.infarrayy = array.array('%(typecode)s', itertools.repeat(math.inf, self.arraysize))
		self.infarrayz = array.array('%(typecode)s', itertools.repeat(math.inf, self.arraysize))

		# inf as individual value.
		self.infnumx = math.inf
		self.infnumy = math.inf
		self.infnumz = math.inf

		# Negative inf as array.
		self.ninfarrayx = array.array('%(typecode)s', itertools.repeat(-math.inf, self.arraysize))
		self.ninfarrayy = array.array('%(typecode)s', itertools.repeat(-math.inf, self.arraysize))
		self.ninfarrayz = array.array('%(typecode)s', itertools.repeat(-math.inf, self.arraysize))

		# Negative inf as individual value.
		self.ninfnumx = -math.inf
		self.ninfnumy = -math.inf
		self.ninfnumz = -math.inf

'''

nan_data_error_fma_template_tests = '''
	########################################################
	def test_fma_nan_param_%(testlabel)s_a_%(testcount)s(self):
		"""Test fma as *%(testlabel)s* with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.fma(self.%(xpass)sx, self.%(ypass)sy, self.%(zpass)sz%(outpass)s, matherrors=True)

		# This should raise an error.
		with self.assertRaises(ArithmeticError):
			arrayfunc.fma(self.%(xtest)sx, self.%(ytest)sy, self.%(ztest)sz%(outtest)s)


	########################################################
	def test_fma_nan_param_%(testlabel)s_b_%(testcount)s(self):
		"""Test fma as *%(testlabel)s* with error checking - Array code %(typelabel)s.
		"""
		# The expected results.
		expected = [(x * y + z) for x,y,z in zip(self.%(xtest)sx, %(yexp)s, %(zexp)s)]

		# Exceptions are turned off so we can use the results to test for correct values.
		arrayfunc.fma(self.%(xtest)sx, self.%(ytest)sy, self.%(ztest)sz%(outtest)s, matherrors=True)

		# This is used to make template handling simpler.
		inputarray = self.%(xtest)sx

		# Compare the actual results to see if they are the same as the expected.
		for dataoutitem, expecteditem in zip(%(assertinput)s, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)

'''


# ==============================================================================

# ==============================================================================

# This is used to close off classes which are generated dynamically. 
template_class_close = '''

##############################################################################

'''

# ==============================================================================



# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.
funclist = [x for x in oplist if x['test_op_templ'] == 'test_template_fma']

# ==============================================================================

# This is used to generate test data for integer arrays.
def genintarraytestdata():
	""" Generate test data for testing integers as input data. Integers
	are invalid inputs.
	Returns: (list) - A list of dictionaries containing the keys and
		values to generate individual test functions.
	"""

	# Create data for testing using integer arrays and values. Integer data
	# is invalid.
	xtest = ['floatarray', 'floatnum', 'intarray', 'intnum', 'bytes', 'str']
	ytest = ['floatarray', 'floatnum', 'intarray', 'intnum', 'bytes', 'str']
	ztest = ['floatarray', 'floatnum', 'intarray', 'intnum', 'bytes', 'str']
	outtest = [', self.floatarrayout', ', self.floatnumout', ', self.intarrayout', ', self.intnumout', ', self.bytesout', ', self.strout', '']

	# This translates failure causing parameters into ones which will pass.
	xpass = {'floatarray' : 'floatarray',
		'floatnum' : 'floatarray',
		'intarray' : 'floatarray',
		'intnum' : 'floatarray',
		'bytes' : 'floatarray',
		'str' : 'floatarray'}

	# Y and z use the same conditions.
	yzpass = {'floatarray' : 'floatarray',
		'floatnum' : 'floatnum',
		'intarray' : 'floatarray',
		'intnum' : 'floatnum',
		'bytes' : 'floatarray',
		'str' : 'floatarray'}

	# For output.
	outpass = {', self.floatarrayout' : ', self.floatarrayout',
		', self.floatnumout' : ', self.floatarrayout',
		', self.intarrayout' : ', self.floatarrayout',
		', self.intnumout' : ', self.floatarrayout',
		', self.bytesout' : ', self.floatarrayout',
		', self.strout' : ', self.floatarrayout',
		'' : ''}

	# Labels for output array.
	outlabels = {', self.floatarrayout' : 'floatarray',
		', self.floatnumout' : 'floatnum',
		', self.intarrayout' : 'intarray',
		', self.intnumout' : 'intnum',
		', self.bytesout' : 'bytes',
		', self.strout' : 'str',
		'' : 'none'}


	# Create all possible combinations.
	combos = list(itertools.product(xtest, ytest, ztest, outtest))

	# Filter out an combinations which are actually OK so that all combinations will fail.
	f = 'float'
	fa = 'floatarray'
	intfunctest = [(x,y,z,out) for (x,y,z,out) in combos if not ((fa in x) and (f in y) and (f in z) and ((fa in out) or (out == '')))]

	# Create corresponding combinations which will pass but are close to the fail conditions.
	intfuncpass = [(xpass[x], yzpass[y], yzpass[z], outpass[out])for (x,y,z,out) in intfunctest]

	# Create labels for both function names and doc strings.
	intfunclabels = ['%s_%s_%s_%s' % (x,y,z, outlabels[out]) for (x,y,z,out) in intfunctest]

	funcdata = []
	for labeldata, passdata, testdata, testcount in zip(intfunclabels, intfuncpass, intfunctest, range(len(intfunclabels))):
		funcdata.append({'typelabel' : functype, 
				'testlabel' : labeldata,
				'testcount' : testcount,
				'xpass' : passdata[0],
				'ypass' : passdata[1],
				'zpass' : passdata[2],
				'outpass' : passdata[3],
				'xtest' : testdata[0],
				'ytest' : testdata[1],
				'ztest' : testdata[2],
				'outtest' : testdata[3],
		})

	return funcdata


# ==============================================================================

# This is used to generate test data for integer arrays.
def gennantestdata():
	""" Generate test data for testing non-finite numbers such as NaN,
	and +/- infinity.
	Returns: (list) - A list of dictionaries containing the keys and
		values to generate individual test functions.
	"""

	xparams = ['okarray', 'nanarray', 'infarray', 'ninfarray']
	yzparams = ['okarray', 'oknum', 'nanarray', 'nannum', 'infarray', 'infnum', 'ninfarray', 'ninfnum']
	outtest = [', self.arrayout', '']

	# This translates failure causing parameters into ones which will pass.
	yzpass = {'okarray' : 'okarray', 
			'oknum' : 'oknum', 
			'nanarray' : 'okarray', 
			'nannum' : 'oknum', 
			'infarray' : 'okarray', 
			'infnum' : 'oknum', 
			'ninfarray' : 'okarray', 
			'ninfnum' : 'oknum'
			}


	# Labels for output array.
	outlabels = {', self.arrayout' : 'okarray',
			'' : 'none'}

	# This is used to translate the general test type to the form specifically
	# needed for the python version of the test.
	yexp = {'okarray' : 'self.okarrayy', 
			'oknum' : 'itertools.repeat(self.oknumy)', 
			'nanarray' : 'self.nanarrayy', 
			'nannum' : 'itertools.repeat(self.nannumy)', 
			'infarray' : 'self.infarrayy', 
			'infnum' : 'itertools.repeat(self.infnumy)', 
			'ninfarray' : 'self.ninfarrayy', 
			'ninfnum' : 'itertools.repeat(self.ninfnumy)'
			}

	# Same again for the next parameter.
	zexp = {'okarray' : 'self.okarrayz', 
			'oknum' : 'itertools.repeat(self.oknumz)', 
			'nanarray' : 'self.nanarrayz', 
			'nannum' : 'itertools.repeat(self.nannumz)', 
			'infarray' : 'self.infarrayz', 
			'infnum' : 'itertools.repeat(self.infnumz)', 
			'ninfarray' : 'self.ninfarrayz', 
			'ninfnum' : 'itertools.repeat(self.ninfnumz)'
			}


	# Used to look up which input to use for the assert test. This is keyed
	# based on the output array string.
	assertinput = {', self.arrayout' : 'self.arrayout',
				'' : 'inputarray'
	}

	# Create all possible combinations.
	combos = list(itertools.product(xparams, yzpass, yzpass, outtest))

	# Filter out an combinations which are actually OK so that all combinations will fail.
	f = 'ok'
	fa = 'okarray'
	okfunctest = [(x,y,z,out) for (x,y,z,out) in combos if not ((fa in x) and (f in y) and (f in z))]

	# Translate the combinations into something that can be used with the python
	# version of the equation.
	expfunctest = [(x,yexp[y],zexp[z],out) for (x,y,z,out) in okfunctest]


	# Create corresponding combinations which will pass but are close to the fail conditions.
	okfuncpass = [('okarray', yzpass[y], yzpass[z], out)for (x,y,z,out) in okfunctest]


	# Create labels for both function names and doc strings.
	funclabels = ['%s_%s_%s_%s' % (x,y,z, outlabels[out]) for (x,y,z,out) in okfunctest]


	funcdata = []
	for labeldata, passdata, testdata, expdata, testcount in zip(funclabels, okfuncpass, okfunctest, expfunctest, range(len(funclabels))):
		funcdata.append({'typelabel' : functype, 
				'testlabel' : labeldata,
				'testcount' : testcount,
				'xpass' : passdata[0],
				'ypass' : passdata[1],
				'zpass' : passdata[2],
				'outpass' : passdata[3],
				'xtest' : testdata[0],
				'ytest' : testdata[1],
				'ztest' : testdata[2],
				'outtest' : testdata[3],
				'yexp' : expdata[1],
				'zexp' : expdata[2],
				'assertinput' : assertinput[testdata[3]]
		})

	return funcdata



# ==============================================================================


for func in funclist:

	funcname = 'fma'
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '30-Nov-2018', funcname)

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		# Check each array type.
		for functype in codegen_common.floatarrays:

			# Basic tests.
			funcdata = {'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 
				'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y'],
				'test_op_z' : func['test_op_z']}


			# With no test options.
			funcdata['optlable'] = 'optionsnone'
			funcdata['optdescription'] = 'no options'
			funcdata['limexpected_a'] = '# No array limits used.'
			funcdata['limexpected_b'] = '# No array limits used.'
			funcdata['testoptions'] = ''

			funcdata['arrayevenodd'] = 'even'

			f.write(test_template_fma % funcdata)


			#####

			# With maxlen test option.
			funcdata['optlable'] = 'optionsmaxlen'
			funcdata['optdescription'] = 'maxlen option'
			funcdata['limexpected_a'] = 'expected = expected[0:self.limited] + list(self.datax)[self.limited:]'
			funcdata['limexpected_b'] = 'expected = expected[0:self.limited] + list(self.dataout)[self.limited:]'
			funcdata['testoptions'] = ', maxlen=self.limited'

			f.write(test_template_fma % funcdata)

			#####

			# With matherror option.
			funcdata['optlable'] = 'optionsmatherror'
			funcdata['optdescription'] = 'matherror option'
			funcdata['limexpected_a'] = '# No array limits used.'
			funcdata['limexpected_b'] = '# No array limits used.'
			funcdata['testoptions'] = ', matherrors=True'

			f.write(test_template_fma % funcdata)

			#####

			# With maxlen and matherrors test options.
			funcdata['optlable'] = 'optionsmaxlenmatherrors'
			funcdata['optdescription'] = 'maxlen and matherrors option'
			funcdata['limexpected_a'] = 'expected = expected[0:self.limited] + list(self.datax)[self.limited:]'
			funcdata['limexpected_b'] = 'expected = expected[0:self.limited] + list(self.dataout)[self.limited:]'
			funcdata['testoptions'] = ', maxlen=self.limited, matherrors=True'

			f.write(test_template_fma % funcdata)


			#####

			# With matherror option.
			funcdata['limexpected_a'] = '# No array limits used.'
			funcdata['limexpected_b'] = '# No array limits used.'

			# Test options.
			funcdata['arrayevenodd'] = 'even'
			funcdata['testoptions'] = ', matherrors=True'
			f.write(test_template_fma % funcdata)

			# Test options.
			funcdata['arrayevenodd'] = 'odd'
			funcdata['testoptions'] = ', matherrors=True'
			f.write(test_template_fma % funcdata)

			# Test options.
			funcdata['arrayevenodd'] = 'even'
			funcdata['testoptions'] = ''
			f.write(test_template_fma % funcdata)


			#############

			# Try all combinations of integer arrays and values. Integers
			# are an invalid data type.
			funcdata = {'typelabel' : functype, 
				'typecode' : functype, 
				'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y'],
				'test_op_z' : func['test_op_z']}


			# Class start for integer tests.
			f.write(param_int_invalid_template % funcdata)

			#############

			# Generate the individual integer tests.
			for funcdata in genintarraytestdata():
				f.write(param_int_invalid_template_tests % funcdata)

			# Close off the generated class.
			f.write(template_class_close)

			#############


			# Test for invalid numbers and kinds of parameters. 
			funcdata = {'typelabel' : functype, 
				'typecode' : functype, 
				'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y'],
				'test_op_z' : func['test_op_z']}
			f.write(param_invalid_options_template % funcdata)

			#############

			# Class start for non-finite tests.
			f.write(nan_data_error_fma_template % funcdata)

			# Generate the individual non-finite number tests.
			for funcdata in gennantestdata():
				f.write(nan_data_error_fma_template_tests % funcdata)

			# Close off the generated class.
			f.write(template_class_close)


		#############

		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

