#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the code for benchmark tests for math functions.
# Language: Python 3.4
# Date:     17-Sep-2018
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

# The width of the function name column in the output report.
FCOLWIDTH = 10

##############################################################################

# These limits are used with the invert operator. These will NOT produce the
# correct answer in all cases. They are simply intended to provide some sort
# of reasonable run time for comparative benchmarks. 
allinvertlimits = {
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


# ==============================================================================

# The basic class template for benchmarking each array type for an operator.
benchmarkclass_template = '''
##############################################################################
class benchmark_%(funcname)s:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = %(supportedarrays)s
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = '%(funcname)s'
		self.runtimetarget = 0.1
		self.needsydatafix = %(needsydatafix)s



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in (%(floatarrays)s):
			xdata = [float(x) for x in [%(test_op_x)s]]
			ydata = [float(x) for x in [%(test_op_y)s]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [%(test_op_x)s]]
			ydata = [int(x) for x in [%(test_op_y)s]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in (%(unsignedint)s)):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
		self.arraylength = len(self.datax)
		self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))

		# Function ldexp needs a specific array type as the second parameter.
		if self.funcname == 'ldexp':
			self.ldexp_y = int(ydata[-1])
		else:
			self.ldexp_y = None


		# This is used for some optimised tests.
		if len(ydata) > 0:
			self.yvalue = abs(self.datay[-1])
		else:
			self.yvalue = None



	########################################################
	def InitResults(self):
		"""Initialise the attributes which store the test results.
		"""
		self.PyData = dict.fromkeys(arraycodes, None)
		self.AfData = dict.fromkeys(arraycodes, None)
		self.RelData = dict.fromkeys(arraycodes, None)

		self.PyDataFast = dict.fromkeys(arraycodes, None)
		self.AfDataFast = dict.fromkeys(arraycodes, None)
		self.RelDataFast = dict.fromkeys(arraycodes, None)


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''


		self.pythontime = []
		self.aftime = []
		self.relativetime = []
		self.relativetimefast = []



	########################################################
	def fmtreldata(self, val):
		"""Format the output data for relative performance.
		"""
		if val == None:
			return ' '.rjust(5)

		if val >= 10.0:
			return ('%%0.0f' %% val).rjust(5)
		else:
			return ('%%0.1f' %% val).rjust(5)


	########################################################
	def fmtabsdata(self, val):
		"""Format the output data for micro-second results.
		"""
		if val == None:
			return ' '.rjust(8)
		else:
			return ('%%d' %% (val * 1000000.0)).rjust(8)


	##############################################################################
	def invertpysigned(self, val, maxval):
		"""This is used to benchmark invert Python native operations on 
		signed integers.
		"""
		return ~val


	##############################################################################
	def invertpyunsigned(self, val, maxval):
		"""This is used to benchmark invert Python native operations on 
		unsigned integers.
		"""
		if val >= 0:
			return maxval - val
		else:
			return maxval + val


	########################################################
	def RunTests(self):
		"""Run all the tests.
		"""

		# First, do a timing calibration run.
		# Python native time.
		for arraycode in self.supportedarrays:
			pytime = self.BenchmarkPython(arraycode)
			self.pythontime.append(pytime)


		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			aftime = self.BenchmarkAF(arraycode)
			self.aftime.append(aftime)


		# Now calculate the average execution time and adjust the iterations
		# so that the tests will take approximately 0.1 seconds.
		self.pyitercounts = int(self.runtimetarget / (sum(self.pythontime) / len(self.pythontime))) + 1
		self.afitercounts = int(self.runtimetarget / (sum(self.aftime) / len(self.pythontime))) + 1


		# Clear the results from the calibration run.
		self.InitResults()

		# Now repeat using the stabilized timing calibration data.
		# Python native time.
		for arraycode in self.supportedarrays:
			pytime = self.BenchmarkPython(arraycode)
			self.PyData[arraycode] = pytime
			self.pythontime.append(pytime)

		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			aftime = self.BenchmarkAF(arraycode)
			self.AfData[arraycode] = aftime
			self.aftime.append(aftime)

		# Relative time.
		reldata = dict([(x, self.PyData[x] / y) for x,y in self.AfData.items() if y != None])
		self.RelData.update(reldata)
		self.relativetime = [self.PyData[x] / self.AfData[x] for x in self.supportedarrays] 


		# We need to escape any function names ending with an underscore to 
		# prevent it being interpreted as a formatting character in restructured
		# text input. 
		if self.funcname.endswith('_'):
			funcesc = self.funcname.rstrip('_') + '\_'
		else:
			funcesc = self.funcname
		fname = funcesc.rjust(FCOLWIDTH)

		# Format the results strings.
		self.PyResults = fname + ' '.join([self.fmtabsdata(self.PyData[x]) for x in arraycodes])
		self.FuncResults = fname + ' '.join([self.fmtabsdata(self.AfData[x]) for x in arraycodes])
		self.RelativeResults = fname + ' '.join([self.fmtreldata(self.RelData[x]) for x in arraycodes])


		# Repeat using optimised options and call forms.
		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			self.AfDataFast[arraycode] = self.BenchmarkAFFast(arraycode)

		# Relative time.
		reldatafast = dict([(x, self.PyData[x] / y) for x,y in self.AfDataFast.items() if y != None])
		self.RelDataFast.update(reldatafast)
		self.relativetimefast = [self.PyData[x] / self.AfDataFast[x] for x in self.supportedarrays] 


		# Format the fast result strings.
		self.PyResultsFast = self.PyResults
		self.FuncResultsFast = fname + ' '.join([self.fmtabsdata(self.AfDataFast[x]) for x in arraycodes])
		self.RelativeResultsFast = fname + ' '.join([self.fmtreldata(self.RelDataFast[x]) for x in arraycodes])



	########################################################
	def BenchmarkPython(self, arraycode):
		"""Measure execution time of native Python code.
		"""
		# This is only for benchmarking invert operations.
		invertmaxval = allinvertlimits[arraycode]
		if arraycode in ('b', 'h', 'i', 'l', 'q'):
			invertop = self.invertpysigned
		else:
			invertop = self.invertpyunsigned


		# Initialise the test data arrays. We provide a local reference to
		# the arrays to make the representation simpler.
		self.InitDataArrays(arraycode)
		datax = self.datax
		datay = self.datay
		dataout = self.dataout
		# Used for ldexp only.
		ldexp_y = self.ldexp_y
		truediv_type = self.truediv_type


		# This is used for some tests only. 
		result = True


		# Time for python.
		starttime = time.perf_counter()
		for x in range(self.pyitercounts):
			for i in range(self.arraylength):
				%(pyequ)s
		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		return pythontime


	########################################################
	def BenchmarkAF(self, arraycode):
		"""Measure execution time for arrayfunc.
		"""
		# This is used for some tests only. 
		result = True

		# Initialise the test data arrays again with fresh data. 
		self.InitDataArrays(arraycode)
		datax = self.datax
		datay = self.datay
		dataout = self.dataout
		# Used for ldexp only.
		ldexp_y = self.ldexp_y



		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			%(arrayfuncequ)s
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime



	########################################################
	def BenchmarkAFFast(self, arraycode):
		"""Measure execution time for arrayfunc with optimised calls.
		"""
		# This is used for some tests only. 
		result = True

		# Initialise the test data arrays again with fresh data. 
		self.InitDataArrays(arraycode)
		datax = self.datax
		datay = self.datay
		dataout = self.dataout
		yvalue = self.yvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			%(arrayfuncequfast)s
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################
'''


# ==============================================================================

# This accumulate the list of tests to run.
benchclasslisttemplate = """

BenchClasses = [%s]

arraycodes = %s

TestLabels = [y for x,y in BenchClasses]

"""

# ==============================================================================

# This is used to run all the tests.
benchruntemplate = '''

##############################################################################

# Create the table header.
def FormatHeaderLabels(columnwidth):
	"""Return a string containing the table header labels.
	"""
	return ('function'.center(FCOLWIDTH)) + ' '.join([x.center(columnwidth) for x in arraycodes]) + '\\n'


def FormatTableSep(columnwidth):
	"""Return a string containing the table separator.
	"""
	return '=' * FCOLWIDTH + ' ' + ' '.join(['=' * columnwidth] * len(arraycodes)) + '\\n'


##############################################################################

# Write out the platform data to keep track of what platform the test was run on.
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

PyResults = []
FuncResults = []
RelativeResults = []
RelativeResultsFast = []
numstats = []
numstatsfast = []

CalDataPy = {}
CalDataAF = {}

# Run the tests.
for benchcode, funcname in BenchClasses:
	print(funcname)
	bc = benchcode()
	bc.RunTests()

	
	RelativeResults.append(bc.RelativeResults)
	RelativeResultsFast.append(bc.RelativeResultsFast)
	PyResults.append(bc.PyResults)
	FuncResults.append(bc.FuncResults)

	numstats.extend(bc.relativetime)
	numstatsfast.extend(bc.relativetimefast)


	CalDataPy[funcname] = sum(bc.pythontime) / len(bc.pythontime)
	CalDataAF[funcname] = sum(bc.aftime) / len(bc.aftime)


##############################################################################

# Print the results

with open('benchmathdata.txt', 'w') as f:

	f.write(time.ctime() + '\\n')

	WritePlatformSignature(f)


	##########################################################################

	# The relative performance stats in default configuration.

	f.write('Relative Performance - Python Time / Arrayfunc Time.\\n')
	f.write(FormatTableSep(5))
	f.write(FormatHeaderLabels(5))
	f.write(FormatTableSep(5))
	
	f.write('\\n'.join(RelativeResults) + '\\n')

	f.write(FormatTableSep(5))

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


	# The relative performance stats in optimised configuration.

	f.write('Relative Performance with Optimisations - Python Time / Arrayfunc Time.\\n')
	f.write(FormatTableSep(5))
	f.write(FormatHeaderLabels(5))
	f.write(FormatTableSep(5))
	
	f.write('\\n'.join(RelativeResultsFast) + '\\n')

	f.write(FormatTableSep(5))


	avgvalfast = sum(numstatsfast) / len(numstatsfast)
	maxvalfast = max(numstatsfast)
	minvalfast = min(numstatsfast)


	f.write('\\n\\n\\n')
	f.write('=========== ========\\n')
	f.write('Stat         Value\\n')
	f.write('=========== ========\\n')
	f.write('Average:    %0.0f\\n' % avgvalfast)
	f.write('Maximum:    %0.0f\\n' % maxvalfast)
	f.write('Minimum:    %0.1f\\n' % minvalfast)
	f.write('Array size: %d\\n' % ARRAYSIZE)
	f.write('=========== ========\\n')


	##########################################################################

	f.write('\\n\\n\\n')

	f.write('Python native time in micro-seconds.\\n')
	f.write(FormatTableSep(8))
	f.write(FormatHeaderLabels(8))
	f.write(FormatTableSep(8))
	
	f.write('\\n'.join(PyResults) + '\\n')

	f.write(FormatTableSep(8))



	f.write('\\n\\nArrayfunc time in micro-seconds.\\n')
	f.write(FormatTableSep(8))
	f.write(FormatHeaderLabels(8))
	f.write(FormatTableSep(8))
	
	f.write('\\n'.join(FuncResults) + '\\n')

	f.write(FormatTableSep(8))



##############################################################################


'''


# ==============================================================================

# This defines the python code form of the benchmark equations.
pyequ = {'test_template_noparams' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_invert' : 'dataout[i] = invertop(datax[i], invertmaxval)',
	'test_template_uniop' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_nonfinite' : 'result = %(pyop)s(datax[i])',
	'test_template_ldexp' : 'dataout[i] = %(pyop)s(datax[i], ldexp_y)',
	'test_template' : 'dataout[i] = %(pyop)s(datax[i], datay[i])',
	'test_template_binop' : 'dataout[i] = datax[i] %(pyop)s datay[i]',
	'test_template_comp' : 'result = datax[i] %(pyop)s datay[i]',
	'test_template_op' : 'dataout[i] = datax[i] %(pyop)s datay[i]',
}


# This defines the arrayfunc code form of the benchmark equations.
arrayfuncequ = {'test_template_noparams' : 'arrayfunc.%s(datax, dataout)',
	'test_template_invert' : 'arrayfunc.%s(datax, dataout)',
	'test_template_uniop' : 'arrayfunc.%s(datax, dataout)',
	'test_template_nonfinite' : 'result = arrayfunc.%s(datax)',
	'test_template_ldexp' : 'arrayfunc.%s(datax, ldexp_y, dataout)',
	'test_template' : 'arrayfunc.%s(datax, datay, dataout)',
	'test_template_binop' : 'arrayfunc.%s(datax, datay, dataout)',
	'test_template_comp' : 'result = arrayfunc.%s(datax, datay)',
	'test_template_op' : 'arrayfunc.%s(datax, datay, dataout)',
}


# This defines the *optimised* arrayfunc code form of the benchmark equations.
arrayfuncequfast = {'test_template_noparams' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_invert' : 'arrayfunc.%s(datax, dataout)',
	'test_template_uniop' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_nonfinite' : 'result = arrayfunc.%s(datax)',
	'test_template_ldexp' : 'arrayfunc.%s(datax, ldexp_y, dataout, matherrors=True)',
	'test_template' : 'arrayfunc.%s(datax, datay, dataout, matherrors=True)',
	'test_template_binop' : 'arrayfunc.%s(datax, datay, dataout)',
	'test_template_comp' : 'result = arrayfunc.%s(datax, datay)',
	'test_template_op' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True)',
	
}


