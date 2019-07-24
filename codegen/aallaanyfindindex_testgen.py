#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for aall, aany, findindex.
# Language: Python 3.4
# Date:     21-May-2014
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


# This template is for aall operations.
test_template_aall = ''' 

##############################################################################
class aall_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_aall
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aall_basic_eq_a1(self):
		"""Test aall for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_eq_a2(self):
		"""Test aall for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = %(typeconverter)s(99)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_eq_a3(self):
		"""Test aall for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_basic_gt_b1(self):
		"""Test aall for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_gt_b2(self):
		"""Test aall for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_gt_b3(self):
		"""Test aall for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_basic_ge_c1(self):
		"""Test aall for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_ge_c2(self):
		"""Test aall for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval - 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_ge_c3(self):
		"""Test aall for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 2

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_ge_c4(self):
		"""Test aall for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_ge_c5(self):
		"""Test aall for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 2

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_basic_lt_d1(self):
		"""Test aall for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_lt_d2(self):
		"""Test aall for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_lt_d3(self):
		"""Test aall for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is equal to the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_basic_le_e1(self):
		"""Test aall for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_le_e2(self):
		"""Test aall for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_le_e3(self):
		"""Test aall for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is greater than the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval + 2

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_le_e4(self):
		"""Test aall for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_le_e5(self):
		"""Test aall for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval + 2

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_basic_ne_f1(self):
		"""Test aall for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are not the same.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_ne_f2(self):
		"""Test aall for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = %(typeconverter)s(99)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_basic_ne_f3(self):
		"""Test aall for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================

# This template is for aany operations.
test_template_aany = ''' 

##############################################################################
class aany_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_aany
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aany_basic_eq_a1(self):
		"""Test aany for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_eq_a2(self):
		"""Test aany for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = %(typeconverter)s(99)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_eq_a3(self):
		"""Test aany for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_basic_gt_b1(self):
		"""Test aany for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_gt_b2(self):
		"""Test aany for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_gt_b3(self):
		"""Test aany for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is greater than to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_basic_ge_c1(self):
		"""Test aany for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_ge_c2(self):
		"""Test aany for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval - 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_ge_c3(self):
		"""Test aany for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval - 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval + 2

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_ge_c4(self):
		"""Test aany for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_ge_c5(self):
		"""Test aany for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval - 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_basic_lt_d1(self):
		"""Test aany for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_lt_d2(self):
		"""Test aany for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_lt_d3(self):
		"""Test aany for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 1

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_basic_le_e1(self):
		"""Test aany for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_le_e2(self):
		"""Test aany for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_le_e3(self):
		"""Test aany for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 2

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_le_e4(self):
		"""Test aany for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_le_e5(self):
		"""Test aany for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 2

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_basic_ne_f1(self):
		"""Test aany for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are not the same.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_ne_f2(self):
		"""Test aany for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = %(typeconverter)s(99)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_basic_ne_f3(self):
		"""Test aany for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is not the same.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================


