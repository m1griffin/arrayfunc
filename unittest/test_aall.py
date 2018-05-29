#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_aall.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     20-May-2014.
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
"""This conducts unit tests for aall.
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
class aall_operator_with_simd_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('b', datalisteven)
		self.dataodd = array.array('b', datalistodd)
		self.dataeven2 = array.array('b', datalisteven2)
		self.dataodd2 = array.array('b', datalistodd2)
		self.dataeven3 = array.array('b', datalisteven3)
		self.dataodd3 = array.array('b', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('b', datalisteven)
		self.dataodd = array.array('b', datalistodd)
		self.dataeven2 = array.array('b', datalisteven2)
		self.dataodd2 = array.array('b', datalistodd2)
		self.dataeven3 = array.array('b', datalisteven3)
		self.dataodd3 = array.array('b', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)
		self.dataeven2 = array.array('B', datalisteven2)
		self.dataodd2 = array.array('B', datalistodd2)
		self.dataeven3 = array.array('B', datalisteven3)
		self.dataodd3 = array.array('B', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)
		self.dataeven2 = array.array('B', datalisteven2)
		self.dataodd2 = array.array('B', datalistodd2)
		self.dataeven3 = array.array('B', datalisteven3)
		self.dataodd3 = array.array('B', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('h', datalisteven)
		self.dataodd = array.array('h', datalistodd)
		self.dataeven2 = array.array('h', datalisteven2)
		self.dataodd2 = array.array('h', datalistodd2)
		self.dataeven3 = array.array('h', datalisteven3)
		self.dataodd3 = array.array('h', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('h', datalisteven)
		self.dataodd = array.array('h', datalistodd)
		self.dataeven2 = array.array('h', datalisteven2)
		self.dataodd2 = array.array('h', datalistodd2)
		self.dataeven3 = array.array('h', datalisteven3)
		self.dataodd3 = array.array('h', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('H', datalisteven)
		self.dataodd = array.array('H', datalistodd)
		self.dataeven2 = array.array('H', datalisteven2)
		self.dataodd2 = array.array('H', datalistodd2)
		self.dataeven3 = array.array('H', datalisteven3)
		self.dataodd3 = array.array('H', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('H', datalisteven)
		self.dataodd = array.array('H', datalistodd)
		self.dataeven2 = array.array('H', datalisteven2)
		self.dataodd2 = array.array('H', datalistodd2)
		self.dataeven3 = array.array('H', datalisteven3)
		self.dataodd3 = array.array('H', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('i', datalisteven)
		self.dataodd = array.array('i', datalistodd)
		self.dataeven2 = array.array('i', datalisteven2)
		self.dataodd2 = array.array('i', datalistodd2)
		self.dataeven3 = array.array('i', datalisteven3)
		self.dataodd3 = array.array('i', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('i', datalisteven)
		self.dataodd = array.array('i', datalistodd)
		self.dataeven2 = array.array('i', datalisteven2)
		self.dataodd2 = array.array('i', datalistodd2)
		self.dataeven3 = array.array('i', datalisteven3)
		self.dataodd3 = array.array('i', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('I', datalisteven)
		self.dataodd = array.array('I', datalistodd)
		self.dataeven2 = array.array('I', datalisteven2)
		self.dataodd2 = array.array('I', datalistodd2)
		self.dataeven3 = array.array('I', datalisteven3)
		self.dataodd3 = array.array('I', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('I', datalisteven)
		self.dataodd = array.array('I', datalistodd)
		self.dataeven2 = array.array('I', datalisteven2)
		self.dataodd2 = array.array('I', datalistodd2)
		self.dataeven3 = array.array('I', datalisteven3)
		self.dataodd3 = array.array('I', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('l', datalisteven)
		self.dataodd = array.array('l', datalistodd)
		self.dataeven2 = array.array('l', datalisteven2)
		self.dataodd2 = array.array('l', datalistodd2)
		self.dataeven3 = array.array('l', datalisteven3)
		self.dataodd3 = array.array('l', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('l', datalisteven)
		self.dataodd = array.array('l', datalistodd)
		self.dataeven2 = array.array('l', datalisteven2)
		self.dataodd2 = array.array('l', datalistodd2)
		self.dataeven3 = array.array('l', datalisteven3)
		self.dataodd3 = array.array('l', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('L', datalisteven)
		self.dataodd = array.array('L', datalistodd)
		self.dataeven2 = array.array('L', datalisteven2)
		self.dataodd2 = array.array('L', datalistodd2)
		self.dataeven3 = array.array('L', datalisteven3)
		self.dataodd3 = array.array('L', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('L', datalisteven)
		self.dataodd = array.array('L', datalistodd)
		self.dataeven2 = array.array('L', datalisteven2)
		self.dataodd2 = array.array('L', datalistodd2)
		self.dataeven3 = array.array('L', datalisteven3)
		self.dataodd3 = array.array('L', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('q', datalisteven)
		self.dataodd = array.array('q', datalistodd)
		self.dataeven2 = array.array('q', datalisteven2)
		self.dataodd2 = array.array('q', datalistodd2)
		self.dataeven3 = array.array('q', datalisteven3)
		self.dataodd3 = array.array('q', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('q', datalisteven)
		self.dataodd = array.array('q', datalistodd)
		self.dataeven2 = array.array('q', datalisteven2)
		self.dataodd2 = array.array('q', datalistodd2)
		self.dataeven3 = array.array('q', datalisteven3)
		self.dataodd3 = array.array('q', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('Q', datalisteven)
		self.dataodd = array.array('Q', datalistodd)
		self.dataeven2 = array.array('Q', datalisteven2)
		self.dataodd2 = array.array('Q', datalistodd2)
		self.dataeven3 = array.array('Q', datalisteven3)
		self.dataodd3 = array.array('Q', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('Q', datalisteven)
		self.dataodd = array.array('Q', datalistodd)
		self.dataeven2 = array.array('Q', datalisteven2)
		self.dataodd2 = array.array('Q', datalistodd2)
		self.dataeven3 = array.array('Q', datalisteven3)
		self.dataodd3 = array.array('Q', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('f', datalisteven)
		self.dataodd = array.array('f', datalistodd)
		self.dataeven2 = array.array('f', datalisteven2)
		self.dataodd2 = array.array('f', datalistodd2)
		self.dataeven3 = array.array('f', datalisteven3)
		self.dataodd3 = array.array('f', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100.0 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('f', datalisteven)
		self.dataodd = array.array('f', datalistodd)
		self.dataeven2 = array.array('f', datalisteven2)
		self.dataodd2 = array.array('f', datalistodd2)
		self.dataeven3 = array.array('f', datalisteven3)
		self.dataodd3 = array.array('f', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100.0 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_with_simd_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('d', datalisteven)
		self.dataodd = array.array('d', datalistodd)
		self.dataeven2 = array.array('d', datalisteven2)
		self.dataodd2 = array.array('d', datalistodd2)
		self.dataeven3 = array.array('d', datalisteven3)
		self.dataodd3 = array.array('d', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100.0 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_operator_without_simd_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [100] * 160

		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		datalisteven3 = [100] * 160
		datalisteven3[-1] = 101

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(100)

		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		datalistodd3 = [100] * 160
		datalistodd3.append(101)


		self.dataeven = array.array('d', datalisteven)
		self.dataodd = array.array('d', datalistodd)
		self.dataeven2 = array.array('d', datalisteven2)
		self.dataodd2 = array.array('d', datalistodd2)
		self.dataeven3 = array.array('d', datalisteven3)
		self.dataodd3 = array.array('d', datalistodd3)



	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataeven2, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('==', self.dataodd2, 100.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataeven3, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>', self.dataodd3, 100.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataeven2, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('>=', self.dataodd2, 100.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataeven, 98.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<', self.dataodd, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataeven3, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('<=', self.dataodd3, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataeven2, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aall('!=', self.dataodd2, 100.0 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aall_parameter_b(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('b', [100]*100)
		self.dataempty = array.array('b')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code b.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_B(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', [100]*100)
		self.dataempty = array.array('B')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code B.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_h(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('h', [100]*100)
		self.dataempty = array.array('h')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code h.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_H(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('H', [100]*100)
		self.dataempty = array.array('H')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code H.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_i(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('i', [100]*100)
		self.dataempty = array.array('i')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code i.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_I(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('I', [100]*100)
		self.dataempty = array.array('I')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code I.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_l(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('l', [100]*100)
		self.dataempty = array.array('l')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code l.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_L(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('L', [100]*100)
		self.dataempty = array.array('L')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code L.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_q(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('q', [100]*100)
		self.dataempty = array.array('q')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_Q(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('Q', [100]*100)
		self.dataempty = array.array('Q')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code Q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_f(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [100.0]*100)
		self.dataempty = array.array('f')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code f.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100.0)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100.0)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_parameter_d(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [100.0]*100)
		self.dataempty = array.array('d')


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code d.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall('!', self.data, 100.0)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(62, self.data, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', 99, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall('==', self.dataempty, 100.0)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('==', self.data, 100.0, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################


##############################################################################
class aall_overflow_b(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('b', [100]*100)
		self.MinVal = arrayfunc.arraylimits.b_min
		self.Maxval = arrayfunc.arraylimits.b_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code b.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_B(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', [100]*100)
		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code B.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_h(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('h', [100]*100)
		self.MinVal = arrayfunc.arraylimits.h_min
		self.Maxval = arrayfunc.arraylimits.h_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code h.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_H(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('H', [100]*100)
		self.MinVal = arrayfunc.arraylimits.H_min
		self.Maxval = arrayfunc.arraylimits.H_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code H.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_i(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('i', [100]*100)
		self.MinVal = arrayfunc.arraylimits.i_min
		self.Maxval = arrayfunc.arraylimits.i_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code i.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_I(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('I', [100]*100)
		self.MinVal = arrayfunc.arraylimits.I_min
		self.Maxval = arrayfunc.arraylimits.I_max


	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code I.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_l(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('l', [100]*100)
		self.MinVal = arrayfunc.arraylimits.l_min
		self.Maxval = arrayfunc.arraylimits.l_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code l.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_q(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('q', [100]*100)
		self.MinVal = arrayfunc.arraylimits.q_min
		self.Maxval = arrayfunc.arraylimits.q_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code q.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_f(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [100.0]*100)
		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal * 1.1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval * 1.1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code f.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_overflow_d(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [100.0]*100)
		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.MinVal * 1.1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, self.Maxval * 1.1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code d.
		"""
		result = arrayfunc.aall('==', self.data, self.MinVal)
		result = arrayfunc.aall('==', self.data, self.Maxval)

