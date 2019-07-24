#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the code for benchmark tests for 'arrayfunc' functions.
# Language: Python 3.5
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
headertemplate = '''#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   %(testfilename)s.py
# Purpose:  Benchmark tests for 'arrayfunc' functions.
# Language: Python 3.5
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
FCOLWIDTH = 12

# The width of data columns for absolute (actual time) data.
ABSCOLWIDTH=10

# The width of data columns for relative time data.
RELCOLWIDTH=5

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

# This defines which functions and which array types have SIMD versions.
# This was generated automtically by searching through the C source code 
# header files which must be present in the expected place when the 
# benchmark program is generated.

SIMDFuncs = %(SIMD_data)s

# This one is a list of functions which use the 'matherrors' option.
OptFuncs = %(Opt_data)s

##############################################################################

##############################################################################

def comptype(arraycode, cval):
	"""Return the compare value in the correct type.
	"""
	if arraycode in ('f', 'd'):
		return float(cval)
	else:
		return int(cval)


def pyfindindices(datax, dataout, compval):
	"""Used to emulate the findindices arrayfunc function.
	"""
	z = 0
	for x in datax:
		if x == compval:
			dataout[z] = z
			z += 1
	return z


def pyfindindex(datax, compval):
	"""Used to emulate the findindex arrayfunc function.
	"""
	try:
		return datax.index(compval)
	except ValueError:
		return -1


def pycount(arraycode, pyitercounts, data):
	"""Used to emulate the count arrayfunc function.
	"""
	# This is used to prevent integers exceeding the maximum size
	# for smaller word sizes.
	rollmasks = {
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

	if arraycode in ('b', 'B', 'h', 'H'):
		mask = rollmasks[arraycode]
		for x, y in zip(itertools.count(0), itertools.repeat(0, ARRAYSIZE)):
			data[x] = x & mask
	else:
		for x, y in zip(itertools.count(0), itertools.repeat(0, ARRAYSIZE)):
			data[x] = x


##############################################################################

# The following is the auto-generated test code.
'''


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

		# We need to escape any function names ending with an underscore to 
		# prevent it being interpreted as a formatting character in restructured
		# text input. 
		if self.funcname.endswith('_'):
			funcesc = self.funcname.rstrip('_') + '\_'
		else:
			funcesc = self.funcname
		self.escfname = funcesc.rjust(FCOLWIDTH)


	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in (%(floatarrays)s):
			xdata = [float(x) for x in %(test_op_x)s]
			ydata = [float(x) for x in %(test_op_y)s]
			zdata = [float(x) for x in %(test_op_z)s]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in %(test_op_x)s]
			ydata = [int(x) for x in %(test_op_y)s]
			zdata = [int(x) for x in %(test_op_z)s]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in (%(unsignedint)s)):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %%d' %% len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in %(arraysreq)s:
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %%d' %% len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in %(arraysreq)s:
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %%d' %% len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in %(arraysreq)s:
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %%d' %% len(self.dataout)
		else:
			self.dataout = None



		# Function ldexp needs a specific array type as the second parameter.
		if self.funcname == 'ldexp':
			self.ldexp_y = int(ydata[-1])
		else:
			self.ldexp_y = None


		# This is used for some optimised tests.
		if len(ydata) > 0:
			self.yvalue = abs(ydata[-1])
		else:
			self.yvalue = None


		# This is used for some tests.
		if arraycode in ('f', 'd'):
			self.compval =  float(%(compval)s)
		else:
			self.compval =  int(%(compval)s)

		
		# Used for compress.
		if '%(funcname)s' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in %(arraysreq)s:
			self.fidataout = array.array('q', itertools.repeat(0, ARRAYSIZE))


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
		self.RelDataOpt = dict.fromkeys(arraycodes, None)
		self.AfDataSIMD = dict.fromkeys(arraycodes, None)
		self.RelDataSIMD = dict.fromkeys(arraycodes, None)

		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelativeResultsSIMD = ''
		self.RelOpt = ''
		self.RelSIMD = ''


		self.pythontime = []
		self.aftime = []
		self.relativetime = []
		self.relativetimefast = []
		self.relativetimesimd = []
		self.relativetimeopt = []



	########################################################
	def fmtreldata(self, val):
		"""Format the output data for relative performance.
		"""
		if val == None:
			return ' '.rjust(RELCOLWIDTH)

		if val >= 10.0:
			return ('%%0.0f' %% val).rjust(RELCOLWIDTH)
		else:
			return ('%%0.1f' %% val).rjust(RELCOLWIDTH)


	########################################################
	def fmtabsdata(self, val):
		"""Format the output data for micro-second results.
		"""
		if val == None:
			return ' '.rjust(ABSCOLWIDTH)
		else:
			return ('%%0.1f' %% (val * 1000000.0)).rjust(ABSCOLWIDTH)


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


	##############################################################################
	def comparedata(self, refdata, testdata):
		"""Compare the resulting test data.
				refdata (dict): The reference the new test data is being compared to.
				testdata (dict): The new test data which is being compared.
			Returns: reldata (dict) = The speed of the test data compared to the reference data.
					relativetime (list) = The speed of the test data compared to the reference data.
		"""
		reldata = dict([(x, refdata[x] / y) for x,y in testdata.items() if y != None])
		relativetime = [refdata[x] / testdata[x] for x in self.supportedarrays] 
		return reldata, relativetime



	########################################################
	def formattimedata(self, testdata):
		"""Format the data for test data as time in microseconds.
			testdata (dict) : The unformatted test data. 
		Returns : A string formatted into columns.
		"""
		return self.escfname + ' '.join([self.fmtabsdata(testdata[x]) for x in arraycodes])


	########################################################
	def formatreldata(self, testdata):
		"""Format the data for test data relative to a reference data set.
			testdata (dict) : The unformatted test data. 
		Returns : A string formatted into columns.
		"""
		return self.escfname + ' '.join([self.fmtreldata(testdata[x]) for x in arraycodes])


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

		# Make sure we don't do so few iterations that test results
		# vary too much due to quantization errors. 
		if self.pyitercounts < 10:
			self.pyitercounts = 20
		if self.afitercounts < 100:
			self.afitercounts = 100

		# Clear the results from the calibration run.
		self.InitResults()

		# Now repeat using the stabilized timing calibration data.
		# Python native time.
		for arraycode in self.supportedarrays:
			self.PyData[arraycode] = self.BenchmarkPython(arraycode)

		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			self.AfData[arraycode] = self.BenchmarkAF(arraycode)

		# Repeat using optimised options and call forms.
		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			self.AfDataFast[arraycode] = self.BenchmarkAFFast(arraycode)


		# Repeat using SIMD options and call forms.
		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			self.AfDataSIMD[arraycode] = self.BenchmarkAFSIMD(arraycode)


		# Relative time, Python versus Arrayfunc.
		reldata, self.relativetime = self.comparedata(self.PyData, self.AfData)
		self.RelData.update(reldata)


		# Relative time, Python versus optimised Arrayfunc.
		reldatafast, self.relativetimefast = self.comparedata(self.PyData, self.AfDataFast)
		self.RelDataFast.update(reldatafast)

		# Relative time, Python versus SIMD optimised Arrayfunc.
		reldatasimd, self.relativetimesimd = self.comparedata(self.PyData, self.AfDataSIMD)
		self.RelDataSIMD.update(reldatasimd)

		# Relative time, non-optimised Arrayfunc versus optimised Arrayfunc.
		reldataopt, self.relativetimeopt = self.comparedata(self.AfData, self.AfDataFast)
		self.RelDataOpt.update(reldataopt)


		# Format the results strings.
		self.PyResults = self.formattimedata(self.PyData)
		self.FuncResults = self.formattimedata(self.AfData)
		self.RelativeResults = self.formatreldata(self.RelData)


		# Format the fast result strings.
		self.FuncResultsFast = self.formattimedata(self.AfDataFast)
		self.RelativeResultsFast = self.formatreldata(self.RelDataFast)


		# Format the fast result strings.
		self.FuncResultsSIMD = self.formattimedata(self.AfDataSIMD)
		self.RelativeResultsSIMD = self.formatreldata(self.RelDataSIMD)

		# Format the optimised versus not optimsed result strings.
		if self.funcname in OptFuncs:
			self.RelOpt = self.formatreldata(self.RelDataOpt)

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = self.escfname + ' '.join([self.simdcalc(x, self.AfDataFast[x], self.AfDataSIMD[x]) for x in arraycodes])


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
		dataz = self.dataz
		dataout = self.dataout
		# Used for ldexp only.
		ldexp_y = self.ldexp_y
		truediv_type = self.truediv_type


		# This is used for some tests only. 
		result = True


		# Time for python.
		starttime = time.perf_counter()
		if %(singledatafunc)s:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					%(pyequ)s
		else:
			for x in range(self.pyitercounts):
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
		dataz = self.dataz
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
		dataz = self.dataz
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



	########################################################
	def BenchmarkAFSIMD(self, arraycode):
		"""Measure execution time for arrayfunc with SIMD.
		"""
		# This is used for some tests only. 
		result = True

		# Initialise the test data arrays again with fresh data. 
		self.InitDataArrays(arraycode)
		datax = self.datax
		datay = self.datay
		dataz = self.dataz
		dataout = self.dataout
		yvalue = self.yvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			%(arrayfuncequsimd)s
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
FuncResultsFast = []
FuncResultsSIMD = []

