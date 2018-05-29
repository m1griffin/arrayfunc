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

import codegen_common


# ==============================================================================

# The documentation templates are assembled from these fragments.

# This is the start to all the documentation templates.
doctempl1 = '''
%(funcname_esc)s
_____________________________

Calculate %(funcname_esc)s over the values in an array. 

======================  ========================================================
Equivalent to:          %(opcodedocs)s
Array types supported:  %(arraytypes)s
Exceptions raised:      %(matherrors)s
======================  ========================================================

Call formats::

'''


doctempl2a = '''
  %(funcname)s(array1, param)
  %(funcname)s(array1, param, outparray)
  %(funcname)s(param, array1)
  %(funcname)s(param, array1, outparray)
  %(funcname)s(array1, array2)
  %(funcname)s(array1, array2, outparray)
  %(funcname)s(array1, param, maxlen=y)
  %(funcname)s(array1, param, matherrors=False)

'''

doctempl2b = '''
  %(funcname)s(array1, param)
  %(funcname)s(array1, param, outparray)
  %(funcname)s(param, array1)
  %(funcname)s(param, array1, outparray)
  %(funcname)s(array1, array2)
  %(funcname)s(array1, array2, outparray)
  %(funcname)s(array1, param, maxlen=y)

'''

doctempl2c = '''
  result = %(funcname)s(array1, param)
  result = %(funcname)s(param, array1)
  result = %(funcname)s(array1, array2)
  result = %(funcname)s(array1, param, maxlen=y)

'''

doctempl2d = '''
    %(funcname)s(array1)
    %(funcname)s(array1, outparray)
    %(funcname)s(array1, maxlen=y)
    %(funcname)s(array1, matherrors=False))
 
'''

doctempl2e = '''
    %(funcname)s(array1)
    %(funcname)s(array1, outparray)
    %(funcname)s(array1, maxlen=y)
 
'''
 
    
doctempl2ldexp = '''
    %(funcname)s(array1, exp)
    %(funcname)s(array1, exp, outparray)
    %(funcname)s(array1, exp, maxlen=y)
    %(funcname)s(array1, exp, matherrors=False))
 
'''
    
doctempl2mathnan = '''
    result = %(funcname)s(array1)
    result = %(funcname)s(array1, maxlen=y)
 
'''

doctempl3arr1 = '''* array1 - The first input data array to be examined. If no output 
  array is provided the results will overwrite the input data. 
'''


doctempl3param = '''* param - A non-array numeric parameter. 
'''


doctempl3arr2 = '''* array2 - A second input data array. Each element in this array is 
  applied to the corresponding element in the first array. 
'''


doctempl3arrout = '''* outparray - The output array. This parameter is optional. 
'''

doctempl3maxlen = '''* maxlen - Limit the length of the array used. This must be a valid 
  positive integer. If a zero or negative length, or a value which is 
  greater than the actual length of the array is specified, this 
  parameter is ignored. 
'''

doctempl3err = '''* matherrors - If true, arithmetic error checking is disabled. The 
  default is false.
'''

doctempl3exp = '''* exp - The exponent to apply to the input array. This must be an integer.
'''


doctempl3resultcomp = '''* result - A boolean value corresponding to the result of all the comparison
  operations. If all comparison operations result in true, the return value
  will be true. If any of them result in false, the return value will be
  false.
'''


doctempl3resultnan = '''* result - A boolean value corresponding to the result of all the 
  comparison operations. If at least one comparison operation results in true, 
  the return value will be true. If none of them result in true, the return 
  value will be false.
'''

# ==============================================================================


template_mathop = [doctempl1, doctempl2a, 
	doctempl3arr1, doctempl3param, doctempl3arr2, doctempl3arrout, 
	doctempl3maxlen, doctempl3err]

template_binop = [doctempl1, doctempl2b, 
	doctempl3arr1, doctempl3param, doctempl3arr2, doctempl3arrout, 
	doctempl3maxlen]

template_comp = [doctempl1, doctempl2c, 
	doctempl3arr1, doctempl3param, doctempl3arr2, 
	doctempl3maxlen, doctempl3resultcomp]

template_mathfunc_2 = template_mathop

template_mathfunc_1 = [doctempl1, doctempl2d, 
	doctempl3arr1, doctempl3arrout, doctempl3maxlen, doctempl3err]

