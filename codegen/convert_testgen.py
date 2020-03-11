#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for convert.
# Language: Python 3.5
# Date:     22-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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


# The template used to generate the tests.
op_template = '''
##############################################################################
class convert_%(typecode)s(unittest.TestCase):
	"""Test for basic convert function.
	op_template
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

		self.TypeCode = '%(typecode)s'



	########################################################
	def test_convert_ops_01(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code b.
		"""
		outputtest = 'b'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_02(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code B.
		"""
		outputtest = 'B'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_03(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code h.
		"""
		outputtest = 'h'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_04(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code H.
		"""
		outputtest = 'H'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_05(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code i.
		"""
		outputtest = 'i'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_06(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code I.
		"""
		outputtest = 'I'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_07(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code l.
		"""
		outputtest = 'l'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_08(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code L.
		"""
		outputtest = 'L'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_09(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code q.
		"""
		outputtest = 'q'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_10(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code Q.
		"""
		outputtest = 'Q'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, dataitem)


	########################################################
	def test_convert_ops_11(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code f.
		"""
		outputtest = 'f'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0.0, len(data)))

		arrayfunc.convert(data, dataout)

		# Both parameters to assertEqual must be floating point in order
		# for the floating point comparison to use FloatassertEqual.
		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, float(dataitem))


	########################################################
	def test_convert_ops_12(self):
		"""Test convert for basic operation in array code  %(typecode)s - Convert to array code d.
		"""
		outputtest = 'd'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0.0, len(data)))

		arrayfunc.convert(data, dataout)

		# Both parameters to assertEqual must be floating point in order
		# for the floating point comparison to use FloatassertEqual.
		for dataitem, dataoutitem in zip(data, dataout):
			self.assertEqual(dataoutitem, float(dataitem))



	########################################################
	def test_convert_ops_13(self):
		"""Test convert for basic operation in array code  %(typecode)s - Test maxlen parameter.
		"""
		outputtest = 'l'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		limlen = len(dataout) // 2

		# Save the second part of the output array. 
		originalout = dataout[limlen:]

		arrayfunc.convert(data, dataout, maxlen=limlen)

		# The first part of the output should be converted.
		converted = dataout[:limlen]

		# This data should be converted.
		for dataitem, dataoutitem in zip(data[:limlen], dataout[:limlen]):
			self.assertEqual(dataoutitem, dataitem)

		# This data should be unchanged.
		for dataitem, dataoutitem in zip(originalout, dataout[limlen:]):
			self.assertEqual(dataoutitem, dataitem)



##############################################################################
'''

# ==============================================================================




# The template used to generate the tests.
param_template = '''
##############################################################################
class convert_params_%(typecode)s(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.zerodata = array.array(self.TypeCode, [])



	########################################################
	def test_convert_params_01(self):
		"""Test convert for parameters in array code  %(typecode)s - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_params_02(self):
		"""Test convert for parameters in array code  %(typecode)s - Unequal array length.
		"""
		testvals = TestData.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, testvals)
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_params_03(self):
		"""Test convert for parameters in array code  %(typecode)s - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_params_04(self):
		"""Test convert for parameters in array code  %(typecode)s - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_params_05(self):
		"""Test convert for parameters in array code  %(typecode)s - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_params_06(self):
		"""Test convert for parameters in array code  %(typecode)s - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_params_07(self):
		"""Test convert for parameters in array code  %(typecode)s - Too many parameters.
		"""
		outputtest = 'b'
		testvals = TestData.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, testvals)

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)



##############################################################################
'''

# ==============================================================================

# ==============================================================================

