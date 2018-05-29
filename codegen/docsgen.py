#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate documentation from the configuration data.
# Language: Python 3.4
# Date:     24-Nov-2014
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

import glob
import os.path
import itertools

import codegen_common

# ==============================================================================

# This is the text which is used for the headings at the top and bottom of the table.

headerbar = '=============== ====================== ===== ===== === ====='

headertext1 = 'Name             Equivalent to          b h   B H   f   OV '
headertext2 = '                                        i l   I L   d      '

topheader = '\n'.join([headerbar, headertext1, headertext2, headerbar])


headerbarcomp = headerbar + ' ========='

headertextcomp1 = headertext1 + '    Compare'
headertextcomp2 = headertext2 + '    Ops    '

topheadercomp = '\n'.join([headerbarcomp, headertextcomp1, headertextcomp2, headerbarcomp])


# ==============================================================================
# TODO: Remove.
# Read in the data from the CSV spreadsheet which holds the configuration.
csvdata = codegen_common.ReadCSVData('arrayfunc.csv')

# ==============================================================================

def DocsOpcodes(outputfile):
	# The documentation for the opcodes.
	tableformat = '%(opcodename)-16s %(opcodedocs)-23s %(bhil)-5s %(BHIL)-4s %(fd)-4s %(OV)-6s %(compare)-7s\n'
	outputfile.write('Documents the op codes for amap and starmap.\n\n')
	outputfile.write(topheadercomp)
	outputfile.write('\n')
	for opcode in csvdata:
		docdata = {'opcodename' : opcode['opcodename'], 
		'opcodedocs' : opcode['opcodedocs'], 
		'bhil' : 'X' if opcode['c_code_template_i_signed'] != '' else '', 
		'BHIL' : 'X' if opcode['c_code_template_i_unsigned'] != '' else '', 
		'fd' : 'X' if opcode['c_code_template_float'] != '' else '', 
		'OV' : 'X' if (opcode['test_ovfl_templ_isigned'] != '') or opcode['test_ovfl_templ_iunsigned'] != '' else '', 
		'compare' : 'X' if opcode['compare_ops'] != '' else '',
		}
		outputfile.write(tableformat % docdata)

	outputfile.write(headerbarcomp)
	outputfile.write('\n\n\n\n')

	for opcode in csvdata:
		docdata = {'opcodename' : opcode['opcodename'], 
		'opcodedocs' : opcode['opcodedocs'], 
		'bhil' : '', 
		'BHIL' : '', 
		'fd' : '', 
		'OV' : '', 
		'compare' : '',
		}
		tabdata = tableformat % docdata
		outputfile.write(tabdata.rstrip() + '\n')

	outputfile.write('\n')


# ==============================================================================


def ACalcDocs(outputfile):
	# The documentation for the opcodes.
	tableformat = '%(opcodename)-16s %(opcodedocs)-23s %(bhil)-5s %(BHIL)-4s %(fd)-4s %(OV)-6s\n'
	outputfile.write('\n\n\nDocuments the op codes for ACalc.\n\n')
	outputfile.write(topheader)
	outputfile.write('\n')
	for opcode in csvdata:
		docdata = {'opcodename' : opcode['opcodename'], 
		'opcodedocs' : opcode['opcodedocs'], 
		'bhil' : 'X' if opcode['c_code_template_i_signed'] != '' else '', 
		'BHIL' : 'X' if opcode['c_code_template_i_unsigned'] != '' else '', 
		'fd' : 'X' if opcode['c_code_template_float'] != '' else '', 
		'OV' : 'X' if (opcode['test_ovfl_templ_isigned'] != '') or opcode['test_ovfl_templ_iunsigned'] != '' else ''
		}
		outputfile.write(tableformat % docdata)

	outputfile.write(headerbar)
	outputfile.write('\n')

# ==============================================================================



# ==============================================================================

# Write the results to disk.
def WriteTableSIMD(cheaderdata, outputfile):
	"""Parameters: cheaderdata (list) = The list of functions and what array 
			types they support.
			outputfile (file object) = The output file object to write to.
	"""
	columnwidth = 3
	tableheader = {'func' : 'function'}
	tableheader.update(dict([(y,x) for x,y in codegen_common.arraytypes.items()]))

	tablesep = dict.fromkeys(codegen_common.arraytypes.values(), '=' * columnwidth)
	tablesep.update({'func' : '==========='})
	tableformat = '%(func)10s ' + ' '.join(['%(' + codegen_common.arraytypes[x] + (')%is' % columnwidth) for x in codegen_common.arraycodes]) + '\n'


	TableData = []
	for func, arrstat in cheaderdata:
		arrformat = dict([(x, 'X' if y else ' ') for x,y in arrstat.items()])
		arrformat['func'] = func
		TableData.append(tableformat % arrformat)


	outputfile.write('\n\n\nDocuments which functions have SIMD support.\n\n')

	outputfile.write(tableformat % tablesep)
	outputfile.write(tableformat % tableheader)
	outputfile.write(tableformat % tablesep)
	outputfile.write(''.join(TableData))
	outputfile.write(tableformat % tablesep)



# ==============================================================================

# Read the C function names from the SIMD header files.
def GetHeaderFileDataSIMD():
	# Get a list of the SIMD related header files.
	filelist=glob.glob('../src/*_simd_*.h')
	filelist.sort()

	filedata = []


	for fname in filelist:
		# This gets the function name from the file, assuming the function
		# name is the first part of the file name (e.g. aall_simd_x86.h ).
		simdfile = os.path.basename(fname)
		funcname = simdfile.partition('_')[0]

		with open(fname, 'r') as f:
			typemaps = dict(zip(codegen_common.arraytypes.values(), itertools.repeat(False)))
			cfuncs = [x for x in f if '_simd(' in x]

			for line in cfuncs:
				funcstart = line.partition('_simd(')[0]
				cfuncname = funcstart.rpartition(' ')[2]
				afuncname = cfuncname.rpartition(funcname)[-1]
				afunctype = afuncname.replace('_', ' ')
				afunclabel = afunctype.strip()
				typemaps[afunclabel] = True
				

			filedata.append((funcname, typemaps))

	return filedata


# ==============================================================================

# Output data used for benchmarking.
def writeBenchMarkData(cheaderdata, outputfile):
	# Create a dictionary which allows a reverse look-up of arraycodes to C types.
	arcodelookup = dict([(y,x) for x,y in codegen_common.arraytypes.items()])
	Reformatted = []
	for funcname, ardata in cheaderdata:
		# First check to see if SIMD is supported at all for this function.
		if any(ardata.values()):
			Reformatted.append((funcname, dict([(arcodelookup[x],y) for x,y in ardata.items()])))


	outputfile.write(str(dict(Reformatted)))

# ==============================================================================

# Get a list of the C function names and their array types from the SIMD
# related C header files.
cheaderdata = GetHeaderFileDataSIMD()


with open('docsgen.txt', 'w') as f:
	# Ops codes.
	DocsOpcodes(f)
	# ACalc
	ACalcDocs(f)
	# SIMD data.
	WriteTableSIMD(cheaderdata, f)

with open('benchdata_simd.txt', 'w') as f:
	# Output data used for benchmarking.
	writeBenchMarkData(cheaderdata, f)

# ==============================================================================
