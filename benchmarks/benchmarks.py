#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   benchmarks.py
# Purpose:  Benchmark tests for 'arrayfunc' functions.
# Language: Python 3.5
# Date:     20-Dec-2018.
# Ver:      22-Dec-2018.
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

SIMDFuncs = {'aall': {'b': True, 'B': False, 'h': True, 'H': False, 'i': True, 'I': False, 'l': False, 'L': False, 'q': False, 'Q': False, 'f': True, 'd': True},
 'aany': {'b': True, 'B': False, 'h': True, 'H': False, 'i': True, 'I': False, 'l': False, 'L': False, 'q': False, 'Q': False, 'f': True, 'd': True},
 'amax': {'b': True, 'B': True, 'h': True, 'H': True, 'i': True, 'I': True, 'l': False, 'L': False, 'q': False, 'Q': False, 'f': True, 'd': True},
 'amin': {'b': True, 'B': True, 'h': True, 'H': True, 'i': True, 'I': True, 'l': False, 'L': False, 'q': False, 'Q': False, 'f': True, 'd': True},
 'asum': {'b': False, 'B': False, 'h': False, 'H': False, 'i': False, 'I': False, 'l': False, 'L': False, 'q': False, 'Q': False, 'f': True, 'd': True},
 'findindex': {'b': True, 'B': False, 'h': True, 'H': False, 'i': True, 'I': False, 'l': False, 'L': False, 'q': False, 'Q': False, 'f': True, 'd': True}}


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

