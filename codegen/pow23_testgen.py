#!/usr/bin/python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for pow2 and pow3.
# Language: Python 3.6
# Date:     10-Oct-2021
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


# ==============================================================================

import itertools
import codegen_common

# ==============================================================================


# Maximum and minimum limits for raising integers to powers of 2 or 3.
pow2_limits_max = {
	'b' : 'SCHAR_POW2MAX',
	'B' : 'UCHAR_POW2MAX',
	'h' : 'SSHORT_POW2MAX',
	'H' : 'USHORT_POW2MAX',
	'i' : 'SINT_POW2MAX',
	'I' : 'UINT_POW2MAX',
	'l' : 'SLINT_POW2MAX',
	'L' : 'ULINT_POW2MAX',
	'q' : 'SLLINT_POW2MAX',
	'Q' : 'ULLINT_POW2MAX',
	'f' : 'SLLINT_POW2MAX',
	'd' : 'SLLINT_POW2MAX',
}

pow2_limits_min = {
	'b' : 'SCHAR_POW2MIN',
	'B' : '0',
	'h' : 'SSHORT_POW2MIN',
	'H' : '0',
	'i' : 'SINT_POW2MIN',
	'I' : '0',
	'l' : 'SLINT_POW2MIN',
	'L' : '0',
	'q' : 'SLLINT_POW2MIN',
	'Q' : '0',
	'f' : 'SLLINT_POW2MIN',
	'd' : 'SLLINT_POW2MIN',
}

pow3_limits_max = {
	'b' : 'SCHAR_POW3MAX',
	'B' : 'UCHAR_POW3MAX',
	'h' : 'SSHORT_POW3MAX',
	'H' : 'USHORT_POW3MAX',
	'i' : 'SINT_POW3MAX',
	'I' : 'UINT_POW3MAX',
	'l' : 'SLINT_POW3MAX',
	'L' : 'ULINT_POW3MAX',
	'q' : 'SLLINT_POW3MAX',
	'Q' : 'ULLINT_POW3MAX',
	'f' : 'SLLINT_POW3MAX',
	'd' : 'SLLINT_POW3MAX',
}

pow3_limits_min = {
	'b' : 'SCHAR_POW3MIN',
	'B' : '0',
	'h' : 'SSHORT_POW3MIN',
	'H' : '0',
	'i' : 'SINT_POW3MIN',
	'I' : '0',
	'l' : 'SLINT_POW3MIN',
	'L' : '0',
	'q' : 'SLLINT_POW3MIN',
	'Q' : '0',
	'f' : 'SLLINT_POW3MIN',
	'd' : 'SLLINT_POW3MIN',
}


pow2_limits_definitions = '''
SCHAR_POW2MAX = 11
SCHAR_POW2MIN = -11 
UCHAR_POW2MAX = 15

SSHORT_POW2MAX = 181
SSHORT_POW2MIN = -181 
USHORT_POW2MAX = 255

SINT_POW2MAX = 46340
SINT_POW2MIN = -46340
UINT_POW2MAX = 65535

# Account for 64 bit versus 32 bit word sizes.
if arrayfunc.arraylimits.l_max == arrayfunc.arraylimits.q_max:

	SLINT_POW2MAX = 3037000499
	SLINT_POW2MIN = -3037000499
	ULINT_POW2MAX = 4294967295

else:

	SLINT_POW2MAX = 46340
	SLINT_POW2MIN = -46340
	ULINT_POW2MAX = 65535


SLLINT_POW2MAX = 3037000499
SLLINT_POW2MIN = -3037000499
ULLINT_POW2MAX = 4294967295

'''


pow3_limits_definitions = '''
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

'''

# ==============================================================================

