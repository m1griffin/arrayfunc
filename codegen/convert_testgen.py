#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for convert.
# Language: Python 3.4
# Date:     22-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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

import codegen_common

# ==============================================================================


# ==============================================================================


# This needs to be present only once.
guardbands = '''
from arrayfunc import arrayguardbands

##############################################################################
class guardbands:
	"""This calculates the guard band values
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

					'f' : arrayfunc.arraylimits.f_max,
					'd' : arrayfunc.arraylimits.f_max,
					}


		# Some platforms do not support q and Q arrays.
		if 'Q' in array.typecodes:
			self.source_d_min['q'] = arrayfunc.arrayguardbands.LLONG_MIN_GUARD_D
			self.source_d_min['Q'] = 0

			self.source_d_max['q'] = arrayfunc.arrayguardbands.LLONG_MAX_GUARD_D
			self.source_d_max['Q'] = arrayfunc.arrayguardbands.ULLONG_MAX_GUARD_D

			self.source_f_min['q'] = arrayfunc.arrayguardbands.LLONG_MIN_GUARD_F
			self.source_f_min['Q'] = 0

			self.source_f_max['q'] = arrayfunc.arrayguardbands.LLONG_MAX_GUARD_F
			self.source_f_max['Q'] = arrayfunc.arrayguardbands.ULLONG_MAX_GUARD_F



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


# Calculate guard bands.
arrayguardbands = guardbands()

##############################################################################
'''

# ==============================================================================


# The template used to generate the tests.
template = '''
##############################################################################
class convert_%(typelabel)s(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.zerodata = array.array(self.TypeCode, [])

		# This is used to test if array codes are floating point.
		self.FloatTypes = set(['d', 'f'])



		# The maximum values for selected array types.
		self.TestLimMax = {'b' : arrayfunc.arraylimits.b_max, 'B' : arrayfunc.arraylimits.B_max, 
					'h' : arrayfunc.arraylimits.h_max, 'H' : arrayfunc.arraylimits.H_max, 
					'i' : arrayfunc.arraylimits.i_max, 'I' : arrayfunc.arraylimits.I_max, 
					'l' : arrayfunc.arraylimits.l_max, 'L' : arrayfunc.arraylimits.L_max, 
					'f' : arrayfunc.arraylimits.f_max, 
					'd' : arrayfunc.arraylimits.d_max}

		self.TestLimMin = {'b' : arrayfunc.arraylimits.b_min, 'B' : arrayfunc.arraylimits.B_min, 
					'h' : arrayfunc.arraylimits.h_min, 'H' : arrayfunc.arraylimits.H_min, 
					'i' : arrayfunc.arraylimits.i_min, 'I' : arrayfunc.arraylimits.I_min, 
					'l' : arrayfunc.arraylimits.l_min, 'L' : arrayfunc.arraylimits.L_min, 
					'f' : arrayfunc.arraylimits.f_min, 
					'd' : arrayfunc.arraylimits.d_min}

		# Add 'Q' arrays if this is supported on this platform.
		if 'Q' in array.typecodes:
			self.TestLimMax['q'] = arrayfunc.arraylimits.q_max
			self.TestLimMax['Q'] = arrayfunc.arraylimits.Q_max
			self.TestLimMin['q'] = arrayfunc.arraylimits.q_min
			self.TestLimMin['Q'] = arrayfunc.arraylimits.Q_min


	########################################################
	def TestLimits(self, datacode, dataoutcode):
		"""Find a set of test values which are compatible with both input and output arrays.
		"""
		if (datacode in ('f', 'd')) and (dataoutcode not in ('f', 'd')):
			dataoutmax = arrayguardbands.arrayguardbands(datacode, dataoutcode, 'max')
			dataoutmin = arrayguardbands.arrayguardbands(datacode, dataoutcode, 'min')
		else:
			dataoutmax = self.TestLimMax[dataoutcode]
			dataoutmin = self.TestLimMin[dataoutcode]

		datamax = self.TestLimMax[datacode]
		datamin = self.TestLimMin[datacode]
		
		maxval = datamax if datamax < dataoutmax else dataoutmax
		minval = datamin if datamin > dataoutmin else dataoutmin

		spread = int(maxval) - int(minval)
		step = spread // 512
		if step < 1:
			step = 1

		return int(minval), int(maxval), int(step)


	########################################################
	def test_convert_01(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code b.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_02(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code B.
		"""
		outputtest = 'B'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_03(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code h.
		"""
		outputtest = 'h'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_04(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code H.
		"""
		outputtest = 'H'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_05(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code i.
		"""
		outputtest = 'i'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				deltaval = min((abs(dataitem), abs(dataoutitem))) / 100.0
				self.assertAlmostEqual(dataoutitem, dataitem, delta=deltaval)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_06(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code I.
		"""
		outputtest = 'I'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_07(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code l.
		"""
		outputtest = 'l'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_08(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code L.
		"""
		outputtest = 'L'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_09(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code q.
		"""
		outputtest = 'q'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_10(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code Q.
		"""
		outputtest = 'Q'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_11(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code f.
		"""
		outputtest = 'f'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0.0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)


	########################################################
	def test_convert_12(self):
		"""Test convert in array code  %(typelabel)s - Convert to array code d.
		"""
		outputtest = 'd'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0.0, len(data)))

		arrayfunc.convert(data, dataout)

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			for dataitem, dataoutitem in zip(data, dataout):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			self.assertEqual(dataout, data)



	########################################################
	def test_convert_13(self):
		"""Test convert in array code  %(typelabel)s - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  %(typelabel)s - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  %(typelabel)s - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  %(typelabel)s - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  %(typelabel)s - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  %(typelabel)s - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  %(typelabel)s - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  %(typelabel)s - Test lim parameter.
		"""
		outputtest = 'l'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		limlen = len(dataout) // 2

		# Save the second part of the output array. 
		originalout = dataout[limlen:]

		arrayfunc.convert(data, dataout, maxlen=limlen)

		# The first part of the output should be converted.
		converted = dataout[:limlen]

		if set([self.TypeCode, outputtest]) & self.FloatTypes:
			# This data should be converted.
			for dataitem, dataoutitem in zip(data[:limlen], dataout[:limlen]):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
			# This data should be unchanged.
			for dataitem, dataoutitem in zip(originalout, dataout[limlen:]):
				self.assertAlmostEqual(dataoutitem, dataitem, delta=abs(dataitem)/100)
		else:
			# This data should be converted.
			self.assertEqual(dataout[:limlen], data[:limlen])
			# This data should be unchanged.
			self.assertEqual(originalout, dataout[limlen:])


##############################################################################
'''

