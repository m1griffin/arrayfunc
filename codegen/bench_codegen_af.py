#!/usr/bin/python3

##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the code for benchmark tests for 'arrayfunc' functions.
# Language: Python 3.5
# Date:     17-Sep-2018
#
###############################################################################
#
#   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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

import datetime

import codegen_common


# ==============================================================================


# This goes at the top of the generated file.
headertemplate = '''#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   %(testfilename)s
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


##############################################################################

import time
import array
import itertools
import math
import platform
import json
import collections
import argparse

import arrayfunc


##############################################################################


%(auxiliaryfuncs)s


########################################################
def InitOptionData(arraycode, arraysize, funcname):
	"""Initialise the data used only for some tests.
	"""

	odata = collections.namedtuple('optiondata', ['truediv_type', 'ldexp_y', 
			'compval', 'pycomp', 'startcycle', 'endcycle', 
			'invertmaxval', 'invertop', 'fidataout'])

	optiondata = odata

	# Ensure the data is in the right format for the array type.
	if arraycode in (%(floatarrays)s):
		optiondata.truediv_type = float
	else:
		optiondata.truediv_type = int

	# Function ldexp needs a specific array type as the second parameter.
	if funcname == 'ldexp':
		ydata = %(test_op_y)s
		optiondata.ldexp_y = int(ydata[-1])
	else:
		optiondata.ldexp_y = None

	# This is used for some tests.
	if arraycode in (%(floatarrays)s):
		optiondata.compval =  float(%(compval)s)
	else:
		optiondata.compval =  int(%(compval)s)

	
	# Used for compress.
	if '%(funcname)s' == 'compress':
		optiondata.compdata = array.array(arraycode, [1,0,1,0])
		optiondata.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(optiondata.compdata), itertools.repeat(0, arraysize))))
	else:
		optiondata.compdata = None
		optiondata.pycomp = None

	# Used for cycle.
	if '%(funcname)s' == 'cycle':
		optiondata.startcycle = comptype(arraycode, 0)
		optiondata.endcycle = comptype(arraycode, 127)
	else:
		optiondata.startcycle = None
		optiondata.endcycle = None

	# Used for invert.
	if '%(funcname)s' == 'invert':
		optiondata.invertmaxval = allinvertlimits[arraycode]
		if arraycode in ('b', 'h', 'i', 'l', 'q'):
			optiondata.invertop = invertpysigned
		else:
			optiondata.invertop = invertpyunsigned
	else:
		optiondata.invertmaxval = None
		optiondata.invertop = None


	# Used for findindices.
	if 'fidataout' in %(arraysreq)s:
		optiondata.fidataout = array.array('q', itertools.repeat(0, arraysize))
	else:
		optiondata.fidataout = None


	return optiondata


########################################################
def InitDataArrays(arraycode, arraysize):
	"""Initialise the data arrays used to run the tests.
	"""
	adata = collections.namedtuple('arraydata', ['datax', 'dataout', 
										'yvalue', 'zvalue', 'arraylength'])

	arraydata = adata


	# Ensure the data is in the right format for the array type.
	if arraycode in (%(floatarrays)s):
		xdata = [float(x) for x in %(test_op_x)s]
	else:
		xdata = [int(x) for x in %(test_op_x)s]

	arraydata.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, arraysize))))
	assert len(arraydata.datax) == arraysize, 'datax is not expected length %%d' %% len(arraydata.datax)

	arraydata.arraylength = len(arraydata.datax)

	# Y data.
	ydata = %(test_op_y)s
	if len(ydata) > 0:
		yvalue = abs(ydata[-1])
		if arraycode in (%(floatarrays)s):
			arraydata.yvalue = float(yvalue)
		else:
			arraydata.yvalue = int(yvalue)
	else:
		arraydata.yvalue = None

	# Z data.
	zdata = %(test_op_z)s
	if len(zdata) > 0:
		zvalue = abs(zdata[-1])
		if arraycode in (%(floatarrays)s):
			arraydata.zvalue = float(zvalue)
		else:
			arraydata.zvalue = int(zvalue)
	else:
		arraydata.zvalue = None


	# Output array.
	if 'dataout' in %(arraysreq)s:
		arraydata.dataout = array.array(arraycode, itertools.repeat(0, arraydata.arraylength))
		assert len(arraydata.dataout) == arraysize, 'dataout is not expected length %%d' %% len(arraydata.dataout)
	else:
		arraydata.dataout = None


	return arraydata


########################################################
def calibrateruntime(arraycode, arraysize, arraydata, optiondata, runtimetarget):
	"""Calibrate the run time for Python and default ArrayFunc.
	"""
	pyitercounts = 1
	afitercounts = 50

	# First, do a timing calibration run.
	# Python native time.
	pytime = BenchmarkPython(pyitercounts, arraycode, arraysize, arraydata, optiondata)

	# Arrayfunc time.
	aftime = BenchmarkAF(afitercounts, arraycode, arraydata, optiondata)


	# Now calculate the average execution time and adjust the iterations
	# so that the tests will take approximately 0.1 seconds.
	# The time returned by the benchmark function is per iteration, so 
	# we don't need to adjust for this again.
	pyitercounts = int(runtimetarget / pytime)
	afitercounts = int(runtimetarget / aftime)

	# Make sure the iteration count is at least 1.
	if pyitercounts < 1:
		pyitercounts = 1
	if afitercounts < 1:
		afitercounts = 1


	return pyitercounts, afitercounts



########################################################
def calibratenosimdruntime(arraycode, arraydata, optiondata, runtimetarget):
	"""Calibrate the run time with SIMD disabled.
	"""
	afiternosidmcounts = 50

	# Arrayfunc time without SIMD for functions with SIMD.
	aftimenosimd = BenchmarkAFNoSIMD(afiternosidmcounts, arraycode, arraydata, optiondata)
	afiternosidmcounts = int(runtimetarget / aftimenosimd)
	if afiternosidmcounts < 1:
		afiternosidmcounts = 1

	return afiternosidmcounts


########################################################
def BenchmarkPython(pyitercounts, arraycode, arraysize, arraydata, optiondata):
	"""Measure execution time of native Python code.
	"""
	# This is used for some tests only. 
	result = True

	# We provide a local reference to the arrays to make the representation simpler.
	datax = arraydata.datax
	dataout = arraydata.dataout
	yvalue = arraydata.yvalue
	zvalue = arraydata.zvalue
	arraylength = arraydata.arraylength
	# Used for ldexp only.
	ldexp_y = optiondata.ldexp_y
	compval = optiondata.compval
	truediv_type = optiondata.truediv_type
	fidataout = optiondata.fidataout
	startcycle = optiondata.startcycle
	endcycle = optiondata.endcycle
	pycomp = optiondata.pycomp
	compdata = optiondata.compdata
	invertmaxval = optiondata.invertmaxval
	invertop = optiondata.invertop


	# Time for python.
	starttime = time.perf_counter()

	if %(singledatafunc)s:
		for x in range(pyitercounts):
			for i in range(arraylength):
				%(pyequ)s
	else:
		for x in range(pyitercounts):
			%(pyequ)s

	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	return pythontime



########################################################
def BenchmarkAF(afitercounts, arraycode, arraydata, optiondata):
	"""Measure execution time for arrayfunc.
	"""
	# This is used for some tests only. 
	result = True

	# We provide a local reference to the arrays to make the representation simpler.
	datax = arraydata.datax
	dataout = arraydata.dataout
	yvalue = arraydata.yvalue
	zvalue = arraydata.zvalue
	# Used for ldexp only.
	ldexp_y = optiondata.ldexp_y
	compval = optiondata.compval
	fidataout = optiondata.fidataout
	startcycle = optiondata.startcycle
	endcycle = optiondata.endcycle
	pycomp = optiondata.pycomp
	compdata = optiondata.compdata


	# Time for arrayfunc version.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		%(arrayfuncequ)s
	endtime = time.perf_counter()

	aftime = (endtime - starttime) / afitercounts

	return aftime


########################################################
def BenchmarkAFNoSIMD(afiternosidmcounts, arraycode, arraydata, optiondata):
	"""Measure execution time for arrayfunc with SIMD turned off calls.
	"""
	# This is used for some tests only. 
	result = True

	# We provide a local reference to the arrays to make the representation simpler.
	datax = arraydata.datax
	dataout = arraydata.dataout
	yvalue = arraydata.yvalue
	zvalue = arraydata.zvalue
	# Used for ldexp only.
	ldexp_y = optiondata.ldexp_y
	compval = optiondata.compval
	fidataout = optiondata.fidataout
	startcycle = optiondata.startcycle
	endcycle = optiondata.endcycle
	pycomp = optiondata.pycomp
	compdata = optiondata.compdata


	# Time for arrayfunc version.
	starttime = time.perf_counter()
	for i in range(afiternosidmcounts):
		%(arrayfuncequfast)s
	endtime = time.perf_counter()

	aftime = (endtime - starttime) / afiternosidmcounts

	return aftime



########################################################
def BenchmarkAFSIMD(afitercounts, arraycode, arraydata, optiondata):
	"""Measure execution time for arrayfunc with SIMD.
	"""
	# This is used for some tests only. 
	result = True

	# We provide a local reference to the arrays to make the representation simpler.
	datax = arraydata.datax
	dataout = arraydata.dataout
	yvalue = arraydata.yvalue
	zvalue = arraydata.zvalue
	# Used for ldexp only.
	ldexp_y = optiondata.ldexp_y
	compval = optiondata.compval
	fidataout = optiondata.fidataout
	startcycle = optiondata.startcycle
	endcycle = optiondata.endcycle
	pycomp = optiondata.pycomp
	compdata = optiondata.compdata


	# Time for arrayfunc version.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		%(arrayfuncequsimd)s
	endtime = time.perf_counter()

	aftime = (endtime - starttime) / afitercounts

	return aftime



##############################################################################

def GetCmdArguments():
	""" Get any command line arguments. These modify the operation of the program.
			rawoutput = If specified, will output raw data instead of a report.
			arraysize = Size of the array in elements.
			runtimetarget = The target length of time in seconds to run a benchmark for.
	"""
	arraysize = 100000
	runtimetarget = 0.1

	# Get any command line arguments.
	parser = argparse.ArgumentParser()

	# Output just the raw data.
	parser.add_argument('--rawoutput', action = 'store_true', help = 'Output raw data.')

	# Size of the test arrays.
	parser.add_argument('--arraysize', type = int, default = arraysize, 
		help='Size of test arrays in number of elements.')

	# The length of time to run each benchmark.
	parser.add_argument('--runtimetarget', type = float, default = runtimetarget, 
		help='Target length of time to run each benchmark for.')

	args = parser.parse_args()

	return args


##############################################################################


CmdArgs = GetCmdArguments()

ArraySize = CmdArgs.arraysize
RunTimeTarget = CmdArgs.runtimetarget


##############################################################################

# Run the benchmarks.
funcname = '%(funcname)s'
supportedarrays = %(supportedarrays)s


# True if function uses SIMD.
HasSIMD = arrayfunc.simdsupport.hassimd


# Detect the hardware platform, and assign the correct platform data table to it.
def platformdetect():
	""" Return a string containing the array codes if the machine supports 
	SIMD for this function. The results will vary depending upon which platform 
	it is running on.
	"""
	# These are the supported options for SIMD. The values depend on
	# the particular function in question.
	# i686 = 32 bit x86, this never has SIMD.
	# x86_64 = 64 bit x86, supported on Linux with GCC only.
	# armv7l = 32 bit ARM, for Raspberry Pi 3 with 32 bit Linux.
	# aarch64 = 64 bit ARM, for Raspberry Pi 3 or 4 with 64 bit Linux.
	# These values were derived from the platform data reported by the benchmark.
	signatures = {
		'i686' : '',
		'x86_64' : '%(simdarrays_x86)s',
		'armv7l' : '%(simdarrays_arm32)s',
		'aarch64' : '%(simdarrays_arm64)s',
	}

	return signatures.get(platform.machine(), '')


if HasSIMD:
	SIMDArrays = platformdetect()
else:
	SIMDArrays = ''


# Used to collect the results.
PyData = {}
AfData = {}
AfDataNoSIMD = {}
AfDataSIMD = {}

# Test using each array type.
for arraycode in supportedarrays:
	# Initialise the data arrays.
	ArrayData = InitDataArrays(arraycode, ArraySize)

	# Initialise the optional data elements that are only used for some tests.
	OptionData = InitOptionData(arraycode, ArraySize, funcname)

	# Calibrate the test runtime targets.
	pyitercounts, afitercounts = calibrateruntime(arraycode, ArraySize, ArrayData, OptionData, RunTimeTarget)
	if arraycode in SIMDArrays:
		afiternosidmcounts = calibratenosimdruntime(arraycode, ArrayData, OptionData, RunTimeTarget)

	# Benchmark the Python implementation.
	PyData[arraycode] = BenchmarkPython(pyitercounts, arraycode, ArraySize, ArrayData, OptionData)


	# Benchmark the Arrayfunc implementation.
	AfData[arraycode] = BenchmarkAF(afitercounts, arraycode, ArrayData, OptionData)


	# If the function supports SIMD operations, repeat the test
	# with SIMD turned off and on. Some function calls only support
	# SIMD if error checking is turned off, so we must do this again
	# to be sure we have data both ways.
	if arraycode in SIMDArrays:
		AfDataNoSIMD[arraycode] = BenchmarkAFNoSIMD(afiternosidmcounts, arraycode, ArrayData, OptionData)
		AfDataSIMD[arraycode] = BenchmarkAFSIMD(afiternosidmcounts, arraycode, ArrayData, OptionData)


##############################################################################

##############################################################################

# Report the benchmarks.

# The format string used to print out results in stand alone mode.
def sformatter(pos, val):
	if val is None:
		return 17 * ' '
	elif (val is not None) and (val < 10.0):
		return '{%%d:>8.1f}         ' %% (pos + 1)
	else:
		return '{%%d:>8.0f}         ' %% (pos + 1)


def printline(label1, col2, col3, col4, col5):
	lineresult = [col2, col3, col4, col5]
	standformat = '{0:^7}' + ''.join([sformatter(x,y) for x,y in enumerate(lineresult)])
	print(standformat.format(label1, col2, col3, col4, col5))


theader = """
Function = {0}
======= ================ ================ ================ ================
 Array    AF vs Python     AF with SIMD      AF no SIMD     SIMD / no SIMD
======= ================ ================ ================ ================""".format(funcname)

tfooter = '======= ================ ================ ================ ================'


def calcstats(statscolumn):
	"""Calculate the states for a column of data.
	Return the average, max, and min.
	If the data column is empty, return None for each value.
	"""
	if len(statscolumn) > 0:
		return sum(statscolumn) / len(statscolumn), max(statscolumn), min(statscolumn)
	else:
		return None, None, None
	


########################################################
def outputstandalone():
	"""Output the results for when the benchmark is run in standalone mode.
	"""
	totalpyrel = []
	totalsimdrel = []
	totalnosimdrel = []
	totalsimdvsnosimd = []

	print(theader)
	for x in supportedarrays:
		pyafrel = PyData[x] / AfData[x]
		totalpyrel.append(pyafrel)
		if x in SIMDArrays:
			# Python versus default ArrayFunc.
			pysimdrel = PyData[x] / AfDataSIMD[x]
			totalsimdrel.append(pysimdrel)

			# Python versus Arrayfunc with SIMD disabled.
			pynosimdrel = PyData[x] / AfDataNoSIMD[x]
			totalnosimdrel.append(pynosimdrel)

			# Default versus no SIMD.
			simdnosimdrel = AfDataNoSIMD[x] / AfDataSIMD[x]
			totalsimdvsnosimd.append(simdnosimdrel)

		else:
			pysimdrel = None
			pynosimdrel = None
			simdnosimdrel = None

		printline(x, pyafrel, pysimdrel, pynosimdrel, simdnosimdrel)
		

	print(tfooter)


	print('\\n')
	print(tfooter)

	# Calculate states.
	# Native Python versus default ArrayFunc.
	col2avg, col2max, col2min = calcstats(totalpyrel)

	# Native Python versus ArrayFunc with SIMD.
	col3avg, col3max, col3min = calcstats(totalsimdrel)

	# Native Python versus ArrayFunc with SIMD disabled.
	col4avg, col4max, col4min = calcstats(totalnosimdrel)

	# SIMD versus no SIMD.
	col5avg, col5max, col5min = calcstats(totalsimdvsnosimd)

	printline('avg', col2avg, col3avg, col4avg, col5avg)
	printline('max', col2max, col3max, col4max, col5max)
	printline('min', col2min, col3min, col4min, col5min)


	print(tfooter)


########################################################



# If raw data is requested, output the raw numbers as JSON.
# This will normally be used by a parent process which called this
# benchmark as a child process.
if CmdArgs.rawoutput:
	# Called by another process, return data as json.
	testresults = {'pydata' : PyData,
					'afdata' : AfData,
					'afdatanosimd' : AfDataNoSIMD,
					'afdatasimd' : AfDataSIMD,
					'benchname' : 'arrayfunc',
					}

	print(json.dumps(testresults))

else:
	# If standalone, print out data in readable format.
	outputstandalone()


##############################################################################
'''

