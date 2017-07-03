#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   benchamap.py
# Purpose:  Benchmark functions for amap and amapi.
# Language: Python 3.4
# Date:     17-Sep-2014.
# Ver:      27-Jun-2017.
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

import time
import array
import itertools
import math
import platform

import arrayfunc

##############################################################################

# The size of test array to use.
ARRAYSIZE = 100000

##############################################################################

# These masks are used with the invert operator. These will NOT produce the
# correct answer in all cases. They are simply intended to provide some sort
# of reasonable run time for comparative benchmarks. 
allinvertmasks = {
	'b' : arrayfunc.arraylimits.b_max,
	'B' : arrayfunc.arraylimits.B_max, 
	'h' : arrayfunc.arraylimits.h_max, 
	'H' : arrayfunc.arraylimits.H_max, 
	'i' : arrayfunc.arraylimits.i_max, 
	'I' : arrayfunc.arraylimits.I_max, 
	'l' : arrayfunc.arraylimits.l_max, 
	'L' : arrayfunc.arraylimits.L_max, 
	'q' : arrayfunc.arraylimits.q_max, 
	'Q' : arrayfunc.arraylimits.Q_max, 
	'f' : arrayfunc.arraylimits.Q_max, 
	'd' : arrayfunc.arraylimits.Q_max, 
}

##############################################################################

# The following is the auto-generated test code.

# These are set to target a balanced execution time for the different tests.
# The target was to cause each test to run for approximately 0.1 second on a
# typical PC. Tests that run too quickly risk poor accuracy due to platform
# timer resolution. 

calibrationdata = {
'af_add' : (10, 1030),
'af_div' : (4, 305),
'af_div_r' : (4, 255),
'af_floordiv' : (7, 220),
'af_floordiv_r' : (7, 225),
'af_mod' : (7, 221),
'af_mod_r' : (9, 249),
'af_mult' : (9, 1075),
'af_neg' : (8, 1111),
'af_pow' : (5, 155),
'af_pow_r' : (4, 143),
'af_sub' : (10, 1123),
'af_sub_r' : (10, 1086),
'af_and' : (8, 1666),
'af_or' : (8, 1639),
'af_xor' : (8, 1666),
'af_invert' : (6, 1587),
'af_eq' : (10, 1408),
'af_gt' : (10, 1176),
'af_gte' : (10, 1388),
'af_lt' : (9, 1408),
'af_lte' : (9, 1136),
'af_ne' : (9, 1369),
'af_lshift' : (8, 1666),
'af_lshift_r' : (8, 1470),
'af_rshift' : (8, 1612),
'af_rshift_r' : (8, 1515),
'af_abs' : (6, 869),
'math_acos' : (4, 51),
'math_acosh' : (3, 25),
'math_asin' : (4, 59),
'math_asinh' : (3, 26),
'math_atan' : (4, 54),
'math_atan2' : (3, 29),
'math_atan2_r' : (3, 34),
'math_atanh' : (3, 29),
'math_ceil' : (3, 216),
'math_copysign' : (4, 316),
'math_cos' : (4, 68),
'math_cosh' : (4, 43),
'math_degrees' : (5, 325),
'math_erf' : (2, 37),
'math_erfc' : (2, 21),
'math_exp' : (4, 54),
'math_expm1' : (3, 29),
'math_fabs' : (5, 327),
'math_factorial' : (6, 500),
'math_floor' : (3, 213),
'math_fmod' : (3, 45),
'math_fmod_r' : (4, 125),
'math_gamma' : (5, 6),
'math_hypot' : (3, 68),
'math_hypot_r' : (3, 68),
'math_isinf' : (4, 276),
'math_isnan' : (4, 290),
'math_ldexp' : (1, 112),
'math_lgamma' : (2, 24),
'math_log' : (3, 48),
'math_log10' : (3, 35),
'math_log1p' : (4, 37),
'math_pow' : (3, 80),
'math_pow_r' : (3, 18),
'math_radians' : (6, 326),
'math_sin' : (4, 67),
'math_sinh' : (3, 19),
'math_sqrt' : (5, 236),
'math_tan' : (3, 25),
'math_tanh' : (3, 22),
'math_trunc' : (3, 175),
'aops_subst_gt' : (7, 1265),
'aops_subst_gte' : (8, 1086),
'aops_subst_lt' : (8, 1219),
'aops_subst_lte' : (8, 1190),
}

