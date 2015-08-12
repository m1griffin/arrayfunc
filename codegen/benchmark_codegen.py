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

import arrayfunc

##############################################################################

# The size of test array to use.
ARRAYSIZE = 100000

##############################################################################

# The following is the auto-generated test code.
"""




# This accumulate the list of tests to run.
benchclasslisttemplate = """

BenchClasses = [%s]
arraycodes = %s

"""



# This is used to run all the tests.
benchruntemplate = '''

tableheader = {'func' : 'opcode', 'b' : 'b', 'B' : 'B', 'h' : 'h', 'H' : 'H', 
		'i' : 'i', 'I' : 'I', 'l' : 'l', 'L' : 'L', 'q' : 'q', 'Q' : 'Q', 
		'f' : 'f', 'd' : 'd'}

tableformat = '%(func)14s %(b)5s %(B)5s %(h)5s %(H)5s %(i)5s %(I)5s %(l)5s %(L)5s %(q)5s %(Q)5s %(f)5s %(d)5s\\n'
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
		InvertMask = %(invertmask)s

		data = array.array('%(typecode)s', (x for x,y in zip(itertools.cycle([%(test_op_x)s]), itertools.repeat(0, ARRAYSIZE))))
		arraylength = len(data)
		dataout = array.array('%(typecode)s', itertools.repeat(0, arraylength))

		# Time for python.
		starttime = time.time()
		for i in range(arraylength):
			dataout[i] = %(pyequ)s
		endtime = time.time()

		pythontime = endtime - starttime

		data = array.array('%(typecode)s', (x for x,y in zip(itertools.cycle([%(test_op_x)s]), itertools.repeat(0, ARRAYSIZE))))
		dataout = array.array('%(typecode)s', itertools.repeat(0, arraylength))

		# Time for amap.
		starttime = time.time()
		arrayfunc.amap(arrayfunc.aops.%(opcodename)s, data, dataout %(yparamdata)s)
		endtime = time.time()

		amaptime = endtime - starttime

		data = array.array('%(typecode)s', (x for x,y in zip(itertools.cycle([%(test_op_x)s]), itertools.repeat(0, ARRAYSIZE))))

		# Time for amapi.
		starttime = time.time()
		arrayfunc.amapi(arrayfunc.aops.%(opcodename)s, data %(yparamdata)s)
		endtime = time.time()

		amapitime = endtime - starttime

		self.TestResults['%(typecode)s'] = (pythontime, amaptime, amapitime, pythontime / amaptime, pythontime / amapitime)

'''


classend = """##############################################################################
"""


# This runs all the tests.
benchrun = """

BenchClasses = [%s]
arraycodes = %s

with open('benchmark.csv', 'w') as f:
	benchheader = 'opcode,' + ','.join(arraycodes) + '\\n'
	f.write(benchheader)
	for i, j in BenchClasses:
		bc = i()
		bc.RunTests()
		print(j, bc.TestResults)
		defaultdata = ['','','','','']
		benchline = j + ',' + ','.join([str(bc.TestResults.get(x, defaultdata)[4]) for x in arraycodes]) + '\\n'
		f.write(benchline)


"""

# ==============================================================================

# These masks are used with the invert operator. These will NOT produce the
# correct answer in all cases. They are simply intended to provide some sort
# of reasonable run time for comparative benchmarks. 
invertmasks = {
	'b' : 0x7f,
	'B' : 0xff, 
	'h' : 0x7fff, 
	'H' : 0xffff, 
	'i' : 0x7fffffff, 
	'I' : 0xffffffff, 
	'l' : 0x7fffffffffffffff, 
	'L' : 0xffffffffffffffff, 
	'q' : 0x7fffffffffffffff, 
	'Q' : 0xffffffffffffffff, 
	'f' : 0xffffffffffffffff, 
	'd' : 0xffffffffffffffff, 
}

# ==============================================================================

# Read the operator and function definition data.
csvdata = codegen_common.ReadCSVData()

# ==============================================================================


with open('benchmark.py', 'w') as f:

	opdata = [x for x in csvdata]

	# The names of all the benchmark classes.
	benchclasses = []

	# Data for the copyright header files.
	headerdate = codegen_common.FormatHeaderData('benchmark', '17-Sep-2014', '')

	# This creates the file header at the top of the file.
	f.write(headertemplate % headerdate)



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

			# This is the mask for the invert operation.
			opdata['invertmask'] = invertmasks[funtypes]

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
		f.write(benchmarkfuncnames_template % ', '.join(funcnames))

		# Write the body of the class.
		f.write(''.join(testclass))

		# A separator comment at the end of the class.
		f.write(classend)


	# This accumulates the list of all the test classes.
	f.write(benchclasslisttemplate % (', '.join(benchclasses), codegen_common.arraycodes))

	# This executes all the tests.
	f.write(benchruntemplate)
