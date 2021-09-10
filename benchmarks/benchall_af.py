#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   benchall_af.py
# Purpose:  Run benchmark tests for 'arrayfunc' functions.
# Language: Python 3.5
# Date:     20-Dec-2018.
# Ver:      16-May-2021.
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

import subprocess
import sys
import glob
import os
import platform
import argparse

import time
import json

# ==============================================================================



##############################################################################
def runbench(funcname, filename, arraysize, runtimetarget, timeout):
	"""This is used to run each individual benchmark.
	"""

	print('Testing %s ... ' % funcname, end = '', flush = True)
	starttime = time.perf_counter()

	try:
		# Older versions of Python (before 3.7) require a different syntax
		# in order to capture output. We use the new syntax, and if that
		# fails we fall back on the old one. The old version can be dropped
		# once we drop support for older versions of Python.
		try:
			result = subprocess.run(
				[sys.executable, filename, '--rawoutput', '--arraysize', '%d' % arraysize, 
						'--runtimetarget', '%.6f' % runtimetarget], 
				capture_output = True, text = True, timeout = timeout
				)
		except TypeError:
			result = subprocess.run(
				[sys.executable, filename, '--rawoutput', '--arraysize', '%d' % arraysize, 
						'--runtimetarget', '%.6f' % runtimetarget], 
				stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True, 
				timeout = timeout
				)

		testresult = result.stdout
		testerror = result.stderr
	except subprocess.TimeoutExpired:
		print('Benchmark timed out ... ', end = '', flush = True)
		testresult = dict({})
		testerror = None
		return testresult, False, 'Benchmark timed out ... '

	print('%.2f seconds.' % (time.perf_counter() - starttime))


	# Check if the benchmark returned an error of its own.
	if len(testerror) > 0:
		print('Error in benchmark ...')
		return dict({}), False, testerror

	try:
		testdata = json.loads(testresult)
	except:
		return dict({}), False, 'Json error ...'


	# Check if benchmark ID field is present.
	if not 'benchname' in testdata:
		return dict({}), False, 'unknown benchmark type ...'

	# Check if the benchmark identifies itself correctly as belonging
	# to this project.
	if testdata['benchname'] != 'arrayfunc':
		return dict({}), False, 'invalid benchmark type: %s.' % testdata['benchname']


	return testdata, True, ''


##############################################################################


##############################################################################
def getbenchmarkfiles():
	'''Get a list of the benchmark files.
	'''
	filelist=glob.glob('benchmark_*.py')
	filelist.sort()
	return filelist

##############################################################################

##############################################################################
def fnamesplit(fname):
	''' Split a file name to extract the function name.
	'''
	# Split off file extension. E.g. ('benchmark_aall', '.py')
	rootname = os.path.splitext(fname)[0]
	# The part we want is the function name, which is the second part.
	return rootname.split('_', maxsplit=1)[1]


##############################################################################


def RunBenchmarks(arraysize, runtimetarget, timeout, errordata):
	''' Run all the benchmarks.
	'''

	# Find all the benchmarks in the current directory. The benchmarks are
	# recognised by the file pattern name.
	filelist = getbenchmarkfiles()

	# Convert the list of file names into a list of function and file names.
	funclist = [(fnamesplit(x), x) for x in filelist]

	totalresults = {}

	# Total any errors so we can report on how many there were.
	totalerrors = 0


	# Run the benchmarks, accumulating the data.
	for funcname, filename in funclist:
		testdata, testOK, errorcode = runbench(funcname, filename, arraysize, runtimetarget, timeout)
		if testOK:
			totalresults[funcname] = testdata
		else:
			print('\n\nBenchmark error in %s: \n%s\n\n' % (funcname, errorcode))
			totalresults[funcname] = errordata
			totalerrors += 1



	# Save just the names of the functions to use in the final report.
	funcnamelist = [x for x,y in funclist]

	return totalresults, funcnamelist, totalerrors


##############################################################################


# Create the table header.
########################################################
def FormatHeaderLabels(columnwidth):
	"""Return a string containing the table header labels.
	"""
	return ('function'.center(FCOLWIDTH)) + ' '.join([x.center(columnwidth) for x in arraycodes]) + '\n'


########################################################
def FormatTableSep(columnwidth):
	"""Return a string containing the table separator.
	"""
	return '=' * FCOLWIDTH + ' ' + ' '.join(['=' * columnwidth] * len(arraycodes)) + '\n'


##############################################################################