##############################################################################
class benchmark_af_add:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['af_add'][0]
		self.afitercounts = calibrationdata['af_add'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] +  25.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_add, data, dataout ,  25.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_div'][0]
		self.afitercounts = calibrationdata['af_div'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int(data[i] /  2)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = float(data[i] /  2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = float(data[i] /  2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_div_r'][0]
		self.afitercounts = calibrationdata['af_div_r'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = int( 100 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = float( 100.0 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = float( 100.0 / data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_div_r, data, dataout ,  100.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_floordiv'][0]
		self.afitercounts = calibrationdata['af_floordiv'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] //  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_floordiv_r'][0]
		self.afitercounts = calibrationdata['af_floordiv_r'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100.0 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  100.0 // data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_floordiv_r, data, dataout ,  100.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_mod'][0]
		self.afitercounts = calibrationdata['af_mod'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] %  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_mod_r'][0]
		self.afitercounts = calibrationdata['af_mod_r'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2.0 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2.0 % data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mod_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_mult'][0]
		self.afitercounts = calibrationdata['af_mult'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] *  3.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_mult, data, dataout ,  3.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_neg'][0]
		self.afitercounts = calibrationdata['af_neg'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_neg, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_pow'][0]
		self.afitercounts = calibrationdata['af_pow'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] **  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_pow_r'][0]
		self.afitercounts = calibrationdata['af_pow_r'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2.0 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2.0 ** data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_pow_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_sub'][0]
		self.afitercounts = calibrationdata['af_sub'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] -  2.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_sub_r'][0]
		self.afitercounts = calibrationdata['af_sub_r'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18.0 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = 18.0 - data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_sub_r, data, dataout , 18.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_and'][0]
		self.afitercounts = calibrationdata['af_and'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] & 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_and, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_or'][0]
		self.afitercounts = calibrationdata['af_or'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] | 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_or, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_xor'][0]
		self.afitercounts = calibrationdata['af_xor'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ^ 5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_xor, data, dataout , 5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_invert'][0]
		self.afitercounts = calibrationdata['af_invert'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = InvertMask &  ~data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([1,2,3,4,5,6,7,8,9,10]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_invert, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_eq'][0]
		self.afitercounts = calibrationdata['af_eq'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] ==  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_eq, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_gt'][0]
		self.afitercounts = calibrationdata['af_gt'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_gte'][0]
		self.afitercounts = calibrationdata['af_gte'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >=  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_gte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_lt'][0]
		self.afitercounts = calibrationdata['af_lt'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_lte'][0]
		self.afitercounts = calibrationdata['af_lte'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <=  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_ne'][0]
		self.afitercounts = calibrationdata['af_ne'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] !=  5.0
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_ne, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_lshift'][0]
		self.afitercounts = calibrationdata['af_lshift'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] <<  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_lshift_r'][0]
		self.afitercounts = calibrationdata['af_lshift_r'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 << data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_lshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_rshift'][0]
		self.afitercounts = calibrationdata['af_rshift'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = data[i] >>  2
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([100,101,102,103,104,105,106,107,108,109]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_rshift_r'][0]
		self.afitercounts = calibrationdata['af_rshift_r'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  2 >> data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_rshift_r, data, dataout ,  2)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['af_abs'][0]
		self.afitercounts = calibrationdata['af_abs'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.af_abs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_acos'][0]
		self.afitercounts = calibrationdata['math_acos'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.acos(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_acos, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.acos(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_acos, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_acosh'][0]
		self.afitercounts = calibrationdata['math_acosh'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.acosh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_acosh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.acosh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_acosh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_asin'][0]
		self.afitercounts = calibrationdata['math_asin'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.asin(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_asin, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.asin(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_asin, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_asinh'][0]
		self.afitercounts = calibrationdata['math_asinh'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.asinh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_asinh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.asinh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_asinh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_atan'][0]
		self.afitercounts = calibrationdata['math_atan'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atan(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atan, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atan(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atan, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_atan2'][0]
		self.afitercounts = calibrationdata['math_atan2'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atan2(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atan2, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atan2(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atan2, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_atan2_r'][0]
		self.afitercounts = calibrationdata['math_atan2_r'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atan2( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atan2_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atan2( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atan2_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_atanh'][0]
		self.afitercounts = calibrationdata['math_atanh'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atanh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atanh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.atanh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_atanh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_ceil'][0]
		self.afitercounts = calibrationdata['math_ceil'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.ceil(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_ceil, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.ceil(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_ceil, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_copysign'][0]
		self.afitercounts = calibrationdata['math_copysign'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.copysign(data[i], 3.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_copysign, data, dataout ,  3.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.copysign(data[i], 3.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_copysign, data, dataout ,  3.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_cos'][0]
		self.afitercounts = calibrationdata['math_cos'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.cos(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_cos, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.cos(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_cos, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_cosh'][0]
		self.afitercounts = calibrationdata['math_cosh'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.cosh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_cosh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.cosh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_cosh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_degrees'][0]
		self.afitercounts = calibrationdata['math_degrees'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.degrees(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_degrees, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.degrees(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_degrees, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_erf'][0]
		self.afitercounts = calibrationdata['math_erf'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.erf(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_erf, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.erf(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_erf, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_erfc'][0]
		self.afitercounts = calibrationdata['math_erfc'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.erfc(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_erfc, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.erfc(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_erfc, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_exp'][0]
		self.afitercounts = calibrationdata['math_exp'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.exp(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_exp, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.exp(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_exp, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_expm1'][0]
		self.afitercounts = calibrationdata['math_expm1'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.expm1(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_expm1, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.expm1(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_expm1, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_fabs'][0]
		self.afitercounts = calibrationdata['math_fabs'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.fabs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_fabs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.fabs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_fabs, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_factorial'][0]
		self.afitercounts = calibrationdata['math_factorial'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.factorial(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_factorial, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_floor'][0]
		self.afitercounts = calibrationdata['math_floor'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.floor(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_floor, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.floor(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_floor, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_fmod'][0]
		self.afitercounts = calibrationdata['math_fmod'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.fmod(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_fmod, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.fmod(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_fmod, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_fmod_r'][0]
		self.afitercounts = calibrationdata['math_fmod_r'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.fmod( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_fmod_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.fmod( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_fmod_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_gamma'][0]
		self.afitercounts = calibrationdata['math_gamma'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.gamma(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_gamma, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.gamma(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_gamma, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_hypot'][0]
		self.afitercounts = calibrationdata['math_hypot'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.hypot(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_hypot, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.hypot(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_hypot, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_hypot_r'][0]
		self.afitercounts = calibrationdata['math_hypot_r'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.hypot( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_hypot_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.hypot( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_hypot_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_isinf'][0]
		self.afitercounts = calibrationdata['math_isinf'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.isinf(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_isinf, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.isinf(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_isinf, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_isnan'][0]
		self.afitercounts = calibrationdata['math_isnan'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.isnan(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_isnan, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.isnan(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_isnan, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_ldexp'][0]
		self.afitercounts = calibrationdata['math_ldexp'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.ldexp(data[i],int( 2.0))
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_ldexp, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.ldexp(data[i],int( 2.0))
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_ldexp, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_lgamma'][0]
		self.afitercounts = calibrationdata['math_lgamma'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.lgamma(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_lgamma, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.lgamma(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_lgamma, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_log'][0]
		self.afitercounts = calibrationdata['math_log'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.log(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_log, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.log(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_log, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_log10'][0]
		self.afitercounts = calibrationdata['math_log10'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.log10(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_log10, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.log10(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_log10, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_log1p'][0]
		self.afitercounts = calibrationdata['math_log1p'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.log1p(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_log1p, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.log1p(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_log1p, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_pow'][0]
		self.afitercounts = calibrationdata['math_pow'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.pow(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_pow, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.pow(data[i], 2.0)
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_pow, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_pow_r'][0]
		self.afitercounts = calibrationdata['math_pow_r'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.pow( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_pow_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.pow( 2.0,data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_pow_r, data, dataout ,  2.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_radians'][0]
		self.afitercounts = calibrationdata['math_radians'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.radians(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_radians, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.radians(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_radians, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_sin'][0]
		self.afitercounts = calibrationdata['math_sin'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.sin(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_sin, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.sin(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_sin, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_sinh'][0]
		self.afitercounts = calibrationdata['math_sinh'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.sinh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_sinh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.sinh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_sinh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_sqrt'][0]
		self.afitercounts = calibrationdata['math_sqrt'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.sqrt(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_sqrt, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.sqrt(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_sqrt, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_tan'][0]
		self.afitercounts = calibrationdata['math_tan'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.tan(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_tan, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.tan(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_tan, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_tanh'][0]
		self.afitercounts = calibrationdata['math_tanh'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.tanh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_tanh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.tanh(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_tanh, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['math_trunc'][0]
		self.afitercounts = calibrationdata['math_trunc'][1]


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
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.trunc(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_trunc, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.trunc(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.math_trunc, data, dataout )
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['aops_subst_gt'][0]
		self.afitercounts = calibrationdata['aops_subst_gt'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] >  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] >  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['aops_subst_gte'][0]
		self.afitercounts = calibrationdata['aops_subst_gte'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] >=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] >=  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] >=  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_gte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['aops_subst_lt'][0]
		self.afitercounts = calibrationdata['aops_subst_lt'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] <  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] <  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lt, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

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
		self.pyitercounts = calibrationdata['aops_subst_lte'][0]
		self.afitercounts = calibrationdata['aops_subst_lte'][1]


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
		InvertMask = allinvertmasks['b']

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_h(self):
		"""Measure execution time.
		"""
		TypeCode = 'h'
		InvertMask = allinvertmasks['h']

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_i(self):
		"""Measure execution time.
		"""
		TypeCode = 'i'
		InvertMask = allinvertmasks['i']

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_l(self):
		"""Measure execution time.
		"""
		TypeCode = 'l'
		InvertMask = allinvertmasks['l']

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_q(self):
		"""Measure execution time.
		"""
		TypeCode = 'q'
		InvertMask = allinvertmasks['q']

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5 if data[i] <=  5 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5,6,7,8,9]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_f(self):
		"""Measure execution time.
		"""
		TypeCode = 'f'
		InvertMask = allinvertmasks['f']

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] <=  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, amaptime, pythontime / amaptime)


	########################################################
	def Benchmark_d(self):
		"""Measure execution time.
		"""
		TypeCode = 'd'
		InvertMask = allinvertmasks['d']

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] =  5.0 if data[i] <=  5.0 else data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.aops_subst_lte, data, dataout ,  5.0)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, amaptime, pythontime / amaptime)

##############################################################################


BenchClasses = [(benchmark_af_add, 'af_add'), (benchmark_af_div, 'af_div'), (benchmark_af_div_r, 'af_div_r'), (benchmark_af_floordiv, 'af_floordiv'), (benchmark_af_floordiv_r, 'af_floordiv_r'), (benchmark_af_mod, 'af_mod'), (benchmark_af_mod_r, 'af_mod_r'), (benchmark_af_mult, 'af_mult'), (benchmark_af_neg, 'af_neg'), (benchmark_af_pow, 'af_pow'), (benchmark_af_pow_r, 'af_pow_r'), (benchmark_af_sub, 'af_sub'), (benchmark_af_sub_r, 'af_sub_r'), (benchmark_af_and, 'af_and'), (benchmark_af_or, 'af_or'), (benchmark_af_xor, 'af_xor'), (benchmark_af_invert, 'af_invert'), (benchmark_af_eq, 'af_eq'), (benchmark_af_gt, 'af_gt'), (benchmark_af_gte, 'af_gte'), (benchmark_af_lt, 'af_lt'), (benchmark_af_lte, 'af_lte'), (benchmark_af_ne, 'af_ne'), (benchmark_af_lshift, 'af_lshift'), (benchmark_af_lshift_r, 'af_lshift_r'), (benchmark_af_rshift, 'af_rshift'), (benchmark_af_rshift_r, 'af_rshift_r'), (benchmark_af_abs, 'af_abs'), (benchmark_math_acos, 'math_acos'), (benchmark_math_acosh, 'math_acosh'), (benchmark_math_asin, 'math_asin'), (benchmark_math_asinh, 'math_asinh'), (benchmark_math_atan, 'math_atan'), (benchmark_math_atan2, 'math_atan2'), (benchmark_math_atan2_r, 'math_atan2_r'), (benchmark_math_atanh, 'math_atanh'), (benchmark_math_ceil, 'math_ceil'), (benchmark_math_copysign, 'math_copysign'), (benchmark_math_cos, 'math_cos'), (benchmark_math_cosh, 'math_cosh'), (benchmark_math_degrees, 'math_degrees'), (benchmark_math_erf, 'math_erf'), (benchmark_math_erfc, 'math_erfc'), (benchmark_math_exp, 'math_exp'), (benchmark_math_expm1, 'math_expm1'), (benchmark_math_fabs, 'math_fabs'), (benchmark_math_factorial, 'math_factorial'), (benchmark_math_floor, 'math_floor'), (benchmark_math_fmod, 'math_fmod'), (benchmark_math_fmod_r, 'math_fmod_r'), (benchmark_math_gamma, 'math_gamma'), (benchmark_math_hypot, 'math_hypot'), (benchmark_math_hypot_r, 'math_hypot_r'), (benchmark_math_isinf, 'math_isinf'), (benchmark_math_isnan, 'math_isnan'), (benchmark_math_ldexp, 'math_ldexp'), (benchmark_math_lgamma, 'math_lgamma'), (benchmark_math_log, 'math_log'), (benchmark_math_log10, 'math_log10'), (benchmark_math_log1p, 'math_log1p'), (benchmark_math_pow, 'math_pow'), (benchmark_math_pow_r, 'math_pow_r'), (benchmark_math_radians, 'math_radians'), (benchmark_math_sin, 'math_sin'), (benchmark_math_sinh, 'math_sinh'), (benchmark_math_sqrt, 'math_sqrt'), (benchmark_math_tan, 'math_tan'), (benchmark_math_tanh, 'math_tanh'), (benchmark_math_trunc, 'math_trunc'), (benchmark_aops_subst_gt, 'aops_subst_gt'), (benchmark_aops_subst_gte, 'aops_subst_gte'), (benchmark_aops_subst_lt, 'aops_subst_lt'), (benchmark_aops_subst_lte, 'aops_subst_lte')]
arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']

TestLabels = [y for x,y in BenchClasses]



##############################################################################

def dataformat(val):
	"""Format the output data.
	"""
	if val >= 10.0:
		return '%0.0f' % val
	else:
		return '%0.1f' % val


##############################################################################

# Write the results to disk.
def WriteResults(outputfile, columnwidth, testresults):
	"""Parameters: outputfile (file object) = The file object for the output file.
			columnwidth (integer) = The width of the data columns.
			testresults (dict of dicts) = The test results.
	"""
	tableheader = {'func' : 'function', 'b' : 'b', 'B' : 'B', 'h' : 'h', 'H' : 'H', 
		'i' : 'i', 'I' : 'I', 'l' : 'l', 'L' : 'L', 'q' : 'q', 'Q' : 'Q', 'f' : 'f', 'd' : 'd'}
	tablesep = dict.fromkeys(arraycodes, '=' * columnwidth)
	tablesep.update({'func' : '=============='})
	tableformat = '%(func)14s ' + ' '.join(['%(' + x + (')%is' % columnwidth) for x in arraycodes]) + '\n'

	outputfile.write(tableformat % tablesep)
	outputfile.write(tableformat % tableheader)
	outputfile.write(tableformat % tablesep)

	for func in TestLabels:
		outputvals = dict.fromkeys(arraycodes, '')

		bc = testresults[func]
		benchdata = {'func' : func}
		benchdata.update(outputvals)
		benchdata.update(bc)
		outputfile.write(tableformat % benchdata)


	outputfile.write(tableformat % tablesep)


##############################################################################

# Write out the platform data to keep track of what platform the
def WritePlatformSignature(f):
	# test was run on.
	# 'Linux'
	f.write('Operating System: ' + platform.system() + '\n')

	# 'Linux-4.4.0-79-generic-x86_64-with-Ubuntu-16.04-xenial'
	f.write('Platform: ' + platform.platform() + '\n')

	# ('64bit', 'ELF')
	f.write('Word size: ' + platform.architecture()[0] + '\n')

	# 'GCC 5.4.0 20160609'
	f.write('Compiler: ' + platform.python_compiler() + '\n')

	# '4.4.0-79-generic'
	f.write('Python release: ' + platform.release() + '\n')
	f.write('\n\n\n')


##############################################################################

PyResults = {}
FuncResults = {}
RelativeResults = {}
numstats = []

# Run the tests.
for i, j in BenchClasses:
	print(j)
	bc = i()
	bc.RunTests()

	PyResults[j] = dict([(x, '%0.0f' % (y[0] * 1000000.0)) for x,y in bc.TestResults.items()])
	FuncResults[j] = dict([(x, '%0.0f' % (y[1] * 1000000.0)) for x,y in bc.TestResults.items()])
	RelativeResults[j] = dict([(x, dataformat(y[2])) for x,y in bc.TestResults.items()])

	numstats.extend([z for x,y,z in bc.TestResults.values()])



##############################################################################

# Print the results

with open('benchamapdata.txt', 'w') as f:

	WritePlatformSignature(f)

	WriteResults(f, 5, RelativeResults)

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



	##########################################################################

	f.write('\n\n\n')

	f.write('Python native time in micro-seconds.\n')
	WriteResults(f, 8, PyResults)

	f.write('\n\nArrayfunc time in micro-seconds.\n')
	WriteResults(f, 8, FuncResults)


##############################################################################