# ==============================================================================

# This is used to start the test for converting floating point nan, inf, or -inf. 
intnantesttemplate = '''
##############################################################################
class convert_nan_%(typecode)s_%(fromtype)s(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_%(fromtype)s_%(typecode)s_01(self):
		"""Test convert floating point nan to array code  %(typecode)s from array code %(fromtype)s.
		"""
		data = array.array('%(fromtype)s', [float('nan')] * 100)
		dataout = array.array('%(typecode)s', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_%(fromtype)s_%(typecode)s_02(self):
		"""Test convert floating point inf to array code  %(typecode)s from array code %(fromtype)s.
		"""
		data = array.array('%(fromtype)s', [float('inf')] * 100)
		dataout = array.array('%(typecode)s', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_%(fromtype)s_%(typecode)s_03(self):
		"""Test convert floating point -inf to array code  %(typecode)s from array code %(fromtype)s.
		"""
		data = array.array('%(fromtype)s', [float('-inf')] * 100)
		dataout = array.array('%(typecode)s', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################
'''



# This is used to start the test for converting floating point nan, inf, or -inf. 
floatnantesttemplate = '''
##############################################################################
class convert_nan_float(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_d_01(self):
		"""Test convert floating point nan to array code d from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('d', itertools.repeat(0.0, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertTrue(all(map(math.isnan, dataout)))


	########################################################
	def test_convert_nan_d_f_02(self):
		"""Test convert floating point nan to array code f from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('f', itertools.repeat(0.0, len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertTrue(all(map(math.isnan, dataout)))


	########################################################
	def test_convert_inf_f_d_03(self):
		"""Test convert floating point inf to array code d from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('d', itertools.repeat(0.0, len(data)))
		compdata = array.array('d', itertools.repeat(float('inf'), len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


	########################################################
	def test_convert_inf_d_f_04(self):
		"""Test convert floating point inf to array code f from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('f', itertools.repeat(0.0, len(data)))
		compdata = array.array('f', itertools.repeat(float('inf'), len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


	########################################################
	def test_convert_ninf_f_d_05(self):
		"""Test convert floating point -inf to array code d from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('d', itertools.repeat(0.0, len(data)))
		compdata = array.array('d', itertools.repeat(float('-inf'), len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


	########################################################
	def test_convert_ninf_d_f_06(self):
		"""Test convert floating point -inf to array code f from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('f', itertools.repeat(0.0, len(data)))
		compdata = array.array('f', itertools.repeat(float('-inf'), len(data)))

		# There should be no error.
		arrayfunc.convert(data, dataout)

		self.assertEqual(dataout, compdata)


##############################################################################
'''

# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_convert', '22-Jun-2014', 'convert')

with open('test_convert.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Add the guard band calculations.
	f.write(guardbands)


	# Output the generated code for all tests.
	for funtypes in codegen_common.arraycodes:
		datarec = {'typecode' : funtypes}
		datarec['typelabel'] = funtypes
		f.write(template % datarec)



	# NaN, inf, -inf tests for integer arrays.
	for fromtype in ('f', 'd'):
		# Integer array types.
		for seq, funtypes in enumerate(codegen_common.intarrays):
			tdata = {'typecode' : funtypes, 'fromtype' : fromtype}
			f.write(intnantesttemplate % tdata)


	# NaN, inf, -inf tests for float and double arrays.
	f.write(floatnantesttemplate)


	# This starts the tests.
	f.write(codegen_common.testendtemplate % 'convert')


