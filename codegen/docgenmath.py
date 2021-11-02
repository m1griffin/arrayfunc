#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the documentation for the math functions.
# Language: Python 3.4
# Date:     30-Apr-2018
#
###############################################################################
#
#   Copyright 2018    Michael Griffin    <m12.griffin@gmail.com>
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
import itertools

import codegen_common

# ==============================================================================

funccategories = [
('mathematical', 'Mathematical operator functions'), 
('compare', 'Comparison operator functions'), 
('bitwise', 'Bitwise operator functions'), 
('logarithmic', 'Power and logarithmic functions'),
('hyperbolic', 'Hyperbolic functions'),
('trigonometric', 'Trigonometric functions'), 
('angular', 'Angular conversion'), 
('representation', 'Number-theoretic and representation functions'), 
('special', 'Special functions'), 
('additional', 'Additional functions'), 
]

# ==============================================================================

def GetCSourceFiles():
	'''Get the list of C source files.
	'''
	# The list of files actually present.
	filelist=glob.glob('../src/*.c')
	filelist.sort()
	return filelist


# ==============================================================================

def GetFuncConfigCategoryData():
	'''Get the category and function name data from the configuration file.
	'''
	# Read the operator and function definition data.
	config = codegen_common.ReadINI('affuncdata.ini')

	# Extract function names.
	funcnames = [x for x in config.keys() if x != 'DEFAULT']

	# Group by category. This produces a dictionary where the category is the
	# key and a list of associated function names is each value.
	cat = [(x,y.get('category')) for x,y in config.items() if x != 'DEFAULT']
	cat.sort(key = lambda x : x[1])
	categories = dict([(y, [i for i,j in x]) for y,x in itertools.groupby(cat, lambda k : k[1])])

	return funcnames, categories


# ==============================================================================

def sanitizer(x):
	'''Sanitizier function. This escapes trailing underscore characters
	for the sake of ReST format where this is a formatting character.
	'''
	# Don't change anything if it is in the form of the function call.
	if ('and_(' in x) or ('or_(' in x) or ('abs_(' in x):
		return x

	if 'and_' in x:
		return x.replace('and_', 'and\_')
	elif 'or_' in x:
		return x.replace('or_', 'or\_')
	elif 'abs_' in x:
		return x.replace('abs_', 'abs\_')
	else:
		return x

def FindFuncDocs(filelist, funcnames):
	'''Get the function documentation directly from the C source code. 
	The list of functions is based on the function configuraiton spreadsheet.
	Parameters:
		filelist (list) = A list of the C file names present.
		funcnames (list) = A list of the function names.
	'''
	# Find which files in the list are actually present.
	funcspresent = [x for x in funcnames if ('../src/' + x + '.c') in filelist]

	funcsdocs = {}

	# Get the documentation directly from the C source file.
	for func in funcspresent:
		with open('../src/' + func + '.c') as f:
			funcdata = f.readlines()
			# The documentation starts with PyDoc_STRVAR and ends with the closing function bracket.
			docdata = itertools.takewhile(lambda x: '");' not in x, itertools.dropwhile(lambda x: 'PyDoc_STRVAR' not in x, funcdata))
			# Sanitize the data by removing the C language string literal control characters, plus end of line blanks.
			docdatastripped = [x.replace('\\n\\', '').rstrip() for x in list(docdata)[1:]]
			# Sanitize some more. There will be a quote character which will be at the start of the function.
			docdatastripped[0] = docdatastripped[0].replace('"', '')
			# Some function names need the trailing '_' character escaped as this is a
			# formatting character for ReST documents.
			docsantizied = [sanitizer(x) for x in docdatastripped]
			# Add some formatting to the display of call formats. To do this we need to
			# add another colon character.
			callformats = [x.replace('Call formats:', 'Call formats::') for x in docsantizied]
				
		funcsdocs[func] = ['\n\n',] + callformats

	return funcsdocs

# ==============================================================================