# This template is for findindex operations.
test_template_findindex = ''' 

##############################################################################
class findindex_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_findindex
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension

		self.ARR_ERR_NOTFOUND = -1


	########################################################
	def test_findindex_basic_eq_a1(self):
		"""Test findindex for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_eq_a2(self):
		"""Test findindex for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = %(typeconverter)s(99)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_eq_a3(self):
		"""Test findindex for eq  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_basic_gt_b1(self):
		"""Test findindex for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_gt_b2(self):
		"""Test findindex for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_gt_b3(self):
		"""Test findindex for gt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is greater than to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_basic_ge_c1(self):
		"""Test findindex for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = %(typeconverter)s(101)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_ge_c2(self):
		"""Test findindex for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval - 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_ge_c3(self):
		"""Test findindex for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval - 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval + 2

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_ge_c4(self):
		"""Test findindex for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_ge_c5(self):
		"""Test findindex for ge  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval - 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_basic_lt_d1(self):
		"""Test findindex for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_lt_d2(self):
		"""Test findindex for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_lt_d3(self):
		"""Test findindex for lt  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 1

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_basic_le_e1(self):
		"""Test findindex for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = %(typeconverter)s(100)
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_le_e2(self):
		"""Test findindex for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are greater than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_le_e3(self):
		"""Test findindex for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(101)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 2

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_le_e4(self):
		"""Test findindex for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data values are equal to the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_le_e5(self):
		"""Test findindex for le  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is less than the test value.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 2

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_basic_ne_f1(self):
		"""Test findindex for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are not the same.
		testval = %(typeconverter)s(100)
		arrayval = testval + 1
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_ne_f2(self):
		"""Test findindex for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = %(typeconverter)s(99)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_basic_ne_f3(self):
		"""Test findindex for ne  - Array code %(typelabel)s. General test %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is not the same.
		testval = %(typeconverter)s(100)
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The basic template for testing parameters.
param_template = '''
##############################################################################
class %(funclabel)s_parameter_%(typelabel)s(unittest.TestCase):
	"""Test for correct parameters for %(funclabel)s.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100]*100)
		self.dataempty = array.array('%(typecode)s')
		self.testdata = %(typeconverter)s(100)
		self.baddata = %(badtypeconverter)s(100)


	########################################################
	def test_%(funclabel)s_param_a1(self):
		"""Test exception when no parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_%(funclabel)s_param_a2(self):
		"""Test exception when one parameter passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_%(funclabel)s_param_a3(self):
		"""Test exception when two parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()


	########################################################
	def test_%(funclabel)s_param_a4(self):
		"""Test exception when six parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', self.data, self.testdata, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_%(funclabel)s_param_b1(self):
		"""Test exception with invalid keyword parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', self.data, self.testdata, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)


	########################################################
	def test_%(funclabel)s_param_b2(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', self.data, self.testdata, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_%(funclabel)s_param_c1(self):
		"""Test exception with invalid first parameter value  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.%(funcname)s('!', self.data, self.testdata)


	########################################################
	def test_%(funclabel)s_param_c3(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(62, self.data, self.testdata)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_%(funclabel)s_param_c4(self):
		"""Test exception with invalid array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', 99, self.testdata)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_%(funclabel)s_param_d1(self):
		"""Test exception with invalid array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.%(funcname)s('==', self.dataempty, self.testdata)


	########################################################
	def test_%(funclabel)s_param_e1(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', self.data, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_%(funclabel)s_param_e2(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', self.data, self.baddata)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


	########################################################
	def test_%(funclabel)s_param_f1(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s('==', self.data, self.testdata, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################

'''
# ==============================================================================

# ==============================================================================


# The basic template for testing parameter overflow.
overflow_template = '''
##############################################################################
class %(funclabel)s_overflow_%(typelabel)s(unittest.TestCase):
	"""Test for parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100]*100)
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max


	########################################################
	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.%(funcname)s('==', self.data, self.MinVal %(overflowdec)s)

	########################################################
	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.%(funcname)s('==', self.data, self.Maxval %(overflowinc)s)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s('==', self.data, self.MinVal)
		result = arrayfunc.%(funcname)s('==', self.data, self.Maxval)

##############################################################################

'''

# ==============================================================================

# ==============================================================================


# This template is for aall operations.
test_template_aall_nonfinite_nan = ''' 