test_general_templ = '''

##############################################################################
class %(funclabel)s_general_%(arrayevenodd)s_arraysize_%(typecode)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using numeric data.
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


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
					raise self.failureException('%%0.3f != %%0.3f at index %%d' %% (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%%d != %%d at index %%d' %% (expecteditem, dataoutitem, index))



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
		powmaxdata = %(powmaxdata)s
		powmindata = %(powmindata)s
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
		if '%(typecode)s' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, %(powraise)s) for x in cls.testdata]



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
		if '%(typecode)s' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('%(typecode)s', self.testdata)
		self.dataoutput = array.array('%(typecode)s', [0] * len(self.data1))



	########################################################
	def test_%(funclabel)s_check_test_data(self):
		"""Test %(funclabel)s to ensure we have valid data present - Array code %(typecode)s.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_%(funclabel)s_basic_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for basic function - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		arrayfunc.%(funcname)s(self.data1)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for basic function - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_%(funclabel)s_basic_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for basic function with array limit - Array code %(typecode)s.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.%(funcname)s(self.data1, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_b2(self):
		"""Test %(funclabel)s as *array-array* for basic function with array limit - Array code %(typecode)s.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.%(funcname)s(self.data1, self.dataoutput, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_%(funclabel)s_basic_array_none_c1(self):
		"""Test %(funclabel)s as *array-none* for basic function with matherrors=True - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		arrayfunc.%(funcname)s(self.data1, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for basic function with matherrors=True - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		arrayfunc.%(funcname)s(self.data1, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


	########################################################
	def test_%(funclabel)s_basic_array_none_d1(self):
		"""Test %(funclabel)s as *array-none* for basic function with matherrors=True and with array limit - Array code %(typecode)s.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.data1)[limited:]

		arrayfunc.%(funcname)s(self.data1, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_d2(self):
		"""Test %(funclabel)s as *array-array* for basic function with matherrors=True and with array limit - Array code %(typecode)s.
		"""
		limited = len(self.data1) // 2

		pydataout = self.pyexpected
		expected = pydataout[0:limited] + list(self.dataoutput)[limited:]

		arrayfunc.%(funcname)s(self.data1, self.dataoutput, maxlen=limited, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)




##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for testing invalid array and
# numeric parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid array and numeric parameters.
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


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
					raise self.failureException('%%0.3f != %%0.3f at index %%d' %% (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%%d != %%d at index %%d' %% (expecteditem, dataoutitem, index))



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
		powmaxdata = %(powmaxdata)s
		powmindata = %(powmindata)s
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
		if '%(typecode)s' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, %(powraise)s) for x in cls.testdata]



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
		if '%(typecode)s' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('%(typecode)s', self.testdata)
		self.dataoutput = array.array('%(typecode)s', [0] * len(self.data1))



	########################################################
	def test_%(funclabel)s_check_test_data(self):
		"""Test %(funclabel)s to ensure we have valid data present - Array code %(typecode)s.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)


	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for invalid type of array - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(bytes([1,2,3,4]))


	########################################################
	def test_%(funclabel)s_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for invalid type of array - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s((bytearray[1,2,3,4]), self.dataoutput)



	########################################################
	def test_%(funclabel)s_array_array_a3(self):
		"""Test %(funclabel)s as *array-array* for invalid type of array - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data1, bytearray([1,2,3,4]))


	########################################################
	def test_%(funclabel)s_array_array_a4(self):
		"""Test %(funclabel)s as *array-array* for invalid type of array - Array code %(typecode)s.
		"""
		expected = self.pyexpected

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(bytearray([1,2,3,4]), bytearray([1,2,3,4]))



	########################################################
	def test_%(funclabel)s_no_params_b1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()



##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for errors flag and maxlen.
param_invalid_opt_template = '''

