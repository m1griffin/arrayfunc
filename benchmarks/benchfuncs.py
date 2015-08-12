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

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	# Native Python time.
	starttime = time.time()
	# We need to prevent overflows.
	if arraycode in ('b', 'B', 'h', 'H'):
		mask = rollmasks[arraycode]
		for x, y in zip(itertools.count(0), itertools.repeat(0, ARRAYSIZE)):
			data[x] = x & mask
	else:
		for x, y in zip(itertools.count(0), itertools.repeat(0, ARRAYSIZE)):
			data[x] = x
	endtime = time.time()

	pythontime = endtime - starttime

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.time()
	arrayfunc.count(data, 0) 
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchcycle(arraycode):
	"""Benchmark the cycle function.
	"""
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	startcycle = comptype(arraycode, 0)
	endcycle = comptype(arraycode, 127)

	# Native Python time.
	cycledata = list(range(128))
	starttime = time.time()
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x
	endtime = time.time()

	pythontime = endtime - starttime

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.time()
	arrayfunc.cycle(data, startcycle, endcycle)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchrepeat(arraycode):
	"""Benchmark the repeat function.
	"""
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	compval = comptype(arraycode, 10)

	# Native Python time.
	starttime = time.time()
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	endtime = time.time()

	pythontime = endtime - starttime

	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.time()
	arrayfunc.repeat(data, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)




#############################################################################

