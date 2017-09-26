#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   benchacalc.py
# Purpose:  Benchmark functions for acalc.
# Language: Python 3.4
# Date:     05-Feb-2016.
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
'add' : (8, 171),
'sub' : (10, 181),
'mult' : (9, 135),
'div' : (4, 138),
'floordiv' : (8, 116),
'mod' : (7, 116),
'uadd' : (12, 404),
'usub' : (9, 247),
'pow' : (5, 91),
'bitand' : (8, 208),
'bitor' : (8, 201),
'bitxor' : (8, 200),
'invert' : (6, 290),
'lshift' : (7, 194),
'rshift' : (7, 197),
'abs' : (8, 403),
'math_acos' : (4, 41),
'math_acosh' : (3, 23),
'math_asin' : (4, 50),
'math_asinh' : (3, 23),
'math_atan' : (4, 44),
'math_atan2' : (3, 25),
'math_atanh' : (3, 26),
'math_ceil' : (3, 132),
'math_copysign' : (4, 133),
'math_cos' : (4, 53),
'math_cosh' : (4, 38),
'math_degrees' : (5, 182),
'math_erf' : (2, 33),
'math_erfc' : (2, 20),
'math_exp' : (4, 45),
'math_expm1' : (4, 26),
'math_fabs' : (5, 271),
'math_factorial' : (6, 200),
'math_floor' : (3, 134),
'math_fmod' : (3, 36),
'math_gamma' : (4, 6),
'math_hypot' : (3, 47),
'math_ldexp' : (2, 68),
'math_lgamma' : (2, 20),
'math_log' : (3, 39),
'math_log10' : (3, 32),
'math_log1p' : (4, 33),
'math_pow' : (4, 58),
'math_radians' : (5, 155),
'math_sin' : (4, 54),
'math_sinh' : (4, 18),
'math_sqrt' : (5, 147),
'math_tan' : (3, 23),
'math_tanh' : (3, 20),
'math_trunc' : (3, 107),

}

