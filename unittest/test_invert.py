#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_invert.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      06-Mar-2020.
#
###############################################################################
#
#   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for invert.
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




##############################################################################
class invert_general_even_arraysize_nosimd_simd_b(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.b_min
		maxval = arrayfunc.arraylimits.b_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('b', xdata)
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [self.InvertPy('b', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code b.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_b(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.b_min
		maxval = arrayfunc.arraylimits.b_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('b', xdata)
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [self.InvertPy('b', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code b.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_b(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.b_min
		maxval = arrayfunc.arraylimits.b_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('b', xdata)
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [self.InvertPy('b', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code b.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_b(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.b_min
		maxval = arrayfunc.arraylimits.b_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('b', xdata)
		self.dataout = array.array('b', [0]*len(self.data))

		self.expected = [self.InvertPy('b', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code b.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code b.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_B(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.B_min
		maxval = arrayfunc.arraylimits.B_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('B', xdata)
		self.dataout = array.array('B', [0]*len(self.data))

		self.expected = [self.InvertPy('B', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code B.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_B(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.B_min
		maxval = arrayfunc.arraylimits.B_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('B', xdata)
		self.dataout = array.array('B', [0]*len(self.data))

		self.expected = [self.InvertPy('B', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code B.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_B(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.B_min
		maxval = arrayfunc.arraylimits.B_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('B', xdata)
		self.dataout = array.array('B', [0]*len(self.data))

		self.expected = [self.InvertPy('B', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code B.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_B(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.B_min
		maxval = arrayfunc.arraylimits.B_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('B', xdata)
		self.dataout = array.array('B', [0]*len(self.data))

		self.expected = [self.InvertPy('B', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code B.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code B.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_h(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.h_min
		maxval = arrayfunc.arraylimits.h_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('h', xdata)
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [self.InvertPy('h', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code h.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_h(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.h_min
		maxval = arrayfunc.arraylimits.h_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('h', xdata)
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [self.InvertPy('h', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code h.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_h(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.h_min
		maxval = arrayfunc.arraylimits.h_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('h', xdata)
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [self.InvertPy('h', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code h.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_h(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.h_min
		maxval = arrayfunc.arraylimits.h_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('h', xdata)
		self.dataout = array.array('h', [0]*len(self.data))

		self.expected = [self.InvertPy('h', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code h.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code h.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_H(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.H_min
		maxval = arrayfunc.arraylimits.H_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('H', xdata)
		self.dataout = array.array('H', [0]*len(self.data))

		self.expected = [self.InvertPy('H', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code H.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_H(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.H_min
		maxval = arrayfunc.arraylimits.H_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('H', xdata)
		self.dataout = array.array('H', [0]*len(self.data))

		self.expected = [self.InvertPy('H', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code H.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_H(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.H_min
		maxval = arrayfunc.arraylimits.H_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('H', xdata)
		self.dataout = array.array('H', [0]*len(self.data))

		self.expected = [self.InvertPy('H', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code H.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_H(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.H_min
		maxval = arrayfunc.arraylimits.H_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('H', xdata)
		self.dataout = array.array('H', [0]*len(self.data))

		self.expected = [self.InvertPy('H', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code H.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code H.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_i(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.i_min
		maxval = arrayfunc.arraylimits.i_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('i', xdata)
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [self.InvertPy('i', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code i.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_i(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.i_min
		maxval = arrayfunc.arraylimits.i_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('i', xdata)
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [self.InvertPy('i', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code i.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_i(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.i_min
		maxval = arrayfunc.arraylimits.i_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('i', xdata)
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [self.InvertPy('i', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code i.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_i(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.i_min
		maxval = arrayfunc.arraylimits.i_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('i', xdata)
		self.dataout = array.array('i', [0]*len(self.data))

		self.expected = [self.InvertPy('i', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code i.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code i.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_I(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.I_min
		maxval = arrayfunc.arraylimits.I_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('I', xdata)
		self.dataout = array.array('I', [0]*len(self.data))

		self.expected = [self.InvertPy('I', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code I.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_I(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.I_min
		maxval = arrayfunc.arraylimits.I_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('I', xdata)
		self.dataout = array.array('I', [0]*len(self.data))

		self.expected = [self.InvertPy('I', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code I.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_I(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.I_min
		maxval = arrayfunc.arraylimits.I_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('I', xdata)
		self.dataout = array.array('I', [0]*len(self.data))

		self.expected = [self.InvertPy('I', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code I.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_I(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.I_min
		maxval = arrayfunc.arraylimits.I_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('I', xdata)
		self.dataout = array.array('I', [0]*len(self.data))

		self.expected = [self.InvertPy('I', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code I.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code I.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_l(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.l_min
		maxval = arrayfunc.arraylimits.l_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('l', xdata)
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [self.InvertPy('l', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code l.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_l(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.l_min
		maxval = arrayfunc.arraylimits.l_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('l', xdata)
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [self.InvertPy('l', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code l.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_l(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.l_min
		maxval = arrayfunc.arraylimits.l_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('l', xdata)
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [self.InvertPy('l', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code l.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_l(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.l_min
		maxval = arrayfunc.arraylimits.l_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('l', xdata)
		self.dataout = array.array('l', [0]*len(self.data))

		self.expected = [self.InvertPy('l', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code l.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code l.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_L(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.L_min
		maxval = arrayfunc.arraylimits.L_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('L', xdata)
		self.dataout = array.array('L', [0]*len(self.data))

		self.expected = [self.InvertPy('L', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code L.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_L(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.L_min
		maxval = arrayfunc.arraylimits.L_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('L', xdata)
		self.dataout = array.array('L', [0]*len(self.data))

		self.expected = [self.InvertPy('L', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code L.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_L(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.L_min
		maxval = arrayfunc.arraylimits.L_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('L', xdata)
		self.dataout = array.array('L', [0]*len(self.data))

		self.expected = [self.InvertPy('L', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code L.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_L(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.L_min
		maxval = arrayfunc.arraylimits.L_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('L', xdata)
		self.dataout = array.array('L', [0]*len(self.data))

		self.expected = [self.InvertPy('L', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code L.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code L.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.q_min
		maxval = arrayfunc.arraylimits.q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('q', xdata)
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [self.InvertPy('q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code q.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.q_min
		maxval = arrayfunc.arraylimits.q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('q', xdata)
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [self.InvertPy('q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code q.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.q_min
		maxval = arrayfunc.arraylimits.q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('q', xdata)
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [self.InvertPy('q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code q.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.q_min
		maxval = arrayfunc.arraylimits.q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('q', xdata)
		self.dataout = array.array('q', [0]*len(self.data))

		self.expected = [self.InvertPy('q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code q.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_nosimd_simd_Q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.Q_min
		maxval = arrayfunc.arraylimits.Q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('Q', xdata)
		self.dataout = array.array('Q', [0]*len(self.data))

		self.expected = [self.InvertPy('Q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code Q.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_even_arraysize_withsimd_simd_Q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'even' == 'even':
			testdatasize = 320
		if 'even' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.Q_min
		maxval = arrayfunc.arraylimits.Q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('Q', xdata)
		self.dataout = array.array('Q', [0]*len(self.data))

		self.expected = [self.InvertPy('Q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code Q.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_nosimd_simd_Q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.Q_min
		maxval = arrayfunc.arraylimits.Q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('Q', xdata)
		self.dataout = array.array('Q', [0]*len(self.data))

		self.expected = [self.InvertPy('Q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code Q.
		"""
		arrayfunc.invert(self.data , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited , nosimd=True)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_general_odd_arraysize_withsimd_simd_Q(unittest.TestCase):
	"""Test for basic general tests.
	test_template_invert
	"""

	##############################################################################
	def InvertPy(self, typecode, val):
		"""This allows for the invert operation to handle both signed and 
		unsigned integers.
		"""
		# Python native integers are signed.
		if typecode in ('b', 'h', 'i', 'l', 'q'):
			return ~val
		# Unsigned integers require more work to invert.
		else:
			maxval = self.IPLims[typecode]
			if val >= 0:
				return maxval - val
			else:
				return maxval + val



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The maximum values for selected array types.
		self.IPLims = {'B' : arrayfunc.arraylimits.B_max , 'H' : arrayfunc.arraylimits.H_max, 
					'I' : arrayfunc.arraylimits.I_max, 'L' : arrayfunc.arraylimits.L_max,
					'Q' : arrayfunc.arraylimits.Q_max} 

		if 'odd' == 'even':
			testdatasize = 320
		if 'odd' == 'odd':
			testdatasize = 319
		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.Q_min
		maxval = arrayfunc.arraylimits.Q_max

		# We don't test the minimum signed integer value as we are not testing
		# the behaviour of integer overflows in this series of tests.
		if minval < 0:
			minval = minval + 1


		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		self.data = array.array('Q', xdata)
		self.dataout = array.array('Q', [0]*len(self.data))

		self.expected = [self.InvertPy('Q', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code Q.
		"""
		arrayfunc.invert(self.data )

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code Q.
		"""
		arrayfunc.invert(self.data, self.dataout, maxlen=self.limited )

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class invert_param_errors_b(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('b', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_b(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('b', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('b', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code b.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_B(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('B', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_B(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('B', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('B', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code B.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_h(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('h', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_h(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('h', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('h', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code h.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_H(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('H', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_H(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('H', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('H', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code H.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_i(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('i', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_i(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('i', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('i', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code i.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_I(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('I', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_I(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('I', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('I', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code I.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_l(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('l', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_l(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('l', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('l', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code l.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_L(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('L', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_L(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('L', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('L', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code L.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_q(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('q', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_q(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('q', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_param_errors_Q(unittest.TestCase):
	"""Test invert for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('Q', [1,2,3,4,5,6,7,8,9,10])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_invert_array_array_a1(self):
		"""Test invert as *array-array* for invalid type of input array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.badarray1, self.dataout)


	########################################################
	def test_invert_array_array_a2(self):
		"""Test invert as *array-array* for invalid type of output array - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.testarray2, self.baddataout)


##############################################################################



##############################################################################
class invert_opt_param_errors_Q(unittest.TestCase):
	"""Test invert for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('Q', [1,2,3,4,5,6,7,8,9,10])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('Q', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_invert_array_none_a1(self):
		"""Test invert as *array-none* for maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, maxlen='a')


	########################################################
	def test_invert_array_none_a2(self):
		"""Test invert as *array-none* for nosimd='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, nosimd='a')


	########################################################
	def test_invert_array_array_b1(self):
		"""Test invert as *array-array* for maxlen='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_invert_array_array_b2(self):
		"""Test invert as *array-array* for nosimd='a' - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_invert_array_none_c1(self):
		"""Test invert as *array-none* for matherrors=True (unsupported option) - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, matherrors=True)


	########################################################
	def test_invert_array_array_d1(self):
		"""Test invert as *array-array* for matherrors=True (unsupported option) - Array code Q.
		"""
		# This version is expected to pass.
		arrayfunc.invert(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_invert_no_params_e1(self):
		"""Test invert with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert()


##############################################################################



##############################################################################
class invert_invalidarray_f(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
		self.dataout = array.array('f', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data, maxlen=self.limited)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data, self.dataout)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data, self.dataout, maxlen=self.limited)


##############################################################################



##############################################################################
class invert_invalidarray_d(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
		self.dataout = array.array('d', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_invert_inplace(self):
		"""Test invert in place - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data)


	########################################################
	def test_invert_inplace_maxlen(self):
		"""Test invert in place with array maxlen  - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data, maxlen=self.limited)


	########################################################
	def test_invert_outputarray(self):
		"""Test invert to output array - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data, self.dataout)


	########################################################
	def test_invert_outputarray_maxlen(self):
		"""Test invert to output array with array maxlen  - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.invert(self.data, self.dataout, maxlen=self.limited)


##############################################################################


##############################################################################
if __name__ == '__main__':

	# Check to see if the log file option has been selected. This is an option
	# which we have added in order to decide where to output the results.
	if '-l' in sys.argv:
		# Remove the option from the argument list so that "unittest" does 
		# not complain about unknown options.
		sys.argv.remove('-l')

		with open('af_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('invert\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