##############################################################################


##############################################################################
class aall_nan_test01_f(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('f', [float('nan')]*100)
		self.data_inf = array.array('f', [float('inf')]*100)
		self.data_ninf = array.array('f', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max

	########################################################
	def test_nan_val01_01_eq(self):
		"""Test eq with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 0.0)

	########################################################
	def test_nan_val01_02_eq(self):
		"""Test eq with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 0.0)

	########################################################
	def test_nan_val01_03_eq(self):
		"""Test eq with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(0.0 == float('-inf'))


	########################################################
	def test_nan_val01_04_gt(self):
		"""Test gt with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 0.0)

	########################################################
	def test_nan_val01_05_gt(self):
		"""Test gt with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 0.0)

	########################################################
	def test_nan_val01_06_gt(self):
		"""Test gt with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 0.0)


	########################################################
	def test_nan_val01_07_gte(self):
		"""Test gte with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 0.0)

	########################################################
	def test_nan_val01_08_gte(self):
		"""Test gte with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 0.0)

	########################################################
	def test_nan_val01_09_gte(self):
		"""Test gte with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 0.0)


	########################################################
	def test_nan_val01_10_lt(self):
		"""Test lt with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 0.0)

	########################################################
	def test_nan_val01_11_lt(self):
		"""Test lt with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 0.0)

	########################################################
	def test_nan_val01_12_lt(self):
		"""Test lt with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 0.0)


	########################################################
	def test_nan_val01_13_lte(self):
		"""Test lte with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 0.0)

	########################################################
	def test_nan_val01_14_lte(self):
		"""Test lte with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 0.0)

	########################################################
	def test_nan_val01_15_lte(self):
		"""Test lte with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 0.0)


	########################################################
	def test_nan_val01_16_ne(self):
		"""Test ne with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_nan, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 0.0)

	########################################################
	def test_nan_val01_17_ne(self):
		"""Test ne with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 0.0)

	########################################################
	def test_nan_val01_18_ne(self):
		"""Test ne with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 0.0)

