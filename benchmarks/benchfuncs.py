#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   benchfuncs.py
# Purpose:  Benchmark functions for miscellaneous functions.
# Language: Python 3.4
# Date:     16-Sep-2014.
# Ver:      29-Sep-2014.
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
ARRAYSIZE = 1000000


##############################################################################

# These are set to target a balanced execution time for the different tests.
# The target was to cause each test to run for approximately 0.1 second on a
# typical PC. Tests that run too quickly risk poor accuracy due to platform
# timer resolution. 
calibrationdata = {
'aall' : (11, 145),
'aany' : (25, 295),
'afilter' : (1, 114),
'amax' : (5, 176),
'amin' : (6, 177),
'asum' : (12, 111),
'compress' : (3, 69),
'count' : (1, 161),
'cycle' : (2, 104),
'dropwhile' : (1, 115),
'findindex' : (6, 139),
'findindices' : (3, 114),
'repeat' : (5, 178),
'takewhile' : (1, 240)
}


arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']

##############################################################################

def comptype(arraycode, cval):
	"""Return the compare value in the correct type.
	"""
	if arraycode in ('f', 'd'):
		return float(cval)
	else:
		return int(cval)


##############################################################################

########################################################
def benchcount(arraycode):
	"""Benchmark the count function.
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

	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['count'][0]
	afitercounts = calibrationdata['count'][1]

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	# Native Python time.
	starttime = time.perf_counter()
	# We need to prevent overflows.
	if arraycode in ('b', 'B', 'h', 'H'):
		mask = rollmasks[arraycode]
		for i in range(pyitercounts):
			for x, y in zip(itertools.count(0), itertools.repeat(0, ARRAYSIZE)):
				data[x] = x & mask
	else:
		for i in range(pyitercounts):
			for x, y in zip(itertools.count(0), itertools.repeat(0, ARRAYSIZE)):
				data[x] = x
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		arrayfunc.count(data, 0) 
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchcycle(arraycode):
	"""Benchmark the cycle function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['cycle'][0]
	afitercounts = calibrationdata['cycle'][1]

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	startcycle = comptype(arraycode, 0)
	endcycle = comptype(arraycode, 127)

	# Native Python time.
	cycledata = list(range(128))
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
			data[x] = x
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		arrayfunc.cycle(data, startcycle, endcycle)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchrepeat(arraycode):
	"""Benchmark the repeat function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['repeat'][0]
	afitercounts = calibrationdata['repeat'][1]

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	compval = comptype(arraycode, 10)

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		arrayfunc.repeat(data, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)




#############################################################################

def benchafilter(arraycode):
	"""Benchmark the afilter function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['afilter'][0]
	afitercounts = calibrationdata['afilter'][1]

	cycledata = list(range(128))
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	compval = comptype(arraycode, 50)

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		dataout = array.array(arraycode, filter(lambda x: x < compval, data))
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.afilter(arrayfunc.aops.af_lt, data, dataout, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchcompress(arraycode):
	"""Benchmark the compress function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['compress'][0]
	afitercounts = calibrationdata['compress'][1]

	cycledata = list(range(128))
	compdata = array.array(arraycode, [1,0,1,0])
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(compdata), itertools.repeat(0, ARRAYSIZE))))

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		dataout = array.array(arraycode, itertools.compress(data, pycomp))
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.compress(data, dataout, compdata)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchdropwhile(arraycode):
	"""Benchmark the dropwhile function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['dropwhile'][0]
	afitercounts = calibrationdata['dropwhile'][1]

	data = array.array(arraycode, itertools.chain(itertools.repeat(5, ARRAYSIZE // 2), itertools.repeat(50, ARRAYSIZE // 2)))
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	compval = comptype(arraycode, 10)

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		dataout = array.array(arraycode, itertools.dropwhile(lambda x : x < compval, data))
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.dropwhile(arrayfunc.aops.af_lt, data, dataout, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)



#############################################################################

def benchtakewhile(arraycode):
	"""Benchmark the takewhile function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['takewhile'][0]
	afitercounts = calibrationdata['takewhile'][1]

	data = array.array(arraycode, itertools.chain(itertools.repeat(5, ARRAYSIZE // 2), itertools.repeat(50, ARRAYSIZE // 2)))
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	compval = comptype(arraycode, 10)

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		dataout = array.array(arraycode, itertools.takewhile(lambda x : x < compval, data))
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.takewhile(arrayfunc.aops.af_lt, data, dataout, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)




#############################################################################

def benchaany(arraycode):
	"""Benchmark the aany function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['aany'][0]
	afitercounts = calibrationdata['aany'][1]

	data = array.array(arraycode, itertools.chain(itertools.repeat(0, ARRAYSIZE // 2), itertools.repeat(10, ARRAYSIZE // 2)))
	compval = comptype(arraycode, 5)

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		x = any(data)
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.aany(arrayfunc.aops.af_gt, data, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchaall(arraycode):
	"""Benchmark the aall function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['aall'][0]
	afitercounts = calibrationdata['aall'][1]

	data = array.array(arraycode, itertools.repeat(10, ARRAYSIZE))
	compval = comptype(arraycode, 5)

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		x = all(data)
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.aall(arrayfunc.aops.af_gt, data, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchamax(arraycode):
	"""Benchmark the amax function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['amax'][0]
	afitercounts = calibrationdata['amax'][1]

	cycledata = list(range(128))
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		x = max(data)
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.amax(data)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchamin(arraycode):
	"""Benchmark the amin function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['amin'][0]
	afitercounts = calibrationdata['amin'][1]

	cycledata = list(range(128))
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		x = min(data)
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.amin(data)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchfindindex(arraycode):
	"""Benchmark the findindex function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['findindex'][0]
	afitercounts = calibrationdata['findindex'][1]

	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		x = data.index(compval)
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.findindex(arrayfunc.aops.af_eq, data, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchfindindices(arraycode):
	"""Benchmark the findindices function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['findindices'][0]
	afitercounts = calibrationdata['findindices'][1]

	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval
	dataout = array.array('q', itertools.repeat(0, ARRAYSIZE))

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		z = 0
		for x in data:
			if x == compval:
				dataout[z] = z
				z += 1
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	dataout = array.array('q', itertools.repeat(0, ARRAYSIZE))

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.findindices(arrayfunc.aops.af_eq, data, dataout, compval)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchasum(arraycode):
	"""Benchmark the asum function.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['asum'][0]
	afitercounts = calibrationdata['asum'][1]

	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		x = sum(data)
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.asum(data)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchasumov(arraycode):
	"""Benchmark the asum function with overflow checking disabled.
	"""
	# These are set to target a balanced execution time for the different tests.
	pyitercounts = calibrationdata['asum'][0]
	afitercounts = calibrationdata['asum'][1]

	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval

	# Native Python time.
	starttime = time.perf_counter()
	for i in range(pyitercounts):
		x = sum(data)
	endtime = time.perf_counter()

	pythontime = (endtime - starttime) / pyitercounts

	# Arrayfunc time.
	starttime = time.perf_counter()
	for i in range(afitercounts):
		x = arrayfunc.asum(data, ov=True)
	endtime = time.perf_counter()

	functime = (endtime - starttime) / afitercounts

	return (pythontime, functime, pythontime / functime)

#############################################################################


def dataformat(val):
	"""Format the output data.
	"""
	if val >= 10.0:
		return '%0.0f' % val
	else:
		return '%0.1f' % val


#############################################################################

TestResults = {}
FuncNames = []

TestNames = [('count', benchcount), ('cycle', benchcycle), ('repeat', benchrepeat),
			('afilter', benchafilter), ('compress', benchcompress), ('dropwhile', benchdropwhile),
			('takewhile', benchtakewhile), ('aany', benchaany), ('aall', benchaall),
			('amax', benchamax), ('amin', benchamin), 
			('findindex', benchfindindex), ('findindices', benchfindindices),
			('asum', benchasum)]

TestNames.sort(key= lambda x: x[0])
TestLabels = [x for x,y in TestNames]


PyResults = {}
FuncResults = {}
RelativeResults = {}
numstats = []

for testname, testfunc in TestNames:
	print(testname)
	PyResults[testname] = {}
	FuncResults[testname] = {}
	RelativeResults[testname] = {}
	
	Results = {}
	for i in arraycodes:
		pyval, funcval, relval = testfunc(i)
		PyResults[testname][i] = '%0.0f' % (pyval * 1000000.0)
		FuncResults[testname][i] = '%0.0f' % (funcval * 1000000.0)
		RelativeResults[testname][i] = dataformat(relval)

		numstats.append(relval)


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
	tablesep.update({'func' : '==========='})
	tableformat = '%(func)11s ' + ' '.join(['%(' + x + (')%is' % columnwidth) for x in arraycodes]) + '\n'

	outputfile.write(tableformat % tablesep)
	outputfile.write(tableformat % tableheader)
	outputfile.write(tableformat % tablesep)

	for func in TestLabels:
		bc = testresults[func]
		benchdata = {'func' : func}
		benchdata.update(bc)
		outputfile.write(tableformat % benchdata)


	outputfile.write(tableformat % tablesep)


##############################################################################

# These are the benchmark results which compares native Python speed to
# ArrayFunc speed.

with open('benchfuncs.txt', 'w') as f:
	WriteResults(f, 5, RelativeResults)

	# Stats for all array types.
	avgval = sum(numstats) / len(numstats)
	maxval = max(numstats)
	minval = min(numstats)


	# Summary
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

# This provides the absolute time for executing each benchmark in order to
# provide relative benchmarks for comparing different platforms. 

##############################################################################

with open('benchfuncsplatform.txt', 'w') as f:

	f.write('Python native time in micro-seconds.\n')
	WriteResults(f, 8, PyResults)

	f.write('\n\nArrayfunc time in micro-seconds.\n')
	WriteResults(f, 8, FuncResults)


##############################################################################
