#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for asum.
# Language: Python 3.6
# Date:     21-May-2014
#
###############################################################################
#
#   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
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

# The basic template for testing each array type for operator function.
op_template_general = '''

##############################################################################
class asum_general_%(arrayevenodd)s_%(typecode)s(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		# It is also big enough that SIMD code that operates on "chunks"
		# of arrays can fit several chunks evenly within the array.
		arraylength = 1024

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if '%(typecode)s' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.%(typecode)s_max
			MinVal = arrayfunc.arraylimits.%(typecode)s_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if '%(typecode)s' in ('L', 'Q'):
			testscale = 1000
		else:
			testscale = 10


		# Set a range of data which will we know will sum to less than
		# the maximum numeric size we can handle in C.
		startdata = int(MinVal // testscale)
		stopdata = int(MaxVal // testscale)
		step = int((stopdata - startdata) // (arraylength // 2))
		# For very small values, we need to avoid having a step of zero.
		if step == 0:
			step = 1
		
		# This produces a list of interleaved values arrays.
		# For signed types, the positive and negative values are interleaved.
		testvalues = list(itertools.chain.from_iterable(zip(range(startdata, stopdata, step), range(stopdata, startdata, -step))))
		testdata = testvalues[:arraylength]


		# Test arrays.
		self.gentest = array.array('%(typecode)s', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code %(typecode)s. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code %(typecode)s. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code %(typecode)s. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code %(typecode)s. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code %(typecode)s. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################

'''

# ==============================================================================


# The basic template for testing each array type for parameter errors.
op_template_params = '''

##############################################################################
class asum_parameter_%(typecode)s(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 1024

		MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.gentest = array.array('%(typecode)s', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code %(typecode)s. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code %(typecode)s. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code %(typecode)s. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code %(typecode)s. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code %(typecode)s. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code %(typecode)s. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code %(typecode)s. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code %(typecode)s. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################

'''

# ==============================================================================

# ==============================================================================

# The basic template for testing for numeric overflow.
op_template_overflow = '''

##############################################################################
%(ovflclassskip)s
class asum_overflow_%(testval)s_%(rotplaces)s_%(typecode)s(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 1024

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = %(rotplaces)s
		basedata = ([1] * arraylength) + [self.%(testval)s, self.%(testval)s] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('%(typecode)s', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if '%(typecode)s' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif '%(typecode)s' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val %% (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code %(typecode)s. Test for overflow with error checking enabled, array data shifted %(rotplaces)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code %(typecode)s. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code %(typecode)s. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################

'''

# ==============================================================================

# The basic template for testing floating point arrays with nan, inf -inf.
nonfinite_template = '''
##############################################################################
class asum_nonfinite_%(rotplaces)s_%(arrayevenodd)s_arraysize_%(typecode)s(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
	nonfinite_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 1024 + arrayextension

		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		MaxVal = arrayfunc.arraylimits.h_max
		MinVal = arrayfunc.arraylimits.h_min

		testscale = 10

		startdata = int(MinVal // testscale)
		stopdata = int(MaxVal // testscale)
		step = int((stopdata - startdata) // (arraylength // 2))

		testvalues = list(itertools.chain.from_iterable(zip(range(startdata, stopdata, step), range(stopdata, startdata, -step))))
		testdata = testvalues[:arraylength]

		# Copy the data so we can modify it in place independently.
		nanvaldatabase = list(testdata)
		infvaldatabase = list(testdata)
		ninfvaldatabase = list(testdata)
		mixedvaldatabase = list(testdata)
		

		# Insert the non-finite test values in the middle of the data.
		tspot = arraylength // 2
		nanvaldatabase[tspot] = math.nan
		infvaldatabase[tspot] = math.inf
		ninfvaldatabase[tspot] = -math.inf
		mixedvaldatabase[tspot] = math.inf
		mixedvaldatabase[tspot + 10] = -math.inf
		mixedvaldatabase[tspot + 20] = math.nan



		# Rotate the values in place in order to create different combinations. 
		# This is being generated through a template to allow us to create 
		# different combinations to help test the effects of having the
		# special values in various locations. This is primarily of use
		# for the SIMD tests which do operations in parallel.
		rotplaces = %(rotplaces)s
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('%(typecode)s', nanvaldatabase)
		self.data_inf = array.array('%(typecode)s',  infvaldatabase)
		self.data_ninf = array.array('%(typecode)s',  ninfvaldatabase)
		self.data_mixed = array.array('%(typecode)s',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code %(typecode)s. Test NaN data with error checking on, %(arrayevenodd)s length, array data shifted %(rotplaces)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code %(typecode)s. Test NaN data with error checking off, no SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code %(typecode)s. Test NaN data with error checking off, with SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code %(typecode)s. Test inf data with error checking on, %(arrayevenodd)s length, array data shifted %(rotplaces)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code %(typecode)s. Test inf data with error checking off, no SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code %(typecode)s. Test inf data with error checking off, with SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code %(typecode)s. Test Negative Inf data with error checking on, %(arrayevenodd)s length, array data shifted %(rotplaces)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code %(typecode)s. Test Negative Inf data with error checking off, no SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code %(typecode)s. Test Negative Inf data with error checking off, with SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code %(typecode)s. Test Mixed data with error checking on, %(arrayevenodd)s length, array data shifted %(rotplaces)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code %(typecode)s. Test Mixed data with error checking off, no SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code %(typecode)s. Test Mixed data with error checking off, with SIMD, %(arrayevenodd)s length array data shifted %(rotplaces)s.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################
'''