# ==============================================================================
# Additional functions used for specific tests. These are included as required.

# Used for cycle only.
comptype = '''
########################################################
def comptype(arraycode, cval):
	"""Return the compare value in the correct type.
	"""
	if arraycode in ('f', 'd'):
		return float(cval)
	else:
		return int(cval)

'''


pyfindindices = '''
########################################################
def pyfindindices(datax, dataout, compval):
	"""Used to emulate the findindices arrayfunc function.
	"""
	z = 0
	for x in datax:
		if x == compval:
			dataout[z] = z
			z += 1
	return z

'''

pyfindindex = '''
########################################################
def pyfindindex(datax, compval):
	"""Used to emulate the findindex arrayfunc function.
	"""
	try:
		return datax.index(compval)
	except ValueError:
		return -1

'''

pycount = '''
########################################################
def pycount(arraycode, pyitercounts, data, arraysize):
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
		for x, y in zip(itertools.count(0), itertools.repeat(0, arraysize)):
			data[x] = x & mask
	else:
		for x, y in zip(itertools.count(0), itertools.repeat(0, arraysize)):
			data[x] = x

'''

pyinvert = '''
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
def invertpysigned(val, maxval):
	"""This is used to benchmark invert Python native operations on 
	signed integers.
	"""
	return ~val


##############################################################################
def invertpyunsigned(val, maxval):
	"""This is used to benchmark invert Python native operations on 
	unsigned integers.
	"""
	if val >= 0:
		return maxval - val
	else:
		return maxval + val

'''

