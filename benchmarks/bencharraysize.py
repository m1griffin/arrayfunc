#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   bencharraysize.py
# Purpose:  Benchmark the effects of array size on 'arrayfunc'.
# Language: Python 3.5
# Date:     20-Dec-2018.
# Ver:      08-Jun-2021.
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

	print('Testing %s with array size %d... ' % (funcname, arraysize), end = '', flush = True)
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
def CheckBenchmarkFiles(benchfiles):
	'''Check to see if the desired benchmark files are present.
	Return the list of expected files which are missing. If they are not 
	missing, an empty list will be returned.
	'''
	filelist = glob.glob('benchmark_*.py')
	missing = list(set(benchfiles) - set(filelist))
	return missing

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


def RunBenchmarks(funcname, filename, runtimetarget, asizes, timeout, errordata):
	''' Run the benchmarks for all array sizes.
	'''

	# Total any errors so we can report on how many there were.
	totalerrors = 0

	totalresults = {}
	# Run test for each array size.
	for arraysize in asizes:
		testdata, testOK, errorcode = runbench(funcname, filename, arraysize, runtimetarget, timeout)
		if testOK:
			totalresults[arraysize] = testdata
		else:
			print('\n\nBenchmark error in %s: \n%s\n\n' % (funcname, errorcode))
			totalresults[arraysize] = errordata
			totalerrors += 1


	return totalresults, totalerrors


##############################################################################


##############################################################################

def GetCmdArguments():
	""" Get any command line arguments. These modify the operation of the program.
			runtimetarget = The target length of time in seconds to run a benchmark for.
	"""
	runtimetarget = 0.1
	timeout = 600

	# Get any command line arguments.
	parser = argparse.ArgumentParser()

	# The length of time to run each benchmark.
	parser.add_argument('--runtimetarget', type = float, default = runtimetarget, 
		help='Target length of time to run each benchmark for.')

	# Individual benchmark timeout in seconds.
	parser.add_argument('--timeout', type = int, default = timeout, 
		help='Timeout in seconds for each benchmark.')


	args = parser.parse_args()

	return args


##############################################################################

##############################################################################

# Write out the platform data to keep track of what platform the test was run on.
def WritePlatformSignature(f):
	f.write('ArrayFunc Benchmarks and Array Size.\n')
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
	standformat = '{0:>10} ' + ''.join([sformatter(x,y) for x,y in enumerate(calcvalues)])
	f.write(standformat.format(label1, *calcvalues))
	f.write('\n')



##############################################################################


def WriteResults(f, totalresults, tableheader, tablefooter, arraycodes):
	''' Write the results to a file as a report. 
	'''
	f.write(tableheader)
	arraysizes = sorted(totalresults.keys())
	haserror = False

	for i in arraysizes:
		resultline = totalresults[i]
		try:
			pydata = resultline['pydata']
			afdata = resultline['afdata']
			calcvalues = [pydata[x] / afdata[x] for x in arraycodes if x in pydata]
			writelinerel(f, i, calcvalues)
		except KeyError:
			f.write('{0:>10}   Key error. Check for time out.\n'.format(i))
			haserror = True
		except ZeroDivisionError:
			f.write('{0:>10}   Divide by zero error.\n'.format(i))
			haserror = True

	f.write(tablefooter)

	return haserror


##############################################################################


CmdArgs = GetCmdArguments()

RunTimeTarget = CmdArgs.runtimetarget
TimeOut = CmdArgs.timeout

##############################################################################

arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']

# This is used in place of actual data when there is an error.
ErrorData = {'error' : len(arraycodes)}


TableHeader = '''
=========== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
Array size    b     B     h     H     i     I     l     L     q     Q     f     d  
=========== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
'''

TableFooter = '''=========== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ====='''


##############################################################################

# Sizes of arrays.
ASizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

# The benchmark files to use.
BenchMarkSelection = {'add' : 'benchmark_add.py', 'xor' : 'benchmark_xor.py'}
BenchFiles = list(BenchMarkSelection.values())

print('\n\nStarting ArrayFunc array size benchmarks.\n')


# Check for missing benchmark files.
MissingFiles = CheckBenchmarkFiles(BenchFiles)

if len(MissingFiles) > 0:
	print('Error: one or more required benchmark files are missing: %s' % ', '.join(MissingFiles))
	sys.exit()


starttime = time.perf_counter()

# Run the benchmarks for add.
TotalResultsAdd, TotalErrorsAdd = RunBenchmarks('add', BenchMarkSelection['add'], RunTimeTarget, ASizes,TimeOut, ErrorData)
# Run the benchmarks for xor.
TotalResultsXor, TotalErrorsXor = RunBenchmarks('xor', BenchMarkSelection['xor'], RunTimeTarget, ASizes, TimeOut, ErrorData)


# Write out the results.
with open('bencharraysize.txt', 'w') as f:

	f.write(time.ctime() + '\n')

	WritePlatformSignature(f)

	# Results for add.
	f.write('\n\n\n')
	f.write('Benchmark the effects of array size on a selected arrayfunc function.\n\n')
	f.write('Add constant to array - times faster than Python, default settings.\n')

	AddError = WriteResults(f, TotalResultsAdd, TableHeader, TableFooter, arraycodes)

	f.write('\n\n\n')
	# Results for xor.
	f.write('Xor an array by a constant - times faster than Python, default settings.\n')

	XorError = WriteResults(f, TotalResultsXor, TableHeader, TableFooter, arraycodes)

	f.write('\n\n')


print('\nTime to run all benchmarks: %.2f seconds.' % (time.perf_counter() - starttime))

if AddError or XorError:
	print('At least one error occured. Check the benchmark output for more information.\n')


##############################################################################