##############################################################################


##############################################################################
class aall_nan_test02_f(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('f', [float('nan')]*100)
		self.data_inf = array.array('f', [float('inf')]*100)
		self.data_ninf = array.array('f', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max

	########################################################
	def test_nan_val02_01_eq(self):
		"""Test eq with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 100.0)

	########################################################
	def test_nan_val02_02_eq(self):
		"""Test eq with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 100.0)

	########################################################
	def test_nan_val02_03_eq(self):
		"""Test eq with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(100.0 == float('-inf'))


	########################################################
	def test_nan_val02_04_gt(self):
		"""Test gt with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 100.0)

	########################################################
	def test_nan_val02_05_gt(self):
		"""Test gt with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 100.0)

	########################################################
	def test_nan_val02_06_gt(self):
		"""Test gt with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 100.0)


	########################################################
	def test_nan_val02_07_gte(self):
		"""Test gte with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 100.0)

	########################################################
	def test_nan_val02_08_gte(self):
		"""Test gte with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 100.0)

	########################################################
	def test_nan_val02_09_gte(self):
		"""Test gte with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 100.0)


	########################################################
	def test_nan_val02_10_lt(self):
		"""Test lt with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 100.0)

	########################################################
	def test_nan_val02_11_lt(self):
		"""Test lt with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 100.0)

	########################################################
	def test_nan_val02_12_lt(self):
		"""Test lt with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 100.0)


	########################################################
	def test_nan_val02_13_lte(self):
		"""Test lte with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 100.0)

	########################################################
	def test_nan_val02_14_lte(self):
		"""Test lte with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 100.0)

	########################################################
	def test_nan_val02_15_lte(self):
		"""Test lte with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 100.0)


	########################################################
	def test_nan_val02_16_ne(self):
		"""Test ne with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_nan, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 100.0)

	########################################################
	def test_nan_val02_17_ne(self):
		"""Test ne with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 100.0)

	########################################################
	def test_nan_val02_18_ne(self):
		"""Test ne with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 100.0)

