#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_convert.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     22-Jun-2014.
# Ver:      28-May-2018.
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
"""This conducts unit tests for convert.
"""

##############################################################################
import sys

import array
import itertools
import math
import operator
import platform
import copy

import unittest

import arrayfunc

##############################################################################

##############################################################################

# The following code is all auto-generated.



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

##############################################################################
class convert_b(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

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
		"""Test convert in array code  b - Convert to array code b.
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
		"""Test convert in array code  b - Convert to array code B.
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
		"""Test convert in array code  b - Convert to array code h.
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
		"""Test convert in array code  b - Convert to array code H.
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
		"""Test convert in array code  b - Convert to array code i.
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
		"""Test convert in array code  b - Convert to array code I.
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
		"""Test convert in array code  b - Convert to array code l.
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
		"""Test convert in array code  b - Convert to array code L.
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
		"""Test convert in array code  b - Convert to array code q.
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
		"""Test convert in array code  b - Convert to array code Q.
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
		"""Test convert in array code  b - Convert to array code f.
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
		"""Test convert in array code  b - Convert to array code d.
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
		"""Test convert in array code  b - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  b - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  b - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  b - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  b - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  b - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  b - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  b - Test lim parameter.
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

##############################################################################
class convert_B(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

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
		"""Test convert in array code  B - Convert to array code b.
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
		"""Test convert in array code  B - Convert to array code B.
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
		"""Test convert in array code  B - Convert to array code h.
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
		"""Test convert in array code  B - Convert to array code H.
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
		"""Test convert in array code  B - Convert to array code i.
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
		"""Test convert in array code  B - Convert to array code I.
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
		"""Test convert in array code  B - Convert to array code l.
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
		"""Test convert in array code  B - Convert to array code L.
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
		"""Test convert in array code  B - Convert to array code q.
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
		"""Test convert in array code  B - Convert to array code Q.
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
		"""Test convert in array code  B - Convert to array code f.
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
		"""Test convert in array code  B - Convert to array code d.
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
		"""Test convert in array code  B - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  B - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  B - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  B - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  B - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  B - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  B - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  B - Test lim parameter.
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

##############################################################################
class convert_h(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

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
		"""Test convert in array code  h - Convert to array code b.
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
		"""Test convert in array code  h - Convert to array code B.
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
		"""Test convert in array code  h - Convert to array code h.
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
		"""Test convert in array code  h - Convert to array code H.
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
		"""Test convert in array code  h - Convert to array code i.
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
		"""Test convert in array code  h - Convert to array code I.
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
		"""Test convert in array code  h - Convert to array code l.
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
		"""Test convert in array code  h - Convert to array code L.
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
		"""Test convert in array code  h - Convert to array code q.
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
		"""Test convert in array code  h - Convert to array code Q.
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
		"""Test convert in array code  h - Convert to array code f.
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
		"""Test convert in array code  h - Convert to array code d.
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
		"""Test convert in array code  h - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  h - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  h - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  h - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  h - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  h - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  h - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  h - Test lim parameter.
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

##############################################################################
class convert_H(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

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
		"""Test convert in array code  H - Convert to array code b.
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
		"""Test convert in array code  H - Convert to array code B.
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
		"""Test convert in array code  H - Convert to array code h.
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
		"""Test convert in array code  H - Convert to array code H.
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
		"""Test convert in array code  H - Convert to array code i.
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
		"""Test convert in array code  H - Convert to array code I.
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
		"""Test convert in array code  H - Convert to array code l.
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
		"""Test convert in array code  H - Convert to array code L.
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
		"""Test convert in array code  H - Convert to array code q.
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
		"""Test convert in array code  H - Convert to array code Q.
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
		"""Test convert in array code  H - Convert to array code f.
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
		"""Test convert in array code  H - Convert to array code d.
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
		"""Test convert in array code  H - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  H - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  H - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  H - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  H - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  H - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  H - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  H - Test lim parameter.
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

##############################################################################
class convert_i(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

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
		"""Test convert in array code  i - Convert to array code b.
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
		"""Test convert in array code  i - Convert to array code B.
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
		"""Test convert in array code  i - Convert to array code h.
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
		"""Test convert in array code  i - Convert to array code H.
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
		"""Test convert in array code  i - Convert to array code i.
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
		"""Test convert in array code  i - Convert to array code I.
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
		"""Test convert in array code  i - Convert to array code l.
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
		"""Test convert in array code  i - Convert to array code L.
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
		"""Test convert in array code  i - Convert to array code q.
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
		"""Test convert in array code  i - Convert to array code Q.
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
		"""Test convert in array code  i - Convert to array code f.
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
		"""Test convert in array code  i - Convert to array code d.
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
		"""Test convert in array code  i - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  i - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  i - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  i - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  i - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  i - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  i - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  i - Test lim parameter.
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

##############################################################################
class convert_I(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

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
		"""Test convert in array code  I - Convert to array code b.
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
		"""Test convert in array code  I - Convert to array code B.
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
		"""Test convert in array code  I - Convert to array code h.
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
		"""Test convert in array code  I - Convert to array code H.
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
		"""Test convert in array code  I - Convert to array code i.
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
		"""Test convert in array code  I - Convert to array code I.
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
		"""Test convert in array code  I - Convert to array code l.
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
		"""Test convert in array code  I - Convert to array code L.
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
		"""Test convert in array code  I - Convert to array code q.
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
		"""Test convert in array code  I - Convert to array code Q.
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
		"""Test convert in array code  I - Convert to array code f.
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
		"""Test convert in array code  I - Convert to array code d.
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
		"""Test convert in array code  I - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  I - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  I - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  I - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  I - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  I - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  I - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  I - Test lim parameter.
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

##############################################################################
class convert_l(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

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
		"""Test convert in array code  l - Convert to array code b.
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
		"""Test convert in array code  l - Convert to array code B.
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
		"""Test convert in array code  l - Convert to array code h.
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
		"""Test convert in array code  l - Convert to array code H.
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
		"""Test convert in array code  l - Convert to array code i.
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
		"""Test convert in array code  l - Convert to array code I.
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
		"""Test convert in array code  l - Convert to array code l.
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
		"""Test convert in array code  l - Convert to array code L.
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
		"""Test convert in array code  l - Convert to array code q.
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
		"""Test convert in array code  l - Convert to array code Q.
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
		"""Test convert in array code  l - Convert to array code f.
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
		"""Test convert in array code  l - Convert to array code d.
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
		"""Test convert in array code  l - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  l - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  l - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  l - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  l - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  l - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  l - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  l - Test lim parameter.
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

##############################################################################
class convert_L(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'

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
		"""Test convert in array code  L - Convert to array code b.
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
		"""Test convert in array code  L - Convert to array code B.
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
		"""Test convert in array code  L - Convert to array code h.
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
		"""Test convert in array code  L - Convert to array code H.
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
		"""Test convert in array code  L - Convert to array code i.
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
		"""Test convert in array code  L - Convert to array code I.
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
		"""Test convert in array code  L - Convert to array code l.
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
		"""Test convert in array code  L - Convert to array code L.
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
		"""Test convert in array code  L - Convert to array code q.
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
		"""Test convert in array code  L - Convert to array code Q.
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
		"""Test convert in array code  L - Convert to array code f.
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
		"""Test convert in array code  L - Convert to array code d.
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
		"""Test convert in array code  L - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  L - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  L - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  L - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  L - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  L - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  L - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  L - Test lim parameter.
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

##############################################################################
class convert_q(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

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
		"""Test convert in array code  q - Convert to array code b.
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
		"""Test convert in array code  q - Convert to array code B.
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
		"""Test convert in array code  q - Convert to array code h.
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
		"""Test convert in array code  q - Convert to array code H.
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
		"""Test convert in array code  q - Convert to array code i.
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
		"""Test convert in array code  q - Convert to array code I.
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
		"""Test convert in array code  q - Convert to array code l.
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
		"""Test convert in array code  q - Convert to array code L.
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
		"""Test convert in array code  q - Convert to array code q.
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
		"""Test convert in array code  q - Convert to array code Q.
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
		"""Test convert in array code  q - Convert to array code f.
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
		"""Test convert in array code  q - Convert to array code d.
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
		"""Test convert in array code  q - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  q - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  q - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  q - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  q - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  q - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  q - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  q - Test lim parameter.
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

##############################################################################
class convert_Q(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'

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
		"""Test convert in array code  Q - Convert to array code b.
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
		"""Test convert in array code  Q - Convert to array code B.
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
		"""Test convert in array code  Q - Convert to array code h.
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
		"""Test convert in array code  Q - Convert to array code H.
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
		"""Test convert in array code  Q - Convert to array code i.
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
		"""Test convert in array code  Q - Convert to array code I.
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
		"""Test convert in array code  Q - Convert to array code l.
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
		"""Test convert in array code  Q - Convert to array code L.
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
		"""Test convert in array code  Q - Convert to array code q.
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
		"""Test convert in array code  Q - Convert to array code Q.
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
		"""Test convert in array code  Q - Convert to array code f.
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
		"""Test convert in array code  Q - Convert to array code d.
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
		"""Test convert in array code  Q - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  Q - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  Q - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  Q - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  Q - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  Q - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  Q - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  Q - Test lim parameter.
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

##############################################################################
class convert_f(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

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
		"""Test convert in array code  f - Convert to array code b.
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
		"""Test convert in array code  f - Convert to array code B.
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
		"""Test convert in array code  f - Convert to array code h.
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
		"""Test convert in array code  f - Convert to array code H.
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
		"""Test convert in array code  f - Convert to array code i.
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
		"""Test convert in array code  f - Convert to array code I.
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
		"""Test convert in array code  f - Convert to array code l.
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
		"""Test convert in array code  f - Convert to array code L.
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
		"""Test convert in array code  f - Convert to array code q.
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
		"""Test convert in array code  f - Convert to array code Q.
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
		"""Test convert in array code  f - Convert to array code f.
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
		"""Test convert in array code  f - Convert to array code d.
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
		"""Test convert in array code  f - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  f - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  f - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  f - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  f - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  f - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  f - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  f - Test lim parameter.
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

##############################################################################
class convert_d(unittest.TestCase):
	"""Test for basic convert function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

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
		"""Test convert in array code  d - Convert to array code b.
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
		"""Test convert in array code  d - Convert to array code B.
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
		"""Test convert in array code  d - Convert to array code h.
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
		"""Test convert in array code  d - Convert to array code H.
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
		"""Test convert in array code  d - Convert to array code i.
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
		"""Test convert in array code  d - Convert to array code I.
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
		"""Test convert in array code  d - Convert to array code l.
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
		"""Test convert in array code  d - Convert to array code L.
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
		"""Test convert in array code  d - Convert to array code q.
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
		"""Test convert in array code  d - Convert to array code Q.
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
		"""Test convert in array code  d - Convert to array code f.
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
		"""Test convert in array code  d - Convert to array code d.
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
		"""Test convert in array code  d - Zero length array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(self.zerodata)))
		with self.assertRaises(IndexError):
			arrayfunc.convert(self.zerodata, dataout)


	########################################################
	def test_convert_14(self):
		"""Test convert in array code  d - Unequal array length.
		"""
		minval, maxval, step = self.TestLimits(self.TypeCode, self.TypeCode)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))
		dataout = array.array(self.TypeCode, itertools.repeat(0, len(data) // 2))

		with self.assertRaises(IndexError):
			arrayfunc.convert(data, dataout)


	########################################################
	def test_convert_15(self):
		"""Test convert in array code  d - Invalid input array data type.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(99, dataout)


	########################################################
	def test_convert_16(self):
		"""Test convert in array code  d - Invalid output array data type.
		"""
		data = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, 99)


	########################################################
	def test_convert_17(self):
		"""Test convert in array code  d - All parameters missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_18(self):
		"""Test convert in array code  d - Second parameter missing.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(0, 100))

		with self.assertRaises(TypeError):
			arrayfunc.convert()


	########################################################
	def test_convert_19(self):
		"""Test convert in array code  d - Too many parameters.
		"""
		outputtest = 'b'
		minval, maxval, step = self.TestLimits(self.TypeCode, outputtest)
		data = array.array(self.TypeCode, range(minval, maxval + 1, step))

		dataout = array.array(outputtest, itertools.repeat(0, len(data)))

		with self.assertRaises(TypeError):
			arrayfunc.convert(data, dataout, 2, maxlen=500)


	########################################################
	def test_convert_20(self):
		"""Test convert in array code  d - Test lim parameter.
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

##############################################################################
class convert_nan_b_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_b_01(self):
		"""Test convert floating point nan to array code  b from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('b', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_b_02(self):
		"""Test convert floating point inf to array code  b from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('b', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_b_03(self):
		"""Test convert floating point -inf to array code  b from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('b', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_B_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_B_01(self):
		"""Test convert floating point nan to array code  B from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('B', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_B_02(self):
		"""Test convert floating point inf to array code  B from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('B', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_B_03(self):
		"""Test convert floating point -inf to array code  B from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('B', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_h_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_h_01(self):
		"""Test convert floating point nan to array code  h from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('h', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_h_02(self):
		"""Test convert floating point inf to array code  h from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('h', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_h_03(self):
		"""Test convert floating point -inf to array code  h from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('h', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_H_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_H_01(self):
		"""Test convert floating point nan to array code  H from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('H', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_H_02(self):
		"""Test convert floating point inf to array code  H from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('H', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_H_03(self):
		"""Test convert floating point -inf to array code  H from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('H', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_i_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_i_01(self):
		"""Test convert floating point nan to array code  i from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('i', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_i_02(self):
		"""Test convert floating point inf to array code  i from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('i', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_i_03(self):
		"""Test convert floating point -inf to array code  i from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('i', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_I_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_I_01(self):
		"""Test convert floating point nan to array code  I from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('I', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_I_02(self):
		"""Test convert floating point inf to array code  I from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('I', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_I_03(self):
		"""Test convert floating point -inf to array code  I from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('I', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_l_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_l_01(self):
		"""Test convert floating point nan to array code  l from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('l', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_l_02(self):
		"""Test convert floating point inf to array code  l from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('l', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_l_03(self):
		"""Test convert floating point -inf to array code  l from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('l', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_L_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_L_01(self):
		"""Test convert floating point nan to array code  L from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('L', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_L_02(self):
		"""Test convert floating point inf to array code  L from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('L', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_L_03(self):
		"""Test convert floating point -inf to array code  L from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('L', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_q_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_q_01(self):
		"""Test convert floating point nan to array code  q from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_q_02(self):
		"""Test convert floating point inf to array code  q from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_q_03(self):
		"""Test convert floating point -inf to array code  q from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_Q_f(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_f_Q_01(self):
		"""Test convert floating point nan to array code  Q from array code f.
		"""
		data = array.array('f', [float('nan')] * 100)
		dataout = array.array('Q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_f_Q_02(self):
		"""Test convert floating point inf to array code  Q from array code f.
		"""
		data = array.array('f', [float('inf')] * 100)
		dataout = array.array('Q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_f_Q_03(self):
		"""Test convert floating point -inf to array code  Q from array code f.
		"""
		data = array.array('f', [float('-inf')] * 100)
		dataout = array.array('Q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_b_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_b_01(self):
		"""Test convert floating point nan to array code  b from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('b', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_b_02(self):
		"""Test convert floating point inf to array code  b from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('b', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_b_03(self):
		"""Test convert floating point -inf to array code  b from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('b', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_B_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_B_01(self):
		"""Test convert floating point nan to array code  B from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('B', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_B_02(self):
		"""Test convert floating point inf to array code  B from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('B', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_B_03(self):
		"""Test convert floating point -inf to array code  B from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('B', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_h_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_h_01(self):
		"""Test convert floating point nan to array code  h from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('h', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_h_02(self):
		"""Test convert floating point inf to array code  h from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('h', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_h_03(self):
		"""Test convert floating point -inf to array code  h from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('h', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_H_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_H_01(self):
		"""Test convert floating point nan to array code  H from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('H', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_H_02(self):
		"""Test convert floating point inf to array code  H from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('H', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_H_03(self):
		"""Test convert floating point -inf to array code  H from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('H', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_i_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_i_01(self):
		"""Test convert floating point nan to array code  i from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('i', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_i_02(self):
		"""Test convert floating point inf to array code  i from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('i', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_i_03(self):
		"""Test convert floating point -inf to array code  i from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('i', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_I_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_I_01(self):
		"""Test convert floating point nan to array code  I from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('I', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_I_02(self):
		"""Test convert floating point inf to array code  I from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('I', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_I_03(self):
		"""Test convert floating point -inf to array code  I from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('I', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_l_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_l_01(self):
		"""Test convert floating point nan to array code  l from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('l', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_l_02(self):
		"""Test convert floating point inf to array code  l from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('l', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_l_03(self):
		"""Test convert floating point -inf to array code  l from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('l', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_L_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_L_01(self):
		"""Test convert floating point nan to array code  L from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('L', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_L_02(self):
		"""Test convert floating point inf to array code  L from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('L', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_L_03(self):
		"""Test convert floating point -inf to array code  L from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('L', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_q_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_q_01(self):
		"""Test convert floating point nan to array code  q from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_q_02(self):
		"""Test convert floating point inf to array code  q from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_q_03(self):
		"""Test convert floating point -inf to array code  q from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

##############################################################################
class convert_nan_Q_d(unittest.TestCase):
	"""Test convert function for nan, inf, or -inf.
	"""

	########################################################
	def test_convert_nan_d_Q_01(self):
		"""Test convert floating point nan to array code  Q from array code d.
		"""
		data = array.array('d', [float('nan')] * 100)
		dataout = array.array('Q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_inf_d_Q_02(self):
		"""Test convert floating point inf to array code  Q from array code d.
		"""
		data = array.array('d', [float('inf')] * 100)
		dataout = array.array('Q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)

	########################################################
	def test_convert_ninf_d_Q_03(self):
		"""Test convert floating point -inf to array code  Q from array code d.
		"""
		data = array.array('d', [float('-inf')] * 100)
		dataout = array.array('Q', itertools.repeat(0, len(data)))

		with self.assertRaises(OverflowError):
			arrayfunc.convert(data, dataout)


##############################################################################

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

##############################################################################
if __name__ == '__main__':

	# Check to see if the log file option has been selected. This is an option
	# which we have added in order to decide where to output the results.
	if '-l' in sys.argv:
		# Remove the option from the argument list so that "unittest" does 
		# not complain about unknown options.
		sys.argv.remove('-l')

		with open('arrayfunc_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('convert\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
