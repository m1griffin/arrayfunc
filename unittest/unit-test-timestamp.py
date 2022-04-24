#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Run this before the unit tests to add in the time stamps.
# Language: Python 3.5
# Date:     26-Jun-2017
#
###############################################################################
#
#   Copyright 2017 - 2021   Michael Griffin    <m12.griffin@gmail.com>
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

##############################################################################

with open('af_unittest.txt', 'w') as f:
	f.write(time.strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
	# Copy the command line parameters. This is intended to be used to record
	# the type of test the unit test was conducted under.
	if len(sys.argv) >= 5:
		f.write("Package: %s\n" % sys.argv[1])
		f.write("Install from: %s\n" % sys.argv[2])
		f.write("Test platform: %s\n" % sys.argv[3])
		f.write("Package version: %s\n" % sys.argv[4])
	f.write("Python Implementation: %s %s\n" % (platform.python_implementation(), platform.python_version()))
	f.write("Compiler: %s\n" % platform.python_compiler())
	f.write("OS System: %s\n" % platform.system())
	f.write("Platform: %s\n" % platform.platform())
	f.write("Machine: %s\n\n" % platform.machine())

