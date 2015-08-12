#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   benchmark.py
# Purpose:  Benchmark functions for amap and amapi.
# Language: Python 3.4
# Date:     17-Sep-2014.
# Ver:      20-May-2015.
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

import time
import array
import itertools
import math

import arrayfunc

##############################################################################

# The size of test array to use.
ARRAYSIZE = 100000

##############################################################################

# The following is the auto-generated test code.

##############################################################################
class benchmark_af_add:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] +  25.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_add, data ,  25.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_div:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int(data[i] /  2)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = float(data[i] /  2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = float(data[i] /  2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_div_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = int( 100 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = float( 100.0 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = float( 100.0 / data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_div_r, data ,  100.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_floordiv:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] //  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_floordiv_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100.0 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  100.0 // data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_floordiv_r, data ,  100.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_mod:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] %  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_mod_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2.0 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2.0 % data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mod_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_mult:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] *  3.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_mult, data ,  3.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_neg:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_h, self.Benchmark_i, self.Benchmark_l, self.Benchmark_q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = -data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_neg, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = -data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_neg, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = -data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_neg, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = -data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_neg, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = -data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_neg, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = -data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_neg, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = -data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_neg, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_pow:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] **  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_pow_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2.0 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2.0 ** data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_pow_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_sub:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] -  2.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_sub_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18.0 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = 18.0 - data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_sub_r, data , 18.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_and:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] & 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_and, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_or:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] | 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_or, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_xor:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ^ 5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_xor, data , 5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_invert:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = InvertMask &  ~data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_invert, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_eq:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] ==  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_eq, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_gt:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_gte:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >=  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_gte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_lt:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_lte:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <=  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_ne:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] !=  5.0
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_ne, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_lshift:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] <<  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_lshift_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 << data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_lshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_rshift:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = data[i] >>  2
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_rshift_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  2 >> data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_rshift_r, data ,  2)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_af_abs:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_h, self.Benchmark_i, self.Benchmark_l, self.Benchmark_q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = abs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_abs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = abs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_abs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = abs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_abs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = abs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_abs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = abs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_abs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = abs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_abs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = abs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.af_abs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_acos:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.acos(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_acos, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_acos, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.acos(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_acos, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_acos, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_acosh:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.acosh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_acosh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_acosh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.acosh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_acosh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_acosh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_asin:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.asin(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_asin, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_asin, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.asin(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_asin, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_asin, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_asinh:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.asinh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_asinh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_asinh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.asinh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_asinh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_asinh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_atan:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atan(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atan, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atan, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atan(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atan, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atan, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_atan2:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atan2(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atan2, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atan2, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atan2(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atan2, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atan2, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_atan2_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atan2( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atan2_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atan2_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atan2( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atan2_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atan2_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_atanh:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atanh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atanh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atanh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.atanh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_atanh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_atanh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_ceil:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.ceil(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_ceil, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_ceil, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.ceil(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_ceil, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_ceil, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_copysign:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.copysign(data[i], 3.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_copysign, data, dataout ,  3.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_copysign, data ,  3.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.copysign(data[i], 3.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_copysign, data, dataout ,  3.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_copysign, data ,  3.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_cos:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.cos(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_cos, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_cos, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.cos(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_cos, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_cos, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_cosh:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.cosh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_cosh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_cosh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.cosh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_cosh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_cosh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_degrees:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.degrees(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_degrees, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_degrees, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.degrees(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_degrees, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_degrees, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_erf:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.erf(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_erf, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_erf, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.erf(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_erf, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_erf, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_erfc:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.erfc(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_erfc, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_erfc, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.erfc(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_erfc, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_erfc, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_exp:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.exp(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_exp, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_exp, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.exp(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_exp, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_exp, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_expm1:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.expm1(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_expm1, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_expm1, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.expm1(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_expm1, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_expm1, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_fabs:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.fabs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_fabs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_fabs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.fabs(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_fabs, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_fabs, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_factorial:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.factorial(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_factorial, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_floor:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.floor(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_floor, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_floor, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.floor(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_floor, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_floor, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_fmod:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.fmod(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_fmod, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_fmod, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.fmod(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_fmod, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_fmod, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_fmod_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.fmod( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_fmod_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_fmod_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.fmod( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_fmod_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_fmod_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_gamma:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.gamma(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_gamma, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_gamma, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.gamma(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_gamma, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_gamma, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_hypot:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.hypot(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_hypot, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_hypot, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.hypot(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_hypot, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_hypot, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_hypot_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.hypot( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_hypot_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_hypot_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.hypot( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_hypot_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_hypot_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_isinf:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.isinf(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_isinf, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_isinf, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.isinf(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_isinf, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_isinf, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_isnan:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.isnan(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_isnan, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_isnan, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.isnan(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_isnan, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_isnan, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_ldexp:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.ldexp(data[i],int( 2.0))
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_ldexp, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_ldexp, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.ldexp(data[i],int( 2.0))
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_ldexp, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_ldexp, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_lgamma:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.lgamma(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_lgamma, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_lgamma, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.lgamma(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_lgamma, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_lgamma, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_log:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.log(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_log, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_log, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.log(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_log, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_log, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_log10:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.log10(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_log10, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_log10, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.log10(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_log10, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_log10, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_log1p:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.log1p(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_log1p, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_log1p, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.log1p(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_log1p, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_log1p, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_pow:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.pow(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_pow, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_pow, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.pow(data[i], 2.0)
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_pow, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_pow, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_pow_r:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.pow( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_pow_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_pow_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.pow( 2.0,data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_pow_r, data, dataout ,  2.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_pow_r, data ,  2.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_radians:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.radians(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_radians, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_radians, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.radians(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_radians, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_radians, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_sin:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.sin(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_sin, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_sin, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.sin(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_sin, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_sin, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_sinh:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.sinh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_sinh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_sinh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.sinh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_sinh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_sinh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_sqrt:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.sqrt(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_sqrt, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_sqrt, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.sqrt(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_sqrt, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_sqrt, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_tan:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.tan(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_tan, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_tan, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.tan(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_tan, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_tan, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_tanh:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.tanh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_tanh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_tanh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.tanh(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_tanh, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_tanh, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_math_trunc:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.trunc(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_trunc, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_trunc, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = math.trunc(data[i])
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.math_trunc, data, dataout )
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.math_trunc, data )
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_aops_subst_gt:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] >  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] >  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_aops_subst_gte:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] >=  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] >=  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_gte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_aops_subst_lt:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] <  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] <  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lt, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################

##############################################################################
class benchmark_aops_subst_lte:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		self.TestFuncs = [self.Benchmark_b, self.Benchmark_B, self.Benchmark_h, self.Benchmark_H, self.Benchmark_i, self.Benchmark_I, self.Benchmark_l, self.Benchmark_L, self.Benchmark_q, self.Benchmark_Q, self.Benchmark_f, self.Benchmark_d]
		for testfunc in self.TestFuncs:
			testfunc()


	########################################################
	def Benchmark_b(self):
		"""Measure execution time.
		"""
		TypeCode = 'b'
		InvertMask = 127

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['b'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = 255

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['B'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = 32767

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['h'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = 65535

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['H'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = 2147483647

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['i'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = 4294967295

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['I'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = 9223372036854775807

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['l'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = 18446744073709551615

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['L'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = 9223372036854775807

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = 18446744073709551615

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['Q'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = 18446744073709551615

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] <=  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['f'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = 18446744073709551615

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] =  5.0 if data[i] <=  5.0 else data[i]
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5.0)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.aops_subst_lte, data ,  5.0)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['d'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

##############################################################################


BenchClasses = [(benchmark_af_add, 'af_add'), (benchmark_af_div, 'af_div'), (benchmark_af_div_r, 'af_div_r'), (benchmark_af_floordiv, 'af_floordiv'), (benchmark_af_floordiv_r, 'af_floordiv_r'), (benchmark_af_mod, 'af_mod'), (benchmark_af_mod_r, 'af_mod_r'), (benchmark_af_mult, 'af_mult'), (benchmark_af_neg, 'af_neg'), (benchmark_af_pow, 'af_pow'), (benchmark_af_pow_r, 'af_pow_r'), (benchmark_af_sub, 'af_sub'), (benchmark_af_sub_r, 'af_sub_r'), (benchmark_af_and, 'af_and'), (benchmark_af_or, 'af_or'), (benchmark_af_xor, 'af_xor'), (benchmark_af_invert, 'af_invert'), (benchmark_af_eq, 'af_eq'), (benchmark_af_gt, 'af_gt'), (benchmark_af_gte, 'af_gte'), (benchmark_af_lt, 'af_lt'), (benchmark_af_lte, 'af_lte'), (benchmark_af_ne, 'af_ne'), (benchmark_af_lshift, 'af_lshift'), (benchmark_af_lshift_r, 'af_lshift_r'), (benchmark_af_rshift, 'af_rshift'), (benchmark_af_rshift_r, 'af_rshift_r'), (benchmark_af_abs, 'af_abs'), (benchmark_math_acos, 'math_acos'), (benchmark_math_acosh, 'math_acosh'), (benchmark_math_asin, 'math_asin'), (benchmark_math_asinh, 'math_asinh'), (benchmark_math_atan, 'math_atan'), (benchmark_math_atan2, 'math_atan2'), (benchmark_math_atan2_r, 'math_atan2_r'), (benchmark_math_atanh, 'math_atanh'), (benchmark_math_ceil, 'math_ceil'), (benchmark_math_copysign, 'math_copysign'), (benchmark_math_cos, 'math_cos'), (benchmark_math_cosh, 'math_cosh'), (benchmark_math_degrees, 'math_degrees'), (benchmark_math_erf, 'math_erf'), (benchmark_math_erfc, 'math_erfc'), (benchmark_math_exp, 'math_exp'), (benchmark_math_expm1, 'math_expm1'), (benchmark_math_fabs, 'math_fabs'), (benchmark_math_factorial, 'math_factorial'), (benchmark_math_floor, 'math_floor'), (benchmark_math_fmod, 'math_fmod'), (benchmark_math_fmod_r, 'math_fmod_r'), (benchmark_math_gamma, 'math_gamma'), (benchmark_math_hypot, 'math_hypot'), (benchmark_math_hypot_r, 'math_hypot_r'), (benchmark_math_isinf, 'math_isinf'), (benchmark_math_isnan, 'math_isnan'), (benchmark_math_ldexp, 'math_ldexp'), (benchmark_math_lgamma, 'math_lgamma'), (benchmark_math_log, 'math_log'), (benchmark_math_log10, 'math_log10'), (benchmark_math_log1p, 'math_log1p'), (benchmark_math_pow, 'math_pow'), (benchmark_math_pow_r, 'math_pow_r'), (benchmark_math_radians, 'math_radians'), (benchmark_math_sin, 'math_sin'), (benchmark_math_sinh, 'math_sinh'), (benchmark_math_sqrt, 'math_sqrt'), (benchmark_math_tan, 'math_tan'), (benchmark_math_tanh, 'math_tanh'), (benchmark_math_trunc, 'math_trunc'), (benchmark_aops_subst_gt, 'aops_subst_gt'), (benchmark_aops_subst_gte, 'aops_subst_gte'), (benchmark_aops_subst_lt, 'aops_subst_lt'), (benchmark_aops_subst_lte, 'aops_subst_lte')]
arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']



tableheader = {'func' : 'opcode', 'b' : 'b', 'B' : 'B', 'h' : 'h', 'H' : 'H', 
		'i' : 'i', 'I' : 'I', 'l' : 'l', 'L' : 'L', 'q' : 'q', 'Q' : 'Q', 
		'f' : 'f', 'd' : 'd'}

tableformat = '%(func)14s %(b)5s %(B)5s %(h)5s %(H)5s %(i)5s %(I)5s %(l)5s %(L)5s %(q)5s %(Q)5s %(f)5s %(d)5s\n'
columnsep = '====='
tablesep = {'func' : '=' * 14, 'b' : columnsep, 'B' : columnsep, 
		'h' : columnsep, 'H' : columnsep, 'i' : columnsep, 'I' : columnsep, 
		'l' : columnsep, 'L' : columnsep, 'q' : columnsep, 'Q' : columnsep, 
		'f' : columnsep, 'd' : columnsep}


##############################################################################

def dataformat(val):
	"""Format the output data.
	"""
	try:
		if val >= 10.0:
			return '%0.0f' % val
		else:
			return '%0.1f' % val
	except:
		return ' '

##############################################################################

with open('benchmarkdata.txt', 'w') as f:

	f.write(tableformat % tablesep)
	f.write(tableformat % tableheader)
	f.write(tableformat % tablesep)

	numstats = []

	for i, j in BenchClasses:
		bc = i()
		bc.RunTests()
		print(j)
		defaultdata = ['','','','','']

		benchdata = {'func' : j}
		benchdata.update(dict([(x, dataformat(bc.TestResults.get(x, defaultdata)[3])) for x in arraycodes]))
		benchline = tableformat % benchdata
		f.write(benchline)

		# Accumulate the data for stats.
		stats = [bc.TestResults.get(x, defaultdata)[3] for x in arraycodes]
		numstats.extend([x for x in stats if x != ''])

	f.write(tableformat % tablesep)


##############################################################################

	avgval = sum(numstats) / len(numstats)
	maxval = max(numstats)
	minval = min(numstats)


	f.write('\n\n\n')
	f.write('=========== ========\n')
	f.write('Stat         Value\n')
	f.write('=========== ========\n')
	f.write('Average:    %0.0f\n' % avgval)
	f.write('Maximum:    %0.0f\n' % maxval)
	f.write('Minimum:    %0.1f\n' % minval)
	f.write('Array size: %d\n' % ARRAYSIZE)
	f.write('=========== ========\n')


##############################################################################

