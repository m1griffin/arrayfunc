#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for compress.
# Language: Python 3.4
# Date:     11-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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


inttestdata = {'initvalin' : 5, 'initvalout' : 6, 'selector' : '[0, 1]', 
	'zeros' : '[0]', 'ones' : '[1]', 'testtype' : 'int'}
floattestdata = {'initvalin' : 5.5, 'initvalout' : 6.6, 'selector' : '[0.0, 1.1]', 
	'zeros' : '[0.0]', 'ones' : '[1.1]', 'testtype' : 'float'}

testdata = {
	'b' : inttestdata, 'B' : inttestdata,
 
	'h' : inttestdata, 'H' : inttestdata,

	'i' : inttestdata, 'I' : inttestdata,

	'l' : inttestdata, 'L' : inttestdata,

	'q' : copy.copy(inttestdata), 'Q' : copy.copy(inttestdata),

	'f' : floattestdata, 'd' : floattestdata,
}



# This is used to insert code to convert the test data to bytes type. 
bytesconverterselector = 'selector = bytes(selector)'
bytesconverterdataout = 'dataout = bytes(dataout)'


# This is used for testing for nan, inf, -inf.
nantestdata = copy.copy(floattestdata)
nantestdata['initvalin'] = "float('nan')"
nantestdata['testtype'] = 'nan'
inftestdata = copy.copy(floattestdata)
inftestdata['initvalin'] = "float('inf')"
inftestdata['testtype'] = 'inf'
ninftestdata = copy.copy(floattestdata)
ninftestdata['initvalin'] = "float('-inf')"
ninftestdata['testtype'] = 'ninf'

nantestseq = [nantestdata, inftestdata, ninftestdata]



# ==============================================================================

op_template = '''
##############################################################################
class compress_%(testtype)s_%(typelabel)s(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.data = array.array(self.TypeCode, itertools.repeat(%(initvalin)s, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(%(initvalout)s, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(%(selector)s, 24)))


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)
			self.dataout = bytes(self.dataout)
			self.selector = bytes(self.selector)



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [%(initvalin)s] * (len(tmpdata) - len(result))
		else:
			pad = [%(initvalout)s] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  %(typelabel)s - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  %(typelabel)s - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  %(typelabel)s - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(%(zeros)s, 24)))
		%(bytesconverterselector)s

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  %(typelabel)s - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(%(ones)s, 24)))
		%(bytesconverterselector)s

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  %(typelabel)s - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(%(initvalout)s, len(self.data) // 4))
		%(bytesconverterdataout)s

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  %(typelabel)s - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(%(initvalout)s, len(self.data) * 2))
		%(bytesconverterdataout)s

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  %(typelabel)s - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  %(typelabel)s - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  %(typelabel)s - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  %(typelabel)s - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  %(typelabel)s - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  %(typelabel)s - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  %(typelabel)s - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  %(typelabel)s - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))

'''


endclass = """
##############################################################################


"""


# ==============================================================================


# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_compress', '11-Jun-2014', 'compress')

with open('test_compress.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for basic operator tests.
	for funtypes in codegen_common.arraycodes:

		datarec = {'typecode' : funtypes}
		datarec['typelabel'] = funtypes
		datarec['bytesconverterselector'] = ''
		datarec['bytesconverterdataout'] = ''
		datarec.update(testdata[funtypes])

		f.write(op_template % datarec)

		f.write(endclass)


	# Do the tests for bytes.
	datarec = testdata['B']
	datarec['typecode'] = 'B'
	datarec['typelabel'] = 'bytes'
	datarec['bytesconverterselector'] = bytesconverterselector
	datarec['bytesconverterdataout'] = bytesconverterdataout
	f.write(op_template % datarec)

	f.write(endclass)


	# Add tests for nan, inf, -inf.
	for funtypes in ('f', 'd'):
		for nantest in nantestseq:
			datarec = {'typecode' : funtypes}
			datarec['typelabel'] = funtypes
			datarec['bytesconverterselector'] = ''
			datarec['bytesconverterdataout'] = ''
			datarec.update(nantest)

			f.write(op_template % datarec)

			f.write(endclass)


	f.write(codegen_common.testendtemplate % 'compress')

