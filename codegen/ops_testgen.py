#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for math operators.
# Language: Python 3.5
# Date:     03-Feb-2018
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

# Data generators. These are used to create test data algorithmically. These will
# vary depending on the operation being performed.


# truediv =============================================================

datafilters = { 'truediv' : '''

########################################################
def inttruediv(x, y):
	"""Perform the math operation. This needs to be specially handled
	for truediv on large signed integer arrays. This is because of a 
	combination of factors. Python will produce a floating point result, 
	but we we want an integer result when using integer arrays. If we 
	simply convert the result back to integer then we lose precision on
	large integers, introducing errors. If we try to emulate it using
	floor division, then when using mixed positive and negative inputs
	the result is rounded away from zero, producing an incorrect result.
	So, we need to take the absolute value, then do floor division, then
	put the correct sign back into the result.
	"""
	# This is intended to catch template errors and should never 
	# occur in normal usage. 

	# For true division on integer arrays.
	# For when signs are opposite in signed arrays.
	if ((x < 0) ^ (y < 0)):
		return -(abs(x) // abs(y))
	else:
		return x // y


########################################################
def filtertestdata(opvalues, minint, maxint, typecode):
	"""Filter the test data for combinations that might cause errors.
	This version is for truediv.
	"""
	# Truediv needs special handling for integer because the C function does 
	# not do actual truediv for integer.
	checkedvalues = [(x,y) for x,y in opvalues if ((y != 0) and (inttruediv(x, y) <= maxint) and (inttruediv(x, y) >= minint))]
	return checkedvalues

''',

# add =============================================================

	'add' : '''

########################################################
def filtertestdata(opvalues, minint, maxint, typecode):
	"""Filter the test data for combinations that might cause errors.
	This version is for add.
	"""
	checkedvalues = [(x,y) for x,y in opvalues if ((x + y) <= maxint) and ((x + y) >= minint)]
	return checkedvalues

''',


# floordiv =============================================================

	'floordiv' : '''


########################################################
def filtertestdata(opvalues, minint, maxint, typecode):
	"""Filter the test data for combinations that might cause errors.
	This version is for floordiv.
	"""
	# Avoid division by zero
	checkedvalues = [(x,y) for x,y in opvalues if ((y != 0) and ((x // y) <= maxint) and ((x // y) >= minint))]
	return checkedvalues

''',

# mod =============================================================

	'mod' : '''


########################################################
def filtertestdata(opvalues, minint, maxint, typecode):
	"""Filter the test data for combinations that might cause errors.
	This version is for mod.
	"""
	# Avoid division by zero
	checkedvalues = [(x,y) for x,y in opvalues if ((y != 0) and ((x % y) <= maxint) and ((x % y) >= minint))]
	return checkedvalues

''',

# mul =============================================================

	'mul' : '''

########################################################
def filtertestdata(opvalues, minint, maxint, typecode):
	"""Filter the test data for combinations that might cause errors.
	This version is for mul.
	"""
	checkedvalues = [(x,y) for x,y in opvalues if ((x * y) <= maxint) and ((x * y) >= minint)]
	return checkedvalues

''',


# pow =============================================================

	'pow' : '''

########################################################
def filtertestdata(opvalues, minint, maxint, typecode):
	"""Filter the test data for combinations that might cause errors.
	This version is for pow.
	"""
	if typecode in ('f', 'd'):
		checkedvalues = [(x, y) for x,y in opvalues if ((not((x == 0) and (y < 0))) and (minint <= (x**y) <= maxint))]
	else:
		checkedvalues = [(x, y) for x,y in opvalues if (y >= 0) and (minint <= (x**y) <= maxint)]
	return checkedvalues

''',


# sub =============================================================

	'sub' : '''

########################################################
def filtertestdata(opvalues, minint, maxint, typecode):
	"""Filter the test data for combinations that might cause errors.
	This version is for sub.
	"""
	checkedvalues = [(x,y) for x,y in opvalues if ((x - y) <= maxint) and ((x - y) >= minint)]
	return checkedvalues

''',

}

# ===


# Used for everything except pow. 
gendata_general = '''

########################################################
def gendata_special(minint, maxint, typecode):
	""" Generate data for special cases which might cause problems. 
	For integers these will be minimum and maximum values, as well as around 
	the zero point.
	"""
	# Make sure that we have coverage for data around the maximum, minimum, and zero
	# points, which we might otherwise not have with larger data sizes.
	halfpoint = (maxint + minint) // 2
	specialvals = [minint, minint + 1, minint + 2, minint + 3, 
				maxint - 3, maxint - 2, maxint - 1, maxint,
				halfpoint - 3, halfpoint - 2, halfpoint - 1, halfpoint, 
				halfpoint + 1, halfpoint + 2, halfpoint + 3, halfpoint + 4]

	# Create combinations of all of these values.
	opvalues = list(itertools.product(specialvals, specialvals))

	# Filter out values which might cause errors.
	checkedvalues = filtertestdata(opvalues, minint, maxint, typecode)

	checkedvalues.sort()

	return checkedvalues



########################################################
def gendata_int(minint, maxint, typecode):
	"""Generate data for general testing. This does not worry about edge case
	data. Edge cases must be created and tested separately. This function 
	generates a wide selection of data over the numeric range. 
	"""
	# This will generate a selection of data spread over most of the integer 
	# while giving the same amount of data for each data type.
	intrange = maxint - minint 
	stepcount = intrange // 256
	stepcount = max(stepcount, 1)
	
	spreaddata = list(range(minint, maxint + 1, stepcount))

	# Make sure we have a good selection of smaller values as well.
	if (maxint > 256):
		if minint < 0:
			mindata = -128
			maxdata = 127
		else:
			mindata = 0
			maxdata = 255

		spreaddata.extend(range(mindata, maxdata, 3))
		# Remove duplicates.
		spreaddata = list(set(spreaddata))

	# Sort the data out in order.
	spreaddata.sort()

	# Trim down the size of the sample.
	selectedspread = spreaddata[::3]

	# Create combinations of all of these values.
	opvalues = list(itertools.product(selectedspread, selectedspread))

	# Filter out values which might cause errors.
	checkedvalues = filtertestdata(opvalues, minint, maxint, typecode)

	# Sort the data out in order.
	checkedvalues.sort()

	# Now pick a smaller and more reasonable size selection over the full range.
	skipsize = len(checkedvalues) // 256
	skipsize = max(skipsize, 1)
	selectedvals = checkedvalues[::skipsize]

	return selectedvals

'''

# Used only for pow.
gendata_pow = '''

########################################################
def gendata_specialpow(minint, maxint, typecode):
	""" Generate data for special cases which might cause problems. 
	This one handles the data for pow only.
	For integers these will be minimum and maximum values, as well as around 
	the zero point.
	"""
	halfpoint = (maxint + minint) // 2
	basevals = [minint, minint + 1, minint + 2, minint + 3, 
				maxint - 3, maxint - 2, maxint - 1, maxint,
				halfpoint - 3, halfpoint - 2, halfpoint - 1, halfpoint, 
				halfpoint + 1, halfpoint + 2, halfpoint + 3, halfpoint + 4]

	# Raise to the power of 0 or 1.
	zerovals = [(x,0) for x in basevals]
	onevals = [(x,1) for x in basevals]

	# Raise 1 or zero to a power. Make sure we don't have negative powers.
	zerovals2 = [(0,x) for x in basevals if x >= 0]
	onevals2 = [(1,x) for x in basevals if x >= 0]

	# Raise some simple values to some common powers.
	if minint < 0:
		minstart = -3
	else:
		minstart = 0
	simplerange = list(range(minstart, 4))
	simplevals = list(itertools.product(simplerange, [0, 1, 2, 3, 4]))

	# These pairs were found to cause problems with some edge cases.
	# They all produce maximum negative integer for certain array types.
	# They represent tests for a variety of array types and have to be
	# filtered for each array code. 
	limitpairs = [(-2, 7), (-2, 15), (-8, 5), (-32, 3), (-2, 31),
		(-2, 63), (-8, 21), (-127, 9), (-512, 7), (-2097152, 3)]

	# Combine them all together.
	allvals = zerovals + onevals + zerovals2 + onevals2 + simplevals + limitpairs

	# Now filter them.
	checkedvalues = filtertestdata(allvals, minint, maxint, typecode)
	
	return checkedvalues


########################################################
def gendata_pow(minint, maxint, typecode):
	"""Generate data for general testing. This is specifically for pow as
	that operation has special requirements. 
	"""
	# We need two values for lval ** rval. The left hand one can be no bigger
	# than the square root of the maximum value in order to fit within the
	# data range (lval ** 2).
	lval = int(math.sqrt(maxint))

	stepcount = lval // 256
	stepcount = max(stepcount, 1)

	if minint < 0:
		lvalstart = -lval
	else:
		lvalstart = 0
	lvalspread = list(range(lvalstart, lval, stepcount))

	# Make sure we have a good selection of smaller values as well.
	if (maxint > 32768):
		if minint < 0:
			mindata = -128
			maxdata = 127
		else:
			mindata = 0
			maxdata = 255

		lvalspread.extend(range(mindata, maxdata, 3))
		# Remove duplicates.
		lvalspread = list(set(lvalspread))

	lvalspread.sort()

	# Take a few values which we will add back in later.
	lvalcentre = len(lvalspread) // 2
	extralvals = lvalspread[2:4] + lvalspread[-4:-2] + lvalspread[lvalcentre : lvalcentre + 2]

	# The right hand one (power to raise by) can be no bigger than 'x' where
	# 2 ** x. and the result is the maximum integer value.
	raisevals = {127 : 7, 255 : 8, 32767 : 15, 65535 : 16, 
		2147483647 : 31, 4294967295 : 32, 
		9223372036854775807 : 63, 18446744073709551615 : 64}
	rval = raisevals[maxint]

	# We start the range at 2 because 0 and 1 are trivial and we don't want
	# too many of them in the data mix.
	rvalspread = list(range(2, rval))


	# Create the combinations
	opvalues = list(itertools.product(lvalspread, rvalspread))

	# Filter out the values which would go out of range.
	checkedvalues = filtertestdata(opvalues, minint, maxint, typecode)
	

	# Sort the data out in order.
	checkedvalues.sort()

	# Now pick a smaller and more reasonable size selection over the full range.
	skipsize = len(checkedvalues) // 256
	skipsize = max(skipsize, 1)
	selectedvals = checkedvalues[::skipsize]

	# Create the additional values involving the trivial cases of raise
	# to the power of 0 or 1.
	additionalvals = list(itertools.product(extralvals, [0, 1]))
	selectedvals.extend(additionalvals)

	selectedvals.sort()

	return selectedvals

'''