##############################################################################


##############################################################################
class aall_nan_test03_f(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('f', [float('nan')]*100)
		self.data_inf = array.array('f', [float('inf')]*100)
		self.data_ninf = array.array('f', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max

	########################################################
	def test_nan_val03_01_eq(self):
		"""Test eq with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == -100.0)

	########################################################
	def test_nan_val03_02_eq(self):
		"""Test eq with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == -100.0)

	########################################################
	def test_nan_val03_03_eq(self):
		"""Test eq with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(-100.0 == float('-inf'))


	########################################################
	def test_nan_val03_04_gt(self):
		"""Test gt with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > -100.0)

	########################################################
	def test_nan_val03_05_gt(self):
		"""Test gt with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > -100.0)

	########################################################
	def test_nan_val03_06_gt(self):
		"""Test gt with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > -100.0)


	########################################################
	def test_nan_val03_07_gte(self):
		"""Test gte with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= -100.0)

	########################################################
	def test_nan_val03_08_gte(self):
		"""Test gte with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= -100.0)

	########################################################
	def test_nan_val03_09_gte(self):
		"""Test gte with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= -100.0)


	########################################################
	def test_nan_val03_10_lt(self):
		"""Test lt with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < -100.0)

	########################################################
	def test_nan_val03_11_lt(self):
		"""Test lt with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < -100.0)

	########################################################
	def test_nan_val03_12_lt(self):
		"""Test lt with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < -100.0)


	########################################################
	def test_nan_val03_13_lte(self):
		"""Test lte with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= -100.0)

	########################################################
	def test_nan_val03_14_lte(self):
		"""Test lte with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= -100.0)

	########################################################
	def test_nan_val03_15_lte(self):
		"""Test lte with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= -100.0)


	########################################################
	def test_nan_val03_16_ne(self):
		"""Test ne with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_nan, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != -100.0)

	########################################################
	def test_nan_val03_17_ne(self):
		"""Test ne with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != -100.0)

	########################################################
	def test_nan_val03_18_ne(self):
		"""Test ne with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != -100.0)

