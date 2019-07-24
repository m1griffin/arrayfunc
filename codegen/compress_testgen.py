#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for compress.
# Language: Python 3.5
# Date:     11-Jun-2014
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

op_template = '''
##############################################################################
class compress_%(testtype)s_%(testdest)s_%(typecode)s(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = '%(typecode)s'

		self.initvalin = %(initvalin)s
		self.initvalout = %(initvalout)s
		self.selector = %(selector)s

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  %(typecode)s %(testtype)s %(testdest)s - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  %(typecode)s %(testtype)s %(testdest)s - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  %(typecode)s %(testtype)s %(testdest)s - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(%(zeros)s, 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  %(typecode)s %(testtype)s %(testdest)s - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(%(ones)s, 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  %(typecode)s %(testtype)s %(testdest)s - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  %(typecode)s %(testtype)s %(testdest)s - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''



# ==============================================================================


# The template used to generate the parameter tests.
param_template = '''
##############################################################################
class compress_params_%(typecode)s(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.initvalin = %(initvalin)s
		self.initvalout = %(initvalout)s
		self.selector = %(selector)s

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  %(typecode)s - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  %(typecode)s - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  %(typecode)s - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  %(typecode)s - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  %(typecode)s - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  %(typecode)s - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  %(typecode)s - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  %(typecode)s - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################

'''

funcname = 'compress'

filenamebase = 'test_' + funcname
filename = filenamebase + '.py'
headerdate = codegen_common.FormatHeaderData(filenamebase, '11-Jun-2014', funcname)


with open(filename, 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	#####
	# Basic tests.

	# Check each array type.
	for arraycode in codegen_common.arraycodes:

		if arraycode in codegen_common.floatarrays:
			initvalin = '5.5'
			initvalout = '6.6'
			selector = '[0.0, 1.0]'
			zeros = '[0.0]'
			ones = '[1.0]'
		else:
			initvalin = '5'
			initvalout = '6'
			selector = '[0, 1]'
			zeros = '[0]'
			ones = '[1]'

		opdata = {'typecode' : arraycode,
				'initvalin' : initvalin,
				'initvalout' : initvalout,
				'selector' : selector,
				'testtype' : 'finite',
				'testdest' : 'finite',
				'zeros' : zeros,
				'ones' : ones,
				}

		f.write(op_template % opdata)
		f.write(param_template % opdata)


	# Non finite tests for parameter tests for floating point arrays.
	initvalin = (('initvalin', 'math.nan'), ('initvalin', 'math.inf'), ('initvalin', '-math.inf'))
	testtype = {'math.nan' : 'nan', 'math.inf' : 'inf', '-math.inf' : 'ninf'}

	selector = (('selector', '[0.0, math.nan]'), ('selector', '[0.0, math.inf]'), ('selector', '[0.0, -math.inf]'))
	selectortype = {'[0.0, math.nan]' : 'nan', '[0.0, math.inf]' : 'inf', '[0.0, -math.inf]' : 'ninf'}

	arraycode = [('typecode', x) for x in codegen_common.floatarrays]

	# Create a variety of input values with non-finite data.
	for opvalues in list(itertools.product(arraycode, initvalin)):
		opdata = dict(opvalues)
		# Add in labels that go with 
		opdata['testtype'] = testtype[opdata['initvalin']]
		opdata.update({'initvalout' : '6.6',
					'zeros' : '[0.0]',
					'ones' : '[1.0]',
					'selector' : '[0.0, 1.0]',
					'testdest' : 'inp'})


		f.write(op_template % opdata)


	# Create a variety of selector values with non-finite data.
	for opvalues in list(itertools.product(arraycode, selector)):
		opdata = dict(opvalues)
		# Add in labels that go with 
		opdata['testtype'] = selectortype[opdata['selector']]
		opdata.update({'initvalout' : '6.6',
					'zeros' : '[0.0]',
					'ones' : '[1.0]',
					'initvalin' : '5.5',
					'testdest' : 'sel'})


		f.write(op_template % opdata)


	#####
	# The code which initiates the unit test.

	f.write(codegen_common.testendtemplate % funcname)


# ==============================================================================