# Used for everything including pow.
gendata_fullrange = '''

########################################################
def gendata_fullrange(minint, maxint, typecode):
	"""Generate data for general testing. Generate all combinations of data
	that do not result in an overflow. This should only be used for small integers
	as otherwise the amount of data generated is excessive.
	This version does handle pow (**) as well as other operations.
	"""
	spreaddata = list(range(minint, maxint + 1, 1))

	# Create combinations of all of these values.
	opvalues = list(itertools.product(spreaddata, spreaddata))

	# Filter out values which might cause errors.
	checkedvalues = filtertestdata(opvalues, minint, maxint, typecode)

	# Sort the data out in order.
	checkedvalues.sort()

	return checkedvalues



########################################################
def groupdata(datasample, desiredlen):
	"""This takes the data pairs and groups them together such that there is a 
	sequence and a value (e.g. ([1,2,3,4}, 9) ). The sequence groups together 
	all the values which are compatible with the value in this operation. If 
	the sequence is shorter than the desired length it is repeated as many 
	times as necessary to pad it out to the desired length.
	"""
	# This helps pad out the data for pairs which have sequences shorter than desired.
	padder = lambda x : x if len(x) > desiredlen else (x * (desiredlen // len(x))) + x[: desiredlen % len(x)]
	# Group the samples.
	return [(padder([i for i,j in x]),y) for y,x in itertools.groupby(datasample, lambda k : k[1])]


'''



# ==============================================================================

# This template is for operators (e.g. +, -, /, *, etc.).
test_op_templ = '''

##############################################################################
class %(funclabel)s_general_%(datagenerator)s_%(arrayevenodd)s_arraysize_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using numeric data.
	test_op_templ
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	##############################################################################
	def FloatListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			# NaN cannot be compared using normal means.
			if math.isnan(dataoutitem) and math.isnan(expecteditem):
				pass
			# Anything else can be compared normally.
			else:
				if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
					raise self.failureException('%%0.3f != %%0.3f at index %%d' %% (expecteditem, dataoutitem, index))


	##############################################################################
	def IntListassertEqual(self, dataout, expected, msg=None):
		"""This function is patched into assertEqual to allow testing for
		lists of integers.
		"""
		for index, (dataoutitem, expecteditem) in enumerate(zip(dataout, expected)):
			if expecteditem != dataoutitem:
				raise self.failureException('%%d != %%d at index %%d' %% (expecteditem, dataoutitem, index))



	########################################################
	@classmethod
	def setUpClass(cls):

		# For operations that support SIMD, this is intended to allow 
		# selecting data sets that fit evenly in the SIMD register width,
		# and also data sets that don't, and so require the non-SIMD
		# clean-up code to be exercised.
		# Since SIMD registers can be 256 bits wide (although not all
		# platforms, we want at least that much data for byte arrays.
		cls.simdincr = 256 // 8
		if '%(arrayevenodd)s' == 'even':
			cls.testdatasize = cls.simdincr * 4
		if '%(arrayevenodd)s' == 'odd':
			cls.testdatasize = (cls.simdincr * 4) - 1


		# For floating point values limit the test values to within
		# the range of precision so that we don't create artificial 
		# test errors due to problems related to numerical resolution.
		if '%(typecode)s' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif '%(typecode)s' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.%(typelabel)s_min
			maxval = arrayfunc.arraylimits.%(typelabel)s_max


		# Generate the test data for this set of tests.
		tdata = gendata_%(datagenerator)s(minval, maxval, '%(typecode)s')

		# If floating point, convert the data to the correct type.
		if '%(typecode)s' in ('f', 'd'):
			testdata = [(float(x), float(y)) for x,y in tdata]
		else:
			testdata = tdata


		# And separate the data pairs. 
		# This is used for array-array
		cls.datax = [x for x,y in testdata]
		cls.datay = [y for x,y in testdata]



		# Group the data samples so we have sequences to fill arrays and
		# individual values to use to perform operations on them.
		# This version provides (sequence, value) e.g. ([1,2,3] , 9)
		# This is used for array-num
		datasample = testdata
		datasample.sort(key = lambda x : x[1])
		cls.groupeddatax = groupdata(datasample, cls.testdatasize)

		
		# Swap the elements around so we can group them the other way.
		# This version provides (value, sequence) e.g. (9, [1,2,3])
		# This is used for num-array
		datasampy = [(y,x) for x,y in testdata]
		datasampy.sort(key = lambda x : x[1])

		grptmp = groupdata(datasampy, cls.testdatasize)
		# Swap them back so they are the way we expect them.
		cls.groupeddatay = [(y,x) for x,y in grptmp]



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		# These handles lists of floats and ints respectively. 
		# Without using a specialised comparison function it's not 
		# possibly to compare floats properly. These functions allow
		# for better performance on very large data sets than calling
		# assertEqual repeatedly on individual items.
		if '%(typecode)s' in ('f', 'd'):
			self.addTypeEqualityFunc(list, self.FloatListassertEqual)
		else:
			self.addTypeEqualityFunc(list, self.IntListassertEqual)



		# Make the data we want to use in the tests accessible with shorter labels.
		# This first line gives us a reference to the class containing these tests
		# as we need this to get at data created by setUpClass.
		classref = self.__class__
		self.groupeddatax = classref.groupeddatax
		self.groupeddatay = classref.groupeddatay
		self.datax = classref.datax
		self.datay = classref.datay
		self.simdincr = classref.simdincr
		


	########################################################
	def test_%(funclabel)s_check_test_data(self):
		"""Test %(funclabel)s to ensure we have valid data present - Array code %(typelabel)s.
		"""
		# Make sure we don't have any empty or trivial length data sets.
		# This test exists purely to ensure that the generated and filtered
		# data in setUp is actually present and we don't have any empty
		# data sets after we have pruned them. This condition should not
		# arise unless the test has been edited carelessly.

		self.assertTrue(len(self.datax) >= self.simdincr)
		self.assertTrue(len(self.datay) >= self.simdincr)



	########################################################
	def test_%(funclabel)s_basic_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for basic function - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)

				# Calculate the expected result.
				expected = [%(operatorfunc)s(x, testvaly) for x in testdatax]

				arrayfunc.%(funcname)s(data1, testvaly)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)

				# Calculate the expected result.
				expected = [%(operatorfunc)s(x, testvaly) for x in testdatax]

				arrayfunc.%(funcname)s(data1, testvaly, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a3(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(x, testvaly) for x in testdatax]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(data1, testvaly, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a4(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(x, testvaly) for x in testdatax]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(data1, testvaly, matherrors=True, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)



	########################################################
	def test_%(funclabel)s_basic_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for basic function - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				# Calculate the expected result.
				expected = [%(operatorfunc)s(x, testvaly) for x in testdatax]

				arrayfunc.%(funcname)s(data1, testvaly, dataout)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				# Calculate the expected result.
				expected = [%(operatorfunc)s(x, testvaly) for x in testdatax]

				arrayfunc.%(funcname)s(data1, testvaly, dataout, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(x, testvaly) for x in testdatax]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(data1, testvaly, dataout, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b4(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testdatax, testvaly in self.groupeddatax:
			with self.subTest(msg='Failed with parameter', testval = (testdatax, testvaly)):

				data1 = array.array('%(typecode)s', testdatax)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(x, testvaly) for x in testdatax]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(data1, testvaly, dataout, matherrors=True, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)



	########################################################
	def test_%(funclabel)s_basic_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for basic function - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)

				# Calculate the expected result.
				expected = [%(operatorfunc)s(testvalx, y) for y in testdatay]

				arrayfunc.%(funcname)s(testvalx, data1)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)

				# Calculate the expected result.
				expected = [%(operatorfunc)s(testvalx, y) for y in testdatay]

				arrayfunc.%(funcname)s(testvalx, data1, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c3(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(testvalx, y) for y in testdatay]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(testvalx, data1, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c4(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(testvalx, y) for y in testdatay]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(testvalx, data1, matherrors=True, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)



	########################################################
	def test_%(funclabel)s_basic_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for basic function - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				# Calculate the expected result.
				expected = [%(operatorfunc)s(testvalx, y) for y in testdatay]

				arrayfunc.%(funcname)s(testvalx, data1, dataout)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				# Calculate the expected result.
				expected = [%(operatorfunc)s(testvalx, y) for y in testdatay]

				arrayfunc.%(funcname)s(testvalx, data1, dataout, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d3(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(testvalx, y) for y in testdatay]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(testvalx, data1, dataout, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d4(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testvalx, testdatay in self.groupeddatay:
			with self.subTest(msg='Failed with parameter', testval = (testvalx, testdatay)):

				data1 = array.array('%(typecode)s', testdatay)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				# Calculate the expected result.
				pydataout = [%(operatorfunc)s(testvalx, y) for y in testdatay]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(testvalx, data1, dataout, matherrors=True, maxlen=limited)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)



	########################################################
	def test_%(funclabel)s_basic_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)

		expected = [%(operatorfunc)s(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.%(funcname)s(data1, data2)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)

		expected = [%(operatorfunc)s(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.%(funcname)s(data1, data2, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e3(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)

		limited = len(data1) // 2

		pydataout = [%(operatorfunc)s(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.%(funcname)s(data1, data2, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e4(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)

		limited = len(data1) // 2

		pydataout = [%(operatorfunc)s(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.%(funcname)s(data1, data2, matherrors=True, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)
		dataout = array.array('%(typecode)s', [0]*len(data1))

		expected = [%(operatorfunc)s(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.%(funcname)s(data1, data2, dataout)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)
		dataout = array.array('%(typecode)s', [0]*len(data1))

		expected = [%(operatorfunc)s(x, y) for (x, y) in zip(data1, data2)]

		arrayfunc.%(funcname)s(data1, data2, dataout, matherrors=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_f3(self):
		"""Test %(funclabel)s as *array-array-array* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)
		dataout = array.array('%(typecode)s', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [%(operatorfunc)s(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.%(funcname)s(data1, data2, dataout, matherrors=True, maxlen=limited)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(dataout), expected)



##############################################################################

'''