# Used to select which auxiliary functions to insert into the main template.
auxiliaryfuncs = {
	'count' : pycount,
	'findindex' : pyfindindex,
	'findindices' : pyfindindices,
	'cycle' : comptype,
	'invert' : pyinvert,
}


# ==============================================================================


# This defines the python code form of the benchmark equations.
pyequ = {'test_template_noparams' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_noparams_1simd' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_invert' : 'dataout[i] = invertop(datax[i], invertmaxval)',
	'test_template_uniop' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_factorial' : 'dataout[i] = %(pyop)s(datax[i])',
	'test_template_nonfinite' : 'result = %(pyop)s(datax[i])',
	'test_template_ldexp' : 'dataout[i] = %(pyop)s(datax[i], ldexp_y)',
	'test_template' : 'dataout[i] = %(pyop)s(datax[i], yvalue)',
	'test_template_binop' : 'dataout[i] = datax[i] %(pyop)s yvalue',
	'test_template_binop2' : 'dataout[i] = datax[i] %(pyop)s yvalue',
	'test_template_comp' : 'result = datax[i] %(pyop)s yvalue',
	'test_template_op' : 'dataout[i] = datax[i] %(pyop)s yvalue',
	'test_template_op_simd' : 'dataout[i] = datax[i] %(pyop)s yvalue',
	'test_template_fma' : 'dataout[i] = datax[i] * yvalue + zvalue',
}


