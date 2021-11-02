#!/usr/bin/python3

import configparser
import csv
import argparse


# ==============================================================================

# This is the list of valid headings in the original spreadsheet. 
# This should be used to control the generation of CSV files as the order
# of data is important to make sure it ends up under the right columns.
CSVHeadings = ['funcname', 'opcodedocs', 'category', 'matherrors', 'pyoperator', 
	'c_operator_i', 'c_operator_d', 'c_operator_f', 'c_code_template', 'simd', 
	'test_op_templ', 'arraytypes', 'test_op_x', 'test_op_y', 'test_op_z', 
	'test_op_y_fail', 'test_nan_data_template', 'test_inf_data_template', 
	'test_ninf_data_template', 'test_nan_default']


# ==============================================================================
# This function has been copied in from codegen_common as when this utility
# has been completed there will no longer be reason to have this function
# in that file.
def ReadCSVData(filename):
	"""Read the operator and function definition data from a CSV file. All of
	the data to create the C code is stored in a spreadsheet and then saved to
	a CSV file. This function reads in the file, and saves it in a list of
	dictionaries. While doing this, sanatize the data to take out "'" characters
	which were added to prevent conflicts with spreadsheet codes. 

	The first row of the spreadsheet is used as the expected key names.

	"""
	csvreaddata = []
	with open(filename, 'r') as csvfile:
		# We must specify the quote character to ensure that it doesn't become
		# part of our data.
		opreader = csv.reader(csvfile, delimiter='\t', quotechar="'")
		# The first row is the descriptive headers, which we use as key names.
		dataformat = next(opreader)
		# Read in all the data at once so we can work on it more easily. 
		for rec in opreader:
			csvreaddata.append(dict([(x,y.replace("'", '')) for x,y in zip(dataformat, rec)]))
		print(dataformat)
		# Sanitise the data to remove quote characters which were added to the
		# spreadsheet to prevent conflicts with spreadsheet formatting codes.
		csvdata = []
		for rec in csvreaddata:
			rec['pyoperator'] = rec['pyoperator'].replace("'", '')
			csvdata.append(rec)


	return csvdata


def CSVtoIni(csvnamein, ininameout):
	'''Import a CSV file and write it out as an INI file.
	'''
	# It is important to disable interpolation as otherwise the parser
	# will have problems with the mod operator %.
	config = configparser.ConfigParser(interpolation=None, delimiters=':')

	# This reads the CSV file in and returns it as a list of dictionaries.
	funcdata = ReadCSVData(csvnamein)

	# We now need to reformat the 
	for func in funcdata:
		funcname = func['funcname']
		# Strip out the function name as a key value entry as it will now
		# be the section heading. 
		config[funcname] = dict([(x,y) for x,y in func.items() if x != 'funcname'])

	# Now write out the INI file.
	with open(ininameout, 'w') as configfile:
		config.write(configfile)


# ==============================================================================


# ==============================================================================
def ReadINI(ininamein):
	'''Read in an INI file.
	'''
	# It is important to disable interpolation as otherwise the parser
	# will have problems with the mod operator %.
	config = configparser.ConfigParser(interpolation=None, delimiters=':')
	config.read(ininamein)

	return config


# ==============================================================================
# Read in an INI configuration file and export it to a CSV file.

def INItoCSV(ininamein, csvnameout):
	'''Import a CSV file and write it out as an INI file.
	'''
	# Read in the INI file.
	config = ReadINI(ininamein)

	with open(csvnameout, 'w', newline='') as csvoutfile:
		# By default we quote everything to avoid data loss on round-trip of data.
		csvout = csv.writer(csvoutfile, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)

		# The headings need to appear at the top of the file.
		csvout.writerow(CSVHeadings)

		# We output the data for each function, being sure to keep the
		# data in the correct column by using the headings list to
		# index them.
		for funcname in config.sections():
			csvout.writerow([funcname, ] + [config[funcname][x] for x in CSVHeadings if x != 'funcname'])


# ==============================================================================
def ListFuncs(ininame):
	'''List the names of the functions found in the INI configuration file.
	'''
	configdata = ReadINI(ininame)
	print('List of functions defined within the INI file.')
	print('==============================================')
	for funcname in configdata.sections():
		print(funcname)


def ListKeys():
	'''List the names of the standard keys used with each section.
	'''
	print('List of standard keys.')
	print('======================')
	for keyname in CSVHeadings:
		print(keyname)


def ListKeyValues(ininame, keyname):
	'''List the values used by particular keys.
	'''
	configdata = ReadINI(ininame)
	print('List of values for key: %s.' % keyname)
	print('============================')

	# Organise the data by value.
	keyvals = {}
	for funcname in configdata.sections():
		currentfunc = configdata[funcname]
		keyvalue = currentfunc[keyname]
		if len(keyvalue) > 0:
			if not keyvalue in keyvals:
				keyvals[keyvalue] = [funcname, ]
			else:
				keyvals[keyvalue].append(funcname)

	# Now print by value / key.
	for val, key in keyvals.items():
		print('%s: ' % val, ', '.join(key))
	
	


# ==============================================================================

def GetCmdArguments():
	""" Get any command line arguments. These modify the operation of the program.
			convert = Convert between CSV and INI file formats.
	"""

	# Get any command line arguments.
	parser = argparse.ArgumentParser()

	parser.add_argument('--file', choices=['import', 'export'], 
			help='File opertions. Specify import (from csv) or export (to csv).')

	parser.add_argument('--funcs', action='store_true', help='List function names.')

	parser.add_argument('--bykey', choices=CSVHeadings,
			help='List values by key name.')


	args = parser.parse_args()

	return args

# ==============================================================================


##############################################################################

# These are the default configuration data files. The INI file is the one
# used by the code generation scripts, while the CSV version is to allow 
# the data to be exported to a spreadsheet for review. 
StdIniFile = 'affuncdata.ini'
StdCsvFile = 'affuncdata.csv'


CmdArgs = GetCmdArguments()

fileops = CmdArgs.file
listfuncs = CmdArgs.funcs
bykey = CmdArgs.bykey

if listfuncs:
	ListFuncs(StdIniFile)
elif bykey is not None:
	ListKeyValues(StdIniFile, bykey)
elif fileops is not None:
	if fileops == 'import':
		CSVtoIni(StdCsvFile, StdIniFile)
	elif fileops == 'export':
		INItoCSV(StdIniFile, StdCsvFile)
	else:
		print('Unknown file operation: %s' % fileops)
else:
	print('Error - Unknown command.')


##############################################################################