# ==============================================================================

# This template is for operators (e.g. +, -, *, etc.) which have SIMD support.
test_op_simd_templ = ''' 

##############################################################################
class %(funclabel)s_general_%(arrayevenodd)s_arraysize_simd_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using numeric 
	data %(test_op_y)s.
	test_op_simd_templ
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		if '%(arrayevenodd)s' == 'even':
			testdatasize = 160
		if '%(arrayevenodd)s' == 'odd':
			testdatasize = 159
		paramitersize = 10

		xdata = [x for x,y in zip(itertools.cycle([%(test_op_x)s]), range(testdatasize))]
		self.datax = array.array('%(typecode)s', xdata)
		self.datay = [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.datax)]


		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.dataxparam = self.datax[:paramitersize]
		self.datayparam = self.datay[:paramitersize]


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datax)

				expected = %(typeconv1)s [x %(pyoperator)s testval for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(data1, testval)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datax)

				expected = %(typeconv1)s [x %(pyoperator)s testval for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(data1, testval, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a3(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True and nosimd=True - Array code %(typelabel)s.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datax)

				expected = %(typeconv1)s [x %(pyoperator)s testval for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(data1, testval, matherrors=True, nosimd=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)



	########################################################
	def test_%(funclabel)s_basic_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datax)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = %(typeconv1)s [x %(pyoperator)s testval for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(data1, testval, dataout)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datax)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = %(typeconv1)s [x %(pyoperator)s testval for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(data1, testval, dataout, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True and nosimd=True - Array code %(typelabel)s.
		"""
		for testval in self.datayparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datax)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = %(typeconv1)s [x %(pyoperator)s testval for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(data1, testval, dataout, matherrors=True, nosimd=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)



	########################################################
	def test_%(funclabel)s_basic_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datay)

				expected = %(typeconv1)s [testval %(pyoperator)s x for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(testval, data1)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datay)

				expected = %(typeconv1)s [testval %(pyoperator)s x for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(testval, data1, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c3(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with matherrors=True and nosimd=True - Array code %(typelabel)s.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datay)

				expected = %(typeconv1)s [testval %(pyoperator)s x for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(testval, data1, matherrors=True, nosimd=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(data1), expected)



	########################################################
	def test_%(funclabel)s_basic_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for basic function - Array code %(typelabel)s.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datay)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = %(typeconv1)s [testval %(pyoperator)s x for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(testval, data1, dataout)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datay)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = %(typeconv1)s [testval %(pyoperator)s x for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(testval, data1, dataout, matherrors=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d3(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with matherrors=True and nosimd=True - Array code %(typelabel)s.
		"""
		for testval in self.dataxparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', self.datay)
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = %(typeconv1)s [testval %(pyoperator)s x for x in data1] %(typeconv2)s

				arrayfunc.%(funcname)s(testval, data1, dataout, matherrors=True, nosimd=True)

				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(list(dataout), expected)



	########################################################
	def test_%(funclabel)s_basic_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)

		expected = %(typeconv1)s [x %(pyoperator)s y for (x, y) in zip(data1, data2)] %(typeconv2)s
		arrayfunc.%(funcname)s(data1, data2)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with matherrors=True and nosimd=Tru - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)

		expected = %(typeconv1)s [x %(pyoperator)s y for (x, y) in zip(data1, data2)] %(typeconv2)s
		arrayfunc.%(funcname)s(data1, data2, matherrors=True, nosimd=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(data1), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)
		dataout = array.array('%(typecode)s', [0]*len(data1))

		expected = %(typeconv1)s [x %(pyoperator)s y for (x, y) in zip(data1, data2)] %(typeconv2)s
		arrayfunc.%(funcname)s(data1, data2, dataout)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(dataout), expected)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for basic function and nosimd=True - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', self.datax)
		data2 = array.array('%(typecode)s', self.datay)
		dataout = array.array('%(typecode)s', [0]*len(data1))

		expected = %(typeconv1)s [x %(pyoperator)s y for (x, y) in zip(data1, data2)] %(typeconv2)s
		arrayfunc.%(funcname)s(data1, data2, dataout, matherrors=True, nosimd=True)

		# The behavour of assertEqual is modified by addTypeEqualityFunc.
		self.assertEqual(list(dataout), expected)




##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for simd option.
param_invalid_opt_simd_template = '''

##############################################################################
class %(funclabel)s_opt_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid errors for simd option.
	param_invalid_opt_simd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('%(typecode)s', [%(test_op_x)s])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('%(typecode)s', itertools.repeat(%(zero_const)s, arraysize))



	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, nosimd='a')



	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, nosimd='a')



	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, nosimd='a')



	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, nosimd='a')



	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for nosimd='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, nosimd='a')



	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for nosimd='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

'''

# ==============================================================================

# ==============================================================================



# The template used to generate the tests for testing invalid array and
# numeric parameter types.
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
		self.testarray2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.testarray1)])

		arraysize = len(self.testarray1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(%(zero_const)s, arraysize))

		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('%(badcode)s', [%(badconv)s(x) for x in self.testarray1])
		self.badarray2 = array.array('%(badcode)s', [%(badconv)s(x) for x in self.testarray2])

		self.baddataout = array.array('%(badcode)s', [%(badconv)s(x) for x in self.dataout])


	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for invalid type of array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(badarray1, testvalue)


	########################################################
	def test_%(funclabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for invalid type of number - Array code %(typelabel)s.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testarray1, badvalue)



	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for invalid type of array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(badarray1, testvalue, self.dataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for invalid type of number - Array code %(typelabel)s.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for invalid type of output array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testarray1, testvalue, self.baddataout)



	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for invalid type of array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, badarray2)


	########################################################
	def test_%(funclabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for invalid type of number - Array code %(typelabel)s.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(badvalue, testarray2)



	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for invalid type of array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for invalid type of number - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d3(self):
		"""Test %(funclabel)s as *num-array-array* for invalid type of output array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for invalid type of array - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testarray1, self.badarray2)


	########################################################
	def test_%(funclabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for invalid type of array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.testarray2)



	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for invalid type of array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for invalid type of array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f3(self):
		"""Test %(funclabel)s as *array-array-array* for invalid type of output array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_%(funclabel)s_no_params_g1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()



##############################################################################

'''

# ==============================================================================

# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for errors flag and maxlen.
param_invalid_opt_template = '''

##############################################################################
class %(funclabel)s_opt_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid errors flag and maxlen parameters.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('%(typecode)s', [%(test_op_x)s])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.inparray1a)])
		self.inparray2b = copy.copy(self.inparray2a)

		arraysize = len(self.inparray1a)

		self.dataout = array.array('%(typecode)s', itertools.repeat(%(zero_const)s, arraysize))

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for matherrors='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, matherrors='a')


	########################################################
	def test_%(funclabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for matherrors='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, matherrors='a')


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for matherrors='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, matherrors=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, matherrors='a')


	########################################################
	def test_%(funclabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for matherrors='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_%(funclabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for matherrors='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, matherrors='a')


	########################################################
	def test_%(funclabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for maxlen='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for matherrors='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, matherrors='a')


	########################################################
	def test_%(funclabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for maxlen='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')



##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected.
nan_data_error_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using parameter %(errordata)s.
	nan_data_error_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataok2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x %(pyoperator)s testval for x in self.errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x %(pyoperator)s testval for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(testval, errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval %(pyoperator)s x for x in self.errordata]

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval %(pyoperator)s x for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(dataok1, self.errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [y %(pyoperator)s x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [y %(pyoperator)s x for x,y in zip(self.errordata, self.dataok1)]

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected. This is a special version for division.
nan_div_data_error_template = '''

##############################################################################
class %(funclabel)s_div_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using parameter %(errordata)s.
	This version is for division operations where division by inf and -inf 
	results in zero.
	nan_div_data_error_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataok2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x %(pyoperator)s testval for x in self.errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x %(pyoperator)s testval for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [testval %(pyoperator)s x for x in self.errordata]

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [testval %(pyoperator)s x for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [x %(pyoperator)s y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [x %(pyoperator)s y for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected. This is a special version for division.
inf_floordiv_data_error_template = '''

##############################################################################
class %(funclabel)s_div_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using parameter %(errordata)s.
	This version is for division operations where division by inf and -inf 
	results in zero.
	inf_floordiv_data_error_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataok2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				# Inf divided by anything other than 0, inf, or nan, is inf. 
				# We need to calculate this as follows in order to transfer the
				# sign over correctly.
				expected = [x / testval for x in self.errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Inf divided by anything other than 0, inf, or nan, is inf. 
				# We need to calculate this as follows in order to transfer the
				# sign over correctly.
				expected = [x / testval for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				# The underlying C library 
				expected = [math.floor(testval / x) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.floor(testval / x) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [math.floor(x / y) for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [math.floor(x / y) for x,y in zip(self.dataok1, self.errordata)]

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows using maximum value.
param_overflow_max_template = '''

##############################################################################
class %(funclabel)s_overflow_max_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for value overflow for max value.
	param_overflow_max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.incvalue = %(incvalue)s
		self.zero_const = %(zero_const)s


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)


		self.inparray2amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zeroarray = array.array('%(typecode)s', [self.zero_const] * arraysize)
		self.incvaluearray = array.array('%(typecode)s', [self.incvalue] * arraysize)


		self.dataout = array.array('%(typecode)s', itertools.repeat(self.zero_const, arraysize))



	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amax, self.zero_const)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmax, self.incvalue)


	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amax, self.zero_const, self.dataout)


		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmax, self.incvalue, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zero_const, self.inparray2amax)


		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvalue, self.inparray2bmax)


	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zero_const, self.inparray2amax, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvalue, self.inparray2bmax, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amax, self.zeroarray)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmax, self.incvaluearray)


	########################################################
	def test_%(funclabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroarray, self.inparray1amax)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvaluearray, self.inparray1bmax)


	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amax, self.zeroarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmax, self.incvaluearray, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for max value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroarray, self.inparray1amax, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvaluearray, self.inparray1bmax, self.dataout)