# Write out the platform data to keep track of what platform the test was run on.
def WritePlatformSignature(f):
	f.write('ArrayFunc Benchmarks.\n')
	# test was run on.
	# 'Linux'
	f.write('Operating System: ' + platform.system() + '\n')

	# 'Linux-4.4.0-79-generic-x86_64-with-Ubuntu-16.04-xenial'
	f.write('Platform: ' + platform.platform() + '\n')

	# 'x86_64'
	f.write('Machine: ' + platform.machine() + '\n')

	# ('64bit', 'ELF')
	f.write('Word size: ' + platform.architecture()[0] + '\n')

	# 'GCC 5.4.0 20160609'
	f.write('Compiler: ' + platform.python_compiler() + '\n')

	# '4.4.0-79-generic'
	f.write('Python release: ' + platform.release() + '\n')


##############################################################################



########################################################
def escapename(funcname):
	''' We need to escape any function names ending with an underscore to 
	prevent it being interpreted as a formatting character in restructured
	text input. 
	''' 
	if funcname.endswith('_'):
		return funcname.rstrip('_') + '\_'
	else:
		return funcname


########################################################
def relcalc(acode, numerator, demoninator):
	'''Calculate the relative performance. If either value is None, this
	indicates that there is no data for that array code.
	'''
	if (numerator is None) or (demoninator is None):
		return None
	else:
		return numerator / demoninator

########################################################
def tomicrosecond(val):
	''' If numeric, convert to microseconds by multiplying by 1,000,000. 
	If None, then return None.
	'''
	if val is None:
		return None
	else:
		return val * 1000000.0


# The format string used to print out results.
########################################################
def sformatter(pos, val):
	if val is None:
		return 6 * ' '
	elif (val is not None) and (val < 10.0):
		return '{%d:>5.1f} ' % (pos + 1)
	else:
		return '{%d:>5.0f} ' % (pos + 1)


########################################################
def writelinerel(f, label1, calcvalues):
	''' Write the results for a line of relative data. 
	'''
	labelesc = escapename(label1)
	standformat = '{0:>12}' + ''.join([sformatter(x,y) for x,y in enumerate(calcvalues)])
	f.write(standformat.format(labelesc, *calcvalues))
	f.write('\n')


########################################################
def writelinedata(f, label1, calcvalues):
	''' Write the results for a line of raw data. 
	'''
	labelesc = escapename(label1)
	rformatter = lambda x, y: ' ' * 11 if y is None else '{%d:>10.1f} ' % (x + 1)
	standformat = '{0:>12}' + ''.join([rformatter(x,y) for x,y in enumerate(calcvalues)])
	f.write(standformat.format(labelesc, *calcvalues))
	f.write('\n')



########################################################
def writelinerelerror(f, label1, calcvalues):
	''' Write the error message instead of test results for relative results. 
	'''
	labelesc = escapename(label1)
	standformat = '{0:>12}' + ('  err ' * calcvalues['error'])
	f.write(standformat.format(labelesc))
	f.write('\n')



########################################################
def writelinedataerror(f, label1, calcvalues):
	''' Write the error message instead of test results for raw data results. 
	'''
	labelesc = escapename(label1)
	standformat = '{0:>12}' + ('  error    ' * calcvalues['error'])
	f.write(standformat.format(labelesc))
	f.write('\n')

##############################################################################


########################################################
def WriteRelativeResults(f, numerator, denominator, totalresults, funcnamelist, arraysize):
	'''The relative performance stats in default configuration.
	'''
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))

	numstats = []

	# Go through the list of functions benchmarked. We iterate this way
	# so we can get the results in alphabetical order.
	for func in funcnamelist:
		# Get the results for just this function.
		funcvals = totalresults[func]

		# Make sure that valid data is present.
		if 'error' not in funcvals:
			# These will be dictionaries with the keys being the array codes.
			numervals = funcvals[numerator]
			denomvals = funcvals[denominator]
			# This does the actual calculation. None is inserted as a placeholder
			# for values which cannot be calculated.
			calcvalues = [relcalc(x, numervals.get(x, None), denomvals.get(x, None)) for x in arraycodes]
			# Write out the formatted line.
			writelinerel(f, func, calcvalues)
			# Accumulate the values for the statistical summary. 
			numstats.extend([x for x in calcvalues if x is not None])
		else:
			# Write the string instead.
			writelinerelerror(f, func, funcvals)


	f.write(FormatTableSep(RELCOLWIDTH))

	# Avoid division by zero if all tests fail.
	try:
		avgval = sum(numstats) / len(numstats)
		maxval = max(numstats)
		minval = min(numstats)
	except:
		avgval = 0.0
		maxval = 0.0
		minval = 0.0


	f.write('\n\n\n')
	f.write('=========== ========\n')
	f.write('Stat         Value\n')
	f.write('=========== ========\n')
	f.write('Average:    %0.0f\n' % avgval)
	f.write('Maximum:    %0.0f\n' % maxval)
	f.write('Minimum:    %0.1f\n' % minval)
	f.write('Array size: %d\n' % arraysize)
	f.write('=========== ========\n')
	



