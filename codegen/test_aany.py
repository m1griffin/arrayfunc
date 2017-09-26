#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_aany.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     20-May-2014.
# Ver:      24-Sep-2017.
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
"""This conducts unit tests for aany.
"""

##############################################################################
import array
import itertools
import math
import operator
import platform

import unittest

import arrayfunc

##############################################################################

##############################################################################

# The following code is all auto-generated.



##############################################################################
class aany_operator_with_simd_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('b', datalisteven)
		self.dataodd = array.array('b', datalistodd)
		self.dataeven2 = array.array('b', datalisteven2)
		self.dataodd2 = array.array('b', datalistodd2)
		self.dataeven3 = array.array('b', datalisteven3)
		self.dataodd3 = array.array('b', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'b' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code b. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code b. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('b', datalisteven)
		self.dataodd = array.array('b', datalistodd)
		self.dataeven2 = array.array('b', datalisteven2)
		self.dataodd2 = array.array('b', datalistodd2)
		self.dataeven3 = array.array('b', datalisteven3)
		self.dataodd3 = array.array('b', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'b' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code b. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code b. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)
		self.dataeven2 = array.array('B', datalisteven2)
		self.dataodd2 = array.array('B', datalistodd2)
		self.dataeven3 = array.array('B', datalisteven3)
		self.dataodd3 = array.array('B', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'B' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code B. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code B. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)
		self.dataeven2 = array.array('B', datalisteven2)
		self.dataodd2 = array.array('B', datalistodd2)
		self.dataeven3 = array.array('B', datalisteven3)
		self.dataodd3 = array.array('B', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'B' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code B. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code B. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('h', datalisteven)
		self.dataodd = array.array('h', datalistodd)
		self.dataeven2 = array.array('h', datalisteven2)
		self.dataodd2 = array.array('h', datalistodd2)
		self.dataeven3 = array.array('h', datalisteven3)
		self.dataodd3 = array.array('h', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'h' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code h. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code h. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('h', datalisteven)
		self.dataodd = array.array('h', datalistodd)
		self.dataeven2 = array.array('h', datalisteven2)
		self.dataodd2 = array.array('h', datalistodd2)
		self.dataeven3 = array.array('h', datalisteven3)
		self.dataodd3 = array.array('h', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'h' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code h. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code h. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('H', datalisteven)
		self.dataodd = array.array('H', datalistodd)
		self.dataeven2 = array.array('H', datalisteven2)
		self.dataodd2 = array.array('H', datalistodd2)
		self.dataeven3 = array.array('H', datalisteven3)
		self.dataodd3 = array.array('H', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'H' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code H. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code H. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('H', datalisteven)
		self.dataodd = array.array('H', datalistodd)
		self.dataeven2 = array.array('H', datalisteven2)
		self.dataodd2 = array.array('H', datalistodd2)
		self.dataeven3 = array.array('H', datalisteven3)
		self.dataodd3 = array.array('H', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'H' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code H. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code H. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('i', datalisteven)
		self.dataodd = array.array('i', datalistodd)
		self.dataeven2 = array.array('i', datalisteven2)
		self.dataodd2 = array.array('i', datalistodd2)
		self.dataeven3 = array.array('i', datalisteven3)
		self.dataodd3 = array.array('i', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'i' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code i. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code i. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('i', datalisteven)
		self.dataodd = array.array('i', datalistodd)
		self.dataeven2 = array.array('i', datalisteven2)
		self.dataodd2 = array.array('i', datalistodd2)
		self.dataeven3 = array.array('i', datalisteven3)
		self.dataodd3 = array.array('i', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'i' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code i. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code i. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('I', datalisteven)
		self.dataodd = array.array('I', datalistodd)
		self.dataeven2 = array.array('I', datalisteven2)
		self.dataodd2 = array.array('I', datalistodd2)
		self.dataeven3 = array.array('I', datalisteven3)
		self.dataodd3 = array.array('I', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'I' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code I. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code I. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('I', datalisteven)
		self.dataodd = array.array('I', datalistodd)
		self.dataeven2 = array.array('I', datalisteven2)
		self.dataodd2 = array.array('I', datalistodd2)
		self.dataeven3 = array.array('I', datalisteven3)
		self.dataodd3 = array.array('I', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'I' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code I. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code I. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('l', datalisteven)
		self.dataodd = array.array('l', datalistodd)
		self.dataeven2 = array.array('l', datalisteven2)
		self.dataodd2 = array.array('l', datalistodd2)
		self.dataeven3 = array.array('l', datalisteven3)
		self.dataodd3 = array.array('l', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'l' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code l. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code l. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('l', datalisteven)
		self.dataodd = array.array('l', datalistodd)
		self.dataeven2 = array.array('l', datalisteven2)
		self.dataodd2 = array.array('l', datalistodd2)
		self.dataeven3 = array.array('l', datalisteven3)
		self.dataodd3 = array.array('l', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'l' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code l. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code l. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('L', datalisteven)
		self.dataodd = array.array('L', datalistodd)
		self.dataeven2 = array.array('L', datalisteven2)
		self.dataodd2 = array.array('L', datalistodd2)
		self.dataeven3 = array.array('L', datalisteven3)
		self.dataodd3 = array.array('L', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'L' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code L. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code L. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('L', datalisteven)
		self.dataodd = array.array('L', datalistodd)
		self.dataeven2 = array.array('L', datalisteven2)
		self.dataodd2 = array.array('L', datalistodd2)
		self.dataeven3 = array.array('L', datalisteven3)
		self.dataodd3 = array.array('L', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'L' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code L. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code L. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('q', datalisteven)
		self.dataodd = array.array('q', datalistodd)
		self.dataeven2 = array.array('q', datalisteven2)
		self.dataodd2 = array.array('q', datalistodd2)
		self.dataeven3 = array.array('q', datalisteven3)
		self.dataodd3 = array.array('q', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'q' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('q', datalisteven)
		self.dataodd = array.array('q', datalistodd)
		self.dataeven2 = array.array('q', datalisteven2)
		self.dataodd2 = array.array('q', datalistodd2)
		self.dataeven3 = array.array('q', datalisteven3)
		self.dataodd3 = array.array('q', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'q' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('Q', datalisteven)
		self.dataodd = array.array('Q', datalistodd)
		self.dataeven2 = array.array('Q', datalisteven2)
		self.dataodd2 = array.array('Q', datalistodd2)
		self.dataeven3 = array.array('Q', datalisteven3)
		self.dataodd3 = array.array('Q', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'Q' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code Q. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code Q. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('Q', datalisteven)
		self.dataodd = array.array('Q', datalistodd)
		self.dataeven2 = array.array('Q', datalisteven2)
		self.dataodd2 = array.array('Q', datalistodd2)
		self.dataeven3 = array.array('Q', datalisteven3)
		self.dataodd3 = array.array('Q', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'Q' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code Q. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code Q. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('f', datalisteven)
		self.dataodd = array.array('f', datalistodd)
		self.dataeven2 = array.array('f', datalisteven2)
		self.dataodd2 = array.array('f', datalistodd2)
		self.dataeven3 = array.array('f', datalisteven3)
		self.dataodd3 = array.array('f', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'f' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code f. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code f. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100.0 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('f', datalisteven)
		self.dataodd = array.array('f', datalistodd)
		self.dataeven2 = array.array('f', datalisteven2)
		self.dataodd2 = array.array('f', datalistodd2)
		self.dataeven3 = array.array('f', datalisteven3)
		self.dataodd3 = array.array('f', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'f' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code f. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code f. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100.0 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('d', datalisteven)
		self.dataodd = array.array('d', datalistodd)
		self.dataeven2 = array.array('d', datalisteven2)
		self.dataodd2 = array.array('d', datalistodd2)
		self.dataeven3 = array.array('d', datalisteven3)
		self.dataodd3 = array.array('d', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'd' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98.0 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code d. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100.0 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100.0 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code d. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100.0 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('d', datalisteven)
		self.dataodd = array.array('d', datalistodd)
		self.dataeven2 = array.array('d', datalisteven2)
		self.dataodd2 = array.array('d', datalistodd2)
		self.dataeven3 = array.array('d', datalisteven3)
		self.dataodd3 = array.array('d', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'd' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98.0 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code d. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100.0 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100.0 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code d. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100.0 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_with_simd_bytes(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)
		self.dataeven2 = array.array('B', datalisteven2)
		self.dataodd2 = array.array('B', datalistodd2)
		self.dataeven3 = array.array('B', datalisteven3)
		self.dataodd3 = array.array('B', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'bytes' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 )
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 )
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 )
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 )
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 )
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 )
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code bytes. General test even length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 )
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 )
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code bytes. General test odd length array with SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 )
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_operator_without_simd_bytes(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)
		self.dataeven2 = array.array('B', datalisteven2)
		self.dataodd2 = array.array('B', datalistodd2)
		self.dataeven3 = array.array('B', datalisteven3)
		self.dataodd3 = array.array('B', datalistodd3)


		# For bytes types, we need a non-array data type.
		if 'bytes' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98 , nosimd=True)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code bytes. General test even length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100 , nosimd=True)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100 , nosimd=True)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code bytes. General test odd length array without SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100 , nosimd=True)
		self.assertFalse(result)




##############################################################################


##############################################################################
class aany_parameter_b(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('b', list(range(97, 107)) * 10)
		self.dataempty = array.array('b')


		# For bytes types, we need a non-array data type.
		if 'b' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code b.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_B(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', list(range(97, 107)) * 10)
		self.dataempty = array.array('B')


		# For bytes types, we need a non-array data type.
		if 'B' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code B.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_h(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('h', list(range(97, 107)) * 10)
		self.dataempty = array.array('h')


		# For bytes types, we need a non-array data type.
		if 'h' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code h.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_H(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('H', list(range(97, 107)) * 10)
		self.dataempty = array.array('H')


		# For bytes types, we need a non-array data type.
		if 'H' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code H.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_i(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('i', list(range(97, 107)) * 10)
		self.dataempty = array.array('i')


		# For bytes types, we need a non-array data type.
		if 'i' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code i.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_I(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('I', list(range(97, 107)) * 10)
		self.dataempty = array.array('I')


		# For bytes types, we need a non-array data type.
		if 'I' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code I.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_l(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('l', list(range(97, 107)) * 10)
		self.dataempty = array.array('l')


		# For bytes types, we need a non-array data type.
		if 'l' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code l.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_L(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('L', list(range(97, 107)) * 10)
		self.dataempty = array.array('L')


		# For bytes types, we need a non-array data type.
		if 'L' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code L.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_q(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('q', list(range(97, 107)) * 10)
		self.dataempty = array.array('q')


		# For bytes types, we need a non-array data type.
		if 'q' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_Q(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('Q', list(range(97, 107)) * 10)
		self.dataempty = array.array('Q')


		# For bytes types, we need a non-array data type.
		if 'Q' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code Q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_f(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', list(range(97, 107)) * 10)
		self.dataempty = array.array('f')


		# For bytes types, we need a non-array data type.
		if 'f' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code f.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100.0)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100.0)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_parameter_d(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', list(range(97, 107)) * 10)
		self.dataempty = array.array('d')


		# For bytes types, we need a non-array data type.
		if 'd' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code d.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100.0)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100.0)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.0, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_overflow_b(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('b', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.b_min
		self.Maxval = arrayfunc.arraylimits.b_max

		# For bytes types, we need a non-array data type.
		if 'b' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code b.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_B(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max

		# For bytes types, we need a non-array data type.
		if 'B' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code B.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_h(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('h', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.h_min
		self.Maxval = arrayfunc.arraylimits.h_max

		# For bytes types, we need a non-array data type.
		if 'h' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code h.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_H(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('H', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.H_min
		self.Maxval = arrayfunc.arraylimits.H_max

		# For bytes types, we need a non-array data type.
		if 'H' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code H.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_i(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('i', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.i_min
		self.Maxval = arrayfunc.arraylimits.i_max

		# For bytes types, we need a non-array data type.
		if 'i' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code i.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_I(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('I', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.I_min
		self.Maxval = arrayfunc.arraylimits.I_max

		# For bytes types, we need a non-array data type.
		if 'I' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code I.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_l(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('l', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.l_min
		self.Maxval = arrayfunc.arraylimits.l_max

		# For bytes types, we need a non-array data type.
		if 'l' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code l.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_q(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('q', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.q_min
		self.Maxval = arrayfunc.arraylimits.q_max

		# For bytes types, we need a non-array data type.
		if 'q' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code q.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_f(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max

		# For bytes types, we need a non-array data type.
		if 'f' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal * 1.1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval * 1.1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_overflow_d(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max

		# For bytes types, we need a non-array data type.
		if 'd' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal * 1.1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval * 1.1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_parameter_bytes(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', list(range(97, 107)) * 10)
		self.dataempty = array.array('B')


		# For bytes types, we need a non-array data type.
		if 'bytes' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code bytes.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, 100)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code bytes.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, 100)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 'e')
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, 100, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################


##############################################################################
class aany_overflow_bytes(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', list(range(97, 107)) * 10)
		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max

		# For bytes types, we need a non-array data type.
		if 'bytes' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code bytes.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal - 1)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code bytes.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval + 1)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code bytes.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################


##############################################################################
class aany_nan_test01_f(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 0.0)

	########################################################
	def test_nan_val01_02_eq(self):
		"""Test eq with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 0.0)

	########################################################
	def test_nan_val01_03_eq(self):
		"""Test eq with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(0.0 == float('-inf'))


	########################################################
	def test_nan_val01_04_gt(self):
		"""Test gt with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 0.0)

	########################################################
	def test_nan_val01_05_gt(self):
		"""Test gt with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 0.0)

	########################################################
	def test_nan_val01_06_gt(self):
		"""Test gt with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 0.0)


	########################################################
	def test_nan_val01_07_gte(self):
		"""Test gte with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 0.0)

	########################################################
	def test_nan_val01_08_gte(self):
		"""Test gte with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 0.0)

	########################################################
	def test_nan_val01_09_gte(self):
		"""Test gte with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 0.0)


	########################################################
	def test_nan_val01_10_lt(self):
		"""Test lt with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 0.0)

	########################################################
	def test_nan_val01_11_lt(self):
		"""Test lt with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 0.0)

	########################################################
	def test_nan_val01_12_lt(self):
		"""Test lt with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 0.0)


	########################################################
	def test_nan_val01_13_lte(self):
		"""Test lte with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 0.0)

	########################################################
	def test_nan_val01_14_lte(self):
		"""Test lte with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 0.0)

	########################################################
	def test_nan_val01_15_lte(self):
		"""Test lte with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 0.0)


	########################################################
	def test_nan_val01_16_ne(self):
		"""Test ne with nan and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 0.0)

	########################################################
	def test_nan_val01_17_ne(self):
		"""Test ne with inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 0.0)

	########################################################
	def test_nan_val01_18_ne(self):
		"""Test ne with -inf and data 0.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 0.0)

##############################################################################


##############################################################################
class aany_nan_test02_f(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 100.0)

	########################################################
	def test_nan_val02_02_eq(self):
		"""Test eq with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 100.0)

	########################################################
	def test_nan_val02_03_eq(self):
		"""Test eq with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(100.0 == float('-inf'))


	########################################################
	def test_nan_val02_04_gt(self):
		"""Test gt with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 100.0)

	########################################################
	def test_nan_val02_05_gt(self):
		"""Test gt with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 100.0)

	########################################################
	def test_nan_val02_06_gt(self):
		"""Test gt with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 100.0)


	########################################################
	def test_nan_val02_07_gte(self):
		"""Test gte with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 100.0)

	########################################################
	def test_nan_val02_08_gte(self):
		"""Test gte with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 100.0)

	########################################################
	def test_nan_val02_09_gte(self):
		"""Test gte with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 100.0)


	########################################################
	def test_nan_val02_10_lt(self):
		"""Test lt with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 100.0)

	########################################################
	def test_nan_val02_11_lt(self):
		"""Test lt with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 100.0)

	########################################################
	def test_nan_val02_12_lt(self):
		"""Test lt with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 100.0)


	########################################################
	def test_nan_val02_13_lte(self):
		"""Test lte with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 100.0)

	########################################################
	def test_nan_val02_14_lte(self):
		"""Test lte with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 100.0)

	########################################################
	def test_nan_val02_15_lte(self):
		"""Test lte with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 100.0)


	########################################################
	def test_nan_val02_16_ne(self):
		"""Test ne with nan and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 100.0)

	########################################################
	def test_nan_val02_17_ne(self):
		"""Test ne with inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 100.0)

	########################################################
	def test_nan_val02_18_ne(self):
		"""Test ne with -inf and data 100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 100.0)

##############################################################################


##############################################################################
class aany_nan_test03_f(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == -100.0)

	########################################################
	def test_nan_val03_02_eq(self):
		"""Test eq with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == -100.0)

	########################################################
	def test_nan_val03_03_eq(self):
		"""Test eq with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(-100.0 == float('-inf'))


	########################################################
	def test_nan_val03_04_gt(self):
		"""Test gt with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > -100.0)

	########################################################
	def test_nan_val03_05_gt(self):
		"""Test gt with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > -100.0)

	########################################################
	def test_nan_val03_06_gt(self):
		"""Test gt with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > -100.0)


	########################################################
	def test_nan_val03_07_gte(self):
		"""Test gte with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= -100.0)

	########################################################
	def test_nan_val03_08_gte(self):
		"""Test gte with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= -100.0)

	########################################################
	def test_nan_val03_09_gte(self):
		"""Test gte with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= -100.0)


	########################################################
	def test_nan_val03_10_lt(self):
		"""Test lt with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < -100.0)

	########################################################
	def test_nan_val03_11_lt(self):
		"""Test lt with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < -100.0)

	########################################################
	def test_nan_val03_12_lt(self):
		"""Test lt with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < -100.0)


	########################################################
	def test_nan_val03_13_lte(self):
		"""Test lte with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= -100.0)

	########################################################
	def test_nan_val03_14_lte(self):
		"""Test lte with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= -100.0)

	########################################################
	def test_nan_val03_15_lte(self):
		"""Test lte with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= -100.0)


	########################################################
	def test_nan_val03_16_ne(self):
		"""Test ne with nan and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != -100.0)

	########################################################
	def test_nan_val03_17_ne(self):
		"""Test ne with inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != -100.0)

	########################################################
	def test_nan_val03_18_ne(self):
		"""Test ne with -inf and data -100.0 - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != -100.0)

##############################################################################


##############################################################################
class aany_nan_test04_f(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.MinVal)

	########################################################
	def test_nan_val04_02_eq(self):
		"""Test eq with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.MinVal)

	########################################################
	def test_nan_val04_03_eq(self):
		"""Test eq with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(self.MinVal == float('-inf'))


	########################################################
	def test_nan_val04_04_gt(self):
		"""Test gt with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.MinVal)

	########################################################
	def test_nan_val04_05_gt(self):
		"""Test gt with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.MinVal)

	########################################################
	def test_nan_val04_06_gt(self):
		"""Test gt with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.MinVal)


	########################################################
	def test_nan_val04_07_gte(self):
		"""Test gte with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.MinVal)

	########################################################
	def test_nan_val04_08_gte(self):
		"""Test gte with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.MinVal)

	########################################################
	def test_nan_val04_09_gte(self):
		"""Test gte with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.MinVal)


	########################################################
	def test_nan_val04_10_lt(self):
		"""Test lt with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.MinVal)

	########################################################
	def test_nan_val04_11_lt(self):
		"""Test lt with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.MinVal)

	########################################################
	def test_nan_val04_12_lt(self):
		"""Test lt with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.MinVal)


	########################################################
	def test_nan_val04_13_lte(self):
		"""Test lte with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.MinVal)

	########################################################
	def test_nan_val04_14_lte(self):
		"""Test lte with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.MinVal)

	########################################################
	def test_nan_val04_15_lte(self):
		"""Test lte with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.MinVal)


	########################################################
	def test_nan_val04_16_ne(self):
		"""Test ne with nan and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.MinVal)

	########################################################
	def test_nan_val04_17_ne(self):
		"""Test ne with inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.MinVal)

	########################################################
	def test_nan_val04_18_ne(self):
		"""Test ne with -inf and data self.MinVal - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.MinVal)

