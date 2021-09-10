#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_asum.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
# Ver:      09-Sep-2021.
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
"""This conducts unit tests for asum.
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
class asum_general_even_b(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'b' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.b_max
			MinVal = arrayfunc.arraylimits.b_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'b' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('b', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code b. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code b. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code b. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code b. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code b. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_b(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'b' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.b_max
			MinVal = arrayfunc.arraylimits.b_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'b' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('b', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code b. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code b. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code b. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code b. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code b. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_B(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'B' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.B_max
			MinVal = arrayfunc.arraylimits.B_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'B' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('B', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code B. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code B. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code B. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code B. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code B. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_B(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'B' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.B_max
			MinVal = arrayfunc.arraylimits.B_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'B' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('B', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code B. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code B. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code B. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code B. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code B. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_h(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'h' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'h' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('h', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code h. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code h. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code h. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code h. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code h. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_h(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'h' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'h' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('h', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code h. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code h. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code h. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code h. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code h. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_H(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'H' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.H_max
			MinVal = arrayfunc.arraylimits.H_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'H' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('H', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code H. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code H. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code H. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code H. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code H. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_H(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'H' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.H_max
			MinVal = arrayfunc.arraylimits.H_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'H' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('H', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code H. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code H. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code H. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code H. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code H. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_i(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'i' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.i_max
			MinVal = arrayfunc.arraylimits.i_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'i' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('i', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code i. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code i. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code i. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code i. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code i. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_i(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'i' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.i_max
			MinVal = arrayfunc.arraylimits.i_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'i' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('i', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code i. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code i. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code i. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code i. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code i. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_I(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'I' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.I_max
			MinVal = arrayfunc.arraylimits.I_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'I' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('I', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code I. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code I. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code I. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code I. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code I. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_I(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'I' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.I_max
			MinVal = arrayfunc.arraylimits.I_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'I' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('I', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code I. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code I. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code I. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code I. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code I. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_l(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'l' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.l_max
			MinVal = arrayfunc.arraylimits.l_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'l' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('l', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code l. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code l. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code l. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code l. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code l. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_l(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'l' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.l_max
			MinVal = arrayfunc.arraylimits.l_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'l' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('l', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code l. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code l. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code l. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code l. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code l. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_L(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'L' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.L_max
			MinVal = arrayfunc.arraylimits.L_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'L' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('L', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code L. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code L. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code L. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code L. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code L. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_L(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'L' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.L_max
			MinVal = arrayfunc.arraylimits.L_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'L' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('L', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code L. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code L. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code L. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code L. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code L. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_q(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'q' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.q_max
			MinVal = arrayfunc.arraylimits.q_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'q' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('q', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code q. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code q. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code q. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code q. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code q. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_q(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'q' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.q_max
			MinVal = arrayfunc.arraylimits.q_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'q' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('q', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code q. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code q. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code q. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code q. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code q. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_Q(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'Q' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.Q_max
			MinVal = arrayfunc.arraylimits.Q_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'Q' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('Q', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code Q. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code Q. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code Q. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code Q. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code Q. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_Q(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'Q' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.Q_max
			MinVal = arrayfunc.arraylimits.Q_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'Q' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('Q', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code Q. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code Q. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code Q. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code Q. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code Q. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_f(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'f' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.f_max
			MinVal = arrayfunc.arraylimits.f_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'f' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('f', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code f. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code f. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code f. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code f. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code f. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_f(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'f' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.f_max
			MinVal = arrayfunc.arraylimits.f_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'f' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('f', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code f. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code f. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code f. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code f. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code f. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_even_d(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'd' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.d_max
			MinVal = arrayfunc.arraylimits.d_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'd' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('d', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code d. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code d. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code d. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code d. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code d. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_general_odd_d(unittest.TestCase):
	"""Test asum for basic general function operation.
	op_template_general
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# The size of the test arrays. The default length is an even
		# number so that if fits entirely within SIMD registers.
		arraylength = 96

		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arraylength = arraylength + 1


		# For floating point data, limit the test data to the same range
		# as smaller integer. This is to avoid problems with loss of
		# precision when adding FP numbers of widely different sizes. 
		if 'd' in ('f', 'd'):
			MaxVal = arrayfunc.arraylimits.h_max
			MinVal = arrayfunc.arraylimits.h_min
		else:
			MaxVal = arrayfunc.arraylimits.d_max
			MinVal = arrayfunc.arraylimits.d_min


		# The test values for the largest integer array types need to be
		# scaled down more to prevent integer overflow.
		if 'd' in ('L', 'Q'):
			testscale = 100
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
		self.gentest = array.array('d', [x for x,y in zip(itertools.cycle(testdata), range(arraylength))])


	########################################################
	def test_asum_general_function_A1(self):
		"""Test asum  - Array code d. General test.
		"""
		result = arrayfunc.asum(self.gentest)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_B1(self):
		"""Test asum  - Array code d. Test optional maxlen parameter.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50)
		self.assertEqual(result, sum(self.gentest[:50]))


	########################################################
	def test_asum_general_function_C1(self):
		"""Test asum  - Array code d. Test optional matherrors parameter.
		"""
		result = arrayfunc.asum(self.gentest, matherrors=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_D1(self):
		"""Test asum  - Array code d. Test optional nosimd parameter.
		"""
		result = arrayfunc.asum(self.gentest, nosimd=True)
		self.assertEqual(result, sum(self.gentest))


	########################################################
	def test_asum_general_function_E1(self):
		"""Test asum  - Array code d. Test optional maxlen, matherrors, nosimd parameters together.
		"""
		result = arrayfunc.asum(self.gentest, maxlen=50, nosimd=True, matherrors=True)
		self.assertEqual(result, sum(self.gentest[:50]))



##############################################################################



##############################################################################
class asum_parameter_b(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.b_max
		MinVal = arrayfunc.arraylimits.b_min

		self.gentest = array.array('b', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code b. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code b. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code b. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code b. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code b. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code b. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code b. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code b. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_B(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.B_max
		MinVal = arrayfunc.arraylimits.B_min

		self.gentest = array.array('B', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code B. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code B. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code B. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code B. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code B. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code B. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code B. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code B. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_h(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.h_max
		MinVal = arrayfunc.arraylimits.h_min

		self.gentest = array.array('h', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code h. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code h. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code h. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code h. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code h. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code h. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code h. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code h. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_H(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.H_max
		MinVal = arrayfunc.arraylimits.H_min

		self.gentest = array.array('H', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code H. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code H. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code H. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code H. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code H. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code H. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code H. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code H. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_i(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.i_max
		MinVal = arrayfunc.arraylimits.i_min

		self.gentest = array.array('i', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code i. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code i. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code i. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code i. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code i. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code i. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code i. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code i. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_I(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.I_max
		MinVal = arrayfunc.arraylimits.I_min

		self.gentest = array.array('I', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code I. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code I. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code I. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code I. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code I. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code I. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code I. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code I. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_l(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.l_max
		MinVal = arrayfunc.arraylimits.l_min

		self.gentest = array.array('l', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code l. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code l. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code l. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code l. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code l. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code l. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code l. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code l. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_L(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.L_max
		MinVal = arrayfunc.arraylimits.L_min

		self.gentest = array.array('L', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code L. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code L. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code L. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code L. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code L. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code L. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code L. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code L. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_q(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.q_max
		MinVal = arrayfunc.arraylimits.q_min

		self.gentest = array.array('q', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code q. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code q. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code q. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code q. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code q. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code q. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code q. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code q. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_Q(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.Q_max
		MinVal = arrayfunc.arraylimits.Q_min

		self.gentest = array.array('Q', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code Q. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code Q. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code Q. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code Q. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code Q. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code Q. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code Q. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code Q. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_f(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.f_max
		MinVal = arrayfunc.arraylimits.f_min

		self.gentest = array.array('f', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code f. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code f. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code f. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code f. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code f. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code f. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code f. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code f. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################



##############################################################################
class asum_parameter_d(unittest.TestCase):
	"""Test asum for basic parameter tests.
	op_template_params
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		MaxVal = arrayfunc.arraylimits.d_max
		MinVal = arrayfunc.arraylimits.d_min

		self.gentest = array.array('d', [100] * arraylength)


	########################################################
	def test_asum_param_function_A1(self):
		"""Test asum  - Array code d. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_A2(self):
		"""Test asum  - Array code d. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum('xxxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum('xxxxx')


	########################################################
	def test_asum_param_function_B1(self):
		"""Test asum  - Array code d. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_asum_param_function_B2(self):
		"""Test asum  - Array code d. Test excess parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, 5, 2, 2, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, 2, 3)


	########################################################
	def test_asum_param_function_C1(self):
		"""Test asum  - Array code d. Test invalid keyword parameter name.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, xxxx=5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(self.gentest, xxxx=5)


	########################################################
	def test_asum_param_function_D1(self):
		"""Test asum  - Array code d. Test invalid maxlen keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, maxlen='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D2(self):
		"""Test asum  - Array code d. Test invalid matherrors keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, matherrors='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


	########################################################
	def test_asum_param_function_D3(self):
		"""Test asum  - Array code d. Test invalid nosimd keyword type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(self.gentest, nosimd='xxxx')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)