def GetSIMDTable(filepath):
	"""Create a table of which functions support which array types with SIMD.
	Parameters: (string) filepath = The path to the SIMD files.
	This returns a list of formatted strings.
	"""
	columnwidth = 3
	tableheader = {'func' : 'function'}
	tableheader.update(dict([(y,x) for x,y in codegen_common.arraytypes.items()]))

	tablesep = dict.fromkeys(codegen_common.arraytypes.values(), '=' * columnwidth)
	tablesep.update({'func' : '==========='})
	tableformat = '%(func)10s ' + ' '.join(['%(' + codegen_common.arraytypes[x] + (')%is' % columnwidth) for x in codegen_common.arraycodes]) + '\n'


	# Get a list of the C function names and their array types from the SIMD
	# related C header files.
	cheaderdata = codegen_common.GetHeaderFileDataSIMD(filepath)


	tabledata = []
	tabledata.append(tableformat % tablesep)
	tabledata.append(tableformat % tableheader)
	tabledata.append(tableformat % tablesep)


	for func, arrstat in cheaderdata:
		arrformat = dict([(x, 'X' if y else ' ') for x,y in arrstat.items()])

		# We need to escape any function names ending with an underscore to 
		# prevent it being interpreted as a formatting character. 
		if func.endswith('_'):
			arrformat['func'] = func.rstrip('_') + '\_'
		else:
			arrformat['func'] = func
		
		tabledata.append(tableformat % arrformat)

	tabledata.append(tableformat % tablesep)

	return ''.join(tabledata)


# ==============================================================================

def MakeFuncDocs(funccategories, funcsdocs, configcategories):
	'''Extract the function documentation and order them in the correct
	categories.
	Parameters: funccategories = The function categories.
		configcategories = A dict with function names grouped by category.
	Returns: The function documentation as a block of text.
	'''
	opdocs = []

	# The function categories
	for cat in funccategories:
		# Get all the names of the functions in this category.
		funcnames = configcategories[cat[0]]
		funcnames.sort()

		# Create the category title. But first add some blank lines.
		opdocs.append('\n\n')
		opdocs.append(cat[1])
		opdocs.append('-' * len(cat[1]))

		# Gather all the documentation for that section.
		sectiondocs = [funcsdocs.get(x, '') for x in funcnames]

		secdocs = ['\n'.join(x) for x in sectiondocs]

		opdocs.append('\n'.join(secdocs))


	return '\n'.join(opdocs)


# ==============================================================================

# Format the function documentation.
# This is for functions that do not need to be sorted into categories.
def FormatFuncsDocs(funcsdocs):
	'''Format the function documentation.
	'''
	funcnames = list(funcsdocs.keys())
	funcnames.sort()

	docs = ['\n'.join(funcsdocs[x]) for x in funcnames]

	return ''.join(docs)


# ==============================================================================

def MakeSummaryTable(funccategories, funcsdocs, funcnames, configcategories):
	'''Extract the function documentation and order them in the correct
	categories in the form of a one line summary based on the equivalent
	Python operation.
	Parameters: funccategories = The function categories.
		configcategories = A dict with function names grouped by category.
	Returns: The function summary as a block of text.
	'''
	functitlesize = max([len(x) for x in funcnames])
	functitlepad = max(functitlesize, len('Function')) + 2

	summdocs = []
	tablesep = '=' * functitlepad + ' ' + '=' * 50

	tablehead = tablesep + '\n' + 'Function'.center(functitlepad) + '      Equivalent to' + '\n' + tablesep

	# The function categories
	for cat in funccategories:
		# Get all the names of the functions in this category.
		funcnames = configcategories[cat[0]]
		funcnames.sort()

		# Create the category title. But first add some blank lines.
		summdocs.append('\n\n')
		summdocs.append(cat[1])
		summdocs.append('-' * len(cat[1]))

		summdocs.append('\n' + tablehead)

		# Gather all the documentation for that section.
		for func in funcnames:
			# Extract just the equivalent operation. 
			equiv = ''.join([x for x in funcsdocs[func] if 'Equivalent to' in x])
			equivtext = equiv.partition(':')[2].lstrip().rstrip()

			# Escape the function name in the event it contains underscores.
			# This is required for RST when converting to PDF or HTML. 
			funcrst = sanitizer(func)
			# Format the line.
			summdocs.append(funcrst.rjust(functitlepad) + ' ' + equivtext)

		summdocs.append(tablesep)

	return '\n'.join(summdocs)


