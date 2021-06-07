#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   benchmark_fabs.py
# Purpose:  Benchmark tests for 'arrayfunc' functions.
# Language: Python 3.5
# Date:     20-Dec-2018.
# Ver:      31-May-2021.
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





########################################################
def InitOptionData(arraycode, arraysize, funcname):
	"""Initialise the data used only for some tests.
	"""

	odata = collections.namedtuple('optiondata', ['truediv_type', 'ldexp_y', 
			'compval', 'pycomp', 'startcycle', 'endcycle', 
			'invertmaxval', 'invertop', 'fidataout'])

	optiondata = odata

	# Ensure the data is in the right format for the array type.
	if arraycode in ('f', 'd'):
		optiondata.truediv_type = float
	else:
		optiondata.truediv_type = int

	# Function ldexp needs a specific array type as the second parameter.
	if funcname == 'ldexp':
		ydata = []
		optiondata.ldexp_y = int(ydata[-1])
	else:
		optiondata.ldexp_y = None

	# This is used for some tests.
	if arraycode in ('f', 'd'):
		optiondata.compval =  float(0)
	else:
		optiondata.compval =  int(0)

	
	# Used for compress.
	if 'fabs' == 'compress':
		optiondata.compdata = array.array(arraycode, [1,0,1,0])
		optiondata.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(optiondata.compdata), itertools.repeat(0, arraysize))))
	else:
		optiondata.compdata = None
		optiondata.pycomp = None

	# Used for cycle.
	if 'fabs' == 'cycle':
		optiondata.startcycle = comptype(arraycode, 0)
		optiondata.endcycle = comptype(arraycode, 127)
	else:
		optiondata.startcycle = None
		optiondata.endcycle = None

	# Used for invert.
	if 'fabs' == 'invert':
		optiondata.invertmaxval = allinvertlimits[arraycode]
		if arraycode in ('b', 'h', 'i', 'l', 'q'):
			optiondata.invertop = invertpysigned
		else:
			optiondata.invertop = invertpyunsigned
	else:
		optiondata.invertmaxval = None
		optiondata.invertop = None


	# Used for findindices.
	if 'fidataout' in ('dataout'):
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
	if arraycode in ('f', 'd'):
		xdata = [float(x) for x in [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]]
	else:
		xdata = [int(x) for x in [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]]

	arraydata.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, arraysize))))
	assert len(arraydata.datax) == arraysize, 'datax is not expected length %d' % len(arraydata.datax)

	arraydata.arraylength = len(arraydata.datax)

	# Y data.
	ydata = []
	if len(ydata) > 0:
		yvalue = abs(ydata[-1])
		if arraycode in ('f', 'd'):
			arraydata.yvalue = float(yvalue)
		else:
			arraydata.yvalue = int(yvalue)
	else:
		arraydata.yvalue = None

	# Z data.
	zdata = []
	if len(zdata) > 0:
		zvalue = abs(zdata[-1])
		if arraycode in ('f', 'd'):
			arraydata.zvalue = float(zvalue)
		else:
			arraydata.zvalue = int(zvalue)
	else:
		arraydata.zvalue = None


	# Output array.
	if 'dataout' in ('dataout'):
		arraydata.dataout = array.array(arraycode, itertools.repeat(0, arraydata.arraylength))
		assert len(arraydata.dataout) == arraysize, 'dataout is not expected length %d' % len(arraydata.dataout)
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

	if True:
		for x in range(pyitercounts):
			for i in range(arraylength):
				dataout[i] = math.fabs(datax[i])
	else:
		for x in range(pyitercounts):
			dataout[i] = math.fabs(datax[i])

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
		arrayfunc.fabs(datax, dataout)
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
		arrayfunc.fabs(datax, dataout, matherrors=True)
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
		arrayfunc.fabs(datax, dataout, matherrors=True)
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
funcname = 'fabs'
supportedarrays = ('f', 'd')


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
		'x86_64' : '',
		'armv7l' : '',
		'aarch64' : '',
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
		return '{%d:>8.1f}         ' % (pos + 1)
	else:
		return '{%d:>8.0f}         ' % (pos + 1)


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


	print('\n')
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