##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for overflows using minimum value.
param_overflow_min_template = '''

##############################################################################
class %(funclabel)s_overflow_min_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for value overflow for min value.
	param_overflow_min_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min
		self.incvalue = %(decvalue)s
		self.zero_const = %(zero_const)s


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.inparray2amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray2bmin = copy.copy(self.inparray2amin)


		self.zeroarray = array.array('%(typecode)s', [self.zero_const] * arraysize)
		self.incvaluearray = array.array('%(typecode)s', [self.incvalue] * arraysize)


		self.dataout = array.array('%(typecode)s', itertools.repeat(self.zero_const, arraysize))



	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amin, self.zero_const)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmin, self.incvalue)


	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amin, self.zero_const, self.dataout)


		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmin, self.incvalue, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zero_const, self.inparray2amin)


		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvalue, self.inparray2bmin)


	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zero_const, self.inparray2amin, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvalue, self.inparray2bmin, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amin, self.zeroarray)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmin, self.incvaluearray)


	########################################################
	def test_%(funclabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroarray, self.inparray1amin)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvaluearray, self.inparray1bmin)


	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1amin, self.zeroarray, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.inparray1bmin, self.incvaluearray, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for min value + 1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.zeroarray, self.inparray1amin, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(errorflagexceptioncode)s):
			arrayfunc.%(funcname)s(self.incvaluearray, self.inparray1bmin, self.dataout)


##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for overflows using maximum value.
param_overflow_add_max1_template = '''