##############################################################################


##############################################################################
class aany_nan_test05_f(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.Maxval)

	########################################################
	def test_nan_val05_02_eq(self):
		"""Test eq with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.Maxval)

	########################################################
	def test_nan_val05_03_eq(self):
		"""Test eq with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(self.Maxval == float('-inf'))


	########################################################
	def test_nan_val05_04_gt(self):
		"""Test gt with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.Maxval)

	########################################################
	def test_nan_val05_05_gt(self):
		"""Test gt with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.Maxval)

	########################################################
	def test_nan_val05_06_gt(self):
		"""Test gt with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.Maxval)


	########################################################
	def test_nan_val05_07_gte(self):
		"""Test gte with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.Maxval)

	########################################################
	def test_nan_val05_08_gte(self):
		"""Test gte with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.Maxval)

	########################################################
	def test_nan_val05_09_gte(self):
		"""Test gte with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.Maxval)


	########################################################
	def test_nan_val05_10_lt(self):
		"""Test lt with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.Maxval)

	########################################################
	def test_nan_val05_11_lt(self):
		"""Test lt with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.Maxval)

	########################################################
	def test_nan_val05_12_lt(self):
		"""Test lt with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.Maxval)


	########################################################
	def test_nan_val05_13_lte(self):
		"""Test lte with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.Maxval)

	########################################################
	def test_nan_val05_14_lte(self):
		"""Test lte with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.Maxval)

	########################################################
	def test_nan_val05_15_lte(self):
		"""Test lte with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.Maxval)


	########################################################
	def test_nan_val05_16_ne(self):
		"""Test ne with nan and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.Maxval)

	########################################################
	def test_nan_val05_17_ne(self):
		"""Test ne with inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.Maxval)

	########################################################
	def test_nan_val05_18_ne(self):
		"""Test ne with -inf and data self.Maxval - Array code f.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.Maxval)

##############################################################################


##############################################################################
class aany_nan_test01_d(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 0.0)

	########################################################
	def test_nan_val01_02_eq(self):
		"""Test eq with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 0.0)

	########################################################
	def test_nan_val01_03_eq(self):
		"""Test eq with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(0.0 == float('-inf'))


	########################################################
	def test_nan_val01_04_gt(self):
		"""Test gt with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 0.0)

	########################################################
	def test_nan_val01_05_gt(self):
		"""Test gt with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 0.0)

	########################################################
	def test_nan_val01_06_gt(self):
		"""Test gt with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 0.0)


	########################################################
	def test_nan_val01_07_gte(self):
		"""Test gte with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 0.0)

	########################################################
	def test_nan_val01_08_gte(self):
		"""Test gte with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 0.0)

	########################################################
	def test_nan_val01_09_gte(self):
		"""Test gte with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 0.0)


	########################################################
	def test_nan_val01_10_lt(self):
		"""Test lt with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 0.0)

	########################################################
	def test_nan_val01_11_lt(self):
		"""Test lt with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 0.0)

	########################################################
	def test_nan_val01_12_lt(self):
		"""Test lt with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 0.0)


	########################################################
	def test_nan_val01_13_lte(self):
		"""Test lte with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 0.0)

	########################################################
	def test_nan_val01_14_lte(self):
		"""Test lte with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, 0.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 0.0)

	########################################################
	def test_nan_val01_15_lte(self):
		"""Test lte with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 0.0)


	########################################################
	def test_nan_val01_16_ne(self):
		"""Test ne with nan and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 0.0)

	########################################################
	def test_nan_val01_17_ne(self):
		"""Test ne with inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 0.0)

	########################################################
	def test_nan_val01_18_ne(self):
		"""Test ne with -inf and data 0.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, 0.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 0.0)