##############################################################################
class %(funclabel)s_opt_param_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid errors flag and maxlen parameters.
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


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
					raise self.failureException('%%0.3f != %%0.3f at index %%d' %% (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%%d != %%d at index %%d' %% (expecteditem, dataoutitem, index))



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
		powmaxdata = %(powmaxdata)s
		powmindata = %(powmindata)s
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
		if '%(typecode)s' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, %(powraise)s) for x in cls.testdata]



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
		if '%(typecode)s' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('%(typecode)s', self.testdata)
		self.dataoutput = array.array('%(typecode)s', [0] * len(self.data1))



	########################################################
	def test_%(funclabel)s_check_test_data(self):
		"""Test %(funclabel)s to ensure we have valid data present - Array code %(typecode)s.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-none* for matherrors='a' - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data1, matherrors='a')


	########################################################
	def test_%(funclabel)s_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for matherrors='a' - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data1, self.dataoutput, matherrors='a')



	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for maxlen='a' - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data1, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_b2(self):
		"""Test %(funclabel)s as *array-array* for maxlen='a' - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data1, self.dataoutput, maxlen='a')



	########################################################
	def test_%(funclabel)s_array_num_none_c1(self):
		"""Test %(funclabel)s as *array-none* for matherrors='a' and maxlen='a' - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data1, matherrors='a', maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for matherrors='a' and maxlen='a' - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data1, self.dataoutput, matherrors='a', maxlen='a')




##############################################################################

'''


# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected.
nan_data_error_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using parameter %(errordata)s.
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


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
					raise self.failureException('%%0.3f != %%0.3f at index %%d' %% (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%%d != %%d at index %%d' %% (expecteditem, dataoutitem, index))



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
		powmaxdata = %(powmaxdata)s
		powmindata = %(powmindata)s
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
		if '%(typecode)s' in ('f', 'd'):
			cls.testdata = [float(x) for x in tdata]
		else:
			cls.testdata = tdata

		# Test results.
		cls.pyexpected = [pow(x, %(powraise)s) for x in cls.testdata]



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
		if '%(typecode)s' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.testdata = classref.testdata
		self.pyexpected = classref.pyexpected
		self.data1 = array.array('%(typecode)s', self.testdata)

		arraysize = len(self.data1)

		self.dataoutput = array.array('%(typecode)s', [0] * arraysize)

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('%(typecode)s', self.testdata)
		self.errordataend[-1] = float('%(errordata)s')



	########################################################
	def test_%(funclabel)s_check_test_data(self):
		"""Test %(funclabel)s to ensure we have valid data present - Array code %(typecode)s.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.data1) >= 10)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for %(errordata)s - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for %(errordata)s - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.errordata, self.dataoutput)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for %(errordata)s - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.errordataend)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_b2(self):
		"""Test %(funclabel)s as *array-array* for %(errordata)s - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.data1, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.errordataend, self.dataoutput)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_none_c1(self):
		"""Test %(funclabel)s as *array-none* for %(errordata)s with error check off - Array code %(typecode)s.
		"""
		expected = [pow(x, %(powraise)s) for x in self.errordata]

		arrayfunc.%(funcname)s(self.errordata, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordata), expected)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for %(errordata)s with error check off - Array code %(typecode)s.
		"""
		expected = [pow(x, %(powraise)s) for x in self.errordata]

		arrayfunc.%(funcname)s(self.errordata, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_none_d1(self):
		"""Test %(funclabel)s as *array-none* for %(errordata)s with error check off - Array code %(typecode)s.
		"""
		expected = [pow(x, %(powraise)s) for x in self.errordataend]

		arrayfunc.%(funcname)s(self.errordataend, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.errordataend), expected)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_d2(self):
		"""Test %(funclabel)s as *array-array* for %(errordata)s with error check off - Array code %(typecode)s.
		"""
		expected = [pow(x, %(powraise)s) for x in self.errordataend]

		arrayfunc.%(funcname)s(self.errordataend, self.dataoutput, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(self.dataoutput), expected)


##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for overflows using maximum or minimum value.
param_overflow_template = '''

##############################################################################
class %(funclabel)s_overflow_%(maxofvltest)s_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funclabel)s for value overflow for %(maxofvltest)s value.
	param_overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 160
		# The templates selects whether this testing maximum or minimum values.
		if '%(maxofvltest)s' == 'max':
			limit = arrayfunc.arraylimits.%(typecode)s_max
		else:
			limit = arrayfunc.arraylimits.%(typecode)s_min

		# A value half the size of the data type limit should be good enough
		# for overflowing.
		testval = limit // 2

		# This array should cause an overflow.
		self.data1 = array.array('%(typecode)s', [testval] * arraysize)
		# Zero of course will not cause an overflow.
		self.zeroconst = array.array('%(typecode)s', [0] * arraysize)

		self.dataoutput = array.array('%(typecode)s', [0] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('%(typecode)s', [0] * arraysize)
		self.errordataend[-1] = testval



	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for overflow value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.data1)


	########################################################
	def test_%(funclabel)s_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for overflow value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.data1, self.dataoutput)



	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for overflow value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.errordataend)


	########################################################
	def test_%(funclabel)s_array_array_b2(self):
		"""Test %(funclabel)s as *array-array* for overflow value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.errordataend, self.dataoutput)



	########################################################
	def test_%(funclabel)s_array_none_c1(self):
		"""Test %(funclabel)s as *array-none* for overflow value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.data1, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')


	########################################################
	def test_%(funclabel)s_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for overflow value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.data1, self.dataoutput, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')



	########################################################
	def test_%(funclabel)s_array_none_d1(self):
		"""Test %(funclabel)s as *array-none* for overflow value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.errordataend, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')


	########################################################
	def test_%(funclabel)s_array_array_d2(self):
		"""Test %(funclabel)s as *array-array* for overflow value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroconst, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.errordataend, self.dataoutput, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')


##############################################################################

'''

# ==============================================================================



