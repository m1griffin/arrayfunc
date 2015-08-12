#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate documentation from the configuration data.
# Language: Python 3.4
# Date:     24-Nov-2014
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

# This is the text which is used for the headings at the top and bottom of the table.

headerbar = '=============== ====================== ===== ===== === ===== ========= ====='

headertext1 = 'Name             Equivalent to          b h   B H   f   OV    Compare   Win'
headertext2 = '                                        i l   I L   d         Ops      '

topheader = '\n'.join([headerbar, headertext1, headertext2, headerbar])

# ==============================================================================

# Read in the data from the CSV spreadsheet which holds the configuration.
csvdata = codegen_common.ReadCSVData()


# The documentation for the opcodes.
tableformat = '%(opcodename)-16s %(opcodedocs)-23s %(bhil)-5s %(BHIL)-4s %(fd)-4s %(OV)-6s %(compare)-7s  %(msvs_has)s\n'
with open('docsopcodes.txt', 'w') as f:
	f.write(topheader)
	f.write('\n')
	for opcode in csvdata:
		docdata = {'opcodename' : opcode['opcodename'], 
		'opcodedocs' : opcode['opcodedocs'], 
		'bhil' : 'X' if opcode['c_code_template_i_signed'] != '' else '', 
		'BHIL' : 'X' if opcode['c_code_template_i_unsigned'] != '' else '', 
		'fd' : 'X' if opcode['c_code_template_float'] != '' else '', 
		'OV' : 'X' if (opcode['test_ovfl_templ_isigned'] != '') or opcode['test_ovfl_templ_iunsigned'] != '' else '', 
		'compare' : 'X' if opcode['compare_ops'] != '' else '',
		'msvs_has' : 'X' if opcode['msvs_has'] == '1' else ''}
		f.write(tableformat % docdata)

	f.write(headerbar)
	f.write('\n')

# ==============================================================================