##############################################################################


##############################################################################
class aall_nan_test04_f(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('f', [float('nan')]*100)
		self.data_inf = array.array('f', [float('inf')]*100)
		self.data_ninf = array.array('f', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max

	########################################################
	def test_nan_val04_01_eq(self):
		"""Test eq with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.MinVal)

	########################################################
	def test_nan_val04_02_eq(self):
		"""Test eq with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.MinVal)

	########################################################
	def test_nan_val04_03_eq(self):
		"""Test eq with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(self.MinVal == float('-inf'))


	########################################################
	def test_nan_val04_04_gt(self):
		"""Test gt with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.MinVal)

	########################################################
	def test_nan_val04_05_gt(self):
		"""Test gt with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.MinVal)

	########################################################
	def test_nan_val04_06_gt(self):
		"""Test gt with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.MinVal)


	########################################################
	def test_nan_val04_07_gte(self):
		"""Test gte with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.MinVal)

	########################################################
	def test_nan_val04_08_gte(self):
		"""Test gte with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.MinVal)

	########################################################
	def test_nan_val04_09_gte(self):
		"""Test gte with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.MinVal)


	########################################################
	def test_nan_val04_10_lt(self):
		"""Test lt with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.MinVal)

	########################################################
	def test_nan_val04_11_lt(self):
		"""Test lt with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.MinVal)

	########################################################
	def test_nan_val04_12_lt(self):
		"""Test lt with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.MinVal)


	########################################################
	def test_nan_val04_13_lte(self):
		"""Test lte with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.MinVal)

	########################################################
	def test_nan_val04_14_lte(self):
		"""Test lte with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.MinVal)

	########################################################
	def test_nan_val04_15_lte(self):
		"""Test lte with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.MinVal)


	########################################################
	def test_nan_val04_16_ne(self):
		"""Test ne with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_nan, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.MinVal)

	########################################################
	def test_nan_val04_17_ne(self):
		"""Test ne with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.MinVal)

	########################################################
	def test_nan_val04_18_ne(self):
		"""Test ne with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.MinVal)

##############################################################################


##############################################################################
class aall_nan_test05_f(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('f', [float('nan')]*100)
		self.data_inf = array.array('f', [float('inf')]*100)
		self.data_ninf = array.array('f', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max

	########################################################
	def test_nan_val05_01_eq(self):
		"""Test eq with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.Maxval)

	########################################################
	def test_nan_val05_02_eq(self):
		"""Test eq with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.Maxval)

	########################################################
	def test_nan_val05_03_eq(self):
		"""Test eq with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('==', self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(self.Maxval == float('-inf'))


	########################################################
	def test_nan_val05_04_gt(self):
		"""Test gt with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.Maxval)

	########################################################
	def test_nan_val05_05_gt(self):
		"""Test gt with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.Maxval)

	########################################################
	def test_nan_val05_06_gt(self):
		"""Test gt with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('>', self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.Maxval)


	########################################################
	def test_nan_val05_07_gte(self):
		"""Test gte with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.Maxval)

	########################################################
	def test_nan_val05_08_gte(self):
		"""Test gte with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.Maxval)

	########################################################
	def test_nan_val05_09_gte(self):
		"""Test gte with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.Maxval)


	########################################################
	def test_nan_val05_10_lt(self):
		"""Test lt with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.Maxval)

	########################################################
	def test_nan_val05_11_lt(self):
		"""Test lt with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.Maxval)

	########################################################
	def test_nan_val05_12_lt(self):
		"""Test lt with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('<', self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.Maxval)


	########################################################
	def test_nan_val05_13_lte(self):
		"""Test lte with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.Maxval)

	########################################################
	def test_nan_val05_14_lte(self):
		"""Test lte with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.Maxval)

	########################################################
	def test_nan_val05_15_lte(self):
		"""Test lte with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.Maxval)


	########################################################
	def test_nan_val05_16_ne(self):
		"""Test ne with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_nan, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.Maxval)

	########################################################
	def test_nan_val05_17_ne(self):
		"""Test ne with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.Maxval)

	########################################################
	def test_nan_val05_18_ne(self):
		"""Test ne with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.Maxval)