##############################################################################


##############################################################################
class aany_nan_test02_d(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == 100.0)

	########################################################
	def test_nan_val02_02_eq(self):
		"""Test eq with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == 100.0)

	########################################################
	def test_nan_val02_03_eq(self):
		"""Test eq with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(100.0 == float('-inf'))


	########################################################
	def test_nan_val02_04_gt(self):
		"""Test gt with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > 100.0)

	########################################################
	def test_nan_val02_05_gt(self):
		"""Test gt with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > 100.0)

	########################################################
	def test_nan_val02_06_gt(self):
		"""Test gt with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > 100.0)


	########################################################
	def test_nan_val02_07_gte(self):
		"""Test gte with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= 100.0)

	########################################################
	def test_nan_val02_08_gte(self):
		"""Test gte with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= 100.0)

	########################################################
	def test_nan_val02_09_gte(self):
		"""Test gte with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= 100.0)


	########################################################
	def test_nan_val02_10_lt(self):
		"""Test lt with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < 100.0)

	########################################################
	def test_nan_val02_11_lt(self):
		"""Test lt with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < 100.0)

	########################################################
	def test_nan_val02_12_lt(self):
		"""Test lt with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < 100.0)


	########################################################
	def test_nan_val02_13_lte(self):
		"""Test lte with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= 100.0)

	########################################################
	def test_nan_val02_14_lte(self):
		"""Test lte with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, 100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= 100.0)

	########################################################
	def test_nan_val02_15_lte(self):
		"""Test lte with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= 100.0)


	########################################################
	def test_nan_val02_16_ne(self):
		"""Test ne with nan and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != 100.0)

	########################################################
	def test_nan_val02_17_ne(self):
		"""Test ne with inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != 100.0)

	########################################################
	def test_nan_val02_18_ne(self):
		"""Test ne with -inf and data 100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, 100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != 100.0)

##############################################################################


##############################################################################
class aany_nan_test03_d(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') == -100.0)

	########################################################
	def test_nan_val03_02_eq(self):
		"""Test eq with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') == -100.0)

	########################################################
	def test_nan_val03_03_eq(self):
		"""Test eq with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(-100.0 == float('-inf'))


	########################################################
	def test_nan_val03_04_gt(self):
		"""Test gt with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') > -100.0)

	########################################################
	def test_nan_val03_05_gt(self):
		"""Test gt with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') > -100.0)

	########################################################
	def test_nan_val03_06_gt(self):
		"""Test gt with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > -100.0)


	########################################################
	def test_nan_val03_07_gte(self):
		"""Test gte with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= -100.0)

	########################################################
	def test_nan_val03_08_gte(self):
		"""Test gte with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= -100.0)

	########################################################
	def test_nan_val03_09_gte(self):
		"""Test gte with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= -100.0)


	########################################################
	def test_nan_val03_10_lt(self):
		"""Test lt with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') < -100.0)

	########################################################
	def test_nan_val03_11_lt(self):
		"""Test lt with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') < -100.0)

	########################################################
	def test_nan_val03_12_lt(self):
		"""Test lt with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < -100.0)


	########################################################
	def test_nan_val03_13_lte(self):
		"""Test lte with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= -100.0)

	########################################################
	def test_nan_val03_14_lte(self):
		"""Test lte with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, -100.0)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= -100.0)

	########################################################
	def test_nan_val03_15_lte(self):
		"""Test lte with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= -100.0)


	########################################################
	def test_nan_val03_16_ne(self):
		"""Test ne with nan and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('nan') != -100.0)

	########################################################
	def test_nan_val03_17_ne(self):
		"""Test ne with inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('inf') != -100.0)

	########################################################
	def test_nan_val03_18_ne(self):
		"""Test ne with -inf and data -100.0 - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, -100.0)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != -100.0)

