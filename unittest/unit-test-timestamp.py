#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Run this before the unit tests to add in the time stamps.
# Language: Python 3.5
# Date:     26-Jun-2017
#
###############################################################################
#
#   Copyright 2017 - 2020   Michael Griffin    <m12.griffin@gmail.com>
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
	f.write(time.ctime() + '\n\n')
	# Copy the command line parameters. This is intended to be used to record
	# the type of test the unit test was conducted under.
	f.write(' '.join(sys.argv[1:]) + '\n')
	f.write('%s %s\n' % (platform.python_implementation(), platform.python_version()))
	f.write(platform.python_compiler() + '\n')
	f.write(platform.system() + '\n')
	f.write(platform.platform() + '\n')
	f.write(platform.machine() + '\n\n')