# ==============================================================================

# Read the operator and function definition data.
opdata = codegen_common.ReadCSVData('funcs.csv')


# ==============================================================================

# The names of all the benchmark classes.
benchclasses = []

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('benchamap', '05-Apr-2018', '')


with open('benchmath.py', 'w') as f:

	# This creates the file header at the top of the file.
	f.write(headertemplate % headerdate)

	# This creates the actual tests.
	for op in opdata:
		# Array types to test.
		arraytypes = set(op['arraytypes'].split(','))
		# All array types supported.
		if arraytypes == {'si', 'ui', 'f'}:
			supportedarrays = codegen_common.arraycodes
		# Only signed array types.
		elif arraytypes == {'si', 'f'}:
			supportedarrays = codegen_common.signedint + codegen_common.floatarrays
		# Only integer arrays.
		elif arraytypes == {'si', 'ui'}:
			supportedarrays = codegen_common.intarrays
		# Only floating point arrays.
		elif arraytypes == {'f'}:
			supportedarrays = codegen_common.floatarrays
		else:
			print('Error - supported array types not recognised', op['arraytypes'])

		

		opdata = {'funcname' : op['funcname'],
		'test_op_x' : op['test_op_x'], 'test_op_y' : op['test_op_y'],
		'supportedarrays' : supportedarrays,
		'needsydatafix' : op['test_op_templ'] == 'test_template_op',
		'floatarrays' : "'" + "', '".join(codegen_common.floatarrays) + "'",
		'unsignedint' : "'" + "', '".join(codegen_common.unsignedint) + "'",
		'pyequ' : pyequ[op['test_op_templ']] % {'pyop' : op['pyoperator']},
		'arrayfuncequ' : arrayfuncequ[op['test_op_templ']] % op['funcname'],
		'arrayfuncequfast' : arrayfuncequfast[op['test_op_templ']] % op['funcname'],
		}

		# True division needs a special equation to avoid type errors. In
		# python, truediv aways produces a floating point result, which
		# causes errors when saving into an integer array. To solve this,
		# we call a type conversion function which select at run time.
		if opdata['funcname'] == 'truediv':
			opdata['pyequ'] = 'dataout[i] = truediv_type(datax[i] / datay[i])'


		# Now put it together into a single class.
		f.write(benchmarkclass_template % opdata)

		# Add the name of the class to the list.
		benchclasses.append("(benchmark_%s, '%s')" % (op['funcname'], op['funcname']))



	# The list of benchmark class names.
	f.write(benchclasslisttemplate % (', '.join(benchclasses), codegen_common.arraycodes))


	# This writes the code to execute all the tests.
	f.write(benchruntemplate)