##############################################################################
class benchmark_add:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['add'][0]
		self.afitercounts = calibrationdata['add'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x + y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 25.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_sub:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['sub'][0]
		self.afitercounts = calibrationdata['sub'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x - y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_mult:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['mult'][0]
		self.afitercounts = calibrationdata['mult'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x * y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_div:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['div'][0]
		self.afitercounts = calibrationdata['div'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x / y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_floordiv:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['floordiv'][0]
		self.afitercounts = calibrationdata['floordiv'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x // y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_mod:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['mod'][0]
		self.afitercounts = calibrationdata['mod'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x % y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_uadd:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['uadd'][0]
		self.afitercounts = calibrationdata['uadd'][1]


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

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('b', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4,5]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = +data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('+x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_usub:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['usub'][0]
		self.afitercounts = calibrationdata['usub'][1]


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
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('b', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('b', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('-x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('h', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('h', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('-x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('i', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('i', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('-x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('l', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('l', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('-x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('q', (x for x,y in zip(itertools.cycle([-5,-4,-3,-2,-1,0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('q', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('-x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('-x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = -data[i]
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('-x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_pow:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['pow'][0]
		self.afitercounts = calibrationdata['pow'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x**y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_bitand:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['bitand'][0]
		self.afitercounts = calibrationdata['bitand'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x & y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_bitor:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['bitor'][0]
		self.afitercounts = calibrationdata['bitor'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x | y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_bitxor:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['bitxor'][0]
		self.afitercounts = calibrationdata['bitxor'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x ^ y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([5])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_invert:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['invert'][0]
		self.afitercounts = calibrationdata['invert'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('~x', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_lshift:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['lshift'][0]
		self.afitercounts = calibrationdata['lshift'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x << y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_rshift:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['rshift'][0]
		self.afitercounts = calibrationdata['rshift'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('x >> y', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_abs:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['abs'][0]
		self.afitercounts = calibrationdata['abs'][1]


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


	########################################################
	def Benchmark_B(self):
		"""Measure execution time.
		"""
		TypeCode = 'B'
		InvertMask = allinvertmasks['B']

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('B', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('B', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('B', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


	########################################################
	def Benchmark_H(self):
		"""Measure execution time.
		"""
		TypeCode = 'H'
		InvertMask = allinvertmasks['H']

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('H', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('H', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('H', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


	########################################################
	def Benchmark_I(self):
		"""Measure execution time.
		"""
		TypeCode = 'I'
		InvertMask = allinvertmasks['I']

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('I', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('I', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('I', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


	########################################################
	def Benchmark_L(self):
		"""Measure execution time.
		"""
		TypeCode = 'L'
		InvertMask = allinvertmasks['L']

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('L', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('L', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('L', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


	########################################################
	def Benchmark_Q(self):
		"""Measure execution time.
		"""
		TypeCode = 'Q'
		InvertMask = allinvertmasks['Q']

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = abs(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('Q', (x for x,y in zip(itertools.cycle([0,1,2,3,4]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('Q', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('abs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.acos(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.acos(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.acosh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.acosh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.asin(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.asin(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.asinh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.asinh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.atan(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.atan(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.atan2(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.atan2(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.atanh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.atanh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.ceil(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.ceil(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.copysign(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.copysign(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 3.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.cos(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.cos(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.cosh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.cosh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.degrees(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.degrees(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.erf(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.erf(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.erfc(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.erfc(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.exp(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.exp(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.expm1(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.expm1(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.fabs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.fabs(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['b'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['B'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['h'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['H'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['i'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['I'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['l'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['L'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['q'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.factorial(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['Q'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.floor(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.floor(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.fmod(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.fmod(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.gamma(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.gamma(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.hypot(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.hypot(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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
				dataout[i] = math.ldexp(data[i],int( 2))
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.ldexp(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = math.ldexp(data[i],int( 2))
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.ldexp(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.lgamma(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.lgamma(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log10(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log10(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log1p(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log1p(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################

##############################################################################
class benchmark_math_log2:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['math_log2'][0]
		self.afitercounts = calibrationdata['math_log2'][1]


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
				dataout[i] = math.log2(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('f', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('f', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log2(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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
				dataout[i] = math.log2(data[i])
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('d', (x for x,y in zip(itertools.cycle([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('d', itertools.repeat(0, arraylength))

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.log2(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.pow(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.pow(x, y)', 'x', ['y'])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([ 2.0])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.radians(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.radians(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.sin(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.sin(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.sinh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.sinh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.sqrt(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.sqrt(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.tan(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.tan(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.tanh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.tanh(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.trunc(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['f'] = (pythontime, acalctime, pythontime / acalctime)


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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('math.trunc(x)', 'x', [])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['d'] = (pythontime, acalctime, pythontime / acalctime)

##############################################################################


BenchClasses = [(benchmark_add, 'add'), (benchmark_sub, 'sub'), (benchmark_mult, 'mult'), (benchmark_div, 'div'), (benchmark_floordiv, 'floordiv'), (benchmark_mod, 'mod'), (benchmark_uadd, 'uadd'), (benchmark_usub, 'usub'), (benchmark_pow, 'pow'), (benchmark_bitand, 'bitand'), (benchmark_bitor, 'bitor'), (benchmark_bitxor, 'bitxor'), (benchmark_invert, 'invert'), (benchmark_lshift, 'lshift'), (benchmark_rshift, 'rshift'), (benchmark_abs, 'abs'), (benchmark_math_acos, 'math_acos'), (benchmark_math_acosh, 'math_acosh'), (benchmark_math_asin, 'math_asin'), (benchmark_math_asinh, 'math_asinh'), (benchmark_math_atan, 'math_atan'), (benchmark_math_atan2, 'math_atan2'), (benchmark_math_atanh, 'math_atanh'), (benchmark_math_ceil, 'math_ceil'), (benchmark_math_copysign, 'math_copysign'), (benchmark_math_cos, 'math_cos'), (benchmark_math_cosh, 'math_cosh'), (benchmark_math_degrees, 'math_degrees'), (benchmark_math_erf, 'math_erf'), (benchmark_math_erfc, 'math_erfc'), (benchmark_math_exp, 'math_exp'), (benchmark_math_expm1, 'math_expm1'), (benchmark_math_fabs, 'math_fabs'), (benchmark_math_factorial, 'math_factorial'), (benchmark_math_floor, 'math_floor'), (benchmark_math_fmod, 'math_fmod'), (benchmark_math_gamma, 'math_gamma'), (benchmark_math_hypot, 'math_hypot'), (benchmark_math_ldexp, 'math_ldexp'), (benchmark_math_lgamma, 'math_lgamma'), (benchmark_math_log, 'math_log'), (benchmark_math_log10, 'math_log10'), (benchmark_math_log1p, 'math_log1p'), (benchmark_math_log2, 'math_log2'), (benchmark_math_pow, 'math_pow'), (benchmark_math_radians, 'math_radians'), (benchmark_math_sin, 'math_sin'), (benchmark_math_sinh, 'math_sinh'), (benchmark_math_sqrt, 'math_sqrt'), (benchmark_math_tan, 'math_tan'), (benchmark_math_tanh, 'math_tanh'), (benchmark_math_trunc, 'math_trunc')]
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

with open('benchacalcdata.txt', 'w') as f:

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


