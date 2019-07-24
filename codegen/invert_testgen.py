#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for math operators with one variable.
# Language: Python 3.5
# Date:     08-Dec-2017
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

import itertools
import codegen_common


# ==============================================================================

# This template is for invert. 
test_template_invert = '''

##############################################################################
class %(funclabel)s_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
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

		if '%(arrayevenodd)s' == 'even':
			testdatasize = 160
		if '%(arrayevenodd)s' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([%(test_op_x)s]), range(testdatasize))]

		self.data = array.array('%(typecode)s', xdata)
		self.dataout = array.array('%(typecode)s', [0]*len(self.data))

		self.expected = [self.InvertPy('%(typecode)s', x) for x in self.data]

		self.limited = len(self.data) // 2

		self.expectedlimit1 = self.expected[0:self.limited] + list(self.data)[self.limited:]
		self.expectedlimit2 = self.expected[0:self.limited] + list(self.dataout)[self.limited:]


	########################################################
	def test_%(funclabel)s_inplace(self):
		"""Test %(funclabel)s in place - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.data %(nosimd)s)

		for dataoutitem, expecteditem in zip(list(self.data), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_inplace_maxlen(self):
		"""Test %(funclabel)s in place with array maxlen  - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.data, maxlen=self.limited %(nosimd)s)

		for dataoutitem, expecteditem in zip(list(self.data), self.expectedlimit1):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray(self):
		"""Test %(funclabel)s to output array - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.data, self.dataout %(nosimd)s)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_outputarray_maxlen(self):
		"""Test %(funclabel)s to output array with array maxlen  - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.data, self.dataout, maxlen=self.limited %(nosimd)s)

		for dataoutitem, expecteditem in zip(list(self.dataout), self.expectedlimit2):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''


# ==============================================================================


# The template used to generate the tests for testing invalid parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testarray1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.testarray2 = copy.copy(self.testarray1)

		arraysize = len(self.testarray1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in self.testarray1])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])



	########################################################
	def test_%(funclabel)s_array_array_a1(self):
		"""Test %(funclabel)s as *array-array* for invalid type of input array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_a2(self):
		"""Test %(funclabel)s as *array-array* for invalid type of output array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray2, self.baddataout)


##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for maxlen.
param_invalid_opt_template = '''

##############################################################################
class %(funclabel)s_opt_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('%(typecode)s', [%(test_op_x)s])
		self.inparray1b = copy.copy(self.inparray1a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_%(funclabel)s_array_none_a1(self):
		"""Test %(funclabel)s as *array-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_none_a2(self):
		"""Test %(funclabel)s as *array-none* for nosimd='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, nosimd='a')


	########################################################
	def test_%(funclabel)s_array_array_b1(self):
		"""Test %(funclabel)s as *array-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.dataout, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_b2(self):
		"""Test %(funclabel)s as *array-array* for nosimd='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.dataout, nosimd=False)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.dataout, nosimd='a')


	########################################################
	def test_%(funclabel)s_array_none_c1(self):
		"""Test %(funclabel)s as *array-none* for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_array_d1(self):
		"""Test %(funclabel)s as *array-array* for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.dataout, matherrors=True)


	########################################################
	def test_%(funclabel)s_no_params_e1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()


##############################################################################

'''

# ==============================================================================

# Test to see that invalid arrays are rejected.
test_template_invalidarray = '''

##############################################################################
class %(funclabel)s_invalidarray_%(typelabel)s(unittest.TestCase):
	"""Test for invalid arrays.
	test_template_invalidarray
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataout = array.array('%(typecode)s', [0]*len(self.data))

		self.limited = len(self.data) // 2


	########################################################
	def test_%(funclabel)s_inplace(self):
		"""Test %(funclabel)s in place - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data)


	########################################################
	def test_%(funclabel)s_inplace_maxlen(self):
		"""Test %(funclabel)s in place with array maxlen  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, maxlen=self.limited)


	########################################################
	def test_%(funclabel)s_outputarray(self):
		"""Test %(funclabel)s to output array - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, self.dataout)


	########################################################
	def test_%(funclabel)s_outputarray_maxlen(self):
		"""Test %(funclabel)s to output array with array maxlen  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.data, self.dataout, maxlen=self.limited)


##############################################################################

'''


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['test_op_templ'] == 'test_template_invert']


# ==============================================================================


for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '09-Dec-2017', funcname)

	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		for functype in codegen_common.intarrays:
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : func['test_op_x']}

			# Test for basic operation.
			# With SIMD, even data arra size.
			funcdata['simdpresent'] = 'with'
			funcdata['nosimd'] = ''
			funcdata['arrayevenodd'] = 'even'
			f.write(test_template_invert % funcdata)

			# With SIMD, odd data array size.
			funcdata['simdpresent'] = 'with'
			funcdata['nosimd'] = ''
			funcdata['arrayevenodd'] = 'odd'
			f.write(test_template_invert % funcdata)

			# Without SIMD.
			funcdata['simdpresent'] = 'without'
			funcdata['nosimd'] = ', nosimd=True'
			funcdata['arrayevenodd'] = 'even'
			f.write(test_template_invert % funcdata)


			#####


			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			# Test for invalid optional parameters such as maxlen.
			f.write(param_invalid_opt_template % funcdata)

		# Test to see that calls using unsupported arrays fail.
		for functype in codegen_common.floatarrays:
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 
				'typelabel' : functype, 'typecode' : functype}
			funcdata['test_op_x'] = ','.join([str(abs(float(x))) for x in func['test_op_x'].split(',')])

			f.write(test_template_invalidarray % funcdata)



		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