########################################################
def WriteRelativeResultsSIMD(f, totalresults, funcnamelist, arraysize):
	'''The relative performance stats in SIMD optimised configuration.
	'''
	f.write('Relative Performance with SIMD Optimisations - Python Time / Arrayfunc Time.\n\n')
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))
	
	numstatssimd = []

	# Go through the list of functions benchmarked. We iterate this way
	# so we can get the results in alphabetical order.
	for func in funcnamelist:
		# Get the results for just this function.
		funcvals = totalresults[func]
		# Make sure that valid data is present.
		if 'error' not in funcvals:
			# These will be dictionaries with the keys being the array codes.
			pyvals = funcvals['pydata']
			afvals = funcvals['afdataerrtruesimdfalse']
			# This does the actual calculation. None is inserted as a placeholder
			# for values which cannot be calculated.
			calcvalues = [relcalc(x, pyvals.get(x, None), afvals.get(x, None)) for x in arraycodes]
			# Write out the formatted line.
			writelinerel(f, func, calcvalues)
			# Accumulate the values for the statistical summary. 
			numstatssimd.extend([x for x in calcvalues if x is not None])
		else:
			# Write the string instead.
			writelinerelerror(f, func, funcvals)



	f.write(FormatTableSep(RELCOLWIDTH))


	# Avoid division by zero if all tests fail.
	try:
		avgvalsimd = sum(numstatssimd) / len(numstatssimd)
		maxvalsimd = max(numstatssimd)
		minvalsimd = min(numstatssimd)
	except:
		avgvalsimd = 0.0
		maxvalsimd = 0.0
		minvalsimd = 0.0


	f.write('\n\n\n')
	f.write('=========== ========\n')
	f.write('Stat         Value\n')
	f.write('=========== ========\n')
	f.write('Average:    %0.0f\n' % avgvalsimd)
	f.write('Maximum:    %0.0f\n' % maxvalsimd)
	f.write('Minimum:    %0.1f\n' % minvalsimd)
	f.write('Array size: %d\n' % arraysize)
	f.write('=========== ========\n')



########################################################
def WriteSIMDResults(f, totalresults, funcnamelist):
	'''Results with or without SIMD.
	'''
	f.write('Relative Performance with and without SIMD Optimisations - Optimised / SIMD Time.\n\n')
	f.write(FormatTableSep(RELCOLWIDTH))
	f.write(FormatHeaderLabels(RELCOLWIDTH))
	f.write(FormatTableSep(RELCOLWIDTH))
	
	# Go through the list of functions benchmarked. We iterate this way
	# so we can get the results in alphabetical order.
	for func in funcnamelist:
		# Get the results for just this function.
		funcvals = totalresults[func]
		# Make sure that valid data is present.
		if 'error' not in funcvals:
			# These will be dictionaries with the keys being the array codes.
			afdataerrtruesimdtrue = funcvals['afdataerrtruesimdtrue']
			afdataerrtruesimdfalse = funcvals['afdataerrtruesimdfalse']
			# This does the actual calculation. None is inserted as a placeholder
			# for values which cannot be calculated.
			calcvalues = [relcalc(x, afdataerrtruesimdtrue.get(x, None), afdataerrtruesimdfalse.get(x, None)) for x in arraycodes]
			# Write out the formatted line.
			writelinerel(f, func, calcvalues)
		else:
			# Write the string instead.
			writelinerelerror(f, func, funcvals)


	f.write(FormatTableSep(RELCOLWIDTH) + '\n')



########################################################
def WriteAbsResults(f, datakey, totalresults, funcnamelist):
	''' Write the absolute raw data results. This is called by other functions
	which pass in the dictionary key of the data set they want written.
	'''
	f.write(FormatTableSep(ABSCOLWIDTH))
	f.write(FormatHeaderLabels(ABSCOLWIDTH))
	f.write(FormatTableSep(ABSCOLWIDTH))

	# Go through the list of functions benchmarked. We iterate this way
	# so we can get the results in alphabetical order.
	for func in funcnamelist:
		# Get the results for just this function.
		funcvals = totalresults[func]

		# Make sure that valid data is present.
		if 'error' not in funcvals:
			rawdata = funcvals[datakey]

			# Convert seconds to microseconds and return an ordered list.
			calcvalues = [tomicrosecond(rawdata.get(x, None)) for x in arraycodes]

			writelinedata(f, func, calcvalues)
		else:
			# Write the string instead.
			writelinedataerror(f, func, funcvals)


	f.write(FormatTableSep(ABSCOLWIDTH) + '\n')



########################################################
def WritePyResults(f, totalresults, funcnamelist):
	'''Python native time.
	'''
	f.write('Python native time in micro-seconds.\n')
	WriteAbsResults(f, 'pydata', totalresults, funcnamelist)