RelativeResults = []
RelativeResultsFast = []
RelativeResultsSIMD = []

numstats = []
numstatsfast = []
numstatssimd = []
OptResults = []
SIMDResults = []


# Run the tests.
for benchcode, funcname in BenchClasses:
	print(funcname)
	bc = benchcode()
	bc.RunTests()

	
	RelativeResults.append(bc.RelativeResults)
	RelativeResultsFast.append(bc.RelativeResultsFast)
	RelativeResultsSIMD.append(bc.RelativeResultsSIMD)
	PyResults.append(bc.PyResults)
	FuncResults.append(bc.FuncResults)
	FuncResultsFast.append(bc.FuncResultsFast)
	FuncResultsSIMD.append(bc.FuncResultsSIMD)
	OptResults.append(bc.RelOpt)
	SIMDResults.append(bc.RelSIMD)

	numstats.extend(bc.relativetime)
	numstatsfast.extend(bc.relativetimefast)
	numstatssimd.extend(bc.relativetimesimd)


##############################################################################

# Print the results

with open('benchmarkdata.txt', 'w') as f:

	f.write(time.ctime() + '\\n')

	WritePlatformSignature(f)


	##########################################################################

	# The relative performance stats in default configuration.

	f.write('Relative Performance - Python Time / Arrayfunc Time.\\n')
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))
	
	f.write('\\n'.join(RelativeResults) + '\\n')

	f.write(FormatTableSep(RELCOLWIDTH))

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
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))
	
	f.write('\\n'.join(RelativeResultsFast) + '\\n')

	f.write(FormatTableSep(RELCOLWIDTH))


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


	# The relative performance stats in SIMD optimised configuration.

	f.write('Relative Performance with SIMD Optimisations - Python Time / Arrayfunc Time.\\n')
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))
	
	f.write('\\n'.join(RelativeResultsSIMD) + '\\n')

	f.write(FormatTableSep(RELCOLWIDTH))


	avgvalsimd = sum(numstatssimd) / len(numstatssimd)
	maxvalsimd = max(numstatssimd)
	minvalsimd = min(numstatssimd)


	f.write('\\n\\n\\n')
	f.write('=========== ========\\n')
	f.write('Stat         Value\\n')
	f.write('=========== ========\\n')
	f.write('Average:    %0.0f\\n' % avgvalsimd)
	f.write('Maximum:    %0.0f\\n' % maxvalsimd)
	f.write('Minimum:    %0.1f\\n' % minvalsimd)
	f.write('Array size: %d\\n' % ARRAYSIZE)
	f.write('=========== ========\\n')


	##########################################################################

	f.write('\\n\\n\\n')

	f.write('Relative Performance with and without math Optimisations - Unoptimsed / Optimised Time.\\n')
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))
	
	f.write('\\n'.join([x for x in OptResults if x]) + '\\n')

	f.write(FormatTableSep(RELCOLWIDTH))

	##########################################################################

	f.write('\\n\\n\\n')

	f.write('Relative Performance with and without SIMD Optimisations - Optimsed / SIMD Time.\\n')
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))
	
	f.write('\\n'.join([x for x in SIMDResults if x]) + '\\n')

	f.write(FormatTableSep(RELCOLWIDTH))


	##########################################################################

	f.write('\\n\\n\\n')

	f.write('Python native time in micro-seconds.\\n')
	f.write(FormatTableSep(ABSCOLWIDTH))
	f.write(FormatHeaderLabels(ABSCOLWIDTH))
	f.write(FormatTableSep(ABSCOLWIDTH))
	
	f.write('\\n'.join(PyResults) + '\\n')

	f.write(FormatTableSep(ABSCOLWIDTH))



	f.write('\\n\\nArrayfunc time in micro-seconds.\\n')
	f.write(FormatTableSep(ABSCOLWIDTH))
	f.write(FormatHeaderLabels(ABSCOLWIDTH))
	f.write(FormatTableSep(ABSCOLWIDTH))
	
	f.write('\\n'.join(FuncResults) + '\\n')

	f.write(FormatTableSep(ABSCOLWIDTH))



	f.write('\\n\\nOptimised time in micro-seconds.\\n')
	f.write(FormatTableSep(ABSCOLWIDTH))
	f.write(FormatHeaderLabels(ABSCOLWIDTH))
	f.write(FormatTableSep(ABSCOLWIDTH))
	
	f.write('\\n'.join(FuncResultsFast) + '\\n')

	f.write(FormatTableSep(ABSCOLWIDTH))


	f.write('\\n\\nSIMD Optimised time in micro-seconds.\\n')
	f.write(FormatTableSep(ABSCOLWIDTH))
	f.write(FormatHeaderLabels(ABSCOLWIDTH))
	f.write(FormatTableSep(ABSCOLWIDTH))
	
	f.write('\\n'.join(FuncResultsSIMD) + '\\n')

	f.write(FormatTableSep(ABSCOLWIDTH))