# This is used to start the test for converting floating point nan, inf, or -inf. 
intnonfinitetesttemplate = '''
##############################################################################
class convert_intnonfinite_to_%(typecode)s_from_%(fromtype)s(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf to integer.
	intnonfinitetesttemplate
	"""

	########################################################
	def test_convert_nonfinite_%(fromtype)s_%(typecode)s_01(self):
		"""Test convert floating point nan to array code  %(typecode)s from array code %(fromtype)s.
		"""
		data = array.array('%(fromtype)s', [math.nan] * 100)
		dataout = array.array('%(typecode)s', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_%(fromtype)s_%(typecode)s_02(self):
		"""Test convert floating point inf to array code  %(typecode)s from array code %(fromtype)s.
		"""
		data = array.array('%(fromtype)s', [math.inf] * 100)
		dataout = array.array('%(typecode)s', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_%(fromtype)s_%(typecode)s_03(self):
		"""Test convert floating point -inf to array code  %(typecode)s from array code %(fromtype)s.
		"""
		data = array.array('%(fromtype)s', [-math.inf] * 100)
		dataout = array.array('%(typecode)s', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################
'''



# This is used to start the test for converting floating point nan, inf, or -inf. 
floatnonfinitetesttemplate = '''
##############################################################################
class convert_floatnonfinite_float(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf between floating point types.
	floatnonfinitetesttemplate
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_convert_nonfinite_f_d_01(self):
		"""Test convert floating point nan to array code d from array code f.
		"""
		data = array.array('f', [math.nan] * 100)
		dataout = array.array('d', itertools.repeat(0.0, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertTrue(all(map(math.isnan, dataout)))


	########################################################
	def test_convert_nonfinite_d_f_02(self):
		"""Test convert floating point nan to array code f from array code d.
		"""
		data = array.array('d', [math.nan] * 100)
		dataout = array.array('f', itertools.repeat(0.0, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertTrue(all(map(math.isnan, dataout)))


	########################################################
	def test_convert_inf_f_d_03(self):
		"""Test convert floating point inf to array code d from array code f.
		"""
		data = array.array('f', [math.inf] * 100)
		dataout = array.array('d', itertools.repeat(0.0, len(data)))
		compdata = array.array('d', itertools.repeat(math.inf, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


	########################################################
	def test_convert_inf_d_f_04(self):
		"""Test convert floating point inf to array code f from array code d.
		"""
		data = array.array('d', [math.inf] * 100)
		dataout = array.array('f', itertools.repeat(0.0, len(data)))
		compdata = array.array('f', itertools.repeat(math.inf, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


	########################################################
	def test_convert_ninf_f_d_05(self):
		"""Test convert floating point -inf to array code d from array code f.
		"""
		data = array.array('f', [-math.inf] * 100)
		dataout = array.array('d', itertools.repeat(0.0, len(data)))
		compdata = array.array('d', itertools.repeat(-math.inf, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


	########################################################
	def test_convert_ninf_d_f_06(self):
		"""Test convert floating point -inf to array code f from array code d.
		"""
		data = array.array('d', [-math.inf] * 100)
		dataout = array.array('f', itertools.repeat(0.0, len(data)))
		compdata = array.array('f', itertools.repeat(-math.inf, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


##############################################################################
'''

# ==============================================================================