##############################################################################
class overflow_signed_max1_%(typelabel)s(unittest.TestCase):
	"""Test add for value overflow for max values.
	param_overflow_add_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(floatpad)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_add_array_num_none_a1(self):
		"""Test add as *array-num-none* for max value + 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amax, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmax, 1%(floatpad)s)


	########################################################
	def test_add_array_num_array_a2(self):
		"""Test add as *array-num-array* for max value + 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amax, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmax, 1%(floatpad)s, self.dataout)


	########################################################
	def test_add_num_array_none_a3(self):
		"""Test add as *num-array-none* for max value + 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.MaxLimit, self.plus1array)


	########################################################
	def test_add_num_array_array_a4(self):
		"""Test add as *num-array-array* for max value + 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.MaxLimit, self.plus1array, self.dataout)


	########################################################
	def test_add_array_array_none_a5(self):
		"""Test add as *array-array-none* for max value + 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmax, self.plus1array)


	########################################################
	def test_add_array_array_array_a6(self):
		"""Test add as *array-array-array* for max value + 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmax, self.plus1array, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_add_min1_template = '''

##############################################################################
class overflow_signed_min1_%(typelabel)s(unittest.TestCase):
	"""Test add for value overflow for min values.
	param_overflow_add_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.minus1array = array.array('%(typecode)s', [-1%(floatpad)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_add_array_num_none_b1(self):
		"""Test add as *array-num-none* for min value + -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amin, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmin, -1%(floatpad)s)


	########################################################
	def test_add_array_num_array_b2(self):
		"""Test add as *array-num-array* for min value + -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amin, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmin, -1%(floatpad)s, self.dataout)


	########################################################
	def test_add_num_array_none_b3(self):
		"""Test add as *num-array-none* for min value + -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.MinLimit, self.minus1array)


	########################################################
	def test_add_num_array_array_b4(self):
		"""Test add as *num-array-array* for min value + -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_add_array_num_none_b5(self):
		"""Test add as *array-array-none* for min value + -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmin, self.minus1array)


	########################################################
	def test_add_array_num_none_b6(self):
		"""Test add as *array-array-array* for min value + -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.add(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.add(self.inparray1bmin, self.minus1array, self.dataout)



##############################################################################

'''


# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows using maximum value.
param_overflow_sub_max1_template = '''

##############################################################################
class overflow_signed_max1_%(typelabel)s(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_max1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.minus1array = array.array('%(typecode)s', [-1%(floatpad)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_sub_array_num_none_a1(self):
		"""Test sub as *array-num-none* for max value - -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmax, -1%(floatpad)s)


	########################################################
	def test_sub_array_num_array_a2(self):
		"""Test sub as *array-num-array* for max value - -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmax, -1%(floatpad)s, self.dataout)


	########################################################
	def test_sub_num_array_none_a3(self):
		"""Test sub as *num-array-none* for max value - -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.MaxLimit, self.minus1array)


	########################################################
	def test_sub_num_array_array_a4(self):
		"""Test sub as *num-array-array* for max value - -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.MaxLimit, self.minus1array, self.dataout)


	########################################################
	def test_sub_array_array_none_a5(self):
		"""Test sub as *array-array-none* for max value - -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmax, self.minus1array)


	########################################################
	def test_sub_array_array_array_a6(self):
		"""Test sub as *array-array-array* for max value - -1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmax, self.minus1array, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_sub_min1_template = '''

##############################################################################
class overflow_signed_min1_%(typelabel)s(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_min1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(floatpad)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_sub_array_num_none_b1(self):
		"""Test sub as *array-num-none* for min value - 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmin, 1%(floatpad)s)


	########################################################
	def test_sub_array_num_array_b2(self):
		"""Test sub as *array-num-array* for min value - 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmin, 1%(floatpad)s, self.dataout)


	########################################################
	def test_sub_num_array_none_b3(self):
		"""Test sub as *num-array-none* for min value - 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.MinLimit, self.plus1array)


	########################################################
	def test_sub_num_array_array_b4(self):
		"""Test sub as *num-array-array* for min value - 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.MinLimit, self.plus1array, self.dataout)


	########################################################
	def test_sub_array_num_none_b5(self):
		"""Test sub as *array-array-none* for min value - 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmin, self.plus1array)


	########################################################
	def test_sub_array_num_none_b6(self):
		"""Test sub as *array-array-array* for min value - 1%(floatpad)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.inparray1bmin, self.plus1array, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using maximum value.
param_overflow_sub_1max_template = '''

##############################################################################
class overflow_signed_1max_%(typelabel)s(unittest.TestCase):
	"""Test sub for value overflow for max values.
	param_overflow_sub_1max_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray2amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.minus1array = array.array('%(typecode)s', [-1%(floatpad)s] * arraysize)
		self.minus2array = array.array('%(typecode)s', [-2%(floatpad)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_sub_array_num_none_c1(self):
		"""Test sub as *array-num-none* for -2%(floatpad)s - max value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.minus2array, self.MaxLimit)


	########################################################
	def test_sub_array_num_array_c2(self):
		"""Test sub as *array-num-array* for -2%(floatpad)s - max value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.minus2array, self.MaxLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_c3(self):
		"""Test sub as *num-array-none* for -2%(floatpad)s - max value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2%(floatpad)s, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(-2%(floatpad)s, self.inparray2bmax)


	########################################################
	def test_sub_num_array_array_c4(self):
		"""Test sub as *num-array-array* for -2%(floatpad)s - max value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(-2%(floatpad)s, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(-2%(floatpad)s, self.inparray2bmax, self.dataout)


	########################################################
	def test_sub_array_array_none_c5(self):
		"""Test sub as *array-array-none* for -2%(floatpad)s - max value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.minus2array, self.inparray2bmax)


	########################################################
	def test_sub_array_array_array_c6(self):
		"""Test sub as *array-array-array* for -2%(floatpad)s - max value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.minus1array, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.minus2array, self.inparray2bmax, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_sub_1min_template = '''

##############################################################################
class overflow_signed_1min_%(typelabel)s(unittest.TestCase):
	"""Test sub for value overflow for min values.
	param_overflow_sub_1min_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_sub_array_num_none_d1(self):
		"""Test sub as *array-num-none* for 1%(floatpad)s - min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.zero2array, self.MinLimit)


	########################################################
	def test_sub_array_num_array_d2(self):
		"""Test sub as *array-num-array* for 1%(floatpad)s - min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.zero2array, self.MinLimit, self.dataout)


	########################################################
	def test_sub_num_array_none_d3(self):
		"""Test sub as *num-array-none* for 1%(floatpad)s - min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0%(decimalpoint)s, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(0%(decimalpoint)s, self.inparray1bmin)


	########################################################
	def test_sub_num_array_array_d4(self):
		"""Test sub as *num-array-array* for 1%(floatpad)s - min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(0%(decimalpoint)s, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(0%(decimalpoint)s, self.inparray1bmin, self.dataout)


	########################################################
	def test_sub_array_array_none_d5(self):
		"""Test sub as *array-array-none* for 1%(floatpad)s - min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.zero2array, self.inparray1bmin)


	########################################################
	def test_sub_array_array_array_d6(self):
		"""Test sub as *array-array-array* for 1%(floatpad)s - min value - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.sub(self.zero1array, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.sub(self.zero2array, self.inparray1bmin, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using maximum value.
param_overflow_mul_max2_template = '''

##############################################################################
class overflow_signed_max2_%(typelabel)s(unittest.TestCase):
	"""Test mul for value overflow for max values.
	param_overflow_mul_max2_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus2array = array.array('%(typecode)s', [2%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_mul_array_num_none_a1(self):
		"""Test mul as *array-num-none* for max value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amax, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmax, 2%(decimalpoint)s)


	########################################################
	def test_mul_array_num_array_a2(self):
		"""Test mul as *array-num-array* for max value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amax, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmax, 2%(decimalpoint)s, self.dataout)


	########################################################
	def test_mul_num_array_none_a3(self):
		"""Test mul as *num-array-none* for max value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.MaxLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.MaxLimit, self.plus2array)


	########################################################
	def test_mul_num_array_array_a4(self):
		"""Test mul as *num-array-array* for max value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.MaxLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.MaxLimit, self.plus2array, self.dataout)


	########################################################
	def test_mul_array_array_none_a5(self):
		"""Test mul as *array-array-none* for max value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amax, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmax, self.plus2array)


	########################################################
	def test_mul_array_array_array_a6(self):
		"""Test mul as *array-array-array* for max value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amax, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmax, self.plus2array, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_mul_min2_template = '''

##############################################################################
class overflow_signed_min2_%(typelabel)s(unittest.TestCase):
	"""Test mul for value overflow for min values.
	param_overflow_mul_min2_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus2array = array.array('%(typecode)s', [2%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_mul_array_num_none_b1(self):
		"""Test mul as *array-num-none* for min value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, 2%(decimalpoint)s)


	########################################################
	def test_mul_array_num_array_b2(self):
		"""Test mul as *array-num-array* for min value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, 2%(decimalpoint)s, self.dataout)


	########################################################
	def test_mul_num_array_none_b3(self):
		"""Test mul as *num-array-none* for min value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.MinLimit, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.MinLimit, self.plus2array)


	########################################################
	def test_mul_num_array_array_b4(self):
		"""Test mul as *num-array-array* for min value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.MinLimit, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.MinLimit, self.plus2array, self.dataout)


	########################################################
	def test_mul_array_num_none_b5(self):
		"""Test mul as *array-array-none* for min value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, self.plus2array)


	########################################################
	def test_mul_array_num_none_b6(self):
		"""Test mul as *array-array-array* for min value * 2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, self.plus2array, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using maximum value.
param_overflow_mul_max2neg_template = '''

##############################################################################
class overflow_signed_max2neg_%(typelabel)s(unittest.TestCase):
	"""Test mul for value overflow for max values.
	param_overflow_mul_max2neg_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray2amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray2bmax = copy.copy(self.inparray2amax)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.minus1array = array.array('%(typecode)s', [-1%(decimalpoint)s] * arraysize)
		self.minus2aarray = array.array('%(typecode)s', [-2%(decimalpoint)s] * arraysize)
		self.minus2barray = array.array('%(typecode)s', [-2%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_mul_array_num_none_c1(self):
		"""Test mul as *array-num-none* for max value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray2amax, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray2bmax, -2%(decimalpoint)s)


	########################################################
	def test_mul_array_num_array_c2(self):
		"""Test mul as *array-num-array* for max value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray2amax, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray2bmax, -2%(decimalpoint)s, self.dataout)


	########################################################
	def test_mul_num_array_none_c3(self):
		"""Test mul as *num-array-none* for max value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(-2%(decimalpoint)s, self.zero1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(-2%(decimalpoint)s, self.inparray2bmax)


	########################################################
	def test_mul_num_array_array_c4(self):
		"""Test mul as *num-array-array* for max value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(-2%(decimalpoint)s, self.zero1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(-2%(decimalpoint)s, self.inparray2bmax, self.dataout)


	########################################################
	def test_mul_array_array_none_c5(self):
		"""Test mul as *array-array-none* for max value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.minus1array, self.inparray2amax)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.minus2barray, self.inparray2bmax)


	########################################################
	def test_mul_array_array_array_c6(self):
		"""Test mul as *array-array-array* for max value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.minus1array, self.inparray2amax, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.minus2barray, self.inparray2bmax, self.dataout)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_mul_min2neg_template = '''

##############################################################################
class overflow_signed_min2neg_%(typelabel)s(unittest.TestCase):
	"""Test mul for value overflow for min values.
	param_overflow_mul_min2neg_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)
		self.minus2aarray = array.array('%(typecode)s', [-2%(decimalpoint)s] * arraysize)
		self.minus2barray = array.array('%(typecode)s', [-2%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_mul_array_num_none_d1(self):
		"""Test mul as *array-num-none* for min value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, -2%(decimalpoint)s)


	########################################################
	def test_mul_array_num_array_d2(self):
		"""Test mul as *array-num-array* for min value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, -2%(decimalpoint)s, self.dataout)


	########################################################
	def test_mul_num_array_none_d3(self):
		"""Test mul as *num-array-none* for min value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(0%(decimalpoint)s, self.inparray1amin)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(-2%(decimalpoint)s, self.inparray1bmin)


	########################################################
	def test_mul_num_array_array_d4(self):
		"""Test mul as *num-array-array* for min value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(0%(decimalpoint)s, self.inparray1amin, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(-2%(decimalpoint)s, self.inparray1bmin, self.dataout)


	########################################################
	def test_mul_array_array_none_d5(self):
		"""Test mul as *array-array-none* for min value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.minus2aarray, self.zero3array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.minus2barray, self.inparray1bmin)


	########################################################
	def test_mul_array_array_array_d6(self):
		"""Test mul as *array-array-array* for min value * -2%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.minus2aarray, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.minus2barray, self.inparray1bmin, self.dataout)



##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_mul_min1neg_template = '''

##############################################################################
class overflow_signed_min1neg_%(typelabel)s(unittest.TestCase):
	"""Test mul for value overflow for min values.
	param_overflow_mul_min1neg_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.zero2array = copy.copy(self.zero1array)
		self.zero3array = copy.copy(self.zero1array)
		self.minus1aarray = array.array('%(typecode)s', [-1%(decimalpoint)s] * arraysize)
		self.minus1barray = array.array('%(typecode)s', [-1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_mul_array_num_none_e1(self):
		"""Test mul as *array-num-none* for min value * -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, 0%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, -1%(decimalpoint)s)


	########################################################
	def test_mul_array_num_array_e2(self):
		"""Test mul as *array-num-array* for min value * -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.inparray1amin, 0%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.inparray1bmin, -1%(decimalpoint)s, self.dataout)


	########################################################
	def test_mul_num_array_none_e3(self):
		"""Test mul as *num-array-none* for min value * -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(0%(decimalpoint)s, self.inparray1amin)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(-1%(decimalpoint)s, self.inparray1bmin)


	########################################################
	def test_mul_num_array_array_e4(self):
		"""Test mul as *num-array-array* for min value * -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(0%(decimalpoint)s, self.inparray1amin, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(-1%(decimalpoint)s, self.inparray1bmin, self.dataout)


	########################################################
	def test_mul_array_array_none_e5(self):
		"""Test mul as *array-array-none* for min value * -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.minus1aarray, self.zero3array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.minus1barray, self.inparray1bmin)


	########################################################
	def test_mul_array_array_array_e6(self):
		"""Test mul as *array-array-array* for min value * -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mul(self.minus1aarray, self.zero3array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.mul(self.minus1barray, self.inparray1bmin, self.dataout)



##############################################################################

'''

# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows with divide by zero.
param_overflow_truediv_divzero_template = '''

##############################################################################
class overflow_signed_divzero_%(typelabel)s(unittest.TestCase):
	"""Test truediv for value divide by zero.
	param_overflow_truediv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0%(decimalpoint)s)


	########################################################
	def test_truediv_array_num_array_a2(self):
		"""Test truediv as *array-num-array* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0%(decimalpoint)s, self.dataout)


	########################################################
	def test_truediv_num_array_none_a3(self):
		"""Test truediv as *num-array-none* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array)


	########################################################
	def test_truediv_num_array_array_a4(self):
		"""Test truediv as *num-array-array* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_truediv_array_array_none_a5(self):
		"""Test truediv as *array-array-none* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_truediv_array_array_array_a6(self):
		"""Test truediv as *array-array-array* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################

'''


# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows with divide by zero with
# overflow checking disabled.
param_overflow_truediv_divzero_errors_template = '''

##############################################################################
class overflow_signed_divzero_errors_%(typelabel)s(unittest.TestCase):
	"""Test truediv for value divide by zero with overflow checking disabled.
	param_overflow_truediv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_truediv_array_num_none_b1(self):
		"""Test truediv as *array-num-none* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1%(decimalpoint)s, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0%(decimalpoint)s, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, 1%(decimalpoint)s, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, 0%(decimalpoint)s, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_b3(self):
		"""Test truediv as *num-array-none* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_b4(self):
		"""Test truediv as *num-array-array* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_array_none_b5(self):
		"""Test truediv as *array-array-none* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_truediv_array_array_array_b6(self):
		"""Test truediv as *array-array-array* for max value / 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.truediv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_truediv_mindivminus1_template = '''

##############################################################################
class overflow_signed_mindivminus1_%(typelabel)s(unittest.TestCase):
	"""Test truediv for value overflow for min values divided by -1.
	param_overflow_truediv_mindivminus1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)
		self.minus1array = array.array('%(typecode)s', [-1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_truediv_array_num_none_a1(self):
		"""Test truediv as *array-num-none* for min value / -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, -1%(decimalpoint)s)


	########################################################
	def test_truediv_array_num_none_a2(self):
		"""Test truediv as *array-num-none* for min value / -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1%(decimalpoint)s, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, -1%(decimalpoint)s, matherrors=True)


	########################################################
	def test_truediv_array_num_array_b1(self):
		"""Test truediv as *array-num-array* for min value / -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, -1%(decimalpoint)s, self.dataout)


	########################################################
	def test_truediv_array_num_array_b2(self):
		"""Test truediv as *array-num-array* for min value / -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, 1%(decimalpoint)s, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, -1%(decimalpoint)s, self.dataout, matherrors=True)


	########################################################
	def test_truediv_num_array_none_c1(self):
		"""Test truediv as *num-array-none* for min value / -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.MinLimit, self.minus1array)


	########################################################
	def test_truediv_num_array_none_c2(self):
		"""Test truediv as *num-array-none* for min value / -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.MinLimit, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_num_array_array_d1(self):
		"""Test truediv as *num-array-array* for min value / -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_truediv_num_array_array_d2(self):
		"""Test truediv as *num-array-array* for min value / -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.MinLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.MinLimit, self.minus1array, self.dataout, matherrors=True)


	########################################################
	def test_truediv_array_num_none_e1(self):
		"""Test truediv as *array-array-none* for min value / -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array)


	########################################################
	def test_truediv_array_num_none_e2(self):
		"""Test truediv as *array-array-none* for min value / -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, matherrors=True)


	########################################################
	def test_truediv_array_num_none_f1(self):
		"""Test truediv as *array-array-array* for min value / -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout)


	########################################################
	def test_truediv_array_num_none_f2(self):
		"""Test truediv as *array-array-array* for min value / -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.truediv(self.inparray1amin, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.truediv(self.inparray1bmin, self.minus1array, self.dataout, matherrors=True)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows with divide by zero.
param_overflow_floordiv_divzero_template = '''

##############################################################################
class overflow_signed_divzero_%(typelabel)s(unittest.TestCase):
	"""Test floordiv for value divide by zero.
	param_overflow_floordiv_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_floordiv_array_num_none_a1(self):
		"""Test floordiv as *array-num-none* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, 1%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, 0%(decimalpoint)s)


	########################################################
	def test_floordiv_array_num_array_a2(self):
		"""Test floordiv as *array-num-array* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, 1%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, 0%(decimalpoint)s, self.dataout)


	########################################################
	def test_floordiv_num_array_none_a3(self):
		"""Test floordiv as *num-array-none* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.MaxLimit, self.zero1array)


	########################################################
	def test_floordiv_num_array_array_a4(self):
		"""Test floordiv as *num-array-array* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_floordiv_array_array_none_a5(self):
		"""Test floordiv as *array-array-none* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, self.zero1array)


	########################################################
	def test_floordiv_array_array_array_a6(self):
		"""Test floordiv as *array-array-array* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################

'''


# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows with divide by zero with
# overflow checking disabled.
param_overflow_floordiv_divzero_errors_template = '''

##############################################################################
class overflow_signed_divzero_errors_%(typelabel)s(unittest.TestCase):
	"""Test floordiv for value divide by zero with overflow checking disabled.
	param_overflow_floordiv_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_floordiv_array_num_none_b1(self):
		"""Test floordiv as *array-num-none* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, 1%(decimalpoint)s, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, 0%(decimalpoint)s, matherrors=True)


	########################################################
	def test_floordiv_array_num_array_b2(self):
		"""Test floordiv as *array-num-array* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, 1%(decimalpoint)s, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, 0%(decimalpoint)s, self.dataout, matherrors=True)


	########################################################
	def test_floordiv_num_array_none_b3(self):
		"""Test floordiv as *num-array-none* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_floordiv_num_array_array_b4(self):
		"""Test floordiv as *num-array-array* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_floordiv_array_array_none_b5(self):
		"""Test floordiv as *array-array-none* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_floordiv_array_array_array_b6(self):
		"""Test floordiv as *array-array-array* for max value // 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.floordiv(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows using minimum value.
param_overflow_floordiv_mindivminus1_template = '''

##############################################################################
class overflow_signed_mindivminus1_%(typelabel)s(unittest.TestCase):
	"""Test floordiv for value overflow for min values divided by -1.
	param_overflow_floordiv_mindivminus1_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amin = array.array('%(typecode)s', [self.MinLimit] * arraysize)
		self.inparray1bmin = copy.copy(self.inparray1amin)


		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)
		self.minus1array = array.array('%(typecode)s', [-1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))



	########################################################
	def test_floordiv_array_num_none_a1(self):
		"""Test floordiv as *array-num-none* for min value // -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, 1%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, -1%(decimalpoint)s)


	########################################################
	def test_floordiv_array_num_none_a2(self):
		"""Test floordiv as *array-num-none* for min value // -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, 1%(decimalpoint)s, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, -1%(decimalpoint)s, matherrors=True)


	########################################################
	def test_floordiv_array_num_array_b1(self):
		"""Test floordiv as *array-num-array* for min value // -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, 1%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, -1%(decimalpoint)s, self.dataout)


	########################################################
	def test_floordiv_array_num_array_b2(self):
		"""Test floordiv as *array-num-array* for min value // -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, 1%(decimalpoint)s, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, -1%(decimalpoint)s, self.dataout, matherrors=True)


	########################################################
	def test_floordiv_num_array_none_c1(self):
		"""Test floordiv as *num-array-none* for min value // -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MinLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.MinLimit, self.minus1array)


	########################################################
	def test_floordiv_num_array_none_c2(self):
		"""Test floordiv as *num-array-none* for min value // -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MinLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.MinLimit, self.minus1array, matherrors=True)


	########################################################
	def test_floordiv_num_array_array_d1(self):
		"""Test floordiv as *num-array-array* for min value // -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MinLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.MinLimit, self.minus1array, self.dataout)


	########################################################
	def test_floordiv_num_array_array_d2(self):
		"""Test floordiv as *num-array-array* for min value // -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.MinLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.MinLimit, self.minus1array, self.dataout, matherrors=True)


	########################################################
	def test_floordiv_array_num_none_e1(self):
		"""Test floordiv as *array-array-none* for min value // -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, self.plus1array)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, self.minus1array)


	########################################################
	def test_floordiv_array_num_none_e2(self):
		"""Test floordiv as *array-array-none* for min value // -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, self.minus1array, matherrors=True)


	########################################################
	def test_floordiv_array_num_none_f1(self):
		"""Test floordiv as *array-array-array* for min value // -1%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, self.minus1array, self.dataout)


	########################################################
	def test_floordiv_array_num_none_f2(self):
		"""Test floordiv as *array-array-array* for min value // -1%(decimalpoint)s matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.floordiv(self.inparray1amin, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.floordiv(self.inparray1bmin, self.minus1array, self.dataout, matherrors=True)



##############################################################################

'''


# ==============================================================================

# ==============================================================================

# The template used to generate the tests for overflows with divide by zero.
param_overflow_mod_divzero_template = '''

##############################################################################
class overflow_signed_divzero_%(typelabel)s(unittest.TestCase):
	"""Test mod for value divide by zero.
	param_overflow_mod_divzero_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_mod_array_num_none_a1(self):
		"""Test mod as *array-num-none* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, 1%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, 0%(decimalpoint)s)


	########################################################
	def test_mod_array_num_array_a2(self):
		"""Test mod as *array-num-array* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, 1%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, 0%(decimalpoint)s, self.dataout)


	########################################################
	def test_mod_num_array_none_a3(self):
		"""Test mod as *num-array-none* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.MaxLimit, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.MaxLimit, self.zero1array)


	########################################################
	def test_mod_num_array_array_a4(self):
		"""Test mod as *num-array-array* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.MaxLimit, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.MaxLimit, self.zero1array, self.dataout)


	########################################################
	def test_mod_array_array_none_a5(self):
		"""Test mod as *array-array-none* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, self.plus1array)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, self.zero1array)


	########################################################
	def test_mod_array_array_array_a6(self):
		"""Test mod as *array-array-array* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, self.plus1array, self.dataout)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, self.zero1array, self.dataout)