# This defines the arrayfunc code form of the benchmark equations.
arrayfuncequ = {'test_template_noparams' : 'arrayfunc.%s(datax, dataout)',
	'test_template_noparams_1simd' : 'arrayfunc.%s(datax, dataout)',
	'test_template_noparams' : 'arrayfunc.%s(datax, dataout)',
	'test_template_invert' : 'arrayfunc.%s(datax, dataout)',
	'test_template_uniop' : 'arrayfunc.%s(datax, dataout)',
	'test_template_factorial' : 'arrayfunc.%s(datax, dataout)',
	'test_template_nonfinite' : 'result = arrayfunc.%s(datax)',
	'test_template_ldexp' : 'arrayfunc.%s(datax, ldexp_y, dataout)',
	'test_template' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_binop' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_binop2' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_comp' : 'result = arrayfunc.%s(datax, yvalue)',
	'test_template_op' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_op_simd' : 'arrayfunc.%s(datax, yvalue, dataout)',
	'test_template_fma' : 'arrayfunc.%s(datax, yvalue, zvalue, dataout)',
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
	'test_template_binop' : 'arrayfunc.%s(datax, yvalue, dataout, nosimd=True)',
	'test_template_binop2' : 'arrayfunc.%s(datax, yvalue, dataout, nosimd=True)',
	'test_template_comp' : 'result = arrayfunc.%s(datax, yvalue, nosimd=True)',
	'test_template_op' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True)',
	'test_template_op_simd' : 'arrayfunc.%s(datax, yvalue, dataout, matherrors=True, nosimd=True)',
	'test_template_fma' : 'arrayfunc.%s(datax, yvalue, zvalue, dataout, matherrors=True)',
	
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
	'test_template_fma' : 'arrayfunc.%s(datax, yvalue, zvalue, dataout, matherrors=True)',
	
}