# This needs to be present only once.
testlimits = '''
from arrayfunc import arrayguardbands

##############################################################################
class testlimits:
	"""This calculates the test limits, including guard band values
	"""

	########################################################
	def __init__(self):

		# Min value for when the source is a 'd' (double) array.
		self.source_d_min = {
					'b' : arrayfunc.arraylimits.b_min,
					'B' : arrayfunc.arraylimits.B_min,
					'h' : arrayfunc.arraylimits.h_min,
					'H' : arrayfunc.arraylimits.H_min,
					'i' : arrayfunc.arraylimits.i_min,
					'I' : arrayfunc.arraylimits.I_min,

					'l' : arrayfunc.arrayguardbands.LONG_MIN_GUARD_D,
					'L' : 0,
					'q' : arrayfunc.arrayguardbands.LLONG_MIN_GUARD_D,
					'Q' : 0,

					'f' : arrayfunc.arraylimits.f_min,
					'd' : arrayfunc.arraylimits.d_min,
					}

		# Max value for when the source is a 'd' (double) array.
		self.source_d_max = {
					'b' : arrayfunc.arraylimits.b_max,
					'B' : arrayfunc.arraylimits.B_max,
					'h' : arrayfunc.arraylimits.h_max,
					'H' : arrayfunc.arraylimits.H_max,
					'i' : arrayfunc.arraylimits.i_max,
					'I' : arrayfunc.arraylimits.I_max,

					'l' : arrayfunc.arrayguardbands.LONG_MAX_GUARD_D,
					'L' : arrayfunc.arrayguardbands.ULONG_MAX_GUARD_D,
					'q' : arrayfunc.arrayguardbands.LLONG_MAX_GUARD_D,
					'Q' : arrayfunc.arrayguardbands.ULLONG_MAX_GUARD_D,

					'f' : arrayfunc.arraylimits.f_max,
					'd' : arrayfunc.arraylimits.d_max,
					}


		# Min value for when the source is a 'f' (float) array.
		self.source_f_min = {
					'b' : arrayfunc.arraylimits.b_min,
					'B' : arrayfunc.arraylimits.B_min,
					'h' : arrayfunc.arraylimits.h_min,
					'H' : arrayfunc.arraylimits.H_min,

					'i' : arrayfunc.arrayguardbands.INT_MIN_GUARD_F,
					'I' : arrayfunc.arraylimits.I_min,
					'l' : arrayfunc.arrayguardbands.LONG_MIN_GUARD_F,
					'L' : 0,
					'q' : arrayfunc.arrayguardbands.LLONG_MIN_GUARD_F,
					'Q' : 0,

					'f' : arrayfunc.arraylimits.f_min,
					'd' : arrayfunc.arraylimits.f_min,
					}

		# Max value for when the source is a 'f' (float) array.
		self.source_f_max = {
					'b' : arrayfunc.arraylimits.b_max,
					'B' : arrayfunc.arraylimits.B_max,
					'h' : arrayfunc.arraylimits.h_max,
					'H' : arrayfunc.arraylimits.H_max,

					'i' : arrayfunc.arrayguardbands.INT_MAX_GUARD_F,
					'I' : arrayfunc.arrayguardbands.UINT_MAX_GUARD_F,
					'l' : arrayfunc.arrayguardbands.LONG_MAX_GUARD_F,
					'L' : arrayfunc.arrayguardbands.ULONG_MAX_GUARD_F,
					'q' : arrayfunc.arrayguardbands.LLONG_MAX_GUARD_F,
					'Q' : arrayfunc.arrayguardbands.ULLONG_MAX_GUARD_F,

					'f' : arrayfunc.arraylimits.f_max,
					'd' : arrayfunc.arraylimits.f_max,
					}



		# The maximum values for selected array types.
		self.TestLimMax = {'b' : arrayfunc.arraylimits.b_max, 'B' : arrayfunc.arraylimits.B_max, 
					'h' : arrayfunc.arraylimits.h_max, 'H' : arrayfunc.arraylimits.H_max, 
					'i' : arrayfunc.arraylimits.i_max, 'I' : arrayfunc.arraylimits.I_max, 
					'l' : arrayfunc.arraylimits.l_max, 'L' : arrayfunc.arraylimits.L_max, 
					'q' : arrayfunc.arraylimits.q_max, 'Q' : arrayfunc.arraylimits.Q_max, 
					'f' : arrayfunc.arraylimits.f_max, 
					'd' : arrayfunc.arraylimits.d_max}

		self.TestLimMin = {'b' : arrayfunc.arraylimits.b_min, 'B' : arrayfunc.arraylimits.B_min, 
					'h' : arrayfunc.arraylimits.h_min, 'H' : arrayfunc.arraylimits.H_min, 
					'i' : arrayfunc.arraylimits.i_min, 'I' : arrayfunc.arraylimits.I_min, 
					'l' : arrayfunc.arraylimits.l_min, 'L' : arrayfunc.arraylimits.L_min, 
					'q' : arrayfunc.arraylimits.q_min, 'Q' : arrayfunc.arraylimits.Q_min, 
					'f' : arrayfunc.arraylimits.f_min, 
					'd' : arrayfunc.arraylimits.d_min}


	########################################################
	def arrayguardbands(self, sourcetype, destcode, limtype):
		"""Return the platform limits for each array type.
		"""
		if limtype == 'min':
			if sourcetype == 'd':
				return self.source_d_min[destcode]
			else:
				return self.source_f_min[destcode]
		elif limtype == 'max':
			if sourcetype == 'd':
				return self.source_d_max[destcode]
			else:
				return self.source_f_max[destcode]
		else:
			print('Invalid limit type', limtype)
			return None


	########################################################
	def TestLimits(self, datacode, dataoutcode):
		"""Find a set of test values which are compatible with both input and output arrays.
		Returns a list of data to use for test values.
		"""
		if (datacode in ('f', 'd')) and (dataoutcode not in ('f', 'd')):
			dataoutmax = self.arrayguardbands(datacode, dataoutcode, 'max')
			dataoutmin = self.arrayguardbands(datacode, dataoutcode, 'min')
		else:
			dataoutmax = self.TestLimMax[dataoutcode]
			dataoutmin = self.TestLimMin[dataoutcode]

		datamax = self.TestLimMax[datacode]
		datamin = self.TestLimMin[datacode]

		# Make sure the data fits within the smallest range.
		maxval = min(datamax, dataoutmax)
		minval = max(datamin, dataoutmin)

		spread = int(maxval) - int(minval)
		step = spread // 512
		if step < 1:
			step = 1


		# Source and destination are integers, then use the full data range.
		if (datacode not in ('f', 'd')) and (dataoutcode not in ('f', 'd')):
			return list(range(minval, maxval + 1, step))
		# Either the source or destination are floating point.
		else:
			tmpmin = max(minval, -512)
			tmpmax = min(maxval, 511)
			longdata = list(range(tmpmin, tmpmax + 1, 1))
			if spread > 1024:
				longdata[0] = minval
				longdata[-1] = maxval

			# Make sure the data is in the expected format. 
			if datacode in ('f', 'd'):
				return [float(x) for x in longdata]
			else:
				return [int(x) for x in longdata]




# Calculate test limits.
TestData = testlimits()

##############################################################################
'''

