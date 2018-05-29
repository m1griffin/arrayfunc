#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for findindex.
# Language: Python 3.4
# Date:     21-Jun-2014
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

# ==============================================================================

import copy

import codegen_common

# ==============================================================================


intparams = {'overflowinc' : '+ 1', 'overflowdec' : '- 1', 
	'decimal' : '', 'invaliddecimal' : '.5',
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}

floatparams = {'overflowinc' : '* 1.1', 'overflowdec' : '* 1.1', 
	'decimal' : '.0', 'invaliddecimal' : '',
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}

testdata = {
	'b' : intparams,
	'B' : intparams,
	'h' : intparams,
	'H' : intparams,
	'i' : intparams,
	'I' : copy.copy(intparams),
	'l' : intparams,
	'L' : intparams,
	'q' : copy.copy(intparams),
	'Q' : copy.copy(intparams),
	'f' : floatparams,
	'd' : floatparams,
	}

# Patch in the case for 'I' arrays.
testdata['I']['skipminoverflow'] = codegen_common.OvflTestSkip
testdata['I']['skipmaxoverflow'] = codegen_common.OvflTestSkip


# ==============================================================================

# The template used to generate the tests.
op_template = '''
##############################################################################
class findindex_operator_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		datalisteven = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16


		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103] * 16
		datalistodd.extend([103, 103, 103])


		self.dataeven = array.array('%(typecode)s', datalisteven)
		self.dataodd = array.array('%(typecode)s', datalistodd)


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

		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max


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
		"""Test eq  - Array code %(typelabel)s. - Parameter in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter at start of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[0] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[0] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_05(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter at end of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[-1] = param
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_06(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[-1] = param
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_07(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter not found of even length array %(simdpresent)s SIMD.
		"""
		param = 110%(decimal)s
		result = arrayfunc.findindex('==', self.dataeven, param)
		expected = self.FindIndex('==', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_eq_08(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter not found of odd length array %(simdpresent)s SIMD.
		"""
		param = 110%(decimal)s
		result = arrayfunc.findindex('==', self.dataodd, param)
		expected = self.FindIndex('==', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter at start of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_05(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter at end of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_06(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_07(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter not found of even length array %(simdpresent)s SIMD.
		"""
		param = 110%(decimal)s
		result = arrayfunc.findindex('>', self.dataeven, param)
		expected = self.FindIndex('>', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gt_08(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter not found of odd length array %(simdpresent)s SIMD.
		"""
		param = 110%(decimal)s
		result = arrayfunc.findindex('>', self.dataodd, param)
		expected = self.FindIndex('>', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter > in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter == in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter > in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter == in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_05(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter > at start of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_06(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter == at start of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_07(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter > at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_08(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter == at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_09(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter > at end of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_10(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter == at end of even length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_11(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter > at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_12(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter == at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 105%(decimal)s
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_13(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter not found of even length array %(simdpresent)s SIMD.
		"""
		param = 110%(decimal)s
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_gte_14(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter not found of odd length array %(simdpresent)s SIMD.
		"""
		param = 110%(decimal)s
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter at start of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_05(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter at end of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_06(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_07(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter not found of even length array %(simdpresent)s SIMD.
		"""
		param = 85%(decimal)s
		result = arrayfunc.findindex('<', self.dataeven, param)
		expected = self.FindIndex('<', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lt_08(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter not found of odd length array %(simdpresent)s SIMD.
		"""
		param = 85%(decimal)s
		result = arrayfunc.findindex('<', self.dataodd, param)
		expected = self.FindIndex('<', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter < in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter == in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter < in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter == in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_05(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter < at start of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_06(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter == at start of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[0] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_07(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter < at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[0] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_08(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter == at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[0] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_09(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter < at end of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_10(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter == at end of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[-1] = param
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_11(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter < at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[-1] = param + 1
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_12(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter == at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[-1] = param
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_13(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter not found of even length array %(simdpresent)s SIMD.
		"""
		param = 85%(decimal)s
		result = arrayfunc.findindex('>=', self.dataeven, param)
		expected = self.FindIndex('>=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lte_14(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter not found of odd length array %(simdpresent)s SIMD.
		"""
		param = 85%(decimal)s
		result = arrayfunc.findindex('>=', self.dataodd, param)
		expected = self.FindIndex('>=', self.dataodd, param)
		self.assertEqual(result, expected)



	#####



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter in middle of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[len(self.dataeven) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter in middle of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[len(self.dataodd) // 2] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter at start of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter at start of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[0] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_05(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter at end of even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_06(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter at end of odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_07(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter found in even length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataeven[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataeven, param)
		expected = self.FindIndex('!=', self.dataeven, param)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_ne_08(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter found in odd length array %(simdpresent)s SIMD.
		"""
		param = 90%(decimal)s
		self.dataodd[-1] = param - 1
		result = arrayfunc.findindex('!=', self.dataodd, param)
		expected = self.FindIndex('!=', self.dataodd, param)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================

# The basic template for testing parameters.
param_template = '''
##############################################################################
class findindex_parameter_%(typelabel)s(unittest.TestCase):
	"""Test for correct parameters.
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100]*100)
		self.dataempty = array.array('%(typecode)s')


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
		"""Test array limits  - Array code %(typelabel)s.
		"""
		param = 101%(decimal)s
		result = arrayfunc.findindex('==', self.data, param, maxlen=len(self.data)//2)
		expected = self.FindIndex('==', self.data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test array limits  - Array code %(typelabel)s.
		"""
		param = 101%(decimal)s
		result = arrayfunc.findindex('==', self.data, param, maxlen=-1)
		expected = self.FindIndex('==', self.data, param, maxlen=-1)
		self.assertEqual(result, expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==')


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code %(typelabel)s.
		"""
		param = 101%(decimal)s
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, param, 3, maxlen=2, nosimd=True)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100%(decimal)s, xx=2)


	########################################################
	def test_param_invalid_keyword_param_type_1(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100%(decimal)s, maxlen='x')


	########################################################
	def test_param_invalid_keyword_param_type_2(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100%(decimal)s, nosimd='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindex('!', self.data, 100%(decimal)s)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex(62, self.data, 100%(decimal)s)


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', 99, 100%(decimal)s)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindex('==', self.dataempty, 100%(decimal)s)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100%(invaliddecimal)s)


'''


# ==============================================================================

# The basic template for testing parameter overflow.
overflow_template = '''
##############################################################################
class findindex_overflow_%(typelabel)s(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, list(range(97, 107)))

		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max



	########################################################
%(skipminoverflow)s	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.MinVal %(overflowdec)s)


	########################################################
%(skipmaxoverflow)s	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.dataovfl, self.Maxval %(overflowinc)s)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code %(typelabel)s.
		"""
		result = arrayfunc.findindex('==', self.dataovfl, self.MinVal)
		result = arrayfunc.findindex('==', self.dataovfl, self.Maxval)

'''


# ==============================================================================

# The template used to generate the tests for nan, inf, -inf.
nan_template = '''
##############################################################################
class findindex_nan_%(typelabel)s(unittest.TestCase):
	"""Test for nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100.0] * 10)


	########################################################
	def test_nan_01(self):
		"""Test for param of nan  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('nan'))


	########################################################
	def test_nan_02(self):
		"""Test for param of inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('inf'))


	########################################################
	def test_nan_03(self):
		"""Test for param of -inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindex('==', self.data, float('-inf'))


	########################################################
	def test_nan_04(self):
		"""Test for lim of nan  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('nan'))


	########################################################
	def test_nan_05(self):
		"""Test for lim of inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('inf'))


	########################################################
	def test_nan_06(self):
		"""Test for lim of -inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindex('==', self.data, 100.0, maxlen=float('-inf'))


##############################################################################
'''


# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_findindex', '21-Jun-2014', 'findindex')

with open('test_findindex.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for all tests.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		if funtypes in codegen_common.floatarrays:
			datarec['decimal'] = '.0'
		else:
			datarec['decimal'] = ''

		# With SIMD.
		datarec['simdpresent'] = 'with'
		datarec['nosimd'] = ''
		f.write(op_template % datarec)

		# Without SIMD.
		datarec['simdpresent'] = 'without'
		datarec['nosimd'] = ', nosimd=True'
		f.write(op_template % datarec)



	############################################################################

	# Output the generated code for parameter tests.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(param_template % datarec)


	############################################################################

	# Output the generated code for parameter overflow tests.
	for funtypes in codegen_common.arraycodes:
		# There are some array types we can't test for overflow.
		if funtypes not in 'LQ':
			datarec = testdata[funtypes]
			datarec['typecode'] = funtypes
			datarec['typelabel'] = funtypes
			f.write(overflow_template % datarec)



	############################################################################


	# Output the generated code for nan and inf data in array tests.
	datarec = {}
	for funtypes in codegen_common.floatarrays:
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(nan_template % datarec)


	############################################################################


	f.write(codegen_common.testendtemplate % 'findindex')


	############################################################################