# ==============================================================================

# Overflow tests for array type 'L'. With some architectures, we cannot 
# overflow because the integers are too small.
OvflClassSkip = """# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')"""


# ==============================================================================

# This is used to generate test template data for non-finite tests.
def gennonfinitetestdata():
	""" Generate test template data for non-finite tests.
	Returns: (list) - A list of dictionaries containing the keys and
		values to generate individual test functions.
	"""

	# These are the different test values we will combine in various ways.
	arraycode = [('typecode', x) for x in codegen_common.floatarrays]
	arraylen = (('arrayevenodd', 'even'), ('arrayevenodd', 'odd'))
	datarot = [('rotplaces', x) for x in range(5)]

	# The product function produces all possible combinations.
	combos = list(itertools.product(arraycode, arraylen, datarot))


	# Convert the data into a list of dictionaries.
	testdata = [dict(x) for x in combos]


	return testdata

# ==============================================================================


# This is used to generate test template data for overflow tests.
def genoverflowtestdata(arraystested, maxormin):
	""" Generate test template data for overflow tests.
	arraystested (list) - A list of the array codes to be tested.
	maxormin (string) - Either MaxVal or MinVal.
	Returns: (list) - A list of dictionaries containing the keys and
		values to generate individual test functions.
	"""

	# These are the different test values we will combine in various ways.
	arraycode = [('typecode', x) for x in arraystested]
	testval = [('testval',  maxormin)]
	datarot = [('rotplaces', x) for x in range(5)]

	# The product function produces all possible combinations.
	combos = list(itertools.product(arraycode, testval, datarot))


	# Convert the data into a list of dictionaries.
	testdata = [dict(x) for x in combos]

	# Add in the overflow test skip data.
	for x in testdata:
		# 32 bit integer arrays are different on 32 bit versus 64 bit platforms.
		if x['typecode'] in ('l', 'L'):
			x['ovflclassskip'] = OvflClassSkip
		else:
			x['ovflclassskip'] = ''


	return testdata

# ==============================================================================

# This defines the module name.
modulename = 'arrayfunc'
# Import the array module for testing.
arrayimport = 'import array'

funcname = 'asum'

filenamebase = 'test_' + funcname
filename = filenamebase + '.py'
headerdate = codegen_common.FormatHeaderData(filenamebase, '11-Jun-2014', funcname)

# Add additional header data.
headerdate['modulename'] = modulename
headerdate['arrayimport'] = arrayimport


with open(filename, 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Check each array type.
	for arraycode in codegen_common.arraycodes:

		f.write(op_template_general % {'typecode' : arraycode, 'arrayevenodd' : 'even'})
		f.write(op_template_general % {'typecode' : arraycode, 'arrayevenodd' : 'odd'})

	# Check parameters.
	for arraycode in codegen_common.arraycodes:
		f.write(op_template_params % {'typecode' : arraycode})


	# Output the generated code for non-finite data tests.
	for datarec in gennonfinitetestdata():
		f.write(nonfinite_template % datarec)


	# Test for positive overflow. We don't check the smaller integer types 
	# because we cannot cause an overflow in a reasonable amount of RAM.
	for datarec in genoverflowtestdata(('l', 'L', 'q', 'Q', 'f', 'd'), 'MaxVal'):
		f.write(op_template_overflow % datarec)

	# Test for negative overflow. This can only happen with signed data.
	for datarec in genoverflowtestdata(('l', 'q', 'f', 'd'), 'MinVal'):
		f.write(op_template_overflow % datarec)


	#####
	# The code which initiates the unit test.

	f.write(codegen_common.testendtemplate % {'funcname' : funcname, 'testprefix' : 'af'})

