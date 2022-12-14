#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_version.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.6
# Date:     09-Dec-2022.
# Ver:      12-Dec-2022.
#
###############################################################################
#
#   Copyright 2022    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for version.
"""

##############################################################################
import sys

import platform
import unittest
import subprocess


##############################################################################

# Define the differences here so that it's easy to convert the unit test
# to be used with different packages.

import arrayfunc
TestPkg = arrayfunc
PkgName = 'arrayfunc'
LogfileName = 'af_unittest.txt'


##############################################################################
# Get a PIP package version.
def getpkgversion(pkgname):
	'''Get the package version by calling pip.
	'''
	# The command name for pip3 or pip depends on the platform.
	systype = platform.system()
	if ('FreeBSD' in systype):
		pipcmd = 'pip'
	else:
		pipcmd = 'pip3'

	# We need the python version because distros which use older versions
	# of python require different options.
	pyvermajor, pyverminor, pyverpatch = platform.python_version_tuple()
	useold_subprocess = (int(pyvermajor) == 3) and (int(pyverminor) < 7)
	

	if not useold_subprocess:
		# The timeout must be long enough to avoid timing out on the Raspberry Pi 3.
		result = subprocess.run([pipcmd, 'show', pkgname], capture_output=True, timeout=10)
	else:
		# This is required for Python versions older than 3.7. At this time only Suse was a problem.
		result = subprocess.run([pipcmd, 'show', pkgname], stdout=subprocess.PIPE, timeout=10)
	stdout = result.stdout.decode('utf-8')

	resulttext = [x for x in stdout.split('\n') if 'Version:' in x]
	try:
		pkgversion = resulttext[0].split(':')[1].strip(' []\n\r')
	except:
		pkgversion = 'error'

	return pkgversion


##############################################################################
class VersionCheck(unittest.TestCase):
	"""Check the version numbers.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.pippkgversion = getpkgversion(PkgName)

	########################################################
	def test_version(self):
		"""Compare the version number from PIP to the __version__ attribute.
		"""
		# We access the package indirection through TestPkg to make it easier
		# to change which package we are using.
		pyinitversion = TestPkg.__version__
		self.assertEqual(self.pippkgversion, pyinitversion)


##############################################################################


##############################################################################
if __name__ == '__main__':

	# Check to see if the log file option has been selected. This is an option
	# which we have added in order to decide where to output the results.
	if '-l' in sys.argv:
		# Remove the option from the argument list so that "unittest" does 
		# not complain about unknown options.
		sys.argv.remove('-l')

		with open(LogfileName, 'a') as f:
			f.write('\n\n')
			f.write('version\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