# ==============================================================================

# Create the data.

# The list of C source files.
filelist = GetCSourceFiles()
# The function config data from the config spreadsheet.
funcnames, configcategories = GetFuncConfigCategoryData()

# Extract the function documentation from the C source files.
funcsdocs = FindFuncDocs(filelist, funcnames)

# Get the x86 and ARM SIMD files.
simddata_x86 = GetSIMDTable('../src/*_simd_x86.h')
simddata_armv7 = GetSIMDTable('../src/*_simd_armv7.h')
simddata_armv8 = GetSIMDTable('../src/*_simd_armv8.h')


# Get the documentation from the functions that are not in the spreadsheet.
extrafuncs = ['count', 'cycle', 'repeat', 'afilter', 'compress', 'dropwhile', 
			'takewhile', 'aany', 'aall', 'amax', 'amin', 'findindex', 'findindices', 
			'asum', 'convert']
extrafuncsdocs = FindFuncDocs(filelist, extrafuncs)
FormatFuncsDocs(extrafuncsdocs)

# Format the main function documentation.
opdocs = MakeFuncDocs(funccategories, funcsdocs, configcategories)

# Format the function summary table.
summtable = MakeSummaryTable(funccategories, funcsdocs, funcnames, configcategories)

# Format the function docs that are not defined in the spreadsheet.
extradocs = FormatFuncsDocs(extrafuncsdocs)

# ==============================================================================

# Import the benchmark data.

def GetBenchmarkData():
	'''Read the benchmark data and extract the benchmarks.
	'''
	# These are the benchmark table headings. These are used to find
	# the start and stop of each benchmark table.
	pytitle = 'Relative Performance - Python Time'
	simdtitle = 'Effect of leaving error checking on and disabling SIMD'
	
	simdrel = 'Effect of turning error checking off and leaving SIMD on'
	pyabsolute = 'Python native time in micro-seconds'

	with open('../benchmarks/af_benchmarkdata.txt') as f:
		benchdata = f.readlines()

	# Get the Python native time.
	pybench = ''.join(itertools.takewhile(lambda x: simdtitle not in x, itertools.dropwhile(lambda x: pytitle not in x, benchdata)))
	simdbench = ''.join(itertools.takewhile(lambda x: pyabsolute not in x, itertools.dropwhile(lambda x: simdrel not in x, benchdata)))

	return pybench, simdbench

pybench, simdbench = GetBenchmarkData()


# ==============================================================================

def GetArraySizeBenchData():
	'''Read in the array size benchmark data.
	'''
	with open('../benchmarks/bencharraysize.txt') as f:
		benchdata = f.readlines()

	arraysizebench = ''.join(itertools.dropwhile(lambda x: 'Add constant to array' not in x, benchdata))

	return arraysizebench

arraysizebench = GetArraySizeBenchData()

# ==============================================================================

# Insert the data into the documentation template.
def WriteDocs(summtable, opdocs, extradocs, simddata_x86, simddata_armv7, simddata_armv8, 
		pybench, simdbench, arraysizebench):
	'''Write out the documentation based on the template.
	'''
	# Read in the entire template file.
	with open('docmathtemplate.rst', 'r') as f:
		doctmpl = f.read()

	# Write out the completed documentation file complete with data.
	with open('ArrayFunc.rst', 'w') as f:
		f.write(doctmpl.format(summarytable = summtable, opdocs = opdocs, extradocs = extradocs,
			simddata_x86 = simddata_x86, simddata_armv7 = simddata_armv7, simddata_armv8 = simddata_armv8,
			pybench = pybench, simdbench = simdbench, arraysizebench = arraysizebench))

# Write out the documentation file.
WriteDocs(summtable, opdocs, extradocs, simddata_x86, simddata_armv7, simddata_armv8, 
		pybench, simdbench, arraysizebench)

# ==============================================================================