##############################################################################


'''


# ==============================================================================

# This defines the python code form of the benchmark equations.
pyequ = {'test_template_noparams' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_noparams_1simd' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_invert' : 'dataout[i] = invertop(datax[i], invertmaxval)',
	'test_template_uniop' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_factorial' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_nonfinite' : 'result = %(pyop)s(datax[i])',
	'test_template_ldexp' : 'dataout[i] = %(pyop)s(datax[i], ldexp_y)',
	'test_template' : 'dataout[i] = %(pyop)s(datax[i], datay[i])',
	'test_template_binop' : 'dataout[i] = datax[i] %(pyop)s datay[i]',
	'test_template_binop2' : 'dataout[i] = datax[i] %(pyop)s datay[i]',
	'test_template_comp' : 'result = datax[i] %(pyop)s datay[i]',
	'test_template_op' : 'dataout[i] = datax[i] %(pyop)s datay[i]',
	'test_template_op_simd' : 'dataout[i] = datax[i] %(pyop)s datay[i]',
	'test_template_fma' : 'dataout[i] = datax[i] * datay[i] + dataz[i]',
}


# This defines the arrayfunc code form of the benchmark equations.
arrayfuncequ = {'test_template_noparams' : 'arrayfunc.%s(datax, dataout)',
	'test_template_noparams_1simd' : 'arrayfunc.%s(datax, dataout, nosimd=True)',
	'test_template_noparams' : 'arrayfunc.%s(datax, dataout)',
	'test_template_invert' : 'arrayfunc.%s(datax, dataout, nosimd=True)',
	'test_template_uniop' : 'arrayfunc.%s(datax, dataout, nosimd=True)',
	'test_template_factorial' : 'arrayfunc.%s(datax, dataout)',
	'test_template_nonfinite' : 'result = arrayfunc.%s(datax)',
	'test_template_ldexp' : 'arrayfunc.%s(datax, ldexp_y, dataout)',
	'test_template' : 'arrayfunc.%s(datax, datay, dataout)',
	'test_template_binop' : 'arrayfunc.%s(datax, datay, dataout)',
	'test_template_binop2' : 'arrayfunc.%s(datax, datay, dataout, nosimd=True)',
	'test_template_comp' : 'result = arrayfunc.%s(datax, datay, nosimd=True)',
	'test_template_op' : 'arrayfunc.%s(datax, datay, dataout)',
	'test_template_op_simd' : 'arrayfunc.%s(datax, datay, dataout, nosimd=True)',
	'test_template_fma' : 'arrayfunc.%s(datax, datay, dataz, dataout)',
}


# This defines the *optimised* arrayfunc code form of the benchmark equations.
arrayfuncequfast = {'test_template_noparams' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_noparams_1simd' : 'arrayfunc.%s(datax, dataout, matherrors=True, nosimd=True)',
	'test_template_invert' : 'arrayfunc.%s(datax, dataout, nosimd=True)',
	'test_template_uniop' : 'arrayfunc.%s(datax, dataout, matherrors=True, nosimd=True)',
	'test_template_factorial' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_nonfinite' : 'result = arrayfunc.%s(datax)',
	'test_template_ldexp' : 'arrayfunc.%s(datax, ldexp_y, dataout, matherrors=True)',
	'test_template' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True)',
	'test_template_binop' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_binop2' : 'arrayfunc.%s(datax, yvalue, dataout, nosimd=True)',
	'test_template_comp' : 'result = arrayfunc.%s(datax, yvalue, nosimd=True)',
	'test_template_op' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True)',
	'test_template_op_simd' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True, nosimd=True)',
	'test_template_fma' : 'arrayfunc.%s(datax, datay, dataz, dataout, matherrors=True)',
	
}


# This defines the SIMD optimised arrayfunc code form of the benchmark equations.
arrayfuncequsimd = {'test_template_noparams' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_noparams_1simd' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_invert' : 'arrayfunc.%s(datax, dataout)',
	'test_template_uniop' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_factorial' : 'arrayfunc.%s(datax, dataout, matherrors=True)',
	'test_template_nonfinite' : 'result = arrayfunc.%s(datax)',
	'test_template_ldexp' : 'arrayfunc.%s(datax, ldexp_y, dataout, matherrors=True)',
	'test_template' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True)',
	'test_template_binop' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_binop2' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_comp' : 'result = arrayfunc.%s(datax, yvalue)',
	'test_template_op' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True)',
	'test_template_op_simd' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True)',
	'test_template_fma' : 'arrayfunc.%s(datax, datay, dataz, dataout, matherrors=True)',
	
}


# This defines how may arrays are used. This will allow avoiding initialising
# arrays which are not needed, to save time.
arraysreq = {'test_template_noparams' : "('dataout')",
	'test_template_noparams_1simd' : "('dataout')",
	'test_template_invert' : "('dataout')",
	'test_template_uniop' : "('dataout')",
	'test_template_factorial' : "('dataout')",
	'test_template_nonfinite' : "()",
	'test_template_ldexp' : "('dataout')",
	'test_template' : "('dataout', 'datay')",
	'test_template_binop' : "('dataout', 'datay')",
	'test_template_binop2' : "('dataout', 'datay')",
	'test_template_comp' : "('datay')",
	'test_template_op' : "('dataout', 'datay')",
	'test_template_op_simd' : "('dataout', 'datay')",
	'test_template_fma' : "('dataout', 'datay', 'dataz')",

}


# ==============================================================================


floatarrays = "'" + "', '".join(codegen_common.floatarrays) + "'"
unsignedint = "'" + "', '".join(codegen_common.unsignedint) + "'"



benchfuncs = [

	{'funcname' : 'aall',
	'test_op_x' : '[10]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = all(datax)',
	'arrayfuncequ' : "result = arrayfunc.aall('>', datax, self.compval, nosimd=True)",
	'arrayfuncequfast' : "result = arrayfunc.aall('>', datax, self.compval, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.aall('>', datax, self.compval)",
	'compval' : 5,
	'arraysreq' : "()",
	},


	{'funcname' : 'aany',
	'test_op_x' : 'itertools.chain(itertools.repeat(0, ARRAYSIZE // 2), itertools.repeat(10, ARRAYSIZE // 2))', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = any(datax)',
	'arrayfuncequ' : "result = arrayfunc.aany('>', datax, self.compval, nosimd=True)",
	'arrayfuncequfast' : "result = arrayfunc.aany('>', datax, self.compval, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.aany('>', datax, self.compval)",
	'compval' : 50,
	'arraysreq' : "()",
	},

	{'funcname' : 'afilter',
	'test_op_x' : '[10]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = array.array(arraycode, filter(lambda x: x < self.compval, datax))',
	'arrayfuncequ' : "result = arrayfunc.afilter('<', datax, datay, self.compval)",
	'arrayfuncequfast' : "result = arrayfunc.afilter('<', datax, datay, self.compval)",
	'arrayfuncequsimd' : "result = arrayfunc.afilter('<', datax, datay, self.compval)",
	'compval' : 5,
	'arraysreq' : "('datay')",
	},

	{'funcname' : 'amax',
	'test_op_x' : 'list(range(128))', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = max(datax)',
	'arrayfuncequ' : "result = arrayfunc.amax(datax, nosimd=True)",
	'arrayfuncequfast' : "result = arrayfunc.amax(datax, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.amax(datax)",
	'compval' : 5,
	'arraysreq' : "()",
	},

	{'funcname' : 'amin',
	'test_op_x' : 'list(range(128))', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = min(datax)',
	'arrayfuncequ' : "result = arrayfunc.amin(datax, nosimd=True)",
	'arrayfuncequfast' : "result = arrayfunc.amin(datax, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.amin(datax)",
	'compval' : 5,
	'arraysreq' : "()",
	},

	{'funcname' : 'asum',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = sum(datax)',
	'arrayfuncequ' : 'result = arrayfunc.asum(datax, nosimd=True)',
	'arrayfuncequfast' : 'result = arrayfunc.asum(datax, matherrors=True, nosimd=True)',
	'arrayfuncequsimd' : 'result = arrayfunc.asum(datax, matherrors=True)',
	'compval' : 0,
	'arraysreq' : "()",
	},


	{'funcname' : 'compress',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'dataout = array.array(arraycode, itertools.compress(datax, self.pycomp))',
	'arrayfuncequ' : 'result = arrayfunc.compress(self.pycomp, dataout, self.compdata)',
	'arrayfuncequfast' : 'result = arrayfunc.compress(self.pycomp, dataout, self.compdata)',
	'arrayfuncequsimd' : 'result = arrayfunc.compress(self.pycomp, dataout, self.compdata)',
	'compval' : 0,
	'arraysreq' : "('dataout')",
	},


	{'funcname' : 'count',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = pycount(arraycode, self.pyitercounts, datax)',
	'arrayfuncequ' : 'arrayfunc.count(datax, self.compval)',
	'arrayfuncequfast' : 'arrayfunc.count(datax, self.compval)',
	'arrayfuncequsimd' : 'arrayfunc.count(datax, self.compval)',
	'compval' : 0,
	'arraysreq' : "()",
	},



	{'funcname' : 'cycle',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = array.array(arraycode, [x for x,y in zip(itertools.cycle([1, 2, 3, 4]), itertools.repeat(0, ARRAYSIZE))])',
	'arrayfuncequ' : 'arrayfunc.cycle(datax, self.startcycle, self.endcycle)',
	'arrayfuncequfast' : 'arrayfunc.cycle(datax, self.startcycle, self.endcycle)',
	'arrayfuncequsimd' : 'arrayfunc.cycle(datax, self.startcycle, self.endcycle)',
	'compval' : 0,
	'arraysreq' : "()",
	},


	{'funcname' : 'dropwhile',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'dataout = array.array(arraycode, itertools.dropwhile(lambda x : x < self.compval, datax))',
	'arrayfuncequ' : "result = arrayfunc.dropwhile('<', datax, dataout, self.compval)",
	'arrayfuncequfast' : "result = arrayfunc.dropwhile('<', datax, dataout, self.compval)",
	'arrayfuncequsimd' : "result = arrayfunc.dropwhile('<', datax, dataout, self.compval)",
	'compval' : 10,
	'arraysreq' : "('dataout')",
	},


	{'funcname' : 'findindex',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = pyfindindex(datax, self.compval)',
	'arrayfuncequ' : "result = arrayfunc.findindex('==', self.datax, self.compval, nosimd=True)",
	'arrayfuncequfast' : "result = arrayfunc.findindex('==', self.datax, self.compval, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.findindex('==', self.datax, self.compval)",
	'compval' : 10,
	'arraysreq' : "()",
	},


	{'funcname' : 'findindices',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = pyfindindices(self.datax, self.fidataout, self.compval)',
	'arrayfuncequ' : "result = arrayfunc.findindices('==', datax, self.fidataout, self.compval)",
	'arrayfuncequfast' : "result = arrayfunc.findindices('==', datax, self.fidataout, self.compval)",
	'arrayfuncequsimd' : "result = arrayfunc.findindices('==', datax, self.fidataout, self.compval)",
	'compval' : 10,
	'arraysreq' : "('fidataout')",
	},


	{'funcname' : 'repeat',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'datax = array.array(arraycode, itertools.repeat(self.compval, ARRAYSIZE))',
	'arrayfuncequ' : "arrayfunc.repeat(datax, self.compval)",
	'arrayfuncequfast' : "arrayfunc.repeat(datax, self.compval)",
	'arrayfuncequsimd' : "arrayfunc.repeat(datax, self.compval)",
	'compval' : 10,
	'arraysreq' : "()",
	},


	{'funcname' : 'takewhile',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'dataout = array.array(arraycode, itertools.takewhile(lambda x : x < self.compval, datax))',
	'arrayfuncequ' : "result = arrayfunc.takewhile('<', datax, dataout, self.compval)",
	'arrayfuncequfast' : "result = arrayfunc.takewhile('<', datax, dataout, self.compval)",
	'arrayfuncequsimd' : "result = arrayfunc.takewhile('<', datax, dataout, self.compval)",
	'compval' : 10,
	'arraysreq' : "('dataout')",
	},

]



# ==============================================================================

# Output data used for benchmarking.
def writeBenchMarkData(cheaderdata):
	# Create a dictionary which allows a reverse look-up of arraycodes to C types.
	arcodelookup = dict([(y,x) for x,y in codegen_common.arraytypes.items()])
	reformatted = []
	for funcname, ardata in cheaderdata:
		# First check to see if SIMD is supported at all for this function.
		if any(ardata.values()):
			reformatted.append((funcname, dict([(arcodelookup[x],y) for x,y in ardata.items()])))

	# Convert to a dictionary in a string.
	reformatstr = str(dict(reformatted))
	# Now, reformat the string so that each function appears on a 
	# separate line. This prevents the data string from being one long line.
	finalformat = reformatstr.replace('},', '},\n')
	
	return finalformat


# ==============================================================================

# Read the operator and function definition data.
opdata = codegen_common.ReadCSVData('funcs.csv')


# Get a list of the C function names and their array types from the SIMD
# related C header source files.
cheaderdata = codegen_common.GetHeaderFileDataSIMD()

# Reformat the SIMD data into a string containing the dictionary.
SIMD_data = writeBenchMarkData(cheaderdata)


# Get the names of functions which use 'matherrors'.
# First, search the templates for functions which are not in the spreadsheet.
Opt_data = [x['funcname'] for x in benchfuncs if 'matherrors' in x['arrayfuncequfast']]

# Now find which spreadsheet based templates use 'matherrors'.
melist = [x for x,y in arrayfuncequfast.items() if 'matherrors' in y]
# And which function names this translate to.
melist2 = [x['funcname'] for x in opdata if x['test_op_templ'] in  melist]

# Now combine the two lists so we have a single list to refer to.
Opt_data.extend(melist2)

# ==============================================================================

# The names of all the benchmark classes.
benchclasses = []

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('benchmarks', '20-Dec-2018', '')

headerdate['SIMD_data'] = SIMD_data
headerdate['Opt_data'] = Opt_data


with open('benchmarks.py', 'w') as f:

	# This creates the file header at the top of the file.
	f.write(headertemplate % headerdate)

	for op in benchfuncs:

		# These are common to all related functions.
		op['floatarrays'] = floatarrays
		op['unsignedint'] = unsignedint
		op['supportedarrays'] = codegen_common.arraycodes
		op['needsydatafix'] = False
		op['singledatafunc'] = False


		# Now put it together into a single class.
		f.write(benchmarkclass_template % op)

		# Add the name of the class to the list.
		benchclasses.append("(benchmark_%s, '%s')" % (op['funcname'], op['funcname']))
		


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



		opvalues = {'funcname' : op['funcname'],
		'test_op_x' : '[' + op['test_op_x'] + ']', 
		'test_op_y' : '[' + op['test_op_y'] + ']',
		'test_op_z' : '[' + op['test_op_z'] + ']',
		'supportedarrays' : supportedarrays,
		'needsydatafix' : op['test_op_templ'] in ('test_template_op', 'test_template_op_simd'),
		'floatarrays' : floatarrays,
		'unsignedint' : unsignedint,
		'pyequ' : pyequ[op['test_op_templ']] % {'pyop' : op['pyoperator']},
		'arrayfuncequ' : arrayfuncequ[op['test_op_templ']] % op['funcname'],
		'arrayfuncequfast' : arrayfuncequfast[op['test_op_templ']] % op['funcname'],
		'arrayfuncequsimd' : arrayfuncequsimd[op['test_op_templ']] % op['funcname'],
		'singledatafunc' : True,
		'compval' : 0,
		'arraysreq' : arraysreq[op['test_op_templ']]
		}


		# True division needs a special equation to avoid type errors. In
		# python, truediv aways produces a floating point result, which
		# causes errors when saving into an integer array. To solve this,
		# we call a type conversion function which select at run time.
		if opvalues['funcname'] == 'truediv':
			opvalues['pyequ'] = 'dataout[i] = truediv_type(datax[i] / datay[i])'


		# Now put it together into a single class.
		f.write(benchmarkclass_template % opvalues)

		# Add the name of the class to the list.
		benchclasses.append("(benchmark_%s, '%s')" % (op['funcname'], op['funcname']))



	# The list of benchmark class names.
	f.write(benchclasslisttemplate % (', '.join(benchclasses), codegen_common.arraycodes))


	# This writes the code to execute all the tests.
	f.write(benchruntemplate)