##############################################################################

'''


# ==============================================================================


# ==============================================================================

# The template used to generate the tests for overflows with divide by zero with
# overflow checking disabled.
param_overflow_mod_divzero_errors_template = '''

##############################################################################
class overflow_signed_divzero_errors_%(typelabel)s(unittest.TestCase):
	"""Test mod for value divide by zero with overflow checking disabled.
	param_overflow_mod_divzero_errors_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		arraysize = 200
		self.MaxLimit = arrayfunc.arraylimits.%(typecode)s_max
		self.MinLimit = arrayfunc.arraylimits.%(typecode)s_min


		self.inparray1amax = array.array('%(typecode)s', [self.MaxLimit] * arraysize)
		self.inparray1bmax = copy.copy(self.inparray1amax)

		self.zero1array = array.array('%(typecode)s', [0%(decimalpoint)s] * arraysize)
		self.plus1array = array.array('%(typecode)s', [1%(decimalpoint)s] * arraysize)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, arraysize))


	########################################################
	def test_mod_array_num_none_b1(self):
		"""Test mod as *array-num-none* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, 1%(decimalpoint)s, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, 0%(decimalpoint)s, matherrors=True)


	########################################################
	def test_mod_array_num_array_b2(self):
		"""Test mod as *array-num-array* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, 1%(decimalpoint)s, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, 0%(decimalpoint)s, self.dataout, matherrors=True)


	########################################################
	def test_mod_num_array_none_b3(self):
		"""Test mod as *num-array-none* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.MaxLimit, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.MaxLimit, self.zero1array, matherrors=True)


	########################################################
	def test_mod_num_array_array_b4(self):
		"""Test mod as *num-array-array* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.MaxLimit, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.MaxLimit, self.zero1array, self.dataout, matherrors=True)


	########################################################
	def test_mod_array_array_none_b5(self):
		"""Test mod as *array-array-none* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, self.plus1array, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, self.zero1array, matherrors=True)


	########################################################
	def test_mod_array_array_array_b6(self):
		"""Test mod as *array-array-array* for max value %% 0%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.mod(self.inparray1amax, self.plus1array, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(ZeroDivisionError):
			arrayfunc.mod(self.inparray1bmax, self.zero1array, self.dataout, matherrors=True)



##############################################################################

'''

# ==============================================================================


# ==============================================================================


# The template used to generate the tests for inf, -inf in data arrays
# when exceptions are expected. This is for "mod" only.
inf_mod_data_error_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using parameter %(errordata)s.
	inf_mod_data_error_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataok2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.dataok1)])

		arraysize = len(self.dataok1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [x %(pyoperator)s testval for x in self.errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [x %(pyoperator)s testval for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, dataok2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(testval, errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				# This test results in "nan".
				expected = [math.nan] * len(self.errordata)

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, self.dataok2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This test results in "nan".
				expected = [math.nan] * len(self.errordata)

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(dataok1, self.errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		# This test results in "nan".
		expected = [math.nan] * len(self.errordata)

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		# This test results in "nan".
		expected = [math.nan] * len(self.errordata)

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for negative power.
param_overflow_pow_negy_template = '''

##############################################################################
class overflow_signed_negy_%(typelabel)s(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_negy_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.datax1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.datax2 = copy.copy(self.datax1)
		self.datay1 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.datax1)])
		self.datay2 = copy.copy(self.datay1)

		self.minus1 = array.array('%(typecode)s', [-1] * len(self.datax1))

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, len(self.datax1)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** -1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1)

		# This is the actual test.
		with self.assertRaises(ValueError):
			arrayfunc.pow(self.datax2, -1)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** -1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, 1, self.dataout)

		# This is the actual test.
		with self.assertRaises(ValueError):
			arrayfunc.pow(self.datax2, -1, self.dataout)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** -1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(2, self.minus1)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** -1 with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** -1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(2, self.minus1, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** -1 with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2, self.datay2, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2, self.minus1, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** -1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(self.datax2, self.minus1)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** -1 with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** -1 - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(self.datax2, self.minus1, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** -1 with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax1, self.datay1, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2, self.minus1, self.dataout, matherrors=True)



##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for overflow of power.
param_overflow_pow_error_template = '''

##############################################################################
class overflow_signed_pow_error_%(typelabel)s(unittest.TestCase):
	"""Test pow for value overflow for max values.
	param_overflow_pow_error_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is used as the 'y' value in x ** y. It is intended to cause a math error.
		self.datayovfl = array.array('%(typecode)s', range(0, %(pow_y_err)s, 10))
		# This provides a 'y' value for x ** y which will not cause math error.
		self.datayok = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.datayovfl)])


		# These just provide simple data to work on.
		self.datax2a = array.array('%(typecode)s', [2%(decimalpoint)s] * len(self.datayovfl))
		self.datax2b = copy.copy(self.datax2a)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0%(decimalpoint)s, len(self.datayovfl)))


	########################################################
	def test_pow_array_num_none_a1(self):
		"""Test pow as *array-num-none* for x ** %(pow_y_err)s%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2%(decimalpoint)s)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(self.datax2b, %(pow_y_err)s%(decimalpoint)s)


	########################################################
	def test_pow_array_num_none_a2(self):
		"""Test pow as *array-num-none* for x ** %(pow_y_err)s%(decimalpoint)s with matherrors=True  - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2%(decimalpoint)s, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, %(pow_y_err)s%(decimalpoint)s, matherrors=True)


	########################################################
	def test_pow_array_num_array_b1(self):
		"""Test pow as *array-num-array* for x ** %(pow_y_err)s%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2%(decimalpoint)s, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(self.datax2b, %(pow_y_err)s%(decimalpoint)s, self.dataout)


	########################################################
	def test_pow_array_num_array_b2(self):
		"""Test pow as *array-num-array* for x ** %(pow_y_err)s%(decimalpoint)s with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, 2%(decimalpoint)s, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, %(pow_y_err)s%(decimalpoint)s, self.dataout, matherrors=True)


	########################################################
	def test_pow_num_array_none_c1(self):
		"""Test pow as *num-array-none* for x ** %(pow_y_err)s%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2%(decimalpoint)s, self.datax2a)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(2%(decimalpoint)s, self.datayovfl)


	########################################################
	def test_pow_num_array_none_c2(self):
		"""Test pow as *num-array-none* for x ** %(pow_y_err)s%(decimalpoint)s with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2%(decimalpoint)s, self.datax2a, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2%(decimalpoint)s, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_num_array_array_d1(self):
		"""Test pow as *num-array-array* for x ** %(pow_y_err)s%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2%(decimalpoint)s, self.datax2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(2%(decimalpoint)s, self.datayovfl, self.dataout)


	########################################################
	def test_pow_num_array_array_d2(self):
		"""Test pow as *num-array-array* for x ** %(pow_y_err)s%(decimalpoint)s with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(2%(decimalpoint)s, self.datax2a, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(2%(decimalpoint)s, self.datayovfl, self.dataout, matherrors=True)


	########################################################
	def test_pow_array_array_none_e1(self):
		"""Test pow as *array-array-none* for x ** %(pow_y_err)s%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(self.datax2b, self.datayovfl)


	########################################################
	def test_pow_array_array_none_e2(self):
		"""Test pow as *array-array-none* for x ** %(pow_y_err)s%(decimalpoint)s with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, matherrors=True)

		# This is the actual test. There should be no exception on math errors.
		arrayfunc.pow(self.datax2b, self.datayovfl, matherrors=True)


	########################################################
	def test_pow_array_array_array_f1(self):
		"""Test pow as *array-array-array* for x ** %(pow_y_err)s%(decimalpoint)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout)

		# This is the actual test.
		with self.assertRaises(%(exceptioncode)s):
			arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout)


	########################################################
	def test_pow_array_array_array_f2(self):
		"""Test pow as *array-array-array* for x ** %(pow_y_err)s%(decimalpoint)s with matherrors=True - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.pow(self.datax2a, self.datayok, self.dataout, matherrors=True)

		# This is the actual test. There should be no exception on math error.
		arrayfunc.pow(self.datax2b, self.datayovfl, self.dataout, matherrors=True)