# This defines how may arrays are used. This will allow avoiding initialising
# arrays which are not needed, to save time. Some other functions require a 
# special output array, which is why we can't simply make this a boolean value.
arraysreq = {'test_template_noparams' : "('dataout')",
	'test_template_noparams_1simd' : "('dataout')",
	'test_template_invert' : "('dataout')",
	'test_template_uniop' : "('dataout')",
	'test_template_factorial' : "('dataout')",
	'test_template_nonfinite' : "()",
	'test_template_ldexp' : "('dataout')",
	'test_template' : "('dataout')",
	'test_template_binop' : "('dataout')",
	'test_template_binop2' : "('dataout')",
	'test_template_comp' : "()",
	'test_template_op' : "('dataout')",
	'test_template_op_simd' : "('dataout')",
	'test_template_fma' : "('dataout')",

}

# ==============================================================================


floatarrays = "'" + "', '".join(codegen_common.floatarrays) + "'"
unsignedint = "'" + "', '".join(codegen_common.unsignedint) + "'"


# Function definitions for the non-mathematical functions.
benchfuncs = [

	{'funcname' : 'aall',
	'test_op_x' : '[10]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = all(datax)',
	'arrayfuncequ' : "result = arrayfunc.aall('>', datax, compval)",
	'arrayfuncequfast' : "result = arrayfunc.aall('>', datax, compval, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.aall('>', datax, compval)",
	'compval' : 5,
	'arraysreq' : "()",
	},


	{'funcname' : 'aany',
	'test_op_x' : 'itertools.chain(itertools.repeat(0, arraysize // 2), itertools.repeat(10, arraysize // 2))', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = any(datax)',
	'arrayfuncequ' : "result = arrayfunc.aany('>', datax, compval)",
	'arrayfuncequfast' : "result = arrayfunc.aany('>', datax, compval, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.aany('>', datax, compval)",
	'compval' : 50,
	'arraysreq' : "()",
	},

	{'funcname' : 'afilter',
	'test_op_x' : '[10]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = array.array(arraycode, filter(lambda x: x < compval, datax))',
	'arrayfuncequ' : "result = arrayfunc.afilter('<', datax, dataout, compval)",
	'arrayfuncequfast' : "result = arrayfunc.afilter('<', datax, dataout, compval)",
	'arrayfuncequsimd' : "result = arrayfunc.afilter('<', datax, dataout, compval)",
	'compval' : 5,
	'arraysreq' : "('dataout')",
	},

	{'funcname' : 'amax',
	'test_op_x' : 'list(range(128))', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = max(datax)',
	'arrayfuncequ' : "result = arrayfunc.amax(datax)",
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
	'arrayfuncequ' : "result = arrayfunc.amin(datax)",
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
	'arrayfuncequ' : 'result = arrayfunc.asum(datax)',
	'arrayfuncequfast' : 'result = arrayfunc.asum(datax, matherrors=True, nosimd=True)',
	'arrayfuncequsimd' : 'result = arrayfunc.asum(datax, matherrors=True)',
	'compval' : 0,
	'arraysreq' : "()",
	},


	{'funcname' : 'compress',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'dataout = array.array(arraycode, itertools.compress(datax, pycomp))',
	'arrayfuncequ' : 'result = arrayfunc.compress(pycomp, dataout, compdata)',
	'arrayfuncequfast' : 'result = arrayfunc.compress(pycomp, dataout, compdata)',
	'arrayfuncequsimd' : 'result = arrayfunc.compress(pycomp, dataout, compdata)',
	'compval' : 0,
	'arraysreq' : "('dataout')",
	},


	{'funcname' : 'count',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = pycount(arraycode, pyitercounts, datax, arraysize)',
	'arrayfuncequ' : 'arrayfunc.count(datax, compval)',
	'arrayfuncequfast' : 'arrayfunc.count(datax, compval)',
	'arrayfuncequsimd' : 'arrayfunc.count(datax, compval)',
	'compval' : 0,
	'arraysreq' : "()",
	},



	{'funcname' : 'cycle',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = array.array(arraycode, [x for x,y in zip(itertools.cycle([1, 2, 3, 4]), itertools.repeat(0, arraysize))])',
	'arrayfuncequ' : 'arrayfunc.cycle(datax, startcycle, endcycle)',
	'arrayfuncequfast' : 'arrayfunc.cycle(datax, startcycle, endcycle)',
	'arrayfuncequsimd' : 'arrayfunc.cycle(datax, startcycle, endcycle)',
	'compval' : 0,
	'arraysreq' : "()",
	},


	{'funcname' : 'dropwhile',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'dataout = array.array(arraycode, itertools.dropwhile(lambda x : x < compval, datax))',
	'arrayfuncequ' : "result = arrayfunc.dropwhile('<', datax, dataout, compval)",
	'arrayfuncequfast' : "result = arrayfunc.dropwhile('<', datax, dataout, compval)",
	'arrayfuncequsimd' : "result = arrayfunc.dropwhile('<', datax, dataout, compval)",
	'compval' : 10,
	'arraysreq' : "('dataout')",
	},


	{'funcname' : 'findindex',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = pyfindindex(datax, compval)',
	'arrayfuncequ' : "result = arrayfunc.findindex('==', datax, compval)",
	'arrayfuncequfast' : "result = arrayfunc.findindex('==', datax, compval, nosimd=True)",
	'arrayfuncequsimd' : "result = arrayfunc.findindex('==', datax, compval)",
	'compval' : 10,
	'arraysreq' : "()",
	},


	{'funcname' : 'findindices',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'result = pyfindindices(datax, fidataout, compval)',
	'arrayfuncequ' : "result = arrayfunc.findindices('==', datax, fidataout, compval)",
	'arrayfuncequfast' : "result = arrayfunc.findindices('==', datax, fidataout, compval)",
	'arrayfuncequsimd' : "result = arrayfunc.findindices('==', datax, fidataout, compval)",
	'compval' : 10,
	'arraysreq' : "('fidataout')",
	},


	{'funcname' : 'repeat',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'datax = array.array(arraycode, itertools.repeat(compval, arraysize))',
	'arrayfuncequ' : "arrayfunc.repeat(datax, compval)",
	'arrayfuncequfast' : "arrayfunc.repeat(datax, compval)",
	'arrayfuncequsimd' : "arrayfunc.repeat(datax, compval)",
	'compval' : 10,
	'arraysreq' : "()",
	},


	{'funcname' : 'takewhile',
	'test_op_x' : '[0]', 
	'test_op_y' : '[0]',
	'test_op_z' : '[0]',
	'pyequ' : 'dataout = array.array(arraycode, itertools.takewhile(lambda x : x < compval, datax))',
	'arrayfuncequ' : "result = arrayfunc.takewhile('<', datax, dataout, compval)",
	'arrayfuncequfast' : "result = arrayfunc.takewhile('<', datax, dataout, compval)",
	'arrayfuncequsimd' : "result = arrayfunc.takewhile('<', datax, dataout, compval)",
	'compval' : 10,
	'arraysreq' : "('dataout')",
	},

]

