#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_findindex.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     21-Jun-2014.
# Ver:      13-Jun-2018.
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
"""This conducts unit tests for findindex.
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
class findindex_operator_with_simd_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('b', datalisteven)
		self.dataodd = array.array('b', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.b_min
		self.Maxval = arrayfunc.arraylimits.b_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code b. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code b. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code b. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code b. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code b. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code b. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code b. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code b. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code b. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code b. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code b. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code b. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code b. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code b. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code b. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code b. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code b. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code b. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code b. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code b. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code b. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code b. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code b. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code b. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code b. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code b. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code b. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code b. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code b. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code b. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code b. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code b. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code b. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code b. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code b. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code b. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code b. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code b. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code b. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code b. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code b. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code b. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code b. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code b. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code b. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code b. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code b. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code b. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code b. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code b. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code b. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code b. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code b. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code b. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code b. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code b. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code b. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code b. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code b. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code b. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('b', datalisteven)
		self.dataodd = array.array('b', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.b_min
		self.Maxval = arrayfunc.arraylimits.b_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code b. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code b. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code b. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code b. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code b. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code b. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code b. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code b. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code b. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code b. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code b. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code b. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code b. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code b. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code b. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code b. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code b. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code b. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code b. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code b. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code b. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code b. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code b. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code b. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code b. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code b. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code b. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code b. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code b. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code b. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code b. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code b. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code b. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code b. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code b. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code b. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code b. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code b. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code b. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code b. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code b. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code b. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code b. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code b. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code b. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code b. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code b. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code b. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code b. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code b. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code b. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code b. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code b. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code b. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code b. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code b. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code b. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code b. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code b. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code b. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code B. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code B. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code B. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code B. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code B. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code B. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code B. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code B. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code B. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code B. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code B. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code B. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code B. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code B. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code B. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code B. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code B. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code B. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code B. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code B. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code B. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code B. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code B. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code B. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code B. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code B. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code B. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code B. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code B. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code B. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code B. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code B. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code B. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code B. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code B. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code B. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code B. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code B. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code B. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code B. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code B. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code B. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code B. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code B. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code B. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code B. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code B. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code B. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code B. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code B. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code B. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code B. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code B. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code B. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code B. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code B. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code B. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code B. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code B. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code B. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('B', datalisteven)
		self.dataodd = array.array('B', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code B. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code B. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code B. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code B. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code B. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code B. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code B. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code B. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code B. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code B. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code B. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code B. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code B. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code B. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code B. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code B. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code B. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code B. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code B. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code B. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code B. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code B. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code B. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code B. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code B. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code B. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code B. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code B. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code B. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code B. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code B. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code B. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code B. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code B. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code B. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code B. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code B. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code B. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code B. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code B. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code B. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code B. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code B. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code B. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code B. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code B. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code B. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code B. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code B. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code B. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code B. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code B. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code B. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code B. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code B. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code B. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code B. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code B. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code B. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code B. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('h', datalisteven)
		self.dataodd = array.array('h', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.h_min
		self.Maxval = arrayfunc.arraylimits.h_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code h. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code h. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code h. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code h. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code h. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code h. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code h. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code h. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code h. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code h. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code h. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code h. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code h. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code h. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code h. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code h. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code h. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code h. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code h. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code h. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code h. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code h. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code h. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code h. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code h. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code h. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code h. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code h. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code h. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code h. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code h. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code h. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code h. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code h. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code h. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code h. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code h. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code h. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code h. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code h. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code h. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code h. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code h. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code h. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code h. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code h. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code h. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code h. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code h. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code h. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code h. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code h. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code h. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code h. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code h. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code h. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code h. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code h. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code h. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code h. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('h', datalisteven)
		self.dataodd = array.array('h', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.h_min
		self.Maxval = arrayfunc.arraylimits.h_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code h. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code h. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code h. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code h. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code h. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code h. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code h. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code h. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code h. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code h. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code h. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code h. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code h. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code h. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code h. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code h. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code h. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code h. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code h. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code h. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code h. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code h. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code h. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code h. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code h. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code h. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code h. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code h. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code h. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code h. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code h. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code h. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code h. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code h. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code h. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code h. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code h. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code h. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code h. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code h. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code h. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code h. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code h. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code h. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code h. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code h. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code h. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code h. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code h. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code h. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code h. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code h. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code h. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code h. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code h. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code h. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code h. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code h. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code h. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code h. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('H', datalisteven)
		self.dataodd = array.array('H', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.H_min
		self.Maxval = arrayfunc.arraylimits.H_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code H. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code H. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code H. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code H. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code H. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code H. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code H. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code H. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code H. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code H. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code H. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code H. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code H. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code H. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code H. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code H. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code H. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code H. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code H. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code H. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code H. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code H. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code H. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code H. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code H. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code H. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code H. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code H. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code H. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code H. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code H. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code H. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code H. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code H. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code H. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code H. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code H. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code H. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code H. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code H. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code H. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code H. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code H. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code H. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code H. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code H. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code H. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code H. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code H. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code H. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code H. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code H. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code H. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code H. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code H. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code H. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code H. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code H. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code H. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code H. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('H', datalisteven)
		self.dataodd = array.array('H', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.H_min
		self.Maxval = arrayfunc.arraylimits.H_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code H. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code H. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code H. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code H. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code H. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code H. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code H. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code H. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code H. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code H. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code H. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code H. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code H. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code H. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code H. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code H. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code H. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code H. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code H. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code H. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code H. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code H. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code H. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code H. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code H. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code H. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code H. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code H. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code H. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code H. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code H. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code H. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code H. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code H. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code H. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code H. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code H. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code H. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code H. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code H. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code H. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code H. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code H. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code H. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code H. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code H. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code H. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code H. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code H. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code H. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code H. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code H. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code H. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code H. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code H. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code H. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code H. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code H. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code H. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code H. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('i', datalisteven)
		self.dataodd = array.array('i', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.i_min
		self.Maxval = arrayfunc.arraylimits.i_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code i. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code i. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code i. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code i. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code i. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code i. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code i. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code i. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code i. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code i. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code i. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code i. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code i. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code i. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code i. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code i. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code i. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code i. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code i. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code i. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code i. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code i. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code i. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code i. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code i. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code i. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code i. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code i. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code i. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code i. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code i. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code i. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code i. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code i. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code i. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code i. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code i. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code i. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code i. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code i. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code i. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code i. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code i. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code i. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code i. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code i. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code i. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code i. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code i. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code i. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code i. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code i. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code i. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code i. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code i. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code i. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code i. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code i. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code i. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code i. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('i', datalisteven)
		self.dataodd = array.array('i', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.i_min
		self.Maxval = arrayfunc.arraylimits.i_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code i. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code i. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code i. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code i. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code i. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code i. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code i. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code i. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code i. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code i. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code i. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code i. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code i. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code i. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code i. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code i. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code i. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code i. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code i. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code i. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code i. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code i. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code i. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code i. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code i. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code i. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code i. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code i. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code i. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code i. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code i. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code i. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code i. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code i. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code i. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code i. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code i. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code i. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code i. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code i. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code i. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code i. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code i. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code i. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code i. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code i. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code i. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code i. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code i. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code i. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code i. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code i. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code i. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code i. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code i. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code i. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code i. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code i. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code i. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code i. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('I', datalisteven)
		self.dataodd = array.array('I', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.I_min
		self.Maxval = arrayfunc.arraylimits.I_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code I. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code I. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code I. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code I. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code I. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code I. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code I. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code I. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code I. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code I. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code I. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code I. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code I. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code I. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code I. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code I. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code I. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code I. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code I. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code I. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code I. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code I. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code I. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code I. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code I. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code I. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code I. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code I. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code I. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code I. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code I. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code I. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code I. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code I. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code I. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code I. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code I. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code I. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code I. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code I. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code I. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code I. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code I. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code I. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code I. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code I. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code I. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code I. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code I. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code I. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code I. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code I. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code I. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code I. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code I. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code I. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code I. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code I. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code I. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code I. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('I', datalisteven)
		self.dataodd = array.array('I', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.I_min
		self.Maxval = arrayfunc.arraylimits.I_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code I. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code I. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code I. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code I. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code I. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code I. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code I. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code I. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code I. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code I. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code I. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code I. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code I. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code I. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code I. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code I. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code I. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code I. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code I. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code I. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code I. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code I. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code I. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code I. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code I. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code I. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code I. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code I. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code I. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code I. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code I. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code I. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code I. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code I. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code I. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code I. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code I. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code I. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code I. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code I. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code I. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code I. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code I. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code I. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code I. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code I. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code I. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code I. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code I. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code I. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code I. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code I. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code I. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code I. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code I. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code I. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code I. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code I. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code I. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code I. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('l', datalisteven)
		self.dataodd = array.array('l', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.l_min
		self.Maxval = arrayfunc.arraylimits.l_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code l. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code l. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code l. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code l. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code l. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code l. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code l. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code l. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code l. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code l. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code l. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code l. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code l. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code l. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code l. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code l. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code l. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code l. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code l. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code l. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code l. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code l. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code l. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code l. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code l. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code l. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code l. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code l. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code l. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code l. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code l. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code l. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code l. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code l. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code l. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code l. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code l. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code l. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code l. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code l. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code l. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code l. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code l. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code l. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code l. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code l. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code l. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code l. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code l. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code l. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code l. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code l. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code l. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code l. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code l. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code l. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code l. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code l. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code l. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code l. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('l', datalisteven)
		self.dataodd = array.array('l', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.l_min
		self.Maxval = arrayfunc.arraylimits.l_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code l. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code l. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code l. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code l. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code l. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code l. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code l. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code l. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code l. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code l. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code l. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code l. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code l. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code l. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code l. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code l. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code l. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code l. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code l. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code l. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code l. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code l. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code l. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code l. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code l. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code l. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code l. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code l. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code l. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code l. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code l. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code l. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code l. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code l. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code l. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code l. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code l. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code l. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code l. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code l. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code l. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code l. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code l. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code l. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code l. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code l. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code l. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code l. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code l. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code l. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code l. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code l. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code l. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code l. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code l. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code l. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code l. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code l. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code l. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code l. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('L', datalisteven)
		self.dataodd = array.array('L', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.L_min
		self.Maxval = arrayfunc.arraylimits.L_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code L. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code L. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code L. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code L. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code L. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code L. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code L. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code L. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code L. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code L. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code L. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code L. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code L. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code L. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code L. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code L. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code L. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code L. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code L. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code L. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code L. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code L. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code L. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code L. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code L. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code L. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code L. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code L. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code L. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code L. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code L. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code L. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code L. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code L. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code L. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code L. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code L. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code L. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code L. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code L. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code L. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code L. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code L. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code L. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code L. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code L. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code L. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code L. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code L. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code L. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code L. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code L. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code L. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code L. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code L. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code L. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code L. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code L. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code L. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code L. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('L', datalisteven)
		self.dataodd = array.array('L', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.L_min
		self.Maxval = arrayfunc.arraylimits.L_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code L. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code L. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code L. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code L. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code L. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code L. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code L. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code L. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code L. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code L. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code L. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code L. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code L. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code L. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code L. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code L. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code L. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code L. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code L. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code L. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code L. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code L. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code L. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code L. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code L. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code L. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code L. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code L. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code L. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code L. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code L. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code L. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code L. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code L. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code L. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code L. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code L. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code L. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code L. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code L. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code L. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code L. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code L. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code L. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code L. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code L. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code L. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code L. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code L. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code L. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code L. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code L. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code L. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code L. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code L. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code L. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code L. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code L. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code L. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code L. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('q', datalisteven)
		self.dataodd = array.array('q', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.q_min
		self.Maxval = arrayfunc.arraylimits.q_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code q. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code q. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code q. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code q. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code q. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code q. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code q. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code q. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code q. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code q. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code q. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code q. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code q. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code q. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code q. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code q. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code q. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code q. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code q. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code q. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code q. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code q. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code q. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code q. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code q. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code q. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code q. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code q. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code q. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code q. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code q. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code q. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code q. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code q. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code q. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code q. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code q. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code q. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code q. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code q. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code q. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code q. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code q. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code q. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code q. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code q. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code q. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code q. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code q. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code q. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code q. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code q. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code q. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code q. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code q. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code q. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('q', datalisteven)
		self.dataodd = array.array('q', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.q_min
		self.Maxval = arrayfunc.arraylimits.q_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code q. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code q. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code q. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code q. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code q. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code q. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code q. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code q. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code q. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code q. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code q. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code q. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code q. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code q. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code q. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code q. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code q. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code q. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code q. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code q. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code q. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code q. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code q. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code q. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code q. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code q. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code q. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code q. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code q. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code q. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code q. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code q. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code q. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code q. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code q. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code q. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code q. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code q. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code q. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code q. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code q. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code q. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code q. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code q. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code q. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code q. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code q. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code q. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code q. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code q. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code q. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code q. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code q. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code q. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code q. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code q. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('Q', datalisteven)
		self.dataodd = array.array('Q', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.Q_min
		self.Maxval = arrayfunc.arraylimits.Q_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code Q. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code Q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code Q. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code Q. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code Q. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code Q. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code Q. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code Q. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code Q. - Parameter in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code Q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code Q. - Parameter at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code Q. - Parameter at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code Q. - Parameter at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code Q. - Parameter at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code Q. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code Q. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code Q. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code Q. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code Q. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code Q. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code Q. - Parameter > at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code Q. - Parameter == at start of even length array with SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code Q. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code Q. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code Q. - Parameter > at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code Q. - Parameter == at end of even length array with SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code Q. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code Q. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code Q. - Parameter not found of even length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code Q. - Parameter not found of odd length array with SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code Q. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code Q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code Q. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code Q. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code Q. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code Q. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code Q. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code Q. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code Q. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code Q. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code Q. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code Q. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code Q. - Parameter < at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code Q. - Parameter == at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code Q. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code Q. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code Q. - Parameter < at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code Q. - Parameter == at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code Q. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code Q. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code Q. - Parameter not found of even length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code Q. - Parameter not found of odd length array with SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code Q. - Parameter in middle of even length array with SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code Q. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code Q. - Parameter at start of even length array with SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code Q. - Parameter at start of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code Q. - Parameter at end of even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code Q. - Parameter at end of odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code Q. - Parameter found in even length array with SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code Q. - Parameter found in odd length array with SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('Q', datalisteven)
		self.dataodd = array.array('Q', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.Q_min
		self.Maxval = arrayfunc.arraylimits.Q_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code Q. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code Q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code Q. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code Q. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code Q. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code Q. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code Q. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code Q. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code Q. - Parameter in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code Q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code Q. - Parameter at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code Q. - Parameter at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code Q. - Parameter at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code Q. - Parameter at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code Q. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code Q. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code Q. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code Q. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code Q. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code Q. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code Q. - Parameter > at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code Q. - Parameter == at start of even length array without SIMD.
		"""
		param = 105
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code Q. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code Q. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code Q. - Parameter > at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code Q. - Parameter == at end of even length array without SIMD.
		"""
		param = 105
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code Q. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code Q. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code Q. - Parameter not found of even length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code Q. - Parameter not found of odd length array without SIMD.
		"""
		param = 110
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code Q. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code Q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code Q. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code Q. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code Q. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code Q. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code Q. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code Q. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code Q. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code Q. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code Q. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code Q. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code Q. - Parameter < at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code Q. - Parameter == at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code Q. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code Q. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code Q. - Parameter < at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code Q. - Parameter == at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code Q. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code Q. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code Q. - Parameter not found of even length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code Q. - Parameter not found of odd length array without SIMD.
		"""
		param = 85
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code Q. - Parameter in middle of even length array without SIMD.
		"""
		param = 90
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code Q. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code Q. - Parameter at start of even length array without SIMD.
		"""
		param = 90
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code Q. - Parameter at start of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code Q. - Parameter at end of even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code Q. - Parameter at end of odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code Q. - Parameter found in even length array without SIMD.
		"""
		param = 90
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code Q. - Parameter found in odd length array without SIMD.
		"""
		param = 90
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('f', datalisteven)
		self.dataodd = array.array('f', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code f. - Parameter in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code f. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code f. - Parameter at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code f. - Parameter at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code f. - Parameter at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code f. - Parameter at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code f. - Parameter not found of even length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code f. - Parameter not found of odd length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code f. - Parameter in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code f. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code f. - Parameter at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code f. - Parameter at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code f. - Parameter at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code f. - Parameter at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code f. - Parameter not found of even length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code f. - Parameter not found of odd length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code f. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code f. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code f. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code f. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code f. - Parameter > at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code f. - Parameter == at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code f. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code f. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code f. - Parameter > at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code f. - Parameter == at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code f. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code f. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code f. - Parameter not found of even length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code f. - Parameter not found of odd length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code f. - Parameter in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code f. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code f. - Parameter at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code f. - Parameter at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code f. - Parameter at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code f. - Parameter at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code f. - Parameter not found of even length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code f. - Parameter not found of odd length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code f. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code f. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code f. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code f. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code f. - Parameter < at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code f. - Parameter == at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code f. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code f. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code f. - Parameter < at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code f. - Parameter == at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code f. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code f. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code f. - Parameter not found of even length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code f. - Parameter not found of odd length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code f. - Parameter in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code f. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code f. - Parameter at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code f. - Parameter at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code f. - Parameter at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code f. - Parameter at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code f. - Parameter found in even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code f. - Parameter found in odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('f', datalisteven)
		self.dataodd = array.array('f', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code f. - Parameter in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code f. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code f. - Parameter at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code f. - Parameter at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code f. - Parameter at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code f. - Parameter at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code f. - Parameter not found of even length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code f. - Parameter not found of odd length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code f. - Parameter in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code f. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code f. - Parameter at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code f. - Parameter at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code f. - Parameter at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code f. - Parameter at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code f. - Parameter not found of even length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code f. - Parameter not found of odd length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code f. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code f. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code f. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code f. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code f. - Parameter > at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code f. - Parameter == at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code f. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code f. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code f. - Parameter > at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code f. - Parameter == at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code f. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code f. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code f. - Parameter not found of even length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code f. - Parameter not found of odd length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code f. - Parameter in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code f. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code f. - Parameter at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code f. - Parameter at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code f. - Parameter at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code f. - Parameter at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code f. - Parameter not found of even length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code f. - Parameter not found of odd length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code f. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code f. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code f. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code f. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code f. - Parameter < at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code f. - Parameter == at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code f. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code f. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code f. - Parameter < at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code f. - Parameter == at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code f. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code f. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code f. - Parameter not found of even length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code f. - Parameter not found of odd length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code f. - Parameter in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code f. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code f. - Parameter at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code f. - Parameter at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code f. - Parameter at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code f. - Parameter at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code f. - Parameter found in even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code f. - Parameter found in odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_with_simd_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('d', datalisteven)
		self.dataodd = array.array('d', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code d. - Parameter in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code d. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code d. - Parameter at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code d. - Parameter at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code d. - Parameter at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code d. - Parameter at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code d. - Parameter not found of even length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code d. - Parameter not found of odd length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code d. - Parameter in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code d. - Parameter in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code d. - Parameter at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code d. - Parameter at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code d. - Parameter at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code d. - Parameter at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code d. - Parameter not found of even length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code d. - Parameter not found of odd length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code d. - Parameter > in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code d. - Parameter == in middle of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code d. - Parameter > in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code d. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code d. - Parameter > at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code d. - Parameter == at start of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code d. - Parameter > at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code d. - Parameter == at start of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code d. - Parameter > at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code d. - Parameter == at end of even length array with SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code d. - Parameter > at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code d. - Parameter == at end of odd length array with SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code d. - Parameter not found of even length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code d. - Parameter not found of odd length array with SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code d. - Parameter in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code d. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code d. - Parameter at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code d. - Parameter at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code d. - Parameter at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code d. - Parameter at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code d. - Parameter not found of even length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code d. - Parameter not found of odd length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code d. - Parameter < in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code d. - Parameter == in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code d. - Parameter < in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code d. - Parameter == in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code d. - Parameter < at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code d. - Parameter == at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code d. - Parameter < at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code d. - Parameter == at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code d. - Parameter < at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code d. - Parameter == at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code d. - Parameter < at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code d. - Parameter == at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code d. - Parameter not found of even length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code d. - Parameter not found of odd length array with SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code d. - Parameter in middle of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code d. - Parameter in middle of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code d. - Parameter at start of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code d. - Parameter at start of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code d. - Parameter at end of even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code d. - Parameter at end of odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code d. - Parameter found in even length array with SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code d. - Parameter found in odd length array with SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_operator_without_simd_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('d', datalisteven)
		self.dataodd = array.array('d', datalistodd)


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code d. - Parameter in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code d. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code d. - Parameter at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code d. - Parameter at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code d. - Parameter at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code d. - Parameter at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code d. - Parameter not found of even length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code d. - Parameter not found of odd length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code d. - Parameter in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code d. - Parameter in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code d. - Parameter at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code d. - Parameter at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code d. - Parameter at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code d. - Parameter at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code d. - Parameter not found of even length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code d. - Parameter not found of odd length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code d. - Parameter > in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code d. - Parameter == in middle of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code d. - Parameter > in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code d. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code d. - Parameter > at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code d. - Parameter == at start of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code d. - Parameter > at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code d. - Parameter == at start of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code d. - Parameter > at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code d. - Parameter == at end of even length array without SIMD.
		"""
		param = 105.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code d. - Parameter > at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code d. - Parameter == at end of odd length array without SIMD.
		"""
		param = 105.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code d. - Parameter not found of even length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code d. - Parameter not found of odd length array without SIMD.
		"""
		param = 110.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code d. - Parameter in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code d. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code d. - Parameter at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code d. - Parameter at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code d. - Parameter at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code d. - Parameter at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code d. - Parameter not found of even length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code d. - Parameter not found of odd length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code d. - Parameter < in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code d. - Parameter == in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code d. - Parameter < in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code d. - Parameter == in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code d. - Parameter < at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code d. - Parameter == at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code d. - Parameter < at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code d. - Parameter == at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code d. - Parameter < at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code d. - Parameter == at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code d. - Parameter < at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code d. - Parameter == at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code d. - Parameter not found of even length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code d. - Parameter not found of odd length array without SIMD.
		"""
		param = 85.0
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code d. - Parameter in middle of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code d. - Parameter in middle of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code d. - Parameter at start of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code d. - Parameter at start of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code d. - Parameter at end of even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code d. - Parameter at end of odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code d. - Parameter found in even length array without SIMD.
		"""
		param = 90.0
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code d. - Parameter found in odd length array without SIMD.
		"""
		param = 90.0
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################


##############################################################################
class findindex_parameter_b(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('b', [100]*100)
		self.dataempty = array.array('b')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code b.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code b.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code b.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code b.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_B(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('B', [100]*100)
		self.dataempty = array.array('B')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code B.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code B.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code B.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code B.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_h(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('h', [100]*100)
		self.dataempty = array.array('h')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code h.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code h.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code h.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code h.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_H(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('H', [100]*100)
		self.dataempty = array.array('H')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code H.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code H.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code H.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code H.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_i(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('i', [100]*100)
		self.dataempty = array.array('i')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code i.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code i.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code i.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code i.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_I(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('I', [100]*100)
		self.dataempty = array.array('I')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code I.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code I.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code I.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code I.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_l(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('l', [100]*100)
		self.dataempty = array.array('l')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code l.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code l.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code l.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code l.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_L(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('L', [100]*100)
		self.dataempty = array.array('L')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code L.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code L.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code L.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code L.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_q(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('q', [100]*100)
		self.dataempty = array.array('q')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code q.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code q.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code q.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_Q(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('Q', [100]*100)
		self.dataempty = array.array('Q')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code Q.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code Q.
		"""
		param = 101
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code Q.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code Q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.5)