def benchfilter(arraycode):
	"""Benchmark the filter function.
	"""
	cycledata = list(range(128))
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))

	compval = comptype(arraycode, 50)

	# Native Python time.
	starttime = time.time()
	dataout = array.array(arraycode, filter(lambda x: x < compval, data))
	endtime = time.time()

	pythontime = endtime - starttime

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.afilter(arrayfunc.aops.af_lt, data, dataout, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchcompress(arraycode):
	"""Benchmark the compress function.
	"""
	cycledata = list(range(128))
	compdata = array.array(arraycode, [1,0,1,0])
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(compdata), itertools.repeat(0, ARRAYSIZE))))

	# Native Python time.
	z = 0
	starttime = time.time()
	for x in itertools.compress(data, pycomp):
		dataout[z] = x
		z += 1
	endtime = time.time()

	pythontime = endtime - starttime

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.compress(data, dataout, compdata)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchdropwhile(arraycode):
	"""Benchmark the dropwhile function.
	"""
	data = array.array(arraycode, itertools.chain(itertools.repeat(5, ARRAYSIZE // 2), itertools.repeat(50, ARRAYSIZE // 2)))
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	compval = comptype(arraycode, 10)

	# Native Python time.
	starttime = time.time()
	dataout = array.array(arraycode, itertools.dropwhile(lambda x : x < compval, data))
	endtime = time.time()

	pythontime = endtime - starttime

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.dropwhile(arrayfunc.aops.af_lt, data, dataout, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)



#############################################################################

def benchtakewhile(arraycode):
	"""Benchmark the takewhile function.
	"""
	data = array.array(arraycode, itertools.chain(itertools.repeat(5, ARRAYSIZE // 2), itertools.repeat(50, ARRAYSIZE // 2)))
	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	compval = comptype(arraycode, 10)

	# Native Python time.
	starttime = time.time()
	dataout = array.array(arraycode, itertools.takewhile(lambda x : x < compval, data))
	endtime = time.time()

	pythontime = endtime - starttime

	dataout = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.takewhile(arrayfunc.aops.af_lt, data, dataout, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)




#############################################################################

def benchaany(arraycode):
	"""Benchmark the aany function.
	"""
	data = array.array(arraycode, itertools.chain(itertools.repeat(0, ARRAYSIZE // 2), itertools.repeat(10, ARRAYSIZE // 2)))
	compval = comptype(arraycode, 5)

	# Native Python time.
	starttime = time.time()
	x = any(data)
	endtime = time.time()

	pythontime = endtime - starttime

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.aany(arrayfunc.aops.af_gt, data, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchaall(arraycode):
	"""Benchmark the aall function.
	"""
	data = array.array(arraycode, itertools.repeat(10, ARRAYSIZE))
	compval = comptype(arraycode, 5)

	# Native Python time.
	starttime = time.time()
	x = all(data)
	endtime = time.time()

	pythontime = endtime - starttime

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.aall(arrayfunc.aops.af_gt, data, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchamax(arraycode):
	"""Benchmark the amax function.
	"""
	cycledata = list(range(128))
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x

	# Native Python time.
	starttime = time.time()
	x = max(data)
	endtime = time.time()

	pythontime = endtime - starttime

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.amax(data)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchamin(arraycode):
	"""Benchmark the amin function.
	"""
	cycledata = list(range(128))
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	for x, y in zip(itertools.cycle(cycledata), itertools.repeat(0, ARRAYSIZE)):
		data[x] = x

	# Native Python time.
	starttime = time.time()
	x = min(data)
	endtime = time.time()

	pythontime = endtime - starttime

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.amin(data)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchfindindex(arraycode):
	"""Benchmark the findindex function.
	"""
	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval

	# Native Python time.
	starttime = time.time()
	x = data.index(compval)
	endtime = time.time()

	pythontime = endtime - starttime

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.findindex(arrayfunc.aops.af_eq, data, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchfindindices(arraycode):
	"""Benchmark the findindices function.
	"""
	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval
	dataout = array.array('l', itertools.repeat(0, ARRAYSIZE))

	# Native Python time.
	z = 0
	starttime = time.time()
	for x in data:
		if x == compval:
			dataout[z] = z
			z += 1
	endtime = time.time()

	pythontime = endtime - starttime

	dataout = array.array('l', itertools.repeat(0, ARRAYSIZE))

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.findindices(arrayfunc.aops.af_eq, data, dataout, compval)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchasum(arraycode):
	"""Benchmark the asum function.
	"""
	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval

	# Native Python time.
	starttime = time.time()
	x = sum(data)
	endtime = time.time()

	pythontime = endtime - starttime

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.asum(data)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)


#############################################################################

def benchasumov(arraycode):
	"""Benchmark the asum function with overflow checking disabled.
	"""
	compval = comptype(arraycode, 10)
	data = array.array(arraycode, itertools.repeat(0, ARRAYSIZE))
	data[-1] = compval

	# Native Python time.
	starttime = time.time()
	x = sum(data)
	endtime = time.time()

	pythontime = endtime - starttime

	# Arrayfunc time.
	starttime = time.time()
	x = arrayfunc.asum(data, ov=True)
	endtime = time.time()

	functime = endtime - starttime

	return (pythontime, functime, pythontime / functime)

#############################################################################

TestResults = {}
FuncNames = []

TestNames = [('count', benchcount), ('cycle', benchcycle), ('repeat', benchrepeat),
			('afilter', benchfilter), ('compress', benchcompress), ('dropwhile', benchdropwhile),
			('takewhile', benchtakewhile), ('aany', benchaany), ('aall', benchaall),
			('amax', benchamax), ('amin', benchamin), 
			('findindex', benchfindindex), ('findindices', benchfindindices),
			('asum', benchasum)]

TestNames.sort(key= lambda x: x[0])


for testname, testfunc in TestNames:
	print(testname)
	Results = {}
	for i in arraycodes:
		Results[i] = testfunc(i)
	TestResults[testname] = Results



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


tableheader = {'func' : 'function', 'b' : 'b', 'B' : 'B', 'h' : 'h', 'H' : 'H', 
		'i' : 'i', 'I' : 'I', 'l' : 'l', 'L' : 'L', 'q' : 'q', 'Q' : 'Q', 'f' : 'f', 'd' : 'd'}

tableformat = '%(func)11s %(b)5s %(B)5s %(h)5s %(H)5s %(i)5s %(I)5s %(l)5s %(L)5s %(q)5s %(Q)5s %(f)5s %(d)5s\n'
columnsep = '===='
tablesep = {'func' : '===========', 'b' : columnsep, 'B' : columnsep, 
		'h' : columnsep, 'H' : columnsep, 'i' : columnsep, 'I' : columnsep, 
		'l' : columnsep, 'L' : columnsep, 'q' : columnsep, 'Q' : columnsep, 
		'f' : columnsep, 'd' : columnsep}

defaultdata = ['','','','','']


with open('benchfuncs.txt', 'w') as f:
	f.write(tableformat % tablesep)
	f.write(tableformat % tableheader)
	f.write(tableformat % tablesep)

	numstats = []

	for func, tfunc in TestNames:
		bc = TestResults[func]
		benchdata = {'func' : func}
		benchdata.update(dict([(x, dataformat(bc.get(x, defaultdata)[2])) for x in arraycodes]))
		benchline = tableformat % benchdata
		f.write(benchline)

		# Accumulate the data for stats.
		stats = [bc.get(x, defaultdata)[2] for x in arraycodes]
		numstats.extend([x for x in stats if x != ''])


	f.write(tableformat % tablesep)


##############################################################################

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
