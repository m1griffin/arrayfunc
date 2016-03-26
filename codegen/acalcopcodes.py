#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for the calc op code definitions.
# Language: Python 3.4
# Date:     04-Feb-2016
#
###############################################################################
#
#   Copyright 2014 - 2016    Michael Griffin    <m12.griffin@gmail.com>
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
csvdata = codegen_common.ReadCSVData('arraycalc.csv')

rectemplate = "\t\t\t'%s' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([%s, %s, %s, %s, %s, %s]),\n"

# ==============================================================================

# These are used to define the individual op codes.
cinttemplate = '#define CALCOP_INT_%s %s\n'
cfloattemplate = '#define CALCOP_FLOAT_%s %s\n'

# These are used to define arrays which are used in the C modules to validate
# the array stacks. These are expected to be -1, 0, or 1, with the array index
# corresponding to the array op code.
cintoptemplate = 'signed int intstackcodes[] = {'
cfloatoptemplate = 'signed int floatstackcodes[] = {'


# ==============================================================================


# Construct the definitions for both Python and C code.
pydefs = []
intdefs = []
floatdefs = []

# Construct tables to track the effects on the stack for static stack overflow
# checking.
intstack = []
floatstack = []


pydefs.append('\t\tself._OpCodes = {\n')

opcounterint = -1
opcounterfloat = -1
for opcode in csvdata:
	# Signed and unsigned integer.
	if opcode['c_operator_i'] != '':
		opcounterint += 1
		opvalueint = opcounterint
		intdefs.append(cinttemplate % (opcode['opcodename'].upper().replace('.', '_'), opcounterint))
		intstack.append(opcode['stack_effect'])
	else:
		opvalueint = None

	# Floating point. 
	if opcode['c_operator_d'] != '':
		opcounterfloat += 1
		opvaluefloat = opcounterfloat
		floatdefs.append(cfloattemplate % (opcode['opcodename'].upper().replace('.', '_'), opcounterfloat))
		floatstack.append(opcode['stack_effect'])
	else:
		opvaluefloat = None



	# This is a math library.
	matlib = opcode['lib_func'] == '1'
	# The effect on the stack.
	stackeffect = opcode['stack_effect']
	# Operation is for signed types only.
	signedonly = opcode['signed_only'] == '1'
	# This funciton is supported by Microsoft VC. 
	msvs_has = opcode['msvs_has'] == '1'
	pydefs.append(rectemplate % (opcode['opcodename'], opvalueint, signedonly, opvaluefloat, matlib, stackeffect, msvs_has))

pydefs.append('\t\t\t}\n')

intstacklen = len(intstack)
floatstacklen = len(floatstack)


with open('acalcopcodes.txt', 'w') as f:
	f.write(''.join(pydefs))

	f.write('\n\n\n')

	f.write(''.join(intdefs))

	f.write('\n\n\n')

	f.write(''.join(floatdefs))

	f.write('\n\n\n')

	f.write(cintoptemplate)
	f.write(', '.join(intstack))
	f.write('};\n\n\n')

	f.write(cfloatoptemplate)
	f.write(', '.join(floatstack))
	f.write('};\n\n')

	f.write('#define OPCODEMAXINT %i\n' % (intstacklen - 1))
	f.write('#define OPCODEMAXFLOAT %i\n' % (floatstacklen - 1))


# ==============================================================================