# ==============================================================================

# Convert the SIMD array data to a dictionary of array code strings.
def ReformatSIMDData(cheaderdata):
	# Create a dictionary which allows a reverse look-up of arraycodes to C types.
	arcodelookup = dict([(y,x) for x,y in codegen_common.arraytypes.items()])
	reformatted = []
	for funcname, ardata in cheaderdata:
		# First check to see if SIMD is supported at all for this function.
		if any(ardata.values()):
			reformatted.append((funcname, ''.join([arcodelookup[x] for x,y in ardata.items() if y])))

	return dict(reformatted)
	

# Get a list of the C function names and their array types from the SIMD
# related C header source files.
# For x86-64
cheaderdata_x86 = codegen_common.GetHeaderFileDataSIMD('../src/*_simd_x86.h')

# For ARMv7.
cheaderdata_armv7 = codegen_common.GetHeaderFileDataSIMD('../src/*_simd_armv7.h')

# For ARMv8.
cheaderdata_armv8 = codegen_common.GetHeaderFileDataSIMD('../src/*_simd_armv8.h')


# Reformat the SIMD data into a string containing the dictionary.
SIMD_data_x86 = ReformatSIMDData(cheaderdata_x86)
SIMD_data_armv7 = ReformatSIMDData(cheaderdata_armv7)
SIMD_data_armv8 = ReformatSIMDData(cheaderdata_armv8)