##############################################################################
class aall_nonfinite_nan_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_aall_nonfinite_nan
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aall_nan_eq_a1(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_eq_a2(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_eq_a3(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_eq_a4(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_gt_b1(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_gt_b2(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_gt_b3(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_gt_b4(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_ge_c1(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_ge_c2(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_ge_c3(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_ge_c4(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_nan_lt_d1(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_lt_d2(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_lt_d3(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_nan_lt_d4(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_le_e1(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_le_e2(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_le_e3(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_le_e4(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_nan_ne_f1(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_ne_f2(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_ne_f3(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_nan_ne_f4(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0 + 1.0

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================

# This template is for aany operations.
test_template_aany_nonfinite_nan = ''' 

##############################################################################
class aany_nonfinite_nan_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic fininte number operation.
	test_template_aany_nonfinite_nan
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aany_nan_eq_a1(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_eq_a2(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_eq_a3(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_eq_a4(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_nan_gt_b1(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_gt_b2(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_gt_b3(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_gt_b4(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_nan_ge_c1(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_ge_c2(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_ge_c3(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_ge_c4(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_lt_d1(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_lt_d2(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_lt_d3(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_lt_d4(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_nan_le_e1(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_le_e2(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_le_e3(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_le_e4(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_nan_ne_f1(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_ne_f2(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_ne_f3(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_nan_ne_f4(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = math.nan

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


##############################################################################

'''


# ==============================================================================


# This template is for findindex operations.
test_template_findindex_nonfinite_nan = ''' 

##############################################################################
class findindex_nonfinite_nan_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic fininte number operation.
	test_template_findindex_nonfinite_nan
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension

		self.ARR_ERR_NOTFOUND = -1


	########################################################
	def test_findindex_nan_eq_a1(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_eq_a2(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_eq_a3(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_eq_a4(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_nan_gt_b1(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_gt_b2(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_gt_b3(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_gt_b4(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_nan_ge_c1(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_ge_c2(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_ge_c3(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_ge_c4(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_lt_d1(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_lt_d2(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_lt_d3(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_lt_d4(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_nan_le_e1(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_le_e2(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_le_e3(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_le_e4(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.nan
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_ne_f1(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.nan
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_ne_f2(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_ne_f3(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.nan
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_nan_ne_f4(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite nan %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = math.nan

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# This template is for aall operations.
test_template_aall_nonfinite_inf = ''' 

##############################################################################
class aall_nonfinite_inf_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for non fininte number function operation.
	test_template_aall_nonfinite_inf
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aall_inf_eq_a1(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_eq_a2(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_eq_a3(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_eq_a4(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_gt_b1(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values match.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_gt_b2(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values fail.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_gt_b3(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_gt_b4(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_ge_c1(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values pass.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_ge_c2(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values fail.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_ge_c3(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_ge_c4(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_inf_lt_d1(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_lt_d2(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_lt_d3(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_inf_lt_d4(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_le_e1(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_le_e2(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_le_e3(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0 + 1.0

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_le_e4(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_inf_ne_f1(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_ne_f2(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_ne_f3(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_inf_ne_f4(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0 + 1.0

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================

# This template is for aany operations.
test_template_aany_nonfinite_inf = ''' 

##############################################################################
class aany_nonfinite_inf_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic fininte number operation.
	test_template_aany_nonfinite_inf
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aany_inf_eq_a1(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_eq_a2(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_eq_a3(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_eq_a4(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_inf_gt_b1(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_gt_b2(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_gt_b3(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_gt_b4(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_inf_ge_c1(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_ge_c2(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_ge_c3(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_ge_c4(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_lt_d1(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_lt_d2(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_lt_d3(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_lt_d4(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_inf_le_e1(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_le_e2(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_le_e3(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_le_e4(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_inf_ne_f1(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_ne_f2(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_ne_f3(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_inf_ne_f4(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = math.inf

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


##############################################################################

'''


# ==============================================================================

# This template is for findindex operations.
test_template_findindex_nonfinite_inf = ''' 

##############################################################################
class findindex_nonfinite_inf_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic fininte number operation.
	test_template_findindex_nonfinite_inf
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension

		self.ARR_ERR_NOTFOUND = -1


	########################################################
	def test_findindex_inf_eq_a1(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_eq_a2(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_eq_a3(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_eq_a4(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_inf_gt_b1(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_gt_b2(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_gt_b3(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_gt_b4(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_inf_ge_c1(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_ge_c2(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_ge_c3(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_ge_c4(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_lt_d1(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_lt_d2(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_lt_d3(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_lt_d4(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_inf_le_e1(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_le_e2(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_le_e3(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_le_e4(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_ne_f1(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_ne_f2(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_ne_f3(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_inf_ne_f4(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = math.inf

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================


# ==============================================================================

# This template is for aall operations.
test_template_aall_nonfinite_neginf = ''' 

##############################################################################
class aall_nonfinite_neginf_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for non fininte number function operation.
	test_template_aall_nonfinite_neginf
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aall_neginf_eq_a1(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_eq_a2(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_eq_a3(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_eq_a4(self):
		"""Test aall for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = all([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_gt_b1(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values match.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_gt_b2(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values fail.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_gt_b3(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_gt_b4(self):
		"""Test aall for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = all([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_ge_c1(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values pass.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_ge_c2(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values fail.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_ge_c3(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_ge_c4(self):
		"""Test aall for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = all([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_neginf_lt_d1(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_lt_d2(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_lt_d3(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_neginf_lt_d4(self):
		"""Test aall for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = all([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_le_e1(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_le_e2(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_le_e3(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0 + 1.0

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_le_e4(self):
		"""Test aall for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = all([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aall_neginf_ne_f1(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_ne_f2(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_ne_f3(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is different.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aall_neginf_ne_f4(self):
		"""Test aall for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = 100.0 + 1.0

		# Verify test compatibility.
		expected = all([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aall('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================

# This template is for aany operations.
test_template_aany_nonfinite_neginf = ''' 

##############################################################################
class aany_nonfinite_neginf_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic fininte number operation.
	test_template_aany_nonfinite_neginf
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension


	########################################################
	def test_aany_neginf_eq_a1(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_eq_a2(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_eq_a3(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_eq_a4(self):
		"""Test aany for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x == testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('==', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_neginf_gt_b1(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_gt_b2(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_gt_b3(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_gt_b4(self):
		"""Test aany for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = any([(x > testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_neginf_ge_c1(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_ge_c2(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_ge_c3(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_ge_c4(self):
		"""Test aany for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		expected = any([(x >= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('>=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_lt_d1(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_lt_d2(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_lt_d3(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_lt_d4(self):
		"""Test aany for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = arrayval - 1.0

		# Verify test compatibility.
		expected = any([(x < testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_neginf_le_e1(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_le_e2(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_le_e3(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_le_e4(self):
		"""Test aany for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval - 1.0

		# Verify test compatibility.
		expected = any([(x <= testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('<=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)



	########################################################
	def test_aany_neginf_ne_f1(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertFalse(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_ne_f2(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_ne_f3(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


	########################################################
	def test_aany_neginf_ne_f4(self):
		"""Test aany for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = -math.inf

		# Verify test compatibility.
		expected = any([(x != testval) for x in testdata])

		# The actual test.
		result = arrayfunc.aany('!=', testdata, testval %(nosimd)s)
		self.assertTrue(result)
		self.assertEqual(result, expected)


##############################################################################

'''


# ==============================================================================

# This template is for findindex operations.
test_template_findindex_nonfinite_neginf = ''' 

##############################################################################
class findindex_nonfinite_neginf_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic fininte number operation.
	test_template_findindex_nonfinite_neginf
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# We use a template to generate this code, so the following
		# compare is inserted into the template to generate code which
		# spills over past the SIMD handler.
		if '%(arrayevenodd)s' == 'odd':
			arrayextension = 5
		else:
			arrayextension = 0
		
		self.arraylength = 96 + arrayextension

		self.ARR_ERR_NOTFOUND = -1


	########################################################
	def test_findindex_neginf_eq_a1(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_eq_a2(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_eq_a3(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_eq_a4(self):
		"""Test findindex for eq  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y == testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('==', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_neginf_gt_b1(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_gt_b2(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_gt_b3(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_gt_b4(self):
		"""Test findindex for gt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval + 1.0

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y > testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_neginf_ge_c1(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_ge_c2(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_ge_c3(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_ge_c4(self):
		"""Test findindex for ge  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y >= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('>=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_lt_d1(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_lt_d2(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_lt_d3(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_lt_d4(self):
		"""Test findindex for lt  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = -math.inf

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y < testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



	########################################################
	def test_findindex_neginf_le_e1(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_le_e2(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_le_e3(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = 100.0
		arrayval = -math.inf
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_le_e4(self):
		"""Test findindex for le  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y <= testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('<=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_ne_f1(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are the same.
		testval = -math.inf
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, self.ARR_ERR_NOTFOUND)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_ne_f2(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# All data and test values are different.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_ne_f3(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array is the same.
		testval = -math.inf
		arrayval = 100.0
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = testval

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, 0)
		self.assertEqual(result, expected)


	########################################################
	def test_findindex_neginf_ne_f4(self):
		"""Test findindex for ne  - Array code %(typelabel)s. Test nonfinite negative inf %(arrayevenodd)s length array %(simdpresent)s SIMD.
		"""
		# One test value near the end of the array matches.
		testval = 100.0
		arrayval = testval
		testdata = array.array('%(typecode)s', [arrayval] * self.arraylength)
		testdata[-2] = -math.inf

		# Verify test compatibility.
		pyfind = [x for x,y in enumerate(testdata) if y != testval]
		expected = pyfind[0] if len(pyfind) > 0 else self.ARR_ERR_NOTFOUND

		# The actual test.
		result = arrayfunc.findindex('!=', testdata, testval %(nosimd)s)
		self.assertEqual(result, len(testdata) - 2)
		self.assertEqual(result, expected)



##############################################################################

'''


# ==============================================================================


# ==============================================================================


# This is used to generate test template data for non finite data tests.
def gennonfinitetestdata():
	""" Generate test template data for non finite data tests.
	Returns: (list) - A list of dictionaries containing the keys and
		values to generate individual test functions.
	"""
	# These are the different test values we will combine in various ways.
	arraycode = [('typecode', x) for x in codegen_common.floatarrays]
	hassimd = (('simdpresent', 'with'), ('simdpresent', 'without'))
	arraylen = (('arrayevenodd', 'even'), ('arrayevenodd', 'odd'))

	# The product function produces all possible combinations.
	combos = list(itertools.product(arraycode, hassimd, arraylen))


	# Convert the data into a list of dictionaries.
	testdata = [dict(x) for x in combos]

	nosimd = {'with' : '', 'without' : ', nosimd=True'}

	# Now go through the list and add data which goes with the ones we have already defined.
	for x in testdata:
		x['typelabel'] = x['typecode']
		x['nosimd'] = nosimd[x['simdpresent']]


	return testdata



# ==============================================================================

# ==============================================================================

# This is used to generate test template data for general tests.
def genbasictestdata():
	""" Generate test template data for general tests.
	Returns: (list) - A list of dictionaries containing the keys and
		values to generate individual test functions.
	"""
	# These are the different test values we will combine in various ways.
	arraycode = [('typecode', x) for x in codegen_common.arraycodes]
	hassimd = (('simdpresent', 'with'), ('simdpresent', 'without'))
	arraylen = (('arrayevenodd', 'even'), ('arrayevenodd', 'odd'))

	# The product function produces all possible combinations.
	combos = list(itertools.product(arraycode, hassimd, arraylen))


	# Convert the data into a list of dictionaries.
	testdata = [dict(x) for x in combos]

	nosimd = {'with' : '', 'without' : ', nosimd=True'}
	typconverter = dict([(x, 'int') for x in codegen_common.arraycodes])
	typconverter['f'] = 'float'
	typconverter['d'] = 'float'

	# Now go through the list and add data which goes with the ones we have already defined.
	for x in testdata:
		x['typelabel'] = x['typecode']
		x['nosimd'] = nosimd[x['simdpresent']]
		x['typeconverter'] = typconverter[x['typecode']]


	return testdata


# ==============================================================================

# ==============================================================================


# Select the basic templates.
basictemplates = {'aall' : test_template_aall, 
				'aany' : test_template_aany, 
				'findindex' : test_template_findindex
				}

nonfinitenantemplates = {'aall' : test_template_aall_nonfinite_nan, 
				'aany' : test_template_aany_nonfinite_nan, 
				'findindex' : test_template_findindex_nonfinite_nan
				}

nonfiniteinftemplates = {'aall' : test_template_aall_nonfinite_inf, 
				'aany' : test_template_aany_nonfinite_inf, 
				'findindex' : test_template_findindex_nonfinite_inf
				}


nonfiniteneginftemplates = {'aall' : test_template_aall_nonfinite_neginf, 
				'aany' : test_template_aany_nonfinite_neginf, 
				'findindex' : test_template_findindex_nonfinite_neginf
				}

# ==============================================================================


# The functions which are implemented by this program.
completefuncnames = ('aall', 'aany', 'findindex')


# ==============================================================================

# Output the functions which implement the individual non-SIMD 
# implementation functions.
for funcname in completefuncnames:

	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '20-May-2014', funcname)


	# Select the implementation template for the current function.
	testtemplate = basictemplates[funcname]

	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)

		# Basic tests.
		for gentestdata in genbasictestdata():
			# Basic tests.
			f.write(testtemplate % gentestdata)


		#####
		# Parameter tests.

		# Check each array type.
		for arraycode in codegen_common.arraycodes:

			if arraycode in codegen_common.floatarrays:
				typeconverter = 'float'
				badtypeconverter = 'int'
			else:
				typeconverter = 'int'
				badtypeconverter = 'float'

			f.write(param_template % {'funclabel' : funcname,
									'funcname' : funcname,
									'typelabel' : arraycode,
									'typecode' : arraycode,
									'typeconverter' : typeconverter,
									'badtypeconverter' : badtypeconverter,
									})



		#####
		# Parameter overflow tests.

		# Check each array type.
		for arraycode in codegen_common.arraycodes:

			# There are some array types we can't test for overflow.
			if arraycode not in 'LQd':

				if arraycode in codegen_common.floatarrays:
					overflowdec = '* 1.1'
					overflowinc = '* 1.1'
				else:
					overflowdec = '- 1'
					overflowinc = '+ 1'

				f.write(overflow_template % {'funclabel' : funcname,
										'funcname' : funcname,
										'typelabel' : arraycode,
										'typecode' : arraycode,
										'overflowdec' : overflowdec,
										'overflowinc' : overflowinc,
										})


		#####
		# Tests with non-finite data.

		# Generate all combinations of data.
		# Test nan.
		for nfdata in gennonfinitetestdata():
			f.write(nonfinitenantemplates[funcname] % nfdata)

		# Test inf.
		for nfdata in gennonfinitetestdata():
			f.write(nonfiniteinftemplates[funcname] % nfdata)

		# Test negative inf.
		for nfdata in gennonfinitetestdata():
			f.write(nonfiniteneginftemplates[funcname] % nfdata)


		#####
		# The code which initiates the unit test.

		f.write(codegen_common.testendtemplate % funcname)


# ==============================================================================