########################################################
def WriteFuncResults(f, totalresults, funcnamelist):
	'''Arrayfunc time in default configuration.
	'''
	f.write('\n\nArrayfunc time in micro-seconds.\n')
	WriteAbsResults(f, 'afdata', totalresults, funcnamelist)


########################################################
def WriteFuncResultsFast(f, totalresults, funcnamelist):
	''' Non-SIMD time.
	'''
	f.write('\n\nNon-SIMD time in micro-seconds. Math error checking turned off.\n')
	WriteAbsResults(f, 'afdataerrtruesimdtrue', totalresults, funcnamelist)


########################################################
def WriteFuncResultsSIMD(f, totalresults, funcnamelist):
	''' SIMD results.
	'''
	f.write('\n\nSIMD Optimised time in micro-seconds.\n')
	WriteAbsResults(f, 'afdataerrtruesimdfalse', totalresults, funcnamelist)


##############################################################################

def WriteResults(totalresults, funcnamelist, totalerrors, arraysize):
	''' Write the results to a file as a report. 
	'''
	with open('af_benchmarkdata.txt', 'w') as f:

		f.write(time.ctime() + '\n')

		WritePlatformSignature(f)

		# The total number of tests conducted, and how many errors there were.
		f.write('Total Tests: %d\n' % len(funcnamelist))
		f.write('Total Errors: %d\n' % totalerrors)
		f.write('\n\n')

		# The relative performance stats in default configuration.
		f.write('Relative Performance - Python Time / Arrayfunc Time.\n\n')
		WriteRelativeResults(f, 'pydata', 'afdata', totalresults, funcnamelist, arraysize)

		f.write('\n\n\n')

		# The relative performance stats in SIMD optimised configuration.
		f.write('Effect of leaving error checking on and disabling SIMD for functions with both.\n\n')
		WriteRelativeResults(f, 'afdata', 'afdataerrfalsesimdtrue', totalresults, funcnamelist, arraysize)


		f.write('\n\n\n')

		f.write('Effect of turning both error checking and SIMD off.\n\n')
		WriteRelativeResults(f, 'afdata', 'afdataerrtruesimdtrue', totalresults, funcnamelist, arraysize)


		f.write('\n\n\n')


		f.write('Effect of turning error checking off and leaving SIMD on for functions with both.\n\n')
		WriteRelativeResults(f, 'afdata', 'afdataerrtruesimdfalse', totalresults, funcnamelist, arraysize)


		f.write('\n\n\n')


		WritePyResults(f, totalresults, funcnamelist)

		WriteFuncResults(f, totalresults, funcnamelist)

		WriteFuncResultsFast(f, totalresults, funcnamelist)

		WriteFuncResultsSIMD(f, totalresults, funcnamelist)




##############################################################################

##############################################################################

def GetCmdArguments():
	""" Get any command line arguments. These modify the operation of the program.
			arraysize = Size of the array in elements.
			runtimetarget = The target length of time in seconds to run a benchmark for.
	"""
	arraysize = 100000
	runtimetarget = 0.1
	timeout = 60

	# Get any command line arguments.
	parser = argparse.ArgumentParser()

	# Size of the test arrays.
	parser.add_argument('--arraysize', type = int, default = arraysize, 
		help='Size of test arrays in number of elements.')

	# The length of time to run each benchmark.
	parser.add_argument('--runtimetarget', type = float, default = runtimetarget, 
		help='Target length of time to run each benchmark for.')

	# Individual benchmark timeout in seconds.
	parser.add_argument('--timeout', type = int, default = timeout, 
		help='Timeout in seconds for each benchmark.')


	args = parser.parse_args()

	return args


##############################################################################


CmdArgs = GetCmdArguments()

ArraySize = CmdArgs.arraysize
RunTimeTarget = CmdArgs.runtimetarget
TimeOut = CmdArgs.timeout

##############################################################################

arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']

# This is used in place of actual data when there is an error.
ErrorData = {'error' : len(arraycodes)}


# The width of the function name column in the output report.
FCOLWIDTH = 12
# The width of data columns for absolute (actual time) data.
ABSCOLWIDTH=10
# The width of data columns for relative time data.
RELCOLWIDTH=5

##############################################################################

print('\n\nStarting ArrayFunc benchmarks.\n')

starttime = time.perf_counter()

# Run the benchmarks.
TotalResults, FuncNameList, TotalErrors = RunBenchmarks(ArraySize, RunTimeTarget, TimeOut, ErrorData)

# Write out the results.
WriteResults(TotalResults, FuncNameList, TotalErrors, ArraySize)


print('\nTime to run all benchmarks: %.2f seconds.' % (time.perf_counter() - starttime))
# The total number of tests conducted, and how many errors there were.
print('Total benchmark tests: %d' % len(FuncNameList))
print('Total benchmark errors: %d\n\n' % TotalErrors)


##############################################################################
