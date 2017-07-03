#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the code for the benchmark for acalc.
# Language: Python 3.4
# Date:     04-Feb-2016
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
# Purpose:  Benchmark functions for acalc.
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

# Write out the platform data to keep track of what platform the
def WritePlatformSignature(f):
	# test was run on.
	# 'Linux'
	f.write('Operating System: ' + platform.system() + '\\n')

	# 'Linux-4.4.0-79-generic-x86_64-with-Ubuntu-16.04-xenial'
	f.write('Platform: ' + platform.platform() + '\\n')

	# ('64bit', 'ELF')
	f.write('Word size: ' + platform.architecture()[0] + '\\n')

	# 'GCC 5.4.0 20160609'
	f.write('Compiler: ' + platform.python_compiler() + '\\n')

	# '4.4.0-79-generic'
	f.write('Python release: ' + platform.release() + '\\n')
	f.write('\\n\\n\\n')



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


	f.write('\\n\\n\\n')
	f.write('=========== ========\\n')
	f.write('Stat         Value\\n')
	f.write('=========== ========\\n')
	f.write('Average:    %0.0f\\n' % avgval)
	f.write('Maximum:    %0.0f\\n' % maxval)
	f.write('Minimum:    %0.1f\\n' % minval)
	f.write('Array size: %d\\n' % ARRAYSIZE)
	f.write('=========== ========\\n')



	##########################################################################

	f.write('\\n\\n\\n')

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
class benchmark_%(oplabel)s:
	"""Test for basic operator function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.TestResults = {}
		self.pyitercounts = calibrationdata['%(oplabel)s'][0]
		self.afitercounts = calibrationdata['%(oplabel)s'][1]
'''

# The list of functions to be found in the class.
benchmarkfuncnames_template = '''

	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""

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

		eqnd = arrayfunc.acalc.calc(data, dataout)
		eqnd.comp('%(pyop)s', 'x', [%(yname)s])

		# Time for acalc.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			eqnd.execute([%(yparamdata)s])
		endtime = time.perf_counter()

		acalctime = (endtime - starttime) / self.afitercounts


		self.TestResults['%(typecode)s'] = (pythontime, acalctime, pythontime / acalctime)

'''


classend = """##############################################################################
"""

# ==============================================================================

# Read the operator and function definition data.
csvdata = codegen_common.ReadCSVData('arraycalc.csv')

# ==============================================================================


with open('benchacalc.py', 'w') as f:

	opdata = [x for x in csvdata if x['py_benchmark'] != '']

	# The names of all the benchmark classes.
	benchclasses = []

	# Data for the copyright header files.
	headerdate = codegen_common.FormatHeaderData('benchacalc', '05-Feb-2016', '')

	# This creates the file header at the top of the file.
	f.write(headertemplate % headerdate)

	# Add the test time calibration data. This can be altered if necessary.
	f.write(calibrationdata)


	for op in opdata:

		opvalues = {}
		opvalues.update(op)

		testclass = []
		funcnames = []

		# Sanitize the name to create valid function names without '.' characters.
		sanitizedopcode = op['opcodename'].replace('.', '_')
		benchclasses.append("(benchmark_%s, '%s')" % (sanitizedopcode, sanitizedopcode))

		# Test number and type of parameters.
		for funtypes in codegen_common.arraycodes:
			opvalues['typecode'] = funtypes

			if funtypes in codegen_common.signedint:
				opvalues['test_op_x'] = op['test_op_x_isigned']
				test_op_y = op['test_op_y_isigned']
				typeconvert = 'int'
				typevalid = op['c_code_template_i_signed'] != ''
			elif funtypes in codegen_common.unsignedint:
				opvalues['test_op_x'] = op['test_op_x_iunsigned']
				test_op_y = op['test_op_y_iunsigned']
				typeconvert = 'int'
				typevalid = (op['c_code_template_i_unsigned'] != '') and (op['signed_only'] != '1')
			elif funtypes in codegen_common.floatarrays:
				opvalues['test_op_x'] = op['test_op_x_float']
				test_op_y = op['test_op_y_float']
				typeconvert = 'float'
				typevalid = op['c_code_template_float'] != ''
			else:
				print('Unknown array code.')


			# Skip if the operation is not valid for this type.
			if typevalid:
				opsymbol = opvalues['pyoperator']
				if op['#params'] == '1':
					yvalue = test_op_y.split(',')[-1]
					opvalues['yparamdata'] = '%s' % yvalue
					opvalues['yname'] = "'y'"
				else:
					opvalues['yparamdata'] = ''
					yvalue = ''
					opvalues['yname'] = ''
				opvalues['pyequ'] = op['py_benchmark'] % {'op' : op['pyoperator'], 
					'typeconvert' : typeconvert, 'yparamdata' : yvalue, 'typecode' : funtypes}

				opvalues['pyop'] = op['opcodedocs']

				testclass.append(benchmark_template % opvalues)
				funcnames.append('self.Benchmark_' + funtypes)



		# Write the class header.
		# Sanitize the name to create valid function names without '.' characters.
		f.write(benchmarkclass_template % {'oplabel' : op['opcodename'].replace('.', '_')})

		# Write the list of function names.
		f.write(benchmarkfuncnames_template % ', '.join(funcnames))

		# Write the body of the class.
		f.write(''.join(testclass))

		# A separator comment at the end of the class.
		f.write(classend)


	# This accumulates the list of all the test classes.
	f.write(benchclasslisttemplate % (', '.join(benchclasses), codegen_common.arraycodes))

	# This executes all the tests.
	f.write(benchruntemplate)