# ==============================================================================

# This defines the module name.
modulename = 'arrayfunc'
# Import the array module for testing.
arrayimport = 'import array'

funcname = 'convert'

filenamebase = 'test_' + funcname
filename = filenamebase + '.py'
headerdate = codegen_common.FormatHeaderData(filenamebase, '22-Jun-2014', funcname)

# Add additional header data.
headerdate['modulename'] = modulename
headerdate['arrayimport'] = arrayimport


with open(filename, 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	#####
	# Basic tests.

	# Check each array type.
	for arraycode in codegen_common.arraycodes:

		opdata = {'typecode' : arraycode}

		f.write(op_template % opdata)
		f.write(param_template % opdata)


	tocode = [('typecode', x) for x in codegen_common.intarrays]
	fromcode = [('fromtype', x) for x in codegen_common.floatarrays]

	# Create a variety of input values with non-finite data.
	for opvalues in list(itertools.product(tocode, fromcode)):
		opdata = dict(opvalues)
		f.write(intnonfinitetesttemplate % opdata)


	# This template does not require parameters to complete it. 
	f.write(floatnonfinitetesttemplate)

	# This is a test support function, but we only need one copy.
	f.write(testlimits)

	#####
	# The code which initiates the unit test.

	f.write(codegen_common.testendtemplate % {'funcname' : funcname, 'testprefix' : 'af'})


# ==============================================================================
