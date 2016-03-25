#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the code for the benchmark for amap and amapi.
# Language: Python 3.4
# Date:     17-Sep-2014
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

import itertools
import time

import codegen_common


# ==============================================================================

# This goes at the top of the generated file.
headertemplate = """#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   %(testfilename)s.py
# Purpose:  Benchmark functions for amap and amapi.
# Language: Python 3.4
# Date:     %(startdate)s.
# Ver:      %(verdate)s.
#
###############################################################################
#
#   Copyright 2014 - %(cpyear)s    Michael Griffin    <m12.griffin@gmail.com>
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
"""

calibrationdata = '''
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
'''




# This accumulate the list of tests to run.
benchclasslisttemplate = """

BenchClasses = [%s]
arraycodes = %s

TestLabels = [y for x,y in BenchClasses]

"""



# This is used to run all the tests.
benchruntemplate = '''

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
	tableformat = '%(func)14s ' + ' '.join(['%(' + x + (')%is' % columnwidth) for x in arraycodes]) + '\\n'

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

with open('benchmarkdata.txt', 'w') as f:
	WriteResults(f, 5, RelativeResults)

	avgval = sum(numstats) / len(numstats)
	maxval = max(numstats)
	minval = min(numstats)


	f.write('\\n\\n\\n')
	f.write('=========== ========\\n')
	f.write('Stat         Value\\n')
	f.write('=========== ========\\n')
	f.write('Average:    %0.0f\\n' % avgval)
	f.write('Maximum:    %0.0f\\n' % maxval)
	f.write('Minimum:    %0.1f\\n' % minval)
	f.write('Array size: %d\\n' % ARRAYSIZE)
	f.write('=========== ========\\n')



##############################################################################

with open('benchmarkplatform.txt', 'w') as f:

	f.write('Python native time in micro-seconds.\\n')
	WriteResults(f, 8, PyResults)

	f.write('\\n\\nArrayfunc time in micro-seconds.\\n')
	WriteResults(f, 8, FuncResults)


##############################################################################


'''


# ==============================================================================

# The basic class template for benchmarking each array type for an operator.
benchmarkclass_template = '''
##############################################################################
class benchmark_%(opcodename)s:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['%(opcodename)s'][0]
		self.afitercounts = calibrationdata['%(opcodename)s'][1]
'''

# The list of functions to be found in the class.
benchmarkfuncnames_template = '''

	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""
		# This is a platform check to handle instructions which are not 
		# supported by the MS VC 2010 compiler. 
		self.msvs_has = %s
		if not self.msvs_has and platform.python_compiler().startswith('MSC'):
			return

		self.TestFuncs = [%s]
		for testfunc in self.TestFuncs:
			testfunc()

'''

# The basic template for a single benchmark.
benchmark_template = '''
	########################################################
	def Benchmark_%(typecode)s(self):
		"""Measure execution time.
		"""
		TypeCode = '%(typecode)s'
		InvertMask = allinvertmasks['%(typecode)s']

		data = array.array('%(typecode)s', (x for x,y in zip(itertools.cycle([%(test_op_x)s]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('%(typecode)s', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(arraylength):
				dataout[i] = %(pyequ)s
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		data = array.array('%(typecode)s', (x for x,y in zip(itertools.cycle([%(test_op_x)s]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('%(typecode)s', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.amap(arrayfunc.aops.%(opcodename)s, data, dataout %(yparamdata)s)
		endtime = time.perf_counter()

		amaptime = (endtime - starttime) / self.afitercounts


		self.TestResults['%(typecode)s'] = (pythontime, amaptime, pythontime / amaptime)

'''


classend = """##############################################################################
"""


# ==============================================================================

# Read the operator and function definition data.
csvdata = codegen_common.ReadCSVData('arrayfunc.csv')

# ==============================================================================


with open('benchmark.py', 'w') as f:

	opdata = [x for x in csvdata]

	# The names of all the benchmark classes.
	benchclasses = []

	# Data for the copyright header files.
	headerdate = codegen_common.FormatHeaderData('benchmark', '17-Sep-2014', '')

	# This creates the file header at the top of the file.
	f.write(headertemplate % headerdate)

	# Add the test time calibration data. This can be altered if necessary.
	f.write(calibrationdata)

	# This creates the actual tests.
	for op in opdata:

		opdata = {}
		opdata.update(op)

		testclass = []
		funcnames = []

		benchclasses.append("(benchmark_%s, '%s')" % (op['opcodename'], op['opcodename']))

		# Test number and type of parameters.
		for funtypes in codegen_common.arraycodes:
			opdata['typecode'] = funtypes

			if funtypes in codegen_common.signedint:
				opdata['test_op_x'] = opdata['test_op_x_isigned']
				test_op_y = opdata['test_op_y_isigned']
				typeconvert = 'int'
				typevalid = opdata['c_code_template_i_signed'] != ''
			elif funtypes in codegen_common.unsignedint:
				opdata['test_op_x'] = opdata['test_op_x_iunsigned']
				test_op_y = opdata['test_op_y_iunsigned']
				typeconvert = 'int'
				typevalid = opdata['c_code_template_i_unsigned'] != ''
			elif funtypes in codegen_common.floatarrays:
				opdata['test_op_x'] = opdata['test_op_x_float']
				test_op_y = opdata['test_op_y_float']
				typeconvert = 'float'
				typevalid = opdata['c_code_template_float'] != ''
			else:
				print('Unknown array code.')


			# Skip if the operation is not valid for this type.
			if typevalid:
				opsymbol = opdata['pyoperator']
				if opdata['#params'] == '1':
					yvalue = test_op_y.split(',')[-1]
					opdata['yparamdata'] = ', %s' % yvalue
				else:
					opdata['yparamdata'] = ''
					yvalue = ''
				opdata['pyequ'] = opdata['py_benchmark'] % {'op' : opdata['pyoperator'], 
					'typeconvert' : typeconvert, 'yparamdata' : yvalue, 'typecode' : funtypes}

				testclass.append(benchmark_template % opdata)
				funcnames.append('self.Benchmark_' + funtypes)



		# Write the class header.
		f.write(benchmarkclass_template % op)

		# Write the list of function names.
		f.write(benchmarkfuncnames_template % (op['msvs_has'] != '0', ', '.join(funcnames)))

		# Write the body of the class.
		f.write(''.join(testclass))

		# A separator comment at the end of the class.
		f.write(classend)


	# This accumulates the list of all the test classes.
	f.write(benchclasslisttemplate % (', '.join(benchclasses), codegen_common.arraycodes))

	# This executes all the tests.
	f.write(benchruntemplate)