##############################################################################


##############################################################################
class aall_nan_test01_d(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('d', [float('nan')]*100)
		self.data_inf = array.array('d', [float('inf')]*100)
		self.data_ninf = array.array('d', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max

	########################################################
	def test_nan_val01_01_eq(self):
		"""Test eq with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 0.0)

	########################################################
	def test_nan_val01_02_eq(self):
		"""Test eq with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 0.0)

	########################################################
	def test_nan_val01_03_eq(self):
		"""Test eq with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(0.0 == float('-inf'))


	########################################################
	def test_nan_val01_04_gt(self):
		"""Test gt with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 0.0)

	########################################################
	def test_nan_val01_05_gt(self):
		"""Test gt with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 0.0)

	########################################################
	def test_nan_val01_06_gt(self):
		"""Test gt with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 0.0)


	########################################################
	def test_nan_val01_07_gte(self):
		"""Test gte with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 0.0)

	########################################################
	def test_nan_val01_08_gte(self):
		"""Test gte with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 0.0)

	########################################################
	def test_nan_val01_09_gte(self):
		"""Test gte with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 0.0)


	########################################################
	def test_nan_val01_10_lt(self):
		"""Test lt with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 0.0)

	########################################################
	def test_nan_val01_11_lt(self):
		"""Test lt with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 0.0)

	########################################################
	def test_nan_val01_12_lt(self):
		"""Test lt with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 0.0)


	########################################################
	def test_nan_val01_13_lte(self):
		"""Test lte with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 0.0)

	########################################################
	def test_nan_val01_14_lte(self):
		"""Test lte with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 0.0)

	########################################################
	def test_nan_val01_15_lte(self):
		"""Test lte with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 0.0)


	########################################################
	def test_nan_val01_16_ne(self):
		"""Test ne with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_nan, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 0.0)

	########################################################
	def test_nan_val01_17_ne(self):
		"""Test ne with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 0.0)

	########################################################
	def test_nan_val01_18_ne(self):
		"""Test ne with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 0.0)

##############################################################################


##############################################################################
class aall_nan_test02_d(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('d', [float('nan')]*100)
		self.data_inf = array.array('d', [float('inf')]*100)
		self.data_ninf = array.array('d', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max

	########################################################
	def test_nan_val02_01_eq(self):
		"""Test eq with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 100.0)

	########################################################
	def test_nan_val02_02_eq(self):
		"""Test eq with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 100.0)

	########################################################
	def test_nan_val02_03_eq(self):
		"""Test eq with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(100.0 == float('-inf'))


	########################################################
	def test_nan_val02_04_gt(self):
		"""Test gt with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 100.0)

	########################################################
	def test_nan_val02_05_gt(self):
		"""Test gt with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 100.0)

	########################################################
	def test_nan_val02_06_gt(self):
		"""Test gt with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 100.0)


	########################################################
	def test_nan_val02_07_gte(self):
		"""Test gte with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 100.0)

	########################################################
	def test_nan_val02_08_gte(self):
		"""Test gte with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 100.0)

	########################################################
	def test_nan_val02_09_gte(self):
		"""Test gte with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 100.0)


	########################################################
	def test_nan_val02_10_lt(self):
		"""Test lt with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 100.0)

	########################################################
	def test_nan_val02_11_lt(self):
		"""Test lt with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 100.0)

	########################################################
	def test_nan_val02_12_lt(self):
		"""Test lt with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 100.0)


	########################################################
	def test_nan_val02_13_lte(self):
		"""Test lte with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 100.0)

	########################################################
	def test_nan_val02_14_lte(self):
		"""Test lte with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 100.0)

	########################################################
	def test_nan_val02_15_lte(self):
		"""Test lte with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 100.0)


	########################################################
	def test_nan_val02_16_ne(self):
		"""Test ne with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_nan, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 100.0)

	########################################################
	def test_nan_val02_17_ne(self):
		"""Test ne with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 100.0)

	########################################################
	def test_nan_val02_18_ne(self):
		"""Test ne with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 100.0)