# The template used to generate the tests for overflows at the margins of 
# maximum or minimum values.
param_overflow_margin_template = '''

##############################################################################
class %(funclabel)s_overflow_margin_%(maxofvltest)s_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funclabel)s for marginal value overflow for %(maxofvltest)s value.
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
		if '%(maxofvltest)s' == 'max':
			limit = %(powmaxdata)s
			limitovfl = limit + 1
		else:
			limit = %(powmindata)s
			limitovfl = limit - 1


		# This array should not cause an overflow.
		self.dataok = array.array('%(typecode)s', [limit] * arraysize)

		self.dataoutput = array.array('%(typecode)s', [0] * arraysize)

		# This should produce an overflow.
		self.dataovfl1 = array.array('%(typecode)s', [limitovfl] * arraysize)

		# This has just one error value at the end of the array.
		self.errordataend = array.array('%(typecode)s', [limit] * arraysize)
		self.errordataend[-1] = limitovfl



	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for overflow margin value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.dataovfl1)


	########################################################
	def test_%(funclabel)s_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for overflow margin value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.dataovfl1, self.dataoutput)



	########################################################
	def test_%(funclabel)s_array_none_b1(self):
		"""Test %(funclabel)s as *array-none* for overflow margin value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.errordataend)


	########################################################
	def test_%(funclabel)s_array_array_b2(self):
		"""Test %(funclabel)s as *array-array* for overflow margin value - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok, self.dataoutput)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.errordataend, self.dataoutput)



	########################################################
	def test_%(funclabel)s_array_none_c1(self):
		"""Test %(funclabel)s as *array-none* for overflow margin value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.dataovfl1, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')


	########################################################
	def test_%(funclabel)s_array_array_c2(self):
		"""Test %(funclabel)s as *array-array* for overflow margin value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.dataovfl1, self.dataoutput, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')



	########################################################
	def test_%(funclabel)s_array_none_d1(self):
		"""Test %(funclabel)s as *array-none* for overflow margin value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.errordataend, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')


	########################################################
	def test_%(funclabel)s_array_array_d2(self):
		"""Test %(funclabel)s as *array-array* for overflow margin value with error check off - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok, self.dataoutput)

		# This is the actual test.
		try:
			arrayfunc.%(funcname)s(self.errordataend, self.dataoutput, matherrors=True)
		except %(errorflagexceptioncode)s:
			self.fail('Exception %(errorflagexceptioncode)s raised unexpectedly.')


##############################################################################

'''

# ==============================================================================



# This defines the module name.
modulename = 'arrayfunc'
# Import the array module for testing.
arrayimport = 'import array'

powdata = (('pow2', '2', pow2_limits_definitions, pow2_limits_max, pow2_limits_min),
			('pow3', '3', pow3_limits_definitions, pow3_limits_max, pow3_limits_min))

for funcname, powraise, powlims, pow_limits_max, pow_limits_min in powdata:

	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '10-Oct-2021', funcname)

	# Add additional header data.
	headerdate['modulename'] = modulename
	headerdate['arrayimport'] = arrayimport


	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)

		f.write(powlims)

		# For each array type.
		for arraycode in codegen_common.arraycodes:
			funcdata = {'arrayevenodd' : '_',
						'funclabel' : funcname,
						'funcname' : funcname,
						'typecode' : arraycode,
						'powmaxdata' : pow_limits_max[arraycode],
						'powmindata' : pow_limits_min[arraycode],
						'powraise' : powraise,
						}

			# General tests. Process a wide range of valid data.
			f.write(test_general_templ % funcdata)
			# Test with invalid data.
			f.write(param_invalid_template % funcdata)
			# Test with invalid optional parameters.
			f.write(param_invalid_opt_template % funcdata)

			# These test floating point specific errors.
			if arraycode in codegen_common.floatarrays:
				funcdata['errorlabel'] = 'NaN'
				funcdata['errordata'] = 'nan'
				f.write(nan_data_error_template % funcdata)

				funcdata['errorlabel'] = 'inf'
				funcdata['errordata'] = 'inf'
				f.write(nan_data_error_template % funcdata)

				funcdata['errorlabel'] = 'ninf'
				funcdata['errordata'] = '-inf'
				f.write(nan_data_error_template % funcdata)


			# Overflow errors.
			if arraycode in codegen_common.floatarrays:
				funcdata['errorflagexceptioncode'] = 'ArithmeticError'
			else:
				funcdata['errorflagexceptioncode'] = 'OverflowError'
					
			# For max value.
			funcdata['maxofvltest'] = 'max'
			f.write(param_overflow_template % funcdata)

			# For min value we must use signed data only.
			if arraycode in (codegen_common.signedint + codegen_common.floatarrays):
				funcdata['maxofvltest'] = 'min'
				f.write(param_overflow_template % funcdata)


			# For overflow at the margins where we test the maximum or minimum.
			if arraycode in (codegen_common.intarrays): 
				funcdata['maxofvltest'] = 'max'
				f.write(param_overflow_margin_template % funcdata)

			if arraycode in (codegen_common.signedint): 
				funcdata['maxofvltest'] = 'min'
				f.write(param_overflow_margin_template % funcdata)


		# The block at the end which starts up the tests.
		f.write(codegen_common.testendtemplate % {'funcname' : funcname, 'testprefix' : 'af'})


# ==============================================================================
