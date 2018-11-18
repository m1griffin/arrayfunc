#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   bencharraysize.py
# Purpose:  Benchmark the effects of array size on 'arrayfunc'.
# Language: Python 3.5
# Date:     05-Apr-2018.
# Ver:      26-Jun-2018.
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


##############################################################################

# Write out the platform data to keep track of what platform the test was run on.
def WritePlatformSignature(f):
	# test was run on.
	# 'Linux'
	f.write('Operating System: ' + platform.system() + '\n')

	# 'Linux-4.4.0-79-generic-x86_64-with-Ubuntu-16.04-xenial'
	f.write('Platform: ' + platform.platform() + '\n')

	# ('64bit', 'ELF')
	f.write('Word size: ' + platform.architecture()[0] + '\n')

	# 'GCC 5.4.0 20160609'
	f.write('Compiler: ' + platform.python_compiler() + '\n')

	# '4.4.0-79-generic'
	f.write('Python release: ' + platform.release() + '\n')
	f.write('\n\n\n')


##############################################################################



##############################################################################
class benchmark_add:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'add'
		self.runtimetarget = 0.1



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [float(x) for x in [-25,-1,0,1,25]]
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [int(x) for x in [-25,-1,0,1,25]]

		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if arraycode in ('B', 'H', 'I', 'L', 'Q'):
			ydata = [abs(x) for x in ydata]


		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays saves
		# time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None

		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
		else:
			self.dataout = None



		# This is used for some optimised tests.
		if len(ydata) > 0:
			self.yvalue = abs(ydata[-1])
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


		self.RelativeResults = ''

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
			return ('%0.0f' % val).rjust(5)
		else:
			return ('%0.1f' % val).rjust(5)


	########################################################
	def fmtabsdata(self, val):
		"""Format the output data for micro-second results.
		"""
		if val == None:
			return ' '.rjust(8)
		else:
			return ('%d' % (val * 1000000.0)).rjust(8)


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
			print('Calibrate Python ', arraycode, ARRAYSIZE)
			pytime = self.BenchmarkPython(arraycode)
			self.pythontime.append(pytime)


		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			print('Calibrate Arrayfunc ', arraycode, ARRAYSIZE)
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
			print('Benchmark Python ', arraycode, ARRAYSIZE)
			pytime = self.BenchmarkPython(arraycode)
			self.PyData[arraycode] = pytime
			self.pythontime.append(pytime)

		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			print('Benchmark arrayfunc ', arraycode, ARRAYSIZE)
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

		# Format the results strings.
		self.RelativeResults = ' ' + ' '.join([self.fmtreldata(self.RelData[x]) for x in arraycodes])


		# Repeat using optimised options and call forms.
		# Arrayfunc time.
		for arraycode in self.supportedarrays:
			print('Benchmark fast arrayfunc ', arraycode, ARRAYSIZE)
			self.AfDataFast[arraycode] = self.BenchmarkAFFast(arraycode)

		# Relative time.
		reldatafast = dict([(x, self.PyData[x] / y) for x,y in self.AfDataFast.items() if y != None])
		self.RelDataFast.update(reldatafast)


		# Format the fast result strings.
		self.RelativeResultsFast = ' ' + ' '.join([self.fmtreldata(self.RelDataFast[x]) for x in arraycodes])



	########################################################
	def BenchmarkPython(self, arraycode):
		"""Measure execution time of native Python code.
		"""
		# Initialise the test data arrays. We provide a local reference to
		# the arrays to make the representation simpler.
		self.InitDataArrays(arraycode)
		datax = self.datax
		datay = self.datay
		dataout = self.dataout


		# This is used for some tests only. 
		result = True


		# Time for python.
		starttime = time.perf_counter()
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] + datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] + datay[i]

		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		return pythontime


	########################################################
	def BenchmarkAF(self, arraycode):
		"""Measure execution time for arrayfunc.
		"""
		# Initialise the test data arrays again with fresh data. 
		self.InitDataArrays(arraycode)
		datax = self.datax
		datay = self.datay
		dataout = self.dataout



		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.add(datax, datay, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime



	########################################################
	def BenchmarkAFFast(self, arraycode):
		"""Measure execution time for arrayfunc with optimised calls.
		"""

		# Initialise the test data arrays again with fresh data. 
		self.InitDataArrays(arraycode)
		datax = self.datax
		datay = self.datay
		dataout = self.dataout
		yvalue = self.yvalue


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.add(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################


arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']


bc = benchmark_add()

RelativeResults = []
RelativeResultsFast = []

for ARRAYSIZE in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
	bc.RunTests()
	arsize = ('%i' % ARRAYSIZE).rjust(10)
	RelativeResults.append(arsize + bc.RelativeResults)
	RelativeResultsFast.append(arsize + bc.RelativeResultsFast)


tablesep = '=========== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ====='

headblock = '\n' + tablesep + '''
Array size    b     B     h     H     i     I     l     L     q     Q     f     d  
''' + tablesep + '\n'


with open('bencharraysize.txt', 'w') as f:

	f.write(time.ctime() + '\n')

	WritePlatformSignature(f)

	f.write('Benchmark the effects of array size on a selected arrayfunc function.\n\n')

	f.write('Add two arrays - times faster than Python, unoptimised.')
	f.write(headblock)
	f.write('\n'.join(RelativeResults))
	f.write('\n' + tablesep + '\n\n\n')


	f.write('Add constant to array - times faster than Python, optimised.')
	f.write(headblock)
	f.write('\n'.join(RelativeResultsFast))
	f.write('\n' + tablesep + '\n\n\n')