##############################################################################


##############################################################################
class asum_nonfinite_0_even_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 0
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_1_even_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 1
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_2_even_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 2
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_3_even_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 3
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_4_even_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 4
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_0_odd_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 0
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_1_odd_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 1
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_2_odd_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 2
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_3_odd_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 3
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_4_odd_arraysize_f(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 4
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('f', nanvaldatabase)
		self.data_inf = array.array('f',  infvaldatabase)
		self.data_ninf = array.array('f',  ninfvaldatabase)
		self.data_mixed = array.array('f',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code f. Test NaN data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code f. Test NaN data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code f. Test inf data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code f. Test inf data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code f. Test inf data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code f. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code f. Test Mixed data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code f. Test Mixed data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_0_even_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 0
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, even length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, even length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_1_even_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 1
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, even length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, even length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_2_even_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 2
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, even length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, even length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_3_even_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 3
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, even length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, even length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_4_even_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'even' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 4
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, even length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, even length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_0_odd_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 0
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, odd length, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, odd length array data shifted 0.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_1_odd_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 1
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, odd length, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, odd length array data shifted 1.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_2_odd_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 2
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, odd length, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, odd length array data shifted 2.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_3_odd_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 3
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, odd length, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, odd length array data shifted 3.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################

##############################################################################
class asum_nonfinite_4_odd_arraysize_d(unittest.TestCase):
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if 'odd' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0

		arraylength = 96 + arrayextension

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
		rotplaces = 4
		nanvaldata = nanvaldatabase[rotplaces:] + nanvaldatabase[:rotplaces]
		infvaldata = infvaldatabase[rotplaces:] + infvaldatabase[:rotplaces]
		ninfvaldata = ninfvaldatabase[rotplaces:] + ninfvaldatabase[:rotplaces]
		mixedvaldata = mixedvaldatabase[rotplaces:] + mixedvaldatabase[:rotplaces]


		# These are the test data arrays.
		self.data_nan = array.array('d', nanvaldatabase)
		self.data_inf = array.array('d',  infvaldatabase)
		self.data_ninf = array.array('d',  ninfvaldatabase)
		self.data_mixed = array.array('d',  mixedvaldatabase)




	########################################################
	def test_asum_nonfinite_nan_A1(self):
		"""Test asum  - Array code d. Test NaN data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)


	########################################################
	def test_asum_nonfinite_nan_A2(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_nan))


	########################################################
	def test_asum_nonfinite_nan_A3(self):
		"""Test asum  - Array code d. Test NaN data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_nan, matherrors=True)
		self.assertEqual(result, sum(self.data_nan))



	########################################################
	def test_asum_nonfinite_inf_B1(self):
		"""Test asum  - Array code d. Test inf data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)


	########################################################
	def test_asum_nonfinite_inf_B2(self):
		"""Test asum  - Array code d. Test inf data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_inf))


	########################################################
	def test_asum_nonfinite_inf_B3(self):
		"""Test asum  - Array code d. Test inf data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_inf, matherrors=True)
		self.assertEqual(result, sum(self.data_inf))



	########################################################
	def test_asum_nonfinite_ninf_C1(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


	########################################################
	def test_asum_nonfinite_ninf_C2(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_ninf))


	########################################################
	def test_asum_nonfinite_ninf_C3(self):
		"""Test asum  - Array code d. Test Negative Inf data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_ninf, matherrors=True)
		self.assertEqual(result, sum(self.data_ninf))



	########################################################
	def test_asum_nonfinite_mixed_D1(self):
		"""Test asum  - Array code d. Test Mixed data with error checking on, odd length, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_mixed)


	########################################################
	def test_asum_nonfinite_mixed_D2(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, no SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True, nosimd=True)
		self.assertEqual(result, sum(self.data_mixed))


	########################################################
	def test_asum_nonfinite_mixed_D3(self):
		"""Test asum  - Array code d. Test Mixed data with error checking off, with SIMD, odd length array data shifted 4.
		"""
		result = arrayfunc.asum(self.data_mixed, matherrors=True)
		self.assertEqual(result, sum(self.data_mixed))



##############################################################################


##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_0_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_1_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_2_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_3_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_4_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_0_L(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('L', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'L' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'L' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code L. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_1_L(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('L', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'L' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'L' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code L. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_2_L(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('L', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'L' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'L' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code L. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_3_L(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('L', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'L' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'L' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code L. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MaxVal_4_L(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('L', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'L' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'L' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code L. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code L. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_0_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_1_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_2_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_3_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_4_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_0_Q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('Q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'Q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'Q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_1_Q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('Q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'Q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'Q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_2_Q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('Q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'Q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'Q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_3_Q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('Q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'Q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'Q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_4_Q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('Q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'Q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'Q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code Q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_0_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_1_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_2_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_3_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_4_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_0_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_1_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_2_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_3_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MaxVal_4_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MaxVal, self.MaxVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MinVal_0_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MinVal_1_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MinVal_2_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MinVal_3_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################
# Whether this test can be peformed depends on the integer word sizes in for this architecture.
@unittest.skipIf(arrayfunc.arraylimits.L_max != arrayfunc.arraylimits.Q_max, 
		'Skip test if L integer is not equal to Q.')
class asum_overflow_MinVal_4_l(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('l', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'l' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'l' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code l. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code l. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_0_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_1_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_2_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_3_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_4_q(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('q', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'q' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'q' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code q. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code q. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_0_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_1_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_2_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_3_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_4_f(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('f', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'f' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'f' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code f. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	# There seems to be a problem with 32 bit Debian with array type 'f'.
	# Intermediate values can exceed the maximum array type value without
	# the value overflowing to infinity. This does not happen on x86_64, or
	# 32 bit ARM.
	@unittest.skipIf(('i686' in platform.machine()) and ('debian' in platform.version().lower()), 
			'Skip test if 32 bit x86 Debian float due to apparent bug on overflow.')
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code f. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_0_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 0
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 0.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 0.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_1_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 1
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 1.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 1.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_2_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 2
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 2.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 2.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_3_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 3
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 3.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 3.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


##############################################################################



##############################################################################

class asum_overflow_MinVal_4_d(unittest.TestCase):
	"""Test asum for numeric overflow.
	op_template_overflow
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		arraylength = 96

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		# Rotate the data around a bit to try different locations for overflow.
		# This tests how the SIMD operation will respond to the overflow happening
		# in different locations.
		rotplaces = 4
		basedata = ([1] * arraylength) + [self.MinVal, self.MinVal] + ([1] * arraylength)
		testbasedata = basedata[rotplaces:] + basedata[:rotplaces]

		# Test arrays.
		self.testdata = array.array('d', testbasedata)


	########################################################
	def sumwithoverflow(self, testvalues):
		"""Sum the array, while accounting for overflow with different
		data types.
		"""
		val = sum(testvalues)
		# Single precision floatinng point. Python's own native
		# format is double precision so we have to catch the overflow
		# using a compare.
		if 'd' == 'f':
			if val > arrayfunc.arraylimits.f_max:
				return math.inf
			elif val < arrayfunc.arraylimits.f_min:
				return -math.inf
			else:
				return val
		# Double precision floating point.
		elif 'd' == 'd':
			return val
		# Integer. The way that Python handles negative integers means
		# we can't simply 'and' this with a mask.
		else:
			return val % (self.MaxVal - self.MinVal + 1)


	########################################################
	def test_asum_overflow_A1(self):
		"""Test asum  - Array code d. Test for overflow with error checking enabled, array data shifted 4.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.testdata)


	########################################################
	
	def test_asum_overflow_B1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD enabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


	########################################################
	
	def test_asum_overflow_C1(self):
		"""Test asum  - Array code d. Test for overflow with error checking disabled and SIMD disabled (if present), array data shifted 4.
		"""
		result = arrayfunc.asum(self.testdata, matherrors=True, nosimd=True)
		self.assertEqual(result, self.sumwithoverflow(self.testdata))


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
			f.write('asum\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
