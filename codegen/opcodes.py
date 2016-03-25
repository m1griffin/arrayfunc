#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for the op code definitions.
# Language: Python 3.4
# Date:     25-May-2014
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

# ==============================================================================

import codegen_common

# ==============================================================================



# Read in the data from the CSV spreadsheet which holds the configuration.
csvdata = codegen_common.ReadCSVData('arrayfunc.csv')

# The constant definitions for the opcodes.
with open('defblock.txt', 'w') as f:
	for opcode in csvdata:
		f.write('#define OP_%s %s\n' % (opcode['opcodename'].upper(), opcode['opcode']))

# ==============================================================================

# The named tuple defining the op code names.
with open('opcodes.txt', 'w') as f:

	f.write("aops = collections.namedtuple('aops', [\n")

	# Op code names.
	columncount = 0
	for opcode in csvdata:
		f.write("'%s', " % opcode['opcodename'])
		columncount +=1
		if columncount > 4:
			f.write('\n')
			columncount = 0

	f.write('])._make([\n')

	# Op code integers.
	columncount = 0
	for opcode in csvdata:
		f.write('%s, ' % opcode['opcode'])
		columncount +=1
		if columncount > 4:
			f.write('\n')
			columncount = 0

	f.write('])\n')

# ==============================================================================