##############################################################################
class benchmark_aall:
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
		self.funcname = 'aall'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [10]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [10]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(5)
		else:
			self.compval =  int(5)

		
		# Used for compress.
		if 'aall' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = all(datax)
		else:
			for x in range(self.pyitercounts):
				result = all(datax)

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
			result = arrayfunc.aall('>', datax, self.compval, nosimd=True)
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
			result = arrayfunc.aall('>', datax, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_aany:
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
		self.funcname = 'aany'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in itertools.chain(itertools.repeat(0, ARRAYSIZE // 2), itertools.repeat(10, ARRAYSIZE // 2))]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in itertools.chain(itertools.repeat(0, ARRAYSIZE // 2), itertools.repeat(10, ARRAYSIZE // 2))]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(50)
		else:
			self.compval =  int(50)

		
		# Used for compress.
		if 'aany' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = any(datax)
		else:
			for x in range(self.pyitercounts):
				result = any(datax)

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
			result = arrayfunc.aany('>', datax, self.compval, nosimd=True)
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
			result = arrayfunc.aany('>', datax, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_afilter:
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
		self.funcname = 'afilter'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [10]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [10]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(5)
		else:
			self.compval =  int(5)

		
		# Used for compress.
		if 'afilter' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = array.array(arraycode, filter(lambda x: x < self.compval, datax))
		else:
			for x in range(self.pyitercounts):
				result = array.array(arraycode, filter(lambda x: x < self.compval, datax))

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
			result = arrayfunc.afilter('<', datax, datay, self.compval)
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
			result = arrayfunc.afilter('<', datax, datay, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_amax:
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
		self.funcname = 'amax'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in list(range(128))]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in list(range(128))]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(5)
		else:
			self.compval =  int(5)

		
		# Used for compress.
		if 'amax' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = max(datax)
		else:
			for x in range(self.pyitercounts):
				result = max(datax)

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
			result = arrayfunc.amax(datax, nosimd=True)
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
			result = arrayfunc.amax(datax)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_amin:
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
		self.funcname = 'amin'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in list(range(128))]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in list(range(128))]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(5)
		else:
			self.compval =  int(5)

		
		# Used for compress.
		if 'amin' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = min(datax)
		else:
			for x in range(self.pyitercounts):
				result = min(datax)

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
			result = arrayfunc.amin(datax, nosimd=True)
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
			result = arrayfunc.amin(datax)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_asum:
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
		self.funcname = 'asum'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'asum' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = sum(datax)
		else:
			for x in range(self.pyitercounts):
				result = sum(datax)

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
			result = arrayfunc.asum(datax, nosimd=True)
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
			result = arrayfunc.asum(datax, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_compress:
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
		self.funcname = 'compress'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'compress' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout = array.array(arraycode, itertools.compress(datax, self.pycomp))
		else:
			for x in range(self.pyitercounts):
				dataout = array.array(arraycode, itertools.compress(datax, self.pycomp))

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
			result = arrayfunc.compress(self.pycomp, dataout, self.compdata)
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
			result = arrayfunc.compress(self.pycomp, dataout, self.compdata)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_count:
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
		self.funcname = 'count'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'count' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = pycount(arraycode, self.pyitercounts, datax)
		else:
			for x in range(self.pyitercounts):
				result = pycount(arraycode, self.pyitercounts, datax)

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
			arrayfunc.count(datax, self.compval)
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
			arrayfunc.count(datax, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_cycle:
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
		self.funcname = 'cycle'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'cycle' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = array.array(arraycode, [x for x,y in zip(itertools.cycle([1, 2, 3, 4]), itertools.repeat(0, ARRAYSIZE))])
		else:
			for x in range(self.pyitercounts):
				result = array.array(arraycode, [x for x,y in zip(itertools.cycle([1, 2, 3, 4]), itertools.repeat(0, ARRAYSIZE))])

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
			arrayfunc.cycle(datax, self.startcycle, self.endcycle)
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
			arrayfunc.cycle(datax, self.startcycle, self.endcycle)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_dropwhile:
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
		self.funcname = 'dropwhile'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(10)
		else:
			self.compval =  int(10)

		
		# Used for compress.
		if 'dropwhile' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout = array.array(arraycode, itertools.dropwhile(lambda x : x < self.compval, datax))
		else:
			for x in range(self.pyitercounts):
				dataout = array.array(arraycode, itertools.dropwhile(lambda x : x < self.compval, datax))

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
			result = arrayfunc.dropwhile('<', datax, dataout, self.compval)
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
			result = arrayfunc.dropwhile('<', datax, dataout, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_findindex:
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
		self.funcname = 'findindex'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(10)
		else:
			self.compval =  int(10)

		
		# Used for compress.
		if 'findindex' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = pyfindindex(datax, self.compval)
		else:
			for x in range(self.pyitercounts):
				result = pyfindindex(datax, self.compval)

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
			result = arrayfunc.findindex('==', self.datax, self.compval, nosimd=True)
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
			result = arrayfunc.findindex('==', self.datax, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_findindices:
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
		self.funcname = 'findindices'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('fidataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('fidataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('fidataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(10)
		else:
			self.compval =  int(10)

		
		# Used for compress.
		if 'findindices' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('fidataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = pyfindindices(self.datax, self.fidataout, self.compval)
		else:
			for x in range(self.pyitercounts):
				result = pyfindindices(self.datax, self.fidataout, self.compval)

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
			result = arrayfunc.findindices('==', datax, self.fidataout, self.compval)
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
			result = arrayfunc.findindices('==', datax, self.fidataout, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_repeat:
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
		self.funcname = 'repeat'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(10)
		else:
			self.compval =  int(10)

		
		# Used for compress.
		if 'repeat' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					datax = array.array(arraycode, itertools.repeat(self.compval, ARRAYSIZE))
		else:
			for x in range(self.pyitercounts):
				datax = array.array(arraycode, itertools.repeat(self.compval, ARRAYSIZE))

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
			arrayfunc.repeat(datax, self.compval)
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
			arrayfunc.repeat(datax, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_takewhile:
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
		self.funcname = 'takewhile'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0]]
			ydata = [float(x) for x in [0]]
			zdata = [float(x) for x in [0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0]]
			ydata = [int(x) for x in [0]]
			zdata = [int(x) for x in [0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(10)
		else:
			self.compval =  int(10)

		
		# Used for compress.
		if 'takewhile' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if False:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout = array.array(arraycode, itertools.takewhile(lambda x : x < self.compval, datax))
		else:
			for x in range(self.pyitercounts):
				dataout = array.array(arraycode, itertools.takewhile(lambda x : x < self.compval, datax))

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
			result = arrayfunc.takewhile('<', datax, dataout, self.compval)
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
			result = arrayfunc.takewhile('<', datax, dataout, self.compval)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


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
		self.needsydatafix = True



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [float(x) for x in [-25,-1,0,1,25]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [int(x) for x in [-25,-1,0,1,25]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'add' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
			arrayfunc.add(datax, datay, dataout)
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
			arrayfunc.add(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_truediv:
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
		self.funcname = 'truediv'
		self.runtimetarget = 0.1
		self.needsydatafix = True



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [float(x) for x in [-3,-2,-1,1,2,3,4]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [int(x) for x in [-3,-2,-1,1,2,3,4]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'truediv' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = truediv_type(datax[i] / datay[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = truediv_type(datax[i] / datay[i])

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
			arrayfunc.truediv(datax, datay, dataout)
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
			arrayfunc.truediv(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_floordiv:
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
		self.funcname = 'floordiv'
		self.runtimetarget = 0.1
		self.needsydatafix = True



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [float(x) for x in [-3,-2,-1,1,2,3,4]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [int(x) for x in [-3,-2,-1,1,2,3,4]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'floordiv' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] // datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] // datay[i]

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
			arrayfunc.floordiv(datax, datay, dataout)
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
			arrayfunc.floordiv(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_mod:
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
		self.funcname = 'mod'
		self.runtimetarget = 0.1
		self.needsydatafix = True



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [float(x) for x in [-2,-1,1,2]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [int(x) for x in [-2,-1,1,2]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'mod' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] % datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] % datay[i]

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
			arrayfunc.mod(datax, datay, dataout)
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
			arrayfunc.mod(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_mul:
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
		self.funcname = 'mul'
		self.runtimetarget = 0.1
		self.needsydatafix = True



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [float(x) for x in [-3,-2,-1,0,1,2,3]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [int(x) for x in [-3,-2,-1,0,1,2,3]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'mul' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] * datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] * datay[i]

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
			arrayfunc.mul(datax, datay, dataout)
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
			arrayfunc.mul(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_neg:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'h', 'i', 'l', 'q', 'f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'neg'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [-5,-4,-3,-2,-1,0,1,2,3,4,5]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [-5,-4,-3,-2,-1,0,1,2,3,4,5]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'neg' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = -(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = -(datax[i])

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
			arrayfunc.neg(datax, dataout)
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
			arrayfunc.neg(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_pow:
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
		self.funcname = 'pow'
		self.runtimetarget = 0.1
		self.needsydatafix = True



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [float(x) for x in [0,1,2]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [int(x) for x in [0,1,2]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'pow' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] ** datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] ** datay[i]

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
			arrayfunc.pow(datax, datay, dataout)
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
			arrayfunc.pow(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_sub:
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
		self.funcname = 'sub'
		self.runtimetarget = 0.1
		self.needsydatafix = True



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [float(x) for x in [-2,-1,0,1,2]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [int(x) for x in [-2,-1,0,1,2]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'sub' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] - datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] - datay[i]

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
			arrayfunc.sub(datax, datay, dataout)
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
			arrayfunc.sub(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_and_:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'and_'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [float(x) for x in [0,1,2,3,4,5]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [int(x) for x in [0,1,2,3,4,5]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'and_' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] & datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] & datay[i]

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
			arrayfunc.and_(datax, datay, dataout)
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
			arrayfunc.and_(datax, yvalue, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_or_:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'or_'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [float(x) for x in [0,1,2,3,4,5]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [int(x) for x in [0,1,2,3,4,5]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'or_' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] | datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] | datay[i]

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
			arrayfunc.or_(datax, datay, dataout)
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
			arrayfunc.or_(datax, yvalue, dataout)
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
		self.InitResults()
		self.funcname = 'xor'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [float(x) for x in [0,1,2,3,4,5]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [int(x) for x in [0,1,2,3,4,5]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'xor' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] ^ datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] ^ datay[i]

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
			arrayfunc.xor(datax, datay, dataout)
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
			arrayfunc.xor(datax, yvalue, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_invert:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'invert'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1,2,3,4,5,6,7,8,9,10]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1,2,3,4,5,6,7,8,9,10]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'invert' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = invertop(datax[i], invertmaxval)
		else:
			for x in range(self.pyitercounts):
				dataout[i] = invertop(datax[i], invertmaxval)

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
			arrayfunc.invert(datax, dataout)
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
			arrayfunc.invert(datax, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_eq:
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
		self.funcname = 'eq'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			ydata = [float(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			ydata = [int(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'eq' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = datax[i] == datay[i]
		else:
			for x in range(self.pyitercounts):
				result = datax[i] == datay[i]

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
			result = arrayfunc.eq(datax, datay)
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
			result = arrayfunc.eq(datax, yvalue)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_gt:
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
		self.funcname = 'gt'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			ydata = [float(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			ydata = [int(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'gt' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = datax[i] > datay[i]
		else:
			for x in range(self.pyitercounts):
				result = datax[i] > datay[i]

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
			result = arrayfunc.gt(datax, datay)
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
			result = arrayfunc.gt(datax, yvalue)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_ge:
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
		self.funcname = 'ge'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			ydata = [float(x) for x in [6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			ydata = [int(x) for x in [6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'ge' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = datax[i] >= datay[i]
		else:
			for x in range(self.pyitercounts):
				result = datax[i] >= datay[i]

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
			result = arrayfunc.ge(datax, datay)
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
			result = arrayfunc.ge(datax, yvalue)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_lt:
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
		self.funcname = 'lt'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			ydata = [float(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			ydata = [int(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'lt' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = datax[i] < datay[i]
		else:
			for x in range(self.pyitercounts):
				result = datax[i] < datay[i]

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
			result = arrayfunc.lt(datax, datay)
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
			result = arrayfunc.lt(datax, yvalue)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_le:
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
		self.funcname = 'le'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5]]
			ydata = [float(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5]]
			ydata = [int(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'le' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = datax[i] <= datay[i]
		else:
			for x in range(self.pyitercounts):
				result = datax[i] <= datay[i]

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
			result = arrayfunc.le(datax, datay)
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
			result = arrayfunc.le(datax, yvalue)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_ne:
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
		self.funcname = 'ne'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			ydata = [float(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
			ydata = [int(x) for x in [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'ne' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = datax[i] != datay[i]
		else:
			for x in range(self.pyitercounts):
				result = datax[i] != datay[i]

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
			result = arrayfunc.ne(datax, datay)
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
			result = arrayfunc.ne(datax, yvalue)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_lshift:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'lshift'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [float(x) for x in [0, 1, 2]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5,6,7,8,9]]
			ydata = [int(x) for x in [0, 1, 2]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'lshift' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] << datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] << datay[i]

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
			arrayfunc.lshift(datax, datay, dataout)
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
			arrayfunc.lshift(datax, yvalue, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_rshift:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'rshift'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [float(x) for x in [0, 1, 2]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100,101,102,103,104,105,106,107,108,109]]
			ydata = [int(x) for x in [0, 1, 2]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'rshift' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] >> datay[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] >> datay[i]

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
			arrayfunc.rshift(datax, datay, dataout)
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
			arrayfunc.rshift(datax, yvalue, dataout)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_abs_:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'h', 'i', 'l', 'q', 'f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'abs_'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [-5,-4,-3,-2,-1,0,1,2,3,4,5]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [-5,-4,-3,-2,-1,0,1,2,3,4,5]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'abs_' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = abs(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = abs(datax[i])

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
			arrayfunc.abs_(datax, dataout)
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
			arrayfunc.abs_(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_acos:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'acos'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'acos' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.acos(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.acos(datax[i])

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
			arrayfunc.acos(datax, dataout)
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
			arrayfunc.acos(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_acosh:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'acosh'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'acosh' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.acosh(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.acosh(datax[i])

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
			arrayfunc.acosh(datax, dataout)
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
			arrayfunc.acosh(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_asin:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'asin'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'asin' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.asin(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.asin(datax[i])

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
			arrayfunc.asin(datax, dataout)
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
			arrayfunc.asin(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_asinh:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'asinh'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'asinh' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.asinh(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.asinh(datax[i])

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
			arrayfunc.asinh(datax, dataout)
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
			arrayfunc.asinh(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_atan:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'atan'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'atan' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.atan(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.atan(datax[i])

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
			arrayfunc.atan(datax, dataout)
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
			arrayfunc.atan(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_atan2:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'atan2'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in [-2.0, -1.0, 0.0, 1.0, 2.0]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in [-2.0, -1.0, 0.0, 1.0, 2.0]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'atan2' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.atan2(datax[i], datay[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.atan2(datax[i], datay[i])

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
			arrayfunc.atan2(datax, datay, dataout)
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
			arrayfunc.atan2(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_atanh:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'atanh'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'atanh' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.atanh(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.atanh(datax[i])

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
			arrayfunc.atanh(datax, dataout)
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
			arrayfunc.atanh(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_ceil:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'ceil'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'ceil' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.ceil(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.ceil(datax[i])

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
			arrayfunc.ceil(datax, dataout)
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
			arrayfunc.ceil(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_copysign:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'copysign'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in [-3.0, -1.0, 0.0, 1.0, 3.0]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in [-3.0, -1.0, 0.0, 1.0, 3.0]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'copysign' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.copysign(datax[i], datay[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.copysign(datax[i], datay[i])

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
			arrayfunc.copysign(datax, datay, dataout)
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
			arrayfunc.copysign(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_cos:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'cos'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'cos' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.cos(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.cos(datax[i])

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
			arrayfunc.cos(datax, dataout)
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
			arrayfunc.cos(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_cosh:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'cosh'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'cosh' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.cosh(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.cosh(datax[i])

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
			arrayfunc.cosh(datax, dataout)
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
			arrayfunc.cosh(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_degrees:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'degrees'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'degrees' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.degrees(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.degrees(datax[i])

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
			arrayfunc.degrees(datax, dataout)
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
			arrayfunc.degrees(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_erf:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'erf'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'erf' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.erf(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.erf(datax[i])

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
			arrayfunc.erf(datax, dataout)
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
			arrayfunc.erf(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_erfc:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'erfc'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'erfc' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.erfc(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.erfc(datax[i])

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
			arrayfunc.erfc(datax, dataout)
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
			arrayfunc.erfc(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_exp:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'exp'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'exp' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.exp(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.exp(datax[i])

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
			arrayfunc.exp(datax, dataout)
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
			arrayfunc.exp(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_expm1:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'expm1'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'expm1' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.expm1(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.expm1(datax[i])

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
			arrayfunc.expm1(datax, dataout)
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
			arrayfunc.expm1(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_fabs:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'fabs'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'fabs' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.fabs(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.fabs(datax[i])

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
			arrayfunc.fabs(datax, dataout)
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
			arrayfunc.fabs(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_factorial:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'factorial'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0,1,2,3,4,5]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0,1,2,3,4,5]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'factorial' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.factorial(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.factorial(datax[i])

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
			arrayfunc.factorial(datax, dataout)
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
			arrayfunc.factorial(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_floor:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'floor'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'floor' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.floor(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.floor(datax[i])

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
			arrayfunc.floor(datax, dataout)
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
			arrayfunc.floor(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_fma:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'fma'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in [-2.0, -1.0, 1.0, 2.0]]
			zdata = [float(x) for x in [-2.0, -1.0, 1.0, 2.0]]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in [-2.0, -1.0, 1.0, 2.0]]
			zdata = [int(x) for x in [-2.0, -1.0, 1.0, 2.0]]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay', 'dataz'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay', 'dataz'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay', 'dataz'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'fma' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay', 'dataz'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = datax[i] * datay[i] + dataz[i]
		else:
			for x in range(self.pyitercounts):
				dataout[i] = datax[i] * datay[i] + dataz[i]

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
			arrayfunc.fma(datax, datay, dataz, dataout)
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
			arrayfunc.fma(datax, datay, dataz, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_fmod:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'fmod'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]]
			ydata = [float(x) for x in [-2.0, -1.0, 1.0, 2.0]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0]]
			ydata = [int(x) for x in [-2.0, -1.0, 1.0, 2.0]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'fmod' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.fmod(datax[i], datay[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.fmod(datax[i], datay[i])

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
			arrayfunc.fmod(datax, datay, dataout)
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
			arrayfunc.fmod(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_gamma:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'gamma'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'gamma' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.gamma(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.gamma(datax[i])

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
			arrayfunc.gamma(datax, dataout)
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
			arrayfunc.gamma(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_hypot:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'hypot'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in [-2.0, -1.0, 0.0, 1.0, 2.0]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in [-2.0, -1.0, 0.0, 1.0, 2.0]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout', 'datay'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout', 'datay'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout', 'datay'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'hypot' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout', 'datay'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.hypot(datax[i], datay[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.hypot(datax[i], datay[i])

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
			arrayfunc.hypot(datax, datay, dataout)
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
			arrayfunc.hypot(datax, yvalue, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_isfinite:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'isfinite'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'isfinite' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = math.isfinite(datax[i])
		else:
			for x in range(self.pyitercounts):
				result = math.isfinite(datax[i])

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
			result = arrayfunc.isfinite(datax)
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
			result = arrayfunc.isfinite(datax)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_isinf:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'isinf'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'isinf' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = math.isinf(datax[i])
		else:
			for x in range(self.pyitercounts):
				result = math.isinf(datax[i])

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
			result = arrayfunc.isinf(datax)
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
			result = arrayfunc.isinf(datax)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_isnan:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'isnan'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ():
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ():
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ():
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'isnan' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ():
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					result = math.isnan(datax[i])
		else:
			for x in range(self.pyitercounts):
				result = math.isnan(datax[i])

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
			result = arrayfunc.isnan(datax)
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
			result = arrayfunc.isnan(datax)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_ldexp:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'ldexp'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in [-2, -1, 0, 1, 2]]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in [-2, -1, 0, 1, 2]]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'ldexp' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.ldexp(datax[i], ldexp_y)
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.ldexp(datax[i], ldexp_y)

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
			arrayfunc.ldexp(datax, ldexp_y, dataout)
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
			arrayfunc.ldexp(datax, ldexp_y, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_lgamma:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'lgamma'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'lgamma' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.lgamma(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.lgamma(datax[i])

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
			arrayfunc.lgamma(datax, dataout)
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
			arrayfunc.lgamma(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_log:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'log'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'log' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.log(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.log(datax[i])

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
			arrayfunc.log(datax, dataout)
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
			arrayfunc.log(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_log10:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'log10'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'log10' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.log10(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.log10(datax[i])

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
			arrayfunc.log10(datax, dataout)
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
			arrayfunc.log10(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_log1p:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'log1p'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'log1p' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.log1p(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.log1p(datax[i])

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
			arrayfunc.log1p(datax, dataout)
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
			arrayfunc.log1p(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_log2:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'log2'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'log2' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.log2(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.log2(datax[i])

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
			arrayfunc.log2(datax, dataout)
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
			arrayfunc.log2(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_radians:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'radians'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'radians' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.radians(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.radians(datax[i])

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
			arrayfunc.radians(datax, dataout)
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
			arrayfunc.radians(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_sin:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'sin'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'sin' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.sin(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.sin(datax[i])

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
			arrayfunc.sin(datax, dataout)
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
			arrayfunc.sin(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_sinh:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'sinh'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'sinh' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.sinh(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.sinh(datax[i])

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
			arrayfunc.sinh(datax, dataout)
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
			arrayfunc.sinh(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_sqrt:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'sqrt'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'sqrt' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.sqrt(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.sqrt(datax[i])

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
			arrayfunc.sqrt(datax, dataout)
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
			arrayfunc.sqrt(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_tan:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'tan'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'tan' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.tan(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.tan(datax[i])

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
			arrayfunc.tan(datax, dataout)
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
			arrayfunc.tan(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_tanh:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'tanh'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'tanh' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.tanh(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.tanh(datax[i])

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
			arrayfunc.tanh(datax, dataout)
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
			arrayfunc.tanh(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################

##############################################################################
class benchmark_trunc:
	"""Benchmark a math function.
	"""

	########################################################
	def __init__(self):
		"""Initialise.
		"""
		self.supportedarrays = ('f', 'd')
		self.pyitercounts = 1
		self.afitercounts = 1
		self.InitResults()
		self.funcname = 'trunc'
		self.runtimetarget = 0.1
		self.needsydatafix = False



	########################################################
	def InitDataArrays(self, arraycode):
		"""Initialise the data arrays used to run the tests.
		"""
		# Ensure the data is in the right format for the array type.
		if arraycode in ('f', 'd'):
			xdata = [float(x) for x in [0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]]
			ydata = [float(x) for x in []]
			zdata = [float(x) for x in []]
			self.truediv_type = float
		else:
			xdata = [int(x) for x in [0.0,2.4,4.8,7.2,9.6,12.0,14.4,16.8,19.2,21.6]]
			ydata = [int(x) for x in []]
			zdata = [int(x) for x in []]
			self.truediv_type = int


		# Some operations have negative test data which must be fixed up for
		# unsigned integer arrays.
		if self.needsydatafix and (arraycode in ('B', 'H', 'I', 'L', 'Q')):
			ydata = [abs(x) for x in ydata]

		self.datax = array.array(arraycode, (x for x,y in zip(itertools.cycle(xdata), itertools.repeat(0, ARRAYSIZE))))
		assert len(self.datax) == ARRAYSIZE, 'self.datax is not expected length %d' % len(self.datax)

		self.arraylength = len(self.datax)

		# Not all functions have y data. Avoiding allocating unused arrays 
		# saves time when running the benchmark.
		if 'datay' in ('dataout'):
			self.datay = array.array(arraycode, (x for x,y in zip(itertools.cycle(ydata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.datay) == ARRAYSIZE, 'self.datay is not expected length %d' % len(self.datay)
		else:
			self.datay = None


		# As with above, not all functions have z data. Avoiding allocating 
		# unused arrays saves time when running the benchmark.
		if 'dataz' in ('dataout'):
			self.dataz = array.array(arraycode, (x for x,y in zip(itertools.cycle(zdata), itertools.repeat(0, ARRAYSIZE))))
			assert len(self.dataz) == ARRAYSIZE, 'self.dataz is not expected length %d' % len(self.dataz)
		else:
			self.dataz = None


		if 'dataout' in ('dataout'):
			self.dataout = array.array(arraycode, itertools.repeat(0, self.arraylength))
			assert len(self.dataout) == ARRAYSIZE, 'self.dataout is not expected length %d' % len(self.dataout)
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
			self.compval =  float(0)
		else:
			self.compval =  int(0)

		
		# Used for compress.
		if 'trunc' == 'compress':
			self.compdata = array.array(arraycode, [1,0,1,0])
			self.pycomp = array.array(arraycode, (x for x,y in zip(itertools.cycle(self.compdata), itertools.repeat(0, ARRAYSIZE))))

		# Used for cycle.
		self.startcycle = comptype(arraycode, 0)
		self.endcycle = comptype(arraycode, 127)


		# Used for findindices.
		if 'fidataout' in ('dataout'):
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


		self.PyResults = ''
		self.AfResults = ''
		self.RelativeResults = ''

		self.PyResultsFast = ''
		self.AfResultsFast = ''
		self.RelativeResultsFast = ''
		self.RelSIMD = ''


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


	##############################################################################
	def simdcalc(self, arraycode, afval, affastval):
		"""This is used to calculate and format the relative SIMD performance.
		"""
		if not SIMDFuncs[self.funcname][arraycode]:
			calcval = None
		else:
			calcval = afval/affastval
		
		return self.fmtreldata(calcval)


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

		# Calculate and format the results comparing the non-SIMD and SIMD results
		# for functions with SIMD support.
		if self.funcname in SIMDFuncs:
			self.RelSIMD = fname + ' '.join([self.simdcalc(x, self.AfData[x], self.AfDataFast[x]) for x in arraycodes])


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
		if True:
			for x in range(self.pyitercounts):
				for i in range(self.arraylength):
					dataout[i] = math.trunc(datax[i])
		else:
			for x in range(self.pyitercounts):
				dataout[i] = math.trunc(datax[i])

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
			arrayfunc.trunc(datax, dataout)
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
			arrayfunc.trunc(datax, dataout, matherrors=True)
		endtime = time.perf_counter()

		aftime = (endtime - starttime) / self.afitercounts

		return aftime


##############################################################################


BenchClasses = [(benchmark_aall, 'aall'), (benchmark_aany, 'aany'), (benchmark_afilter, 'afilter'), (benchmark_amax, 'amax'), (benchmark_amin, 'amin'), (benchmark_asum, 'asum'), (benchmark_compress, 'compress'), (benchmark_count, 'count'), (benchmark_cycle, 'cycle'), (benchmark_dropwhile, 'dropwhile'), (benchmark_findindex, 'findindex'), (benchmark_findindices, 'findindices'), (benchmark_repeat, 'repeat'), (benchmark_takewhile, 'takewhile'), (benchmark_add, 'add'), (benchmark_truediv, 'truediv'), (benchmark_floordiv, 'floordiv'), (benchmark_mod, 'mod'), (benchmark_mul, 'mul'), (benchmark_neg, 'neg'), (benchmark_pow, 'pow'), (benchmark_sub, 'sub'), (benchmark_and_, 'and_'), (benchmark_or_, 'or_'), (benchmark_xor, 'xor'), (benchmark_invert, 'invert'), (benchmark_eq, 'eq'), (benchmark_gt, 'gt'), (benchmark_ge, 'ge'), (benchmark_lt, 'lt'), (benchmark_le, 'le'), (benchmark_ne, 'ne'), (benchmark_lshift, 'lshift'), (benchmark_rshift, 'rshift'), (benchmark_abs_, 'abs_'), (benchmark_acos, 'acos'), (benchmark_acosh, 'acosh'), (benchmark_asin, 'asin'), (benchmark_asinh, 'asinh'), (benchmark_atan, 'atan'), (benchmark_atan2, 'atan2'), (benchmark_atanh, 'atanh'), (benchmark_ceil, 'ceil'), (benchmark_copysign, 'copysign'), (benchmark_cos, 'cos'), (benchmark_cosh, 'cosh'), (benchmark_degrees, 'degrees'), (benchmark_erf, 'erf'), (benchmark_erfc, 'erfc'), (benchmark_exp, 'exp'), (benchmark_expm1, 'expm1'), (benchmark_fabs, 'fabs'), (benchmark_factorial, 'factorial'), (benchmark_floor, 'floor'), (benchmark_fma, 'fma'), (benchmark_fmod, 'fmod'), (benchmark_gamma, 'gamma'), (benchmark_hypot, 'hypot'), (benchmark_isfinite, 'isfinite'), (benchmark_isinf, 'isinf'), (benchmark_isnan, 'isnan'), (benchmark_ldexp, 'ldexp'), (benchmark_lgamma, 'lgamma'), (benchmark_log, 'log'), (benchmark_log10, 'log10'), (benchmark_log1p, 'log1p'), (benchmark_log2, 'log2'), (benchmark_radians, 'radians'), (benchmark_sin, 'sin'), (benchmark_sinh, 'sinh'), (benchmark_sqrt, 'sqrt'), (benchmark_tan, 'tan'), (benchmark_tanh, 'tanh'), (benchmark_trunc, 'trunc')]

arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']

TestLabels = [y for x,y in BenchClasses]



##############################################################################

# Create the table header.
def FormatHeaderLabels(columnwidth):
	"""Return a string containing the table header labels.
	"""
	return ('function'.center(FCOLWIDTH)) + ' '.join([x.center(columnwidth) for x in arraycodes]) + '\n'


def FormatTableSep(columnwidth):
	"""Return a string containing the table separator.
	"""
	return '=' * FCOLWIDTH + ' ' + ' '.join(['=' * columnwidth] * len(arraycodes)) + '\n'


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

PyResults = []
FuncResults = []
RelativeResults = []
RelativeResultsFast = []
numstats = []
numstatsfast = []
SIMDResults = []

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
	SIMDResults.append(bc.RelSIMD)

	numstats.extend(bc.relativetime)
	numstatsfast.extend(bc.relativetimefast)


	CalDataPy[funcname] = sum(bc.pythontime) / len(bc.pythontime)
	CalDataAF[funcname] = sum(bc.aftime) / len(bc.aftime)


##############################################################################

# Print the results

with open('benchmarkdata.txt', 'w') as f:

	f.write(time.ctime() + '\n')

	WritePlatformSignature(f)


	##########################################################################

	# The relative performance stats in default configuration.

	f.write('Relative Performance - Python Time / Arrayfunc Time.\n')
	f.write(FormatTableSep(5))
	f.write(FormatHeaderLabels(5))
	f.write(FormatTableSep(5))
	
	f.write('\n'.join(RelativeResults) + '\n')

	f.write(FormatTableSep(5))

	avgval = sum(numstats) / len(numstats)
	maxval = max(numstats)
	minval = min(numstats)


	f.write('\n\n\n')
	f.write('=========== ========\n')
	f.write('Stat         Value\n')
	f.write('=========== ========\n')
	f.write('Average:    %0.0f\n' % avgval)
	f.write('Maximum:    %0.0f\n' % maxval)
	f.write('Minimum:    %0.1f\n' % minval)
	f.write('Array size: %d\n' % ARRAYSIZE)
	f.write('=========== ========\n')

	##########################################################################

	f.write('\n\n\n')


	# The relative performance stats in optimised configuration.

	f.write('Relative Performance with Optimisations - Python Time / Arrayfunc Time.\n')
	f.write(FormatTableSep(5))
	f.write(FormatHeaderLabels(5))
	f.write(FormatTableSep(5))
	
	f.write('\n'.join(RelativeResultsFast) + '\n')

	f.write(FormatTableSep(5))


	avgvalfast = sum(numstatsfast) / len(numstatsfast)
	maxvalfast = max(numstatsfast)
	minvalfast = min(numstatsfast)


	f.write('\n\n\n')
	f.write('=========== ========\n')
	f.write('Stat         Value\n')
	f.write('=========== ========\n')
	f.write('Average:    %0.0f\n' % avgvalfast)
	f.write('Maximum:    %0.0f\n' % maxvalfast)
	f.write('Minimum:    %0.1f\n' % minvalfast)
	f.write('Array size: %d\n' % ARRAYSIZE)
	f.write('=========== ========\n')


	##########################################################################

	f.write('\n\n\n')

	f.write('Relative Performance with and without SIMD Optimisations - Unoptimsed / Optimised Time.\n')
	f.write(FormatTableSep(5))
	f.write(FormatHeaderLabels(5))
	f.write(FormatTableSep(5))
	
	f.write('\n'.join([x for x in SIMDResults if x]) + '\n')

	f.write(FormatTableSep(5))


	##########################################################################

	f.write('\n\n\n')

	f.write('Python native time in micro-seconds.\n')
	f.write(FormatTableSep(8))
	f.write(FormatHeaderLabels(8))
	f.write(FormatTableSep(8))
	
	f.write('\n'.join(PyResults) + '\n')

	f.write(FormatTableSep(8))



	f.write('\n\nArrayfunc time in micro-seconds.\n')
	f.write(FormatTableSep(8))
	f.write(FormatHeaderLabels(8))
	f.write(FormatTableSep(8))
	
	f.write('\n'.join(FuncResults) + '\n')

	f.write(FormatTableSep(8))



##############################################################################

