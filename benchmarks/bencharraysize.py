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

def comptype(arraycode, cval):
	"""Return the compare value in the correct type.
	"""
	if arraycode in ('f', 'd'):
		return float(cval)
	else:
		return int(cval)

##############################################################################

# This defines which functions and which array types have SIMD versions.
# This was generated automtically by searching through the C source code 
# header files which must be present in the expected place when the 
# benchmark program is generated.

# SIMD testing is disabled for for these functions, as we don't 
# use the results comparing SIMD versus non-SIMD.
SIMDFuncs_x86 = {
 #'add': 'bBhHiIfd',
 #'xor': 'bBhHiI'
 }

SIMDFuncs_arm = {
 #'add': 'bBhH',
 #'xor': 'bBhHiI'
 }

# Detect the hardware platform, and assign the correct platform data table to it.
if '-armv' in platform.platform():
	SIMDFuncs = SIMDFuncs_arm
else:
	SIMDFuncs = SIMDFuncs_x86

# This one is a list of functions which use the 'matherrors' option.
OptFuncs = ['add', 'xor']

##############################################################################

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
		self.afiternosidmcounts = 1
		self.InitResults()
		self.funcname = 'add'
		self.runtimetarget = 0.1

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
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			self.truediv_type = int

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, self.arraysize))))
		assert len(self.datax) == self.arraysize, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Y data.
		ydata = [-25,-1,0,1,25]
		if len(ydata) > 0:
			yvalue = abs(ydata[-1])
			if arraycode in ('f', 'd'):
				self.yvalue = float(yvalue)
			else:
				self.yvalue = int(yvalue)
		else:
			self.yvalue = None

		# Z data.
		zdata = []
		if len(zdata) > 0:
			zvalue = abs(zdata[-1])
			if arraycode in ('f', 'd'):
				self.zvalue = float(zvalue)
			else:
				self.zvalue = int(zvalue)
		else:
			self.zvalue = None


		# Output array.
		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == self.arraysize, 'self.dataout is not expected length %d' % len(self.dataout)
		else:
			self.dataout = None



		# Function ldexp needs a specific array type as the second parameter.
		if self.funcname == 'ldexp':
			self.ldexp_y = int(ydata[-1])
		else:
			self.ldexp_y = None



		# This is used for some tests.
		if arraycode in ('f', 'd'):
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'add' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, self.arraysize))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
			self.fidataout = array.array('q', itertools.repeat(0, self.arraysize))


	########################################################
	def InitResults(self):
		"""Initialise the attributes which store the test results.
		"""
		self.PyData = dict.fromkeys(arraycodes, None)
		self.AfData = dict.fromkeys(arraycodes, None)
		self.RelData = dict.fromkeys(arraycodes, None)

		self.PyDataFast = dict.fromkeys(arraycodes, None)
		self.AfDataNoSIMD = dict.fromkeys(arraycodes, None)
		self.RelDataNoSIMD = dict.fromkeys(arraycodes, None)
		self.RelDataOpt = dict.fromkeys(arraycodes, None)
		self.AfDataSIMD = dict.fromkeys(arraycodes, None)
		self.RelDataSIMD = dict.fromkeys(arraycodes, None)

		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.AfResultsFast = ''
		self.FuncResultsFast = ''
		self.RelativeResultsFast = ''
		self.FuncResultsSIMD = ''
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
			return ('%0.0f' % val).rjust(RELCOLWIDTH)
		else:
			return ('%0.1f' % val).rjust(RELCOLWIDTH)


	########################################################
	def fmtabsdata(self, val):
		"""Format the output data for micro-second results.
		"""
		if val == None:
			return ' '.rjust(ABSCOLWIDTH)
		else:
			return ('%0.1f' % (val * 1000000.0)).rjust(ABSCOLWIDTH)


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
		if not arraycode in SIMDFuncs[self.funcname]:
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
	def calibrateruntime(self, arraycode):
		"""Calibrate the run time.
		"""
		self.pyitercounts = 1
		self.afitercounts = 50
		self.afiternosidmcounts = 50

		# First, do a timing calibration run.
		# Python native time.
		pytime = self.BenchmarkPython(arraycode)

		# Arrayfunc time.
		aftime = self.BenchmarkAF(arraycode)


		# Now calculate the average execution time and adjust the iterations
		# so that the tests will take approximately 0.1 seconds.
		# The time returned by the benchmark function is per iteration, so 
		# we don't need to adjust for this again.
		self.pyitercounts = int(self.runtimetarget / pytime)
		self.afitercounts = int(self.runtimetarget / aftime)

		# Make sure the iteration count is at least 1.
		if self.pyitercounts < 1:
			self.pyitercounts = 1
		if self.afitercounts < 1:
			self.afitercounts = 1


		# Arrayfunc time without SIMD for functions with SIMD.
		if self.funcname in SIMDFuncs:
			aftimenosimd = self.BenchmarkAFNoSIMD(arraycode)
			self.afiternosidmcounts = int(self.runtimetarget / aftimenosimd)
			if self.afiternosidmcounts < 1:
				self.afiternosidmcounts = 1


	########################################################
	def RunTests(self, arraysize):
		"""Run all the tests.
		"""
		self.arraysize = arraysize

		# Test using each array type.
		for arraycode in self.supportedarrays:
			self.InitDataArrays(arraycode)

			# Calibrate the run time to set the number of test iterations
			# to meet a target test run time.
			self.calibrateruntime(arraycode)

			# Python native time.
			self.PyData[arraycode] = self.BenchmarkPython(arraycode)

			# Arrayfunc time.
			self.AfData[arraycode] = self.BenchmarkAF(arraycode)
			

			# If the function supports SIMD operations, repeat the test
			# with SIMD turned off and on. Some function calls only support
			# SIMD if error checking is turned off, so we must do this again
			# to be sure we have data both ways.
			if self.funcname in SIMDFuncs:
				self.AfDataNoSIMD[arraycode] = self.BenchmarkAFNoSIMD(arraycode)
				self.AfDataSIMD[arraycode] = self.BenchmarkAFSIMD(arraycode)



		# Calculate and format the results on the collected data.
		# Relative time, Python versus Arrayfunc.
		reldata, self.relativetime = self.comparedata(self.PyData, self.AfData)
		self.RelData.update(reldata)

		# Format the results strings.
		self.PyResults = self.formattimedata(self.PyData)
		self.FuncResults = self.formattimedata(self.AfData)
		self.RelativeResults = self.formatreldata(self.RelData)


		# Calculate the SIMD data results of we did those tests.
		if self.funcname in SIMDFuncs:

			# Calculate and format the results comparing the non-SIMD and SIMD results.
			self.RelSIMD = self.escfname + ' '.join([self.simdcalc(x, self.AfDataNoSIMD[x], self.AfDataSIMD[x]) for x in arraycodes])


			# Relative time, Python versus SIMD optimised Arrayfunc.
			reldatasimd, self.relativetimesimd = self.comparedata(self.PyData, self.AfDataSIMD)
			self.RelDataSIMD.update(reldatasimd)


			# Format the fast result strings.
			self.FuncResultsFast = self.formattimedata(self.AfDataNoSIMD)
			self.RelativeResultsFast = self.formatreldata(self.RelDataNoSIMD)


			# Format the fast result strings.
			self.FuncResultsSIMD = self.formattimedata(self.AfDataSIMD)
			self.RelativeResultsSIMD = self.formatreldata(self.RelDataSIMD)

			# Format the optimised versus not optimsed result strings.
			if self.funcname in OptFuncs:
				self.RelOpt = self.formatreldata(self.RelDataOpt)



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


		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y
		truediv_type = self.truediv_type


		# This is used for some tests only. 
		result = True


		# Time for python.
		starttime = time.perf_counter()

		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] + yvalue
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] + yvalue

		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		return pythontime


	########################################################
	def BenchmarkAF(self, arraycode):
		"""Measure execution time for arrayfunc.
		"""
		# This is used for some tests only. 
		result = True

		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.add(datax, yvalue, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime



	########################################################
	def BenchmarkAFNoSIMD(self, arraycode):
		"""Measure execution time for arrayfunc with SIMD turned off calls.
		"""
		# This is used for some tests only. 
		result = True

		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afiternosidmcounts):
			arrayfunc.add(datax, yvalue, dataout, matherrors=True, nosimd=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afiternosidmcounts

		return aftime



	########################################################
	def BenchmarkAFSIMD(self, arraycode):
		"""Measure execution time for arrayfunc with SIMD.
		"""
		# This is used for some tests only. 
		result = True

		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.add(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################




##############################################################################
class benchmark_xor:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.afiternosidmcounts = 1
		self.InitResults()
		self.funcname = 'xor'
		self.runtimetarget = 0.1

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
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			self.truediv_type = int

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, self.arraysize))))
		assert len(self.datax) == self.arraysize, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Y data.
		ydata = [0,1,2,3,4,5]
		if len(ydata) > 0:
			yvalue = abs(ydata[-1])
			if arraycode in ('f', 'd'):
				self.yvalue = float(yvalue)
			else:
				self.yvalue = int(yvalue)
		else:
			self.yvalue = None

		# Z data.
		zdata = []
		if len(zdata) > 0:
			zvalue = abs(zdata[-1])
			if arraycode in ('f', 'd'):
				self.zvalue = float(zvalue)
			else:
				self.zvalue = int(zvalue)
		else:
			self.zvalue = None


		# Output array.
		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == self.arraysize, 'self.dataout is not expected length %d' % len(self.dataout)
		else:
			self.dataout = None



		# Function ldexp needs a specific array type as the second parameter.
		if self.funcname == 'ldexp':
			self.ldexp_y = int(ydata[-1])
		else:
			self.ldexp_y = None



		# This is used for some tests.
		if arraycode in ('f', 'd'):
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'xor' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, self.arraysize))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
			self.fidataout = array.array('q', itertools.repeat(0, self.arraysize))


	########################################################
	def InitResults(self):
		"""Initialise the attributes which store the test results.
		"""
		self.PyData = dict.fromkeys(arraycodes, None)
		self.AfData = dict.fromkeys(arraycodes, None)
		self.RelData = dict.fromkeys(arraycodes, None)

		self.PyDataFast = dict.fromkeys(arraycodes, None)
		self.AfDataNoSIMD = dict.fromkeys(arraycodes, None)
		self.RelDataNoSIMD = dict.fromkeys(arraycodes, None)
		self.RelDataOpt = dict.fromkeys(arraycodes, None)
		self.AfDataSIMD = dict.fromkeys(arraycodes, None)
		self.RelDataSIMD = dict.fromkeys(arraycodes, None)

		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.AfResultsFast = ''
		self.FuncResultsFast = ''
		self.RelativeResultsFast = ''
		self.FuncResultsSIMD = ''
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
			return ('%0.0f' % val).rjust(RELCOLWIDTH)
		else:
			return ('%0.1f' % val).rjust(RELCOLWIDTH)


	########################################################
	def fmtabsdata(self, val):
		"""Format the output data for micro-second results.
		"""
		if val == None:
			return ' '.rjust(ABSCOLWIDTH)
		else:
			return ('%0.1f' % (val * 1000000.0)).rjust(ABSCOLWIDTH)


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
		if not arraycode in SIMDFuncs[self.funcname]:
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
	def calibrateruntime(self, arraycode):
		"""Calibrate the run time.
		"""
		self.pyitercounts = 1
		self.afitercounts = 50
		self.afiternosidmcounts = 50

		# First, do a timing calibration run.
		# Python native time.
		pytime = self.BenchmarkPython(arraycode)

		# Arrayfunc time.
		aftime = self.BenchmarkAF(arraycode)


		# Now calculate the average execution time and adjust the iterations
		# so that the tests will take approximately 0.1 seconds.
		# The time returned by the benchmark function is per iteration, so 
		# we don't need to adjust for this again.
		self.pyitercounts = int(self.runtimetarget / pytime)
		self.afitercounts = int(self.runtimetarget / aftime)

		# Make sure the iteration count is at least 1.
		if self.pyitercounts < 1:
			self.pyitercounts = 1
		if self.afitercounts < 1:
			self.afitercounts = 1


		# Arrayfunc time without SIMD for functions with SIMD.
		if self.funcname in SIMDFuncs:
			aftimenosimd = self.BenchmarkAFNoSIMD(arraycode)
			self.afiternosidmcounts = int(self.runtimetarget / aftimenosimd)
			if self.afiternosidmcounts < 1:
				self.afiternosidmcounts = 1


	########################################################
	def RunTests(self, arraysize):
		"""Run all the tests.
		"""
		self.arraysize = arraysize

		# Test using each array type.
		for arraycode in self.supportedarrays:
			self.InitDataArrays(arraycode)

			# Calibrate the run time to set the number of test iterations
			# to meet a target test run time.
			self.calibrateruntime(arraycode)

			# Python native time.
			self.PyData[arraycode] = self.BenchmarkPython(arraycode)

			# Arrayfunc time.
			self.AfData[arraycode] = self.BenchmarkAF(arraycode)
			

			# If the function supports SIMD operations, repeat the test
			# with SIMD turned off and on. Some function calls only support
			# SIMD if error checking is turned off, so we must do this again
			# to be sure we have data both ways.
			if self.funcname in SIMDFuncs:
				self.AfDataNoSIMD[arraycode] = self.BenchmarkAFNoSIMD(arraycode)
				self.AfDataSIMD[arraycode] = self.BenchmarkAFSIMD(arraycode)



		# Calculate and format the results on the collected data.
		# Relative time, Python versus Arrayfunc.
		reldata, self.relativetime = self.comparedata(self.PyData, self.AfData)
		self.RelData.update(reldata)

		# Format the results strings.
		self.PyResults = self.formattimedata(self.PyData)
		self.FuncResults = self.formattimedata(self.AfData)
		self.RelativeResults = self.formatreldata(self.RelData)


		# Calculate the SIMD data results of we did those tests.
		if self.funcname in SIMDFuncs:

			# Calculate and format the results comparing the non-SIMD and SIMD results.
			self.RelSIMD = self.escfname + ' '.join([self.simdcalc(x, self.AfDataNoSIMD[x], self.AfDataSIMD[x]) for x in arraycodes])


			# Relative time, Python versus SIMD optimised Arrayfunc.
			reldatasimd, self.relativetimesimd = self.comparedata(self.PyData, self.AfDataSIMD)
			self.RelDataSIMD.update(reldatasimd)


			# Format the fast result strings.
			self.FuncResultsFast = self.formattimedata(self.AfDataNoSIMD)
			self.RelativeResultsFast = self.formatreldata(self.RelDataNoSIMD)


			# Format the fast result strings.
			self.FuncResultsSIMD = self.formattimedata(self.AfDataSIMD)
			self.RelativeResultsSIMD = self.formatreldata(self.RelDataSIMD)

			# Format the optimised versus not optimsed result strings.
			if self.funcname in OptFuncs:
				self.RelOpt = self.formatreldata(self.RelDataOpt)



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


		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y
		truediv_type = self.truediv_type


		# This is used for some tests only. 
		result = True


		# Time for python.
		starttime = time.perf_counter()

		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] ^ yvalue
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] ^ yvalue

		endtime = time.perf_counter()

		pythontime = (endtime - starttime) / self.pyitercounts

		return pythontime


	########################################################
	def BenchmarkAF(self, arraycode):
		"""Measure execution time for arrayfunc.
		"""
		# This is used for some tests only. 
		result = True

		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.xor(datax, yvalue, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime



	########################################################
	def BenchmarkAFNoSIMD(self, arraycode):
		"""Measure execution time for arrayfunc with SIMD turned off calls.
		"""
		# This is used for some tests only. 
		result = True

		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afiternosidmcounts):
			arrayfunc.xor(datax, yvalue, dataout, nosimd=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afiternosidmcounts

		return aftime



	########################################################
	def BenchmarkAFSIMD(self, arraycode):
		"""Measure execution time for arrayfunc with SIMD.
		"""
		# This is used for some tests only. 
		result = True

		# We provide a local reference to the arrays to make the representation simpler.
		datax = self.datax
		dataout = self.dataout
		yvalue = self.yvalue
		zvalue = self.zvalue
		# Used for ldexp only.
		ldexp_y = self.ldexp_y


		# Time for arrayfunc version.
		starttime = time.perf_counter()
		for i in range(self.afitercounts):
			arrayfunc.xor(datax, yvalue, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################


##############################################################################

arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']

tablesep = '=========== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ====='

headblock = '\n' + tablesep + '''
Array size    b     B     h     H     i     I     l     L     q     Q     f     d  
''' + tablesep + '\n'

def RunBenches():

	# Add
	bc = benchmark_add()

	AddRelativeResults = []

	starttime = time.perf_counter()
	for arraysize in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
		print('add', arraysize)
		starttime = time.perf_counter()
		bc.RunTests(arraysize)
		arsize = ('%i' % arraysize).rjust(10)
		AddRelativeResults.append(arsize + '  ' + bc.RelativeResults.lstrip().partition(' ')[2])

	endtime = time.perf_counter()
	print('Test time %.2f sec.' % (endtime - starttime))

	print()

	# XOR
	bc = benchmark_xor()

	XorRelativeResults = []

	starttime = time.perf_counter()
	for arraysize in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
		print('xor', arraysize)
		bc.RunTests(arraysize)
		arsize = ('%i' % arraysize).rjust(10)
		XorRelativeResults.append(arsize + '  ' + bc.RelativeResults.lstrip().partition(' ')[2])

	endtime = time.perf_counter()
	print('Test time %.2f sec.' % (endtime - starttime))


	##############################################################################


	with open('bencharraysize.txt', 'w') as f:

		f.write(time.ctime() + '\n')

		WritePlatformSignature(f)

		f.write('Benchmark the effects of array size on a selected arrayfunc function.\n\n')

		f.write('Add constant to array - times faster than Python, default settings.\n')
		f.write(headblock)
		f.write('\n'.join(AddRelativeResults))
		f.write('\n' + tablesep + '\n\n\n')


		f.write('Xor an array by a constant - times faster than Python, default settings.\n')
		f.write(headblock)
		f.write('\n'.join(XorRelativeResults))
		f.write('\n' + tablesep + '\n\n\n')

##############################################################################

RunBenches()