##############################################################################


##############################################################################
class aall_nan_test03_d(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('d', [float('nan')]*100)
		self.data_inf = array.array('d', [float('inf')]*100)
		self.data_ninf = array.array('d', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max

	########################################################
	def test_nan_val03_01_eq(self):
		"""Test eq with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == -100.0)

	########################################################
	def test_nan_val03_02_eq(self):
		"""Test eq with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == -100.0)

	########################################################
	def test_nan_val03_03_eq(self):
		"""Test eq with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(-100.0 == float('-inf'))


	########################################################
	def test_nan_val03_04_gt(self):
		"""Test gt with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > -100.0)

	########################################################
	def test_nan_val03_05_gt(self):
		"""Test gt with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > -100.0)

	########################################################
	def test_nan_val03_06_gt(self):
		"""Test gt with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > -100.0)


	########################################################
	def test_nan_val03_07_gte(self):
		"""Test gte with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= -100.0)

	########################################################
	def test_nan_val03_08_gte(self):
		"""Test gte with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= -100.0)

	########################################################
	def test_nan_val03_09_gte(self):
		"""Test gte with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= -100.0)


	########################################################
	def test_nan_val03_10_lt(self):
		"""Test lt with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < -100.0)

	########################################################
	def test_nan_val03_11_lt(self):
		"""Test lt with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < -100.0)

	########################################################
	def test_nan_val03_12_lt(self):
		"""Test lt with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < -100.0)


	########################################################
	def test_nan_val03_13_lte(self):
		"""Test lte with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= -100.0)

	########################################################
	def test_nan_val03_14_lte(self):
		"""Test lte with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= -100.0)

	########################################################
	def test_nan_val03_15_lte(self):
		"""Test lte with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= -100.0)


	########################################################
	def test_nan_val03_16_ne(self):
		"""Test ne with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_nan, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != -100.0)

	########################################################
	def test_nan_val03_17_ne(self):
		"""Test ne with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != -100.0)

	########################################################
	def test_nan_val03_18_ne(self):
		"""Test ne with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != -100.0)

##############################################################################


##############################################################################
class aall_nan_test04_d(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('d', [float('nan')]*100)
		self.data_inf = array.array('d', [float('inf')]*100)
		self.data_ninf = array.array('d', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max

	########################################################
	def test_nan_val04_01_eq(self):
		"""Test eq with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.MinVal)

	########################################################
	def test_nan_val04_02_eq(self):
		"""Test eq with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.MinVal)

	########################################################
	def test_nan_val04_03_eq(self):
		"""Test eq with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(self.MinVal == float('-inf'))


	########################################################
	def test_nan_val04_04_gt(self):
		"""Test gt with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.MinVal)

	########################################################
	def test_nan_val04_05_gt(self):
		"""Test gt with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.MinVal)

	########################################################
	def test_nan_val04_06_gt(self):
		"""Test gt with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.MinVal)


	########################################################
	def test_nan_val04_07_gte(self):
		"""Test gte with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.MinVal)

	########################################################
	def test_nan_val04_08_gte(self):
		"""Test gte with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.MinVal)

	########################################################
	def test_nan_val04_09_gte(self):
		"""Test gte with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.MinVal)


	########################################################
	def test_nan_val04_10_lt(self):
		"""Test lt with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.MinVal)

	########################################################
	def test_nan_val04_11_lt(self):
		"""Test lt with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.MinVal)

	########################################################
	def test_nan_val04_12_lt(self):
		"""Test lt with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.MinVal)


	########################################################
	def test_nan_val04_13_lte(self):
		"""Test lte with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.MinVal)

	########################################################
	def test_nan_val04_14_lte(self):
		"""Test lte with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.MinVal)

	########################################################
	def test_nan_val04_15_lte(self):
		"""Test lte with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.MinVal)


	########################################################
	def test_nan_val04_16_ne(self):
		"""Test ne with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_nan, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.MinVal)

	########################################################
	def test_nan_val04_17_ne(self):
		"""Test ne with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.MinVal)

	########################################################
	def test_nan_val04_18_ne(self):
		"""Test ne with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.MinVal)