##############################################################################


##############################################################################
class aany_nan_test04_d(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.MinVal)

	########################################################
	def test_nan_val04_02_eq(self):
		"""Test eq with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.MinVal)

	########################################################
	def test_nan_val04_03_eq(self):
		"""Test eq with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(self.MinVal == float('-inf'))


	########################################################
	def test_nan_val04_04_gt(self):
		"""Test gt with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.MinVal)

	########################################################
	def test_nan_val04_05_gt(self):
		"""Test gt with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.MinVal)

	########################################################
	def test_nan_val04_06_gt(self):
		"""Test gt with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.MinVal)


	########################################################
	def test_nan_val04_07_gte(self):
		"""Test gte with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.MinVal)

	########################################################
	def test_nan_val04_08_gte(self):
		"""Test gte with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.MinVal)

	########################################################
	def test_nan_val04_09_gte(self):
		"""Test gte with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.MinVal)


	########################################################
	def test_nan_val04_10_lt(self):
		"""Test lt with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.MinVal)

	########################################################
	def test_nan_val04_11_lt(self):
		"""Test lt with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.MinVal)

	########################################################
	def test_nan_val04_12_lt(self):
		"""Test lt with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.MinVal)


	########################################################
	def test_nan_val04_13_lte(self):
		"""Test lte with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.MinVal)

	########################################################
	def test_nan_val04_14_lte(self):
		"""Test lte with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, self.MinVal)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.MinVal)

	########################################################
	def test_nan_val04_15_lte(self):
		"""Test lte with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.MinVal)


	########################################################
	def test_nan_val04_16_ne(self):
		"""Test ne with nan and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.MinVal)

	########################################################
	def test_nan_val04_17_ne(self):
		"""Test ne with inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.MinVal)

	########################################################
	def test_nan_val04_18_ne(self):
		"""Test ne with -inf and data self.MinVal - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, self.MinVal)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.MinVal)

##############################################################################


##############################################################################
class aany_nan_test05_d(unittest.TestCase):
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
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') == self.Maxval)

	########################################################
	def test_nan_val05_02_eq(self):
		"""Test eq with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') == self.Maxval)

	########################################################
	def test_nan_val05_03_eq(self):
		"""Test eq with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(self.Maxval == float('-inf'))


	########################################################
	def test_nan_val05_04_gt(self):
		"""Test gt with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') > self.Maxval)

	########################################################
	def test_nan_val05_05_gt(self):
		"""Test gt with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') > self.Maxval)

	########################################################
	def test_nan_val05_06_gt(self):
		"""Test gt with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > self.Maxval)


	########################################################
	def test_nan_val05_07_gte(self):
		"""Test gte with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= self.Maxval)

	########################################################
	def test_nan_val05_08_gte(self):
		"""Test gte with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= self.Maxval)

	########################################################
	def test_nan_val05_09_gte(self):
		"""Test gte with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= self.Maxval)


	########################################################
	def test_nan_val05_10_lt(self):
		"""Test lt with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') < self.Maxval)

	########################################################
	def test_nan_val05_11_lt(self):
		"""Test lt with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') < self.Maxval)

	########################################################
	def test_nan_val05_12_lt(self):
		"""Test lt with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < self.Maxval)


	########################################################
	def test_nan_val05_13_lte(self):
		"""Test lte with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= self.Maxval)

	########################################################
	def test_nan_val05_14_lte(self):
		"""Test lte with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, self.Maxval)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= self.Maxval)

	########################################################
	def test_nan_val05_15_lte(self):
		"""Test lte with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= self.Maxval)


	########################################################
	def test_nan_val05_16_ne(self):
		"""Test ne with nan and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('nan') != self.Maxval)

	########################################################
	def test_nan_val05_17_ne(self):
		"""Test ne with inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('inf') != self.Maxval)

	########################################################
	def test_nan_val05_18_ne(self):
		"""Test ne with -inf and data self.Maxval - Array code d.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, self.Maxval)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != self.Maxval)

##############################################################################


##############################################################################
class aany_nanparam_f(unittest.TestCase):
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
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('nan'))

	########################################################
	def test_nanparam_02_inf(self):
		"""Test parameter inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('inf'))

	########################################################
	def test_nanparam_03_ninf(self):
		"""Test parameter negative inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('-inf'))


##############################################################################


##############################################################################
class aany_nanparam_d(unittest.TestCase):
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
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('nan'))

	########################################################
	def test_nanparam_02_inf(self):
		"""Test parameter inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('inf'))

	########################################################
	def test_nanparam_03_ninf(self):
		"""Test parameter negative inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('-inf'))


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
			f.write('

')
			f.write('aany

')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