template_mathfunc_1s = template_mathfunc_1

template_uniop = [doctempl1, doctempl2d, 
	doctempl3arr1, doctempl3maxlen, doctempl3err]

template_ldexpfunc_2 = [doctempl1, doctempl2ldexp, 
	doctempl3arr1, doctempl3exp, doctempl3arrout, 
	doctempl3maxlen, doctempl3err]

template_mathfuncnan = [doctempl1, doctempl2mathnan,
	doctempl3arr1, doctempl3maxlen, doctempl3resultnan]

template_invert = [doctempl1, doctempl2e, 
	doctempl3arr1, doctempl3arrout, 
	doctempl3maxlen]

# ==============================================================================

doctemplates = {
	'template_invert' : template_invert, 
	'template_mathfunc_1s' : template_mathfunc_1s, 
	'template_mathfuncnan' : template_mathfuncnan, 
	'template_ldexpfunc_2' : template_ldexpfunc_2, 
	'template_uniop' : template_uniop,
	'template_mathfunc_1' : template_mathfunc_1,
	'template_mathfunc_2' : template_mathfunc_2, 
	'template_comp' : template_comp, 
	'template_binop' : template_binop, 
	'template_mathop' : template_mathop, 
}

funccategories = {
'mathematical' : ('0', 'Mathematical operator functions'), 
'compare' : ('1', 'Comparison operator functions'), 
'bitwise' : ('2', 'Bitwise operator functions'), 
'logarithmic' : ('3', 'Power and logarithmic functions'),
'hyperbolic' : ('4', 'Hyperbolic functions'),
'trigonometric' : ('5', 'Trigonometric functions'), 
'angular' : ('6', 'Angular conversion'), 
'representation' : ('7', 'Number-theoretic and representation functions'), 
'special' : ('8', 'Special functions'), 
}



# These are used to create the summary table of function names and description.


mathtableheader = '''
=========== ===============================================
  Function              Equivalent to
=========== ==============================================='''

mathtablefooter = '=========== ==============================================='


# ==============================================================================

# Read the operator and function definition data.
opdata = list(codegen_common.ReadCSVData('funcs.csv'))


# Create and decorate the sorting keys.
for x in opdata:
	x['sortkey'] = funccategories[x['category']][0] + x['category']

# Now sort the list.
sorteddata = sorted(opdata, key=lambda x: x.get('sortkey'))


# ==============================================================================

prevcat = ''
summtable = []


with open('docs_math.txt', 'w') as f:

	f.write('.. contents:: Table of Contents\n\n')

	# Handle each function in sequence.
	for op in sorteddata:

		supportedarrays = codegen_common.FormatDocsArrayTypes(op['arraytypes'])


		# We use the C source code template to decide what sort of documentation
		# template we need to use. 
		doctmp = ''.join(doctemplates[op['c_code_template']])

		# We need to escape any function names ending with an underscore to 
		# prevent it being interpreted as a formatting character. 
		if op['funcname'].endswith('_'):
			funcesc = op['funcname'].rstrip('_') + '\_'
		else:
			funcesc = op['funcname']

		docdata = {'funcname' : op['funcname'], 
				'funcname_esc' : funcesc,
				'opcodedocs' : op['opcodedocs'],
				'arraytypes' : supportedarrays,
				'matherrors' : ', '.join(op['matherrors'].split(','))}


		# Write the category description whenever it changes.
		if op['category'] != prevcat:
			catname = funccategories[op['category']][1]
			f.write('\n' + catname + '\n')
			f.write('-' * len(catname) + '\n\n')

			# Do not need this for first table.
			if len(summtable) > 0:
				summtable.append(mathtablefooter + '\n')

			# For summary table.
			summtable.append(catname)
			summtable.append('-' * len(catname) + '\n')
			summtable.append(mathtableheader)

			prevcat = op['category']

		# Write out the documentation for that function.
		f.write(doctmp % docdata)

		# Append to the summary table.
		summtable.append(funcesc.rjust(11) + ' ' + op['opcodedocs'])


	# Now write out the summary table.
	summtable.append(mathtablefooter)
	f.write('\n\n\n')
	f.write('\n'.join(summtable))
	f.write('\n')

