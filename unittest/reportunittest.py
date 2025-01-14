#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Provide a pass / fail summary of the unit test as well as data
#           about the test environment. It must be run *after* the unit test
#           is complete. See the comments for the required arguments.
# Language: Python 3.8 with work-arounds for older versions.
# Date:     06-Oct-2024
#
###############################################################################
#
#   Copyright 2017 - 2024   Michael Griffin    <m12.griffin@gmail.com>
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
import platform
import sys
import os
import configparser

# We use configparser in order to support older versions of Python
# which may not have a toml library in the standard library.

# Below in the program we try to import importlib.metadata to get the 
# package version. If we can't then we must pass the version to this 
# program as an opional argument.


##############################################################################

# The expected arguments are:
# 1 = The name of the package (e.g. arrayfunc).
# 2 = The source of the package (e.g. local, pypi).
# 3 = The file prefix. This is a short code used to distinguish between
#      instances of the test, generally named after the platform (E.g. Deb64).
# 4 = The name of the unittest file (e.g. af_unittest.txt). This is used for
#      finding the unit test results in order to summarize the pass/fail 
#      results.
# 5 = This is an optional argument, required for older Python versions which
#      do not support importlib.metadata. Where required it is the package
#      version number.

# ======================================================================

# The config file holding the pass / fail criteria.
unittestdataconfig = 'reportunittest.ini'

# ======================================================================

def GetArgs():

	# Get the command line parameters.
	if len(sys.argv) >= 5:
		pkgname = sys.argv[1]
		packsource = sys.argv[2]
		fileprefix = sys.argv[3]
		unittestname = sys.argv[4]
	else:
		print('Error - unitttestdata.py - Insufficient number of arguments.')
		pkgname = ''
		packsource = ''
		fileprefix = ''
		unittestname = ''

	return pkgname, packsource, fileprefix, unittestname

# ======================================================================
# How we get the package version depends on the version of Python being
# run. For older versions which do not support importlib.metadata this has
# to be passed in from the calling program as an optional argument.

def GetPkgVer():
	try:
		import importlib.metadata
		pkgver = importlib.metadata.version(pkgname)
	except:
		if len(sys.argv) >= 6:
			pkgver = sys.argv[5]
		else:
			pkgver = 'Error: Could not find specified package: %s' % pkgname

	return pkgver

# ======================================================================

# General status reporting. 

# Now print out the data we want. The calling program is responsible
# for capturing stdout and redirecting it where necessary.
def ReportStatus(pkgname, pkgver, packsource, fileprefix):
	print(time.strftime('%Y-%m-%d %H:%M:%S'))
	print()
	print("Package: %s" % pkgname)
	print("Package version: %s" % pkgver)
	print("Installed from: %s" % packsource)
	print("Test platform: %s" % fileprefix)
	print("Python Implementation: %s %s" % (platform.python_implementation(), platform.python_version()))
	print("Compiler: %s" % platform.python_compiler())
	print("OS System: %s" % platform.system())
	print("Platform: %s" % platform.platform())
	print("Machine: %s" % platform.machine())
	print()


# ======================================================================

# ======================================================================
# If we can't find the unit test data and pass / fail criteria config
# file then there's no point in going past this point.

def CheckDataFilesExist(unittestname, unittestdataconfig):
	# Check if the specified unit test file exists.
	if not os.path.exists(unittestname):
		print('error - unit test data file not found: %s' % unittestname)
		return False

	# Check if the specified unit test file exists.
	if not os.path.exists(unittestdataconfig):
		print('error - pass-fail config data file not found: %s' % unittestdataconfig)
		return False

	return True

# ======================================================================
# Determine the pass / fail status.

# This opens the file containing the unit test test results.
# This should be in the format used by the unittest module from the 
# standard library. 
def CountOKSkipped(unittestname):
	with open(unittestname, 'r') as utfile:
		# Read in the entire file so we can go over it multiple times.
		utdata = utfile.readlines()
		# Count up the number of 'OK' lines, representing passed tests.
		numok = len([x for x in utdata if x.startswith('OK')])
		# Count up the number of skipped OK tests. These are tests which
		# were supposed to be skipped, generally relating to platform support
		# limitations (e.g. 32 versus 64 bit).
		numskipped = len([x for x in utdata if x.startswith('OK (skipped')])

	return numok, numskipped

# ======================================================================

# Pass / fail criteria from a config file.
def GetPassFailConfig(unittestdataconfig):
	# Read in the config file which has the architecture dependent values.
	config = configparser.ConfigParser()

	try:
		config.read(unittestdataconfig)
	except:
		print('error - bad format in unittest config file: %s' % unittestdataconfig)
		sys.exit(1)

	# Are the values architecture dependent? If not, then there only
	# needs to be one "architecture" section, called 'allarch'.
	# The pass / fail criteria may be architecture dependent due to the way the
	# 'c' compilers define arrays.
	allarch = 'allarch'
	if allarch in config:
		testarch = allarch
	# Windows has a special architecture when it comes to arrays.
	elif platform.system() == 'Windows':
		testarch = 'Windows'
	else:
		testarch = platform.machine()

	# Get the pass / fail criteria for the specified architecture.
	# If the file format is incorrect we just provide some strings which
	# will end up being printed in place of the numbers, providing an error
	# indication message.
	if testarch in config:
		archvalues = config[testarch]
		val = archvalues.get('numok', None)
		try:
			numokexpected = int(val)
		except:
			numokexpected = 'error-not-found'

		val = archvalues.get('numskipped', 'error-not-found')
		try:
			numskippedexpected = int(val)
		except:
			numskippedexpected = 'error-not-found'
	else:
		numokexpected = 'Unknown architecture: %s' % testarch
		numskippedexpected = numokexpected

	return numokexpected, numskippedexpected

# ======================================================================

def PrintPassFail(numok, numskipped, numokexpected, numskippedexpected):
	# If the result was error strings instead of integers, then
	# the test will iherently fail.
	okresult = 'pass' if (numok == numokexpected) else 'fail'
	skippedresult = 'pass' if (numskipped == numskippedexpected) else 'fail'

	# The number of OK and skipped.
	print('Number of OK versus expected: %s / %s' % (numok, numokexpected))
	print('Number of skipped versus expected: %s / %s' % (numskipped, numskippedexpected))

	# WHether the OK and skipped numbers meet the expected criteria.
	print('OK result: %s' % okresult)
	print('Skipped result: %s' % skippedresult)

	# print a divider between the summary and the data.
	print()
	print('=' * 80)
	print()

# ======================================================================

# Get the arguments from the command line.
pkgname, packsource, fileprefix, unittestname = GetArgs()

# Get the package version. If the current version of Python does not
# support the required library, this may need to be passed in on the
# command line.
pkgver = GetPkgVer()

# Report basic test environment values.
ReportStatus(pkgname, pkgver, packsource, fileprefix)

# Check if the data files required to conduct pass / fail evaluations
# are present.
if not CheckDataFilesExist(unittestname, unittestdataconfig):
	sys.exit(1)

# Count up the number of OK and skipped tests.
numok, numskipped = CountOKSkipped(unittestname)

# Get the expected pass fail values from the config file.
numokexpected, numskippedexpected = GetPassFailConfig(unittestdataconfig)

# Print out a pass / fail summary.
PrintPassFail(numok, numskipped, numokexpected, numskippedexpected)