# ==============================================================================


# Timestamp to be used on all files created.
testdate = datetime.date.today()
testdatestamp = testdate.strftime('%d-%b-%Y')


# This part only handles functions defined within this file.
for benchdata in benchfuncs:

	funcname = benchdata['funcname']
	filename = 'benchmark_%s.py' % funcname

	with open(filename, 'w') as f:
		# Data for the copyright header files.

		op = {
		'testfilename' : filename,
		'startdate' : '20-Dec-2018',
		'verdate' : testdatestamp,
		'cpyear' : testdate.year,
		'floatarrays' : floatarrays,

		'singledatafunc' : False,

		'supportedarrays' : codegen_common.arraycodes,

		'simdarrays_arm32' : SIMD_data_armv7.get(funcname, ''),
		'simdarrays_arm64' : SIMD_data_armv8.get(funcname, ''),
		'simdarrays_x86' : SIMD_data_x86.get(funcname, ''),

		'funcname' : benchdata['funcname'],
		'test_op_x' : benchdata['test_op_x'],
		'test_op_y' : benchdata['test_op_y'],
		'test_op_z' : benchdata['test_op_z'],
		'pyequ' : benchdata['pyequ'],
		'arrayfuncequ' : benchdata['arrayfuncequ'],
		'arrayfuncequfast' : benchdata['arrayfuncequfast'],
		'arrayfuncequsimd' : benchdata['arrayfuncequsimd'],
		'compval' : benchdata['compval'],
		'arraysreq' : benchdata['arraysreq'],

		'auxiliaryfuncs' : auxiliaryfuncs.get(funcname, ''),
		}


		f.write(headertemplate % op)