##############################################################################


##############################################################################
class aall_nan_test05_d(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('d', [float('nan')]*100)
		self.data_inf = array.array('d', [float('inf')]*100)
		self.data_ninf = array.array('d', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max

	########################################################
	def test_nan_val05_01_eq(self):
		"""Test eq with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.Maxval)

	########################################################
	def test_nan_val05_02_eq(self):
		"""Test eq with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.Maxval)

	########################################################
	def test_nan_val05_03_eq(self):
		"""Test eq with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('==', self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(self.Maxval == float('-inf'))


	########################################################
	def test_nan_val05_04_gt(self):
		"""Test gt with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.Maxval)

	########################################################
	def test_nan_val05_05_gt(self):
		"""Test gt with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.Maxval)

	########################################################
	def test_nan_val05_06_gt(self):
		"""Test gt with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('>', self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.Maxval)


	########################################################
	def test_nan_val05_07_gte(self):
		"""Test gte with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.Maxval)

	########################################################
	def test_nan_val05_08_gte(self):
		"""Test gte with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.Maxval)

	########################################################
	def test_nan_val05_09_gte(self):
		"""Test gte with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('>=', self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.Maxval)


	########################################################
	def test_nan_val05_10_lt(self):
		"""Test lt with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.Maxval)

	########################################################
	def test_nan_val05_11_lt(self):
		"""Test lt with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.Maxval)

	########################################################
	def test_nan_val05_12_lt(self):
		"""Test lt with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('<', self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.Maxval)


	########################################################
	def test_nan_val05_13_lte(self):
		"""Test lte with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.Maxval)

	########################################################
	def test_nan_val05_14_lte(self):
		"""Test lte with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.Maxval)

	########################################################
	def test_nan_val05_15_lte(self):
		"""Test lte with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('<=', self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.Maxval)


	########################################################
	def test_nan_val05_16_ne(self):
		"""Test ne with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_nan, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.Maxval)

	########################################################
	def test_nan_val05_17_ne(self):
		"""Test ne with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.Maxval)

	########################################################
	def test_nan_val05_18_ne(self):
		"""Test ne with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aall('!=', self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.Maxval)

##############################################################################


##############################################################################
class aall_nanparam_f(unittest.TestCase):
	"""Test for float parameter errors with nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [100.0]*100)


	########################################################
	def test_nanparam_01_nan(self):
		"""Test parameter nan  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, float('nan'))

	########################################################
	def test_nanparam_02_inf(self):
		"""Test parameter inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, float('inf'))

	########################################################
	def test_nanparam_03_ninf(self):
		"""Test parameter negative inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, float('-inf'))


##############################################################################


##############################################################################
class aall_nanparam_d(unittest.TestCase):
	"""Test for float parameter errors with nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [100.0]*100)


	########################################################
	def test_nanparam_01_nan(self):
		"""Test parameter nan  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, float('nan'))

	########################################################
	def test_nanparam_02_inf(self):
		"""Test parameter inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, float('inf'))

	########################################################
	def test_nanparam_03_ninf(self):
		"""Test parameter negative inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall('==', self.data, float('-inf'))


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
			f.write('aall\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