##############################################################################
class findindex_parameter_f(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [100]*100)
		self.dataempty = array.array('f')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code f.
		"""
		param = 101.0
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code f.
		"""
		param = 101.0
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code f.
		"""
		param = 101.0
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code f.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100.0)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100.0)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100.0)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100.0)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100)



##############################################################################
class findindex_parameter_d(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [100]*100)
		self.dataempty = array.array('d')


		# These are the compare operators to use when testing the findindex function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}



	########################################################
	def FindIndex(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				return -1
			if opval(j):
				return i
		
		return -1



	########################################################
	def test_operator_lim_01(self):
		"""Test array limits  - Array code d.
		"""
		param = 101.0
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code d.
		"""
		param = 101.0
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code d.
		"""
		param = 101.0
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code d.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100.0)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100.0)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100.0)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100.0)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100)



##############################################################################
class findindex_overflow_b(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.b_min
		self.Maxval = arrayfunc.arraylimits.b_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code b.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_B(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code B.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_h(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.h_min
		self.Maxval = arrayfunc.arraylimits.h_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code h.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_H(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.H_min
		self.Maxval = arrayfunc.arraylimits.H_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code H.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_i(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.i_min
		self.Maxval = arrayfunc.arraylimits.i_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code i.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_I(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.I_min
		self.Maxval = arrayfunc.arraylimits.I_max



	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code I.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_l(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.l_min
		self.Maxval = arrayfunc.arraylimits.l_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code l.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_q(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.q_min
		self.Maxval = arrayfunc.arraylimits.q_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code q.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_f(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal * 1.1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval * 1.1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code f.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_overflow_d(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal * 1.1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval * 1.1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code d.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)


##############################################################################
class findindex_nan_f(unittest.TestCase):
	"""Test for nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [100.0] * 10)


	########################################################
	def test_nan_01(self):
		"""Test for param of nan  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('nan'))


	########################################################
	def test_nan_02(self):
		"""Test for param of inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('inf'))


	########################################################
	def test_nan_03(self):
		"""Test for param of -inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('-inf'))


	########################################################
	def test_nan_04(self):
		"""Test for lim of nan  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('nan'))


	########################################################
	def test_nan_05(self):
		"""Test for lim of inf  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('inf'))


	########################################################
	def test_nan_06(self):
		"""Test for lim of -inf  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('-inf'))


##############################################################################

##############################################################################
class findindex_nan_d(unittest.TestCase):
	"""Test for nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [100.0] * 10)


	########################################################
	def test_nan_01(self):
		"""Test for param of nan  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('nan'))


	########################################################
	def test_nan_02(self):
		"""Test for param of inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('inf'))


	########################################################
	def test_nan_03(self):
		"""Test for param of -inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('-inf'))


	########################################################
	def test_nan_04(self):
		"""Test for lim of nan  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('nan'))


	########################################################
	def test_nan_05(self):
		"""Test for lim of inf  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('inf'))


	########################################################
	def test_nan_06(self):
		"""Test for lim of -inf  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('-inf'))


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
			f.write('findindex\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