# ==============================================================================


# Read the operator and function definition data.
csvdata = codegen_common.ReadCSVData('funcs.csv')

# This part handles functions defined by the spreadsheet templates.
for funcsdata in csvdata:

	funcname = funcsdata['funcname']
	filename = 'benchmark_%s.py' % funcname

	print(funcname)

	with open(filename, 'w') as f:

		# Array types to test.
		arraytypes = set(funcsdata['arraytypes'].split(','))
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
			print('Error - supported array types not recognised', funcsdata['arraytypes'])

		opvalues = {

		'testfilename' : filename,
		'startdate' : '20-Dec-2018',
		'verdate' : testdatestamp,
		'cpyear' : testdate.year,
		'floatarrays' : floatarrays,


		'funcname' : funcsdata['funcname'],
		'test_op_x' : '[' + funcsdata['test_op_x'] + ']', 
		'test_op_y' : '[' + funcsdata['test_op_y'] + ']',
		'test_op_z' : '[' + funcsdata['test_op_z'] + ']',
		'supportedarrays' : supportedarrays,
		'needsydatafix' : funcsdata['test_op_templ'] in ('test_template_op', 'test_template_op_simd'),
		'floatarrays' : floatarrays,
		'unsignedint' : unsignedint,
		'pyequ' : pyequ[funcsdata['test_op_templ']] % {'pyop' : funcsdata['pyoperator']},
		'arrayfuncequ' : arrayfuncequ[funcsdata['test_op_templ']] % funcsdata['funcname'],
		'arrayfuncequfast' : arrayfuncequfast[funcsdata['test_op_templ']] % funcsdata['funcname'],
		'arrayfuncequsimd' : arrayfuncequsimd[funcsdata['test_op_templ']] % funcsdata['funcname'],
		'singledatafunc' : True,
		'compval' : 0,
		'arraysreq' : arraysreq[funcsdata['test_op_templ']],

		'auxiliaryfuncs' : auxiliaryfuncs.get(funcname, ''),

		'simdarrays_arm32' : SIMD_data_armv7.get(funcname, ''),
		'simdarrays_arm64' : SIMD_data_armv8.get(funcname, ''),
		'simdarrays_x86' : SIMD_data_x86.get(funcname, ''),
		}

		# True division needs a special equation to avoid type errors. In
		# python, truediv aways produces a floating point result, which
		# causes errors when saving into an integer array. To solve this,
		# we call a type conversion function which select at run time.
		if opvalues['funcname'] == 'truediv':
			opvalues['pyequ'] = 'dataout[i] = truediv_type(datax[i] / yvalue)'


		f.write(headertemplate % opvalues)
	

# ==============================================================================