##############################################################################

'''

# ==============================================================================

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# for pow.
nan_data_pow_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_pow_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using parameter %(errordata)s.
	nan_data_pow_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0])
		self.dataok2 = array.array('%(typecode)s', [-2.0, 3.0, -4.0, 5.0, 5.0, 4.0, -3.0, 2.0])

		arraysize = len(self.dataok1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				expected = [math.%(funcname)s(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(errordata, testval)
				else:
					arrayfunc.%(funcname)s(errordata, testval)
					for dataoutitem, expecteditem in zip(errordata, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.%(funcname)s(x, testval) for x in errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				expected = [math.%(funcname)s(x, testval) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(errordata, testval, self.dataout)
				else:
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.dataok2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.%(funcname)s(x, testval) for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok2 = copy.copy(self.dataok2)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, dataok2)

				expected = [math.%(funcname)s(testval, x) for x in errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, errordata)
				else:
					arrayfunc.%(funcname)s(testval, errordata)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expected = [math.%(funcname)s(testval, x) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, self.dataok2, self.dataout)

				expected = [math.%(funcname)s(testval, x) for x in self.errordata]

				# This is the actual test.
				# Some values will produce non-finite (nan, inf, -inf) results
				# while some will not. We therefore provide means of checking both.
				if not all([math.isfinite(x) for x in expected]):
					# At least one value will produce a non-finite result.
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)
				else:
					arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)
					for dataoutitem, expecteditem in zip(self.dataout, expected):
						# The behavour of assertEqual is modified by addTypeEqualityFunc.
						self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.dataok1:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.%(funcname)s(testval, x) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		expected = [math.%(funcname)s(x, y) for x,y in zip(dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.%(funcname)s(dataok1, self.errordata)
		else:
			arrayfunc.%(funcname)s(dataok1, self.errordata)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [math.%(funcname)s(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.%(funcname)s(self.dataok2, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok2, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok1, self.dataok2, self.dataout)

		expected = [math.%(funcname)s(x, y) for x,y in zip(self.dataok1, self.errordata)]

		# This is the actual test.
		# Some values will produce non-finite (nan, inf, -inf) results
		# while some will not. We therefore provide means of checking both.
		if not all([math.isfinite(x) for x in expected]):
			# At least one value will produce a non-finite result.
			with self.assertRaises(ArithmeticError):
				arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout)
		else:
			arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout)
			for dataoutitem, expecteditem in zip(self.dataout, expected):
				# The behavour of assertEqual is modified by addTypeEqualityFunc.
				self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [math.%(funcname)s(y, x) for x,y in zip(self.errordata, self.dataok2)]

		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================

# ==============================================================================


# Which opstemplate is valid for which operation. Each math operation requires
# different templates for signed int, unsigned int, and float.
opstemplates = {
	'+' : {'int' : [param_overflow_add_max1_template, 
					param_overflow_add_min1_template],
			'uint' : [param_overflow_add_max1_template],
			'float' : [param_overflow_add_max1_template, 
						param_overflow_add_min1_template]
	},
	'-' : {'int' : [param_overflow_sub_max1_template, 
					param_overflow_sub_min1_template,
					param_overflow_sub_1max_template,
					param_overflow_sub_1min_template],
			'uint' : [param_overflow_sub_min1_template],
			'float' : [param_overflow_sub_max1_template, 
					param_overflow_sub_min1_template,
					param_overflow_sub_1max_template]
	},
	'*' : {'int' : [param_overflow_mul_max2_template,
					param_overflow_mul_min2_template,
					param_overflow_mul_max2neg_template,
					param_overflow_mul_min2neg_template,
					param_overflow_mul_min1neg_template],
			'uint' : [param_overflow_mul_max2_template],
			'float' : [param_overflow_mul_max2_template,
					param_overflow_mul_min2_template,
					param_overflow_mul_max2neg_template,
					param_overflow_mul_min2neg_template]
	},
	'/' : {'int' : [param_overflow_truediv_divzero_template, 
					param_overflow_truediv_divzero_errors_template,
					param_overflow_truediv_mindivminus1_template],
			'uint' : [param_overflow_truediv_divzero_template,
					param_overflow_truediv_divzero_errors_template],
			'float' : [param_overflow_truediv_divzero_template]
	},
	'//' : {'int' : [param_overflow_floordiv_divzero_template, 
					param_overflow_floordiv_divzero_errors_template,
					param_overflow_floordiv_mindivminus1_template],
			'uint' : [param_overflow_floordiv_divzero_template,
					param_overflow_floordiv_divzero_errors_template],
			'float' : [param_overflow_floordiv_divzero_template]
	},
	'%' : {'int' : [param_overflow_mod_divzero_template, 
					param_overflow_mod_divzero_errors_template],
			'uint' : [param_overflow_mod_divzero_template,
					param_overflow_mod_divzero_errors_template],
			'float' : [param_overflow_mod_divzero_template]
	},

	'**' : {'int' : [param_overflow_pow_negy_template, 
					param_overflow_pow_error_template],
			'uint' : [param_overflow_pow_error_template],
			'float' : [param_overflow_pow_error_template]
	},


}


# ==============================================================================

# These are all the test code templates. 
test_templates = {'test_template_op' : test_op_templ,
			'nan_data_error_template' : nan_data_error_template,
			'nan_div_data_error_template' : nan_div_data_error_template,
			'inf_floordiv_data_error_template' : inf_floordiv_data_error_template,
			'inf_mod_data_error_template' : inf_mod_data_error_template,
			'nan_data_pow_template' : nan_data_pow_template,
}


# ==============================================================================

# Used for creating test data. This covers everything except truediv on integers, 
# which has to be handled by a function inside the test class as we use native
# division for this. 
operatorfunc = {
	'+' : 'operator.add',
	'//' : 'operator.floordiv',
	'%' : 'operator.mod',
	'*' : 'operator.mul',
	'**' : 'operator.pow',
	'-' : 'operator.sub',
	'/' : 'operator.truediv',
	}


# ==============================================================================


# Read in the op codes.
opdata = codegen_common.ReadINI('affuncdata.ini')

# Filter out the desired math functions.
funclist = [(x,dict(y)) for x,y in opdata.items() if y.get('test_op_templ') in ['test_template_op', 'test_template_op_simd']]

# Create a list of names which support SIMD.
havesimd = [x for x,y in funclist if y.get('test_op_templ') == 'test_template_op_simd']


# ==============================================================================

# This defines the module name.
modulename = 'arrayfunc'
# Import the array module for testing.
arrayimport = 'import array'


for funcname, func in funclist:

	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '09-Dec-2017', funcname)

	# Add additional header data.
	headerdate['modulename'] = modulename
	headerdate['arrayimport'] = arrayimport

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		# Insert the helper functions that are not array type dependent.
		# This filters test data based on the operation being performed.
		f.write(datafilters[funcname])


		# Generate the data for the general tests. These functions are
		# called by a number of different classes. 
		# The pow function uses a special version which is different from the rest.
		if funcname == 'pow':
			f.write(gendata_pow)
		else:
			f.write(gendata_general)

		# This generates all possible data combinations for 8 bit arrays.
		f.write(gendata_fullrange)


		# Check each array type.
		for functype in codegen_common.arraycodes:

			# Convert the numeric literals to the appropriate type for the array.
			if functype in codegen_common.floatarrays:
				xvalues = [float(x) for x in func['test_op_x'].split(',')]
				yvalues = [float(x) for x in func['test_op_y'].split(',')]
				zero_const = 0.0
				# Simply increment by the maximum value, instead of figuring out
				# what the smallest increment is for a float or double.
				incvalue = 'self.MaxLimit / 1000000.0'
				decvalue = 'self.MinLimit / 1000000.0'
				errorflagexceptioncode = 'ArithmeticError'
			else:
				xvalues = [int(x) for x in func['test_op_x'].split(',')]
				yvalues = [int(x) for x in func['test_op_y'].split(',')]

				# Make sure we don't have any negative test values for unsigned arrays.
				if functype in codegen_common.unsignedint:
					xmin = min(xvalues)
					if xmin < 0:
						xtmp = [x - xmin for x in xvalues]
					else:
						xtmp = xvalues
					xvalues = xtmp

					ymin = min(yvalues)
					if ymin < 0:
						ytmp = [y - ymin for y in yvalues]
					else:
						ytmp = yvalues
					yvalues = ytmp

					# Avoid zeros in the y parameters for division to avoid
					# dividing by zero.
					if funcname in ('truediv', 'floordiv', 'mod'):
						yvalues = [x for x in yvalues if x != 0]


				zero_const = '0'
				incvalue = '1'
				decvalue = '-1'
				errorflagexceptioncode = 'OverflowError'
				
			# Convert back to a string, as that is what the template expects.
			test_op_x = ','.join([str(x) for x in xvalues])
			test_op_y = ','.join([str(x) for x in yvalues])


			pyoperator = func['pyoperator']
			funcdata = {'funclabel' : funcname, 'funcname' : funcname, 'pyoperator' : pyoperator,
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : test_op_x,
				'test_op_y' : test_op_y, 'zero_const' : zero_const, 
				'incvalue' : incvalue, 'decvalue' : decvalue,
				'errorflagexceptioncode' : errorflagexceptioncode}


			# For integer true division, we must convert the expected values 
			# back to integer in order to compare them to the arrayfunc.truediv
			# result.
			# Python itself outputs a float value for true division, while we 
			# want to keep output array types the same as the input types.
			if (pyoperator == '/') and (functype in codegen_common.intarrays):
				funcdata['typeconv1'] = 'list(map(int,'
				funcdata['typeconv2'] = '))'
				funcdata['operatorfunc'] = 'inttruediv'
			else:
				funcdata['typeconv1'] = ''
				funcdata['typeconv2'] = ''
				funcdata['operatorfunc'] = operatorfunc[pyoperator]


			# Basic tests. Select the test data generator.
			# The data generator forms part of the class name to differentiate
			# between them.
			if funcname == 'pow':
				funcdata['datagenerator'] = 'pow'
			else:
				funcdata['datagenerator'] = 'int'


			# Even array size.
			funcdata['arrayevenodd'] = 'even'
			f.write(test_op_templ % funcdata)


			# Odd array size.
			funcdata['arrayevenodd'] = 'odd'
			f.write(test_op_templ % funcdata)


			# Special data. These values were hand selected.
			if funcname == 'pow':
				funcdata['datagenerator'] = 'specialpow'
			else:
				funcdata['datagenerator'] = 'special'


			# Even array size.
			funcdata['arrayevenodd'] = 'even'
			f.write(test_op_templ % funcdata)

			# Odd array size.
			funcdata['arrayevenodd'] = 'odd'
			f.write(test_op_templ % funcdata)


			# We do a full range test only for the smallest array types
			# as otherwise the test would be excessively long. This
			# tests all possible combinations of values which would
			# not overflow the result.
			if functype in ('b', 'B'):
				# This data generator handles pow data as well as 
				# all other types.
				funcdata['datagenerator'] = 'fullrange'

				# Even array size.
				funcdata['arrayevenodd'] = 'even'
				f.write(test_op_templ % funcdata)

				# Odd array size.
				funcdata['arrayevenodd'] = 'odd'
				f.write(test_op_templ % funcdata)


			#####

			# Not all functions support SIMD operations.
			if funcname in havesimd:
				# Even array size.
				funcdata['arrayevenodd'] = 'even'
				f.write(test_op_simd_templ % funcdata)

				# Odd array size.
				funcdata['arrayevenodd'] = 'odd'
				f.write(test_op_simd_templ % funcdata)

			#####

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			if functype not in ['f', 'd']:
				funcdata['badcode'] = 'd'
				funcdata['badconv'] = 'float'
			else:
				funcdata['badcode'] = 'i'
				funcdata['badconv'] = 'int'
			f.write(param_invalid_template % funcdata)

			# Test for invalid optional parameters such as errors and maxlen.
			f.write(param_invalid_opt_template % funcdata)


			#####

			# Test for invalid nosimd optional parameter.
			# Not all functions support SIMD operations.
			if funcname in havesimd:
				f.write(param_invalid_opt_simd_template % funcdata)


			#####

			# Overflow tests.
			if functype in codegen_common.signedint:
				errors_templt = '\n'.join(opstemplates[func['pyoperator']]['int'])
				funcdata['decimalpoint'] = ''
				funcdata['floatpad'] = ''
				funcdata['exceptioncode'] = 'OverflowError'
				funcdata['pow_y_err'] = '127'
			elif functype in codegen_common.unsignedint:
				errors_templt = '\n'.join(opstemplates[func['pyoperator']]['uint'])
				funcdata['decimalpoint'] = ''
				funcdata['floatpad'] = ''
				funcdata['exceptioncode'] = 'OverflowError'
				funcdata['pow_y_err'] = '127'
			elif functype in codegen_common.floatarrays:
				errors_templt = '\n'.join(opstemplates[func['pyoperator']]['float'])
				funcdata['decimalpoint'] = '.0'
				if functype == 'f':
					funcdata['floatpad'] = '.0e37'
				else:
					funcdata['floatpad'] = '.0e300'
				funcdata['exceptioncode'] = 'ArithmeticError'
				funcdata['pow_y_err'] = '1100'
			else:
				print('Error - Unknown array type ', functype)


			# Math error tests - output the templates.
			f.write(errors_templt % funcdata)


			#####


			# NaN, Inf tests are for floating point only.
			if functype in codegen_common.floatarrays:
				# NaN, inf, -inf tests.
				funcdata = {'funclabel' : funcname, 'funcname' : funcname, 
					'pyoperator' : func['pyoperator'], 
					'typelabel' : functype, 'typecode' : functype, 'test_op_x' : test_op_x,
					'test_op_y' : test_op_y
					}

				# NaN
				testtemplate = test_templates[func['test_nan_data_template']]
				funcdata['errorlabel'] = 'NaN'
				funcdata['errordata'] = 'nan'
				f.write(testtemplate % funcdata)

				# inf
				testtemplate = test_templates[func['test_inf_data_template']]
				funcdata['errorlabel'] = 'inf'
				funcdata['errordata'] = 'inf'
				f.write(testtemplate % funcdata)

				# -inf
				testtemplate = test_templates[func['test_ninf_data_template']]
				funcdata['errorlabel'] = 'ninf'
				funcdata['errordata'] = '-inf'
				f.write(testtemplate % funcdata)


			#####

		f.write(codegen_common.testendtemplate % {'funcname' : funcname, 'testprefix' : 'af'})

# ==============================================================================

