################################################################################
# Project:  arrayfunc
# Module:   acalccomp.py
# Purpose:  Compile equations to byte code for execution by the calc module.
# Language: Python 3
# Date:     08-Dec-2015
#
################################################################################
#
#   Copyright 2014 - 2016    Michael Griffin    <m12.griffin@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http:#www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
################################################################################

import ast
import keyword
import collections
import itertools
import array
import platform
import math

import arrayfunc.acalcvm


##############################################################################
class OpCodeContainer:
	"""Used to contain op code data when analysing AST.
	"""
	########################################################
	def __init__(self, opcode = None, param = None, iscall = False):
		# The name of the op code.
		self.opcode = opcode
		# The op code parameter.
		self.param = param
		# If True, this was a call.
		self.iscall = iscall

##############################################################################


##############################################################################
class AnalyseCode(ast.NodeVisitor):
	"""Analyse an equation at the AST level. 
	"""

	########################################################
	def __init__(self, arrayname):
		"""Parameters: arrayname (string) = The variable name used in the 
		equation for the current array element.
		"""
		# The variable name used in the equation for the current array element.
		self._ArrayName = arrayname
		# This is a running summary of the AST.
		self._CodeDesc = []


	########################################################
	def _AddOpCode(self, op):
		"""Add an op to the list of op codes to be executed. 
		Parameters: op (object) = The op code.
		"""
		self._CodeDesc.append(op)


	########################################################
	def GetOpCodes(self):
		"""Return the accumulated op codes. 
		Returns (list) = A list of objects containing the op codes and parameters.
		"""
		return list(reversed(self._CodeDesc))


	########################################################
	def _OpType(self, node):
		if isinstance(node, ast.Add):
			return 'add'
		elif isinstance(node, ast.Sub):
			return 'sub'
		elif isinstance(node, ast.Mult):
			return 'mult'
		elif isinstance(node, ast.Div):
			return 'div'
		elif isinstance(node, ast.FloorDiv):
			return 'floordiv'
		elif isinstance(node, ast.Mod):
			return 'mod'
		elif isinstance(node, ast.Pow):
			return 'pow'
		elif isinstance(node, ast.LShift):
			return 'lshift'
		elif isinstance(node, ast.RShift):
			return 'rshift'
		elif isinstance(node, ast.BitOr):
			return 'bitor'
		elif isinstance(node, ast.BitXor):
			return 'bitxor'
		elif isinstance(node, ast.BitAnd):
			return 'bitand'

		# Unary ops.
		elif isinstance(node, ast.Invert):
			return 'invert'
		elif isinstance(node, ast.Not):
			return 'not'
		elif isinstance(node, ast.UAdd):
			return 'uadd'
		elif isinstance(node, ast.USub):
			return 'usub'
		else:
			return 'unknown'


	########################################################
	def visit_BinOp(self, node):
		op = OpCodeContainer(self._OpType(node.op), None, False)
		self._AddOpCode(op)
		self.generic_visit(node)
		return node


	########################################################
	def visit_UnaryOp(self, node):
		op = OpCodeContainer(self._OpType(node.op), None, False)
		self._AddOpCode(op)
		self.generic_visit(node)
		return node


	########################################################
	def visit_Call(self, node):
		"""Function calls, either built in, or prefixed with a module name.
		This does not validate the function name. 
		"""
		# Call a built in.
		if isinstance(node.func, ast.Name):
			opcode = node.func.id
		# Function name is prefixed with a module name. 
		elif isinstance(node.func, ast.Attribute):
			opcode = '%s.%s' % (node.func.value.id, node.func.attr)
		# Not sure how we can get this.
		else:
			raise ValueError('unknown call name in ACalc compile.')

		op = OpCodeContainer(opcode, None, True)
		self._AddOpCode(op)

		self.generic_visit(node)
		return node


	########################################################
	def visit_Name(self, node):
		# Drop this if it is 'math'. This name is reserved for the math library.
		# Since we don't actually import the math library, we can drop this
		# operation. The math library functions and attributes can tell for
		# themselves if they are being called.
		if node.id not in ('math', 'abs'):
			if node.id == self._ArrayName:
				opcode = 'pusharray'
			else:
				opcode = 'pushvar'

			op = OpCodeContainer(opcode, node.id, False)
			self._AddOpCode(op)

		self.generic_visit(node)
		return node


	########################################################
	def visit_Attribute(self, node):
		# We recognise only two attributes.
		if (node.attr in ('pi', 'e')) and (node.value.id == 'math'):
			if node.attr == 'pi':
				value = math.pi
			else:
				value = math.e
		
			op = OpCodeContainer('pushconst', value, False)
			self._AddOpCode(op)

		self.generic_visit(node)
		return node


	########################################################
	def visit_Num(self, node):
		op = OpCodeContainer('pushconst', node.n, False)
		self._AddOpCode(op)
		self.generic_visit(node)
		return node


##############################################################################


# This defines the individual op code byte values for float and integer. Values are "None"
# if the operation is not valid for that data type.
_OpCodes = {
	'unknown' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([0, False, 0, False, 0, True]),
	'pusharray' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([1, False, 1, False, 1, True]),
	'pushvar' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([2, False, 2, False, 1, True]),
	'pushconst' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([3, False, 3, False, 1, True]),
	'add' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([4, False, 4, False, -1, True]),
	'sub' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([5, False, 5, False, -1, True]),
	'mult' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([6, False, 6, False, -1, True]),
	'div' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([7, False, 7, False, -1, True]),
	'floordiv' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([8, False, 8, False, -1, True]),
	'mod' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([9, False, 9, False, -1, True]),
	'uadd' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([10, False, 10, False, 0, True]),
	'usub' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([11, True, 11, False, 0, True]),
	'pow' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([12, False, 12, False, -1, True]),
	'bitand' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([13, False, None, False, -1, True]),
	'bitor' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([14, False, None, False, -1, True]),
	'bitxor' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([15, False, None, False, -1, True]),
	'invert' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([16, False, None, False, 0, True]),
	'lshift' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([17, False, None, False, -1, True]),
	'rshift' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([18, False, None, False, -1, True]),
	'abs' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([19, False, 13, True, 0, True]),
	'math.acos' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 14, True, 0, True]),
	'math.acosh' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 15, True, 0, False]),
	'math.asin' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 16, True, 0, True]),
	'math.asinh' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 17, True, 0, False]),
	'math.atan' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 18, True, 0, True]),
	'math.atan2' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 19, True, -1, True]),
	'math.atanh' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 20, True, 0, False]),
	'math.ceil' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 21, True, 0, True]),
	'math.copysign' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 22, True, -1, True]),
	'math.cos' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 23, True, 0, True]),
	'math.cosh' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 24, True, 0, True]),
	'math.degrees' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 25, True, 0, True]),
	'math.erf' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 26, True, 0, False]),
	'math.erfc' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 27, True, 0, False]),
	'math.exp' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 28, True, 0, True]),
	'math.expm1' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 29, True, 0, False]),
	'math.fabs' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 30, True, 0, True]),
	'math.factorial' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([20, False, None, True, 0, True]),
	'math.floor' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 31, True, 0, True]),
	'math.fmod' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 32, True, -1, True]),
	'math.gamma' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 33, True, 0, False]),
	'math.hypot' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 34, True, -1, True]),
	'math.ldexp' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 35, True, -1, True]),
	'math.lgamma' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 36, True, 0, False]),
	'math.log' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 37, True, 0, True]),
	'math.log10' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 38, True, 0, True]),
	'math.log1p' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 39, True, 0, False]),
	'math.pow' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 40, True, -1, True]),
	'math.radians' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 41, True, 0, True]),
	'math.sin' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 42, True, 0, True]),
	'math.sinh' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 43, True, 0, True]),
	'math.sqrt' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 44, True, 0, True]),
	'math.tan' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 45, True, 0, True]),
	'math.tanh' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 46, True, 0, True]),
	'math.trunc' : collections.namedtuple('opcodes', ['intval', 'signedonly', 'floatval', 'mathlib', 'stack', 'msvs_has'])._make([None, False, 47, True, 0, False]),
	}


# Separate the op codes by data class.
# Signed integers.
_OpCodesInt = dict([(x,y.intval) for x,y in _OpCodes.items() if y.intval is not None])
# Unsigned integers.
_OpCodesUInt = dict([(x,y.intval) for x,y in _OpCodes.items() if (y.intval is not None) and not y.signedonly])
# Floating point.
_OpCodesFloat = dict([(x,y.floatval) for x,y in _OpCodes.items() if y.floatval is not None])


# These are the supported library and built-in functions.
# This just contains the base name, and not the extended type codes.
_LibFuncs = [x for x,y in _OpCodes.items() if y.mathlib]

# Find operations and math functions which are not supported by the
# platform compiler.
if platform.python_compiler().startswith('MSC'):
	_UnsupportedCodes = [x for x,y in _OpCodes.items() if not y.msvs_has]
# We need the else clause to support some of the unit tests.
else:
	_UnsupportedCodes = []


# These tokens should not be present. This is not intended as an exhaustive
# list of 'bad' tokens, but just as a simple filter for initial syntax checking.
_InvalidTokens = ('`', '@', '#', '$', ';', ':', '[', ']', '{', '}', '\\')

# These are the valid node types. 
_ValidNodes = [ast.Add, ast.And, ast.Attribute, ast.BinOp, 
	ast.BitAnd, ast.BitOr, ast.BitXor, ast.BoolOp, ast.Call, ast.Compare, 
	ast.Div, ast.Ellipsis, ast.Eq, ast.Expr, ast.FloorDiv, ast.GtE, ast.Gt, 
	ast.Invert, ast.Load, ast.LShift, ast.LtE, ast.Lt, ast.Mod, ast.Mult, 
	ast.Name, ast.NotEq, ast.Not, ast.Num, ast.Or, ast.Pow, 
	ast.RShift, ast.Sub, ast.UAdd, ast.UnaryOp, ast.USub]




##############################################################################
class calc:
	"""Handle a single equation, including parsing the source code, converting
	it to executable Python, and executing the resulting code. 
	"""

	########################################################
	def __init__(self, dataarray, dataoutarray):
		"""Parameters: dataarray (array) = The data array to work on.
				dataoutarray (array) = The data array to save results to.
				Both arrays must be of the same type.
		"""
		if not (isinstance(dataarray, array.array) or isinstance(dataarray, bytes)):
			raise TypeError('first parameter must be an array or bytes in ACalc init.')

		if not (isinstance(dataoutarray, array.array) or isinstance(dataoutarray, bytes)):
			raise TypeError('second parameter must be an array or bytes in ACalc init.')

		self._DataArray = dataarray
		self._DataOutArray = dataoutarray


		# If it is bytes, we assume this will behave the same as signed char.
		if isinstance(self._DataArray, bytes):
			self._ArrayType = 'B'
			dataarrayis = 'bytes'
		else:
			self._ArrayType = self._DataArray.typecode
			dataarrayis = 'array'

		# Same again for the output array.
		if isinstance(self._DataOutArray, bytes):
			outarraytype = 'B'
			dataoutarrayis = 'bytes'
		else:
			outarraytype = self._DataOutArray.typecode
			dataoutarrayis = 'array'

		# Signed integer.
		if self._ArrayType in ('b', 'h', 'i', 'l', 'q'):
			self._DataType = 'int'
		# Unsigned integer.
		elif self._ArrayType in ('B', 'H', 'I', 'L', 'Q'):
			self._DataType = 'uint'
		# Floating point.
		elif self._ArrayType in ('f', 'd'):
			self._DataType = 'float'
		# This should never happen.
		else:
			self._DataType = None
			raise TypeError('unknown array type in ACalc init.')


		# The number of stack "segments" to use when interating over the array in "chunks".
		self._VMStackSegments = 32

		self._ParamNames = []

		# The input and output data arrays must be of the same type.
		if (self._ArrayType != outarraytype) or (dataarrayis != dataoutarrayis):
			raise TypeError('data array type mismatch error in ACalc init.')


		# This is use for the interpreter stack. Create a default stack which 
		# will be replaced later.
		self._VMStack = array.array(self._ArrayType, [0] * self._VMStackSegments)


		# This exists for the purpose of unit testing.
		# The MS Windows VC 2010 does not support some math functions. This 
		# function finds those so the compiler can find them and provide 
		# exceptions. This is provided as a separate functions so that the unit
		# tests can fiddle with it. 
		# This is redundant if MS VC ever comes to support all functions.
		self._UnsupportedCodes = _UnsupportedCodes


	########################################################
	def _CheckParamKeywords(self, arrayname, paramnames):
		"""Check that the variable names do not collide with any Python keyword
		names, or with 'math' or 'abs'.
		Parameters: arrayname (string) = The variable used as the current array
				element.
			paramnames (sequence) = The list of additional parameter names.
		Returns: (set) = Returns the set of names which collide with keywords. 
		"""
		paramcheck = set(paramnames)
		paramcheck.add(arrayname)

		pythonkeywords = set(keyword.kwlist)
		pythonkeywords.update(set(('math', 'abs')))

		return paramcheck & pythonkeywords


	########################################################
	def _AllNodesValid(self, astnode):
		"""Check that the equation only contains instructions which we want to support.
		Parameters: astnode (object) = The equation as an ast tree.
		Returns: (boolean) = Returns True if all the nodes are of the supported
			types. 
		"""
		# Check all the nodes and compare them to the list of valid ones to
		# see if there are any invalid operations present.
		result = [x for x in ast.walk(astnode) if not any((y for y in _ValidNodes if isinstance(x, y)))]

		# We didn't check to see if ast.Expression is present. We expect to see
		# this exactly once (since we are compiling the equation to an expression).
		return ((len(result) == 1) and isinstance(result[0], ast.Expression))



	########################################################
	def _AllFuncCallsValid(self, astnode):
		"""Check that the equation only contains supported function calls.
		Parameters: astnode (object) = The equation as an ast tree.
		Returns: (boolean) = Returns True if all the function calls are of the 
			supported types. 
		"""
		# Filter out the nodes which are function calls.
		funcalls = [x for x in ast.walk(astnode) if isinstance(x, ast.Call)]

		# Get just the built-ins
		builtins = [x.func.id for x in funcalls if isinstance(x.func, ast.Name)]
		# Get the library functions (e.g. math.sin(a)). This also combines the
		# library name and attribute (function name).
		libfuncs = ['%s.%s' % (x.func.value.id, x.func.attr) for x in funcalls if isinstance(x.func, ast.Attribute)]

		# Combine the lists.
		libfuncs.extend(builtins)
		# Find any function calls which are not in the defined lists.
		invalidfuncs = set(libfuncs) - set(_LibFuncs)

		return not invalidfuncs



	########################################################
	def _FilterUSubConst(self, nodelist):
		"""Filter out USub operations on constants. We need to do this in order
		to determine whether constants are within range at compile time. 
		Without this, we cannot determine at compile time whether a negative 
		signed integer will fit within the defined range for that data type. 
		E.g. we can't distinguish between -128 and +128 for 'b' arrays.
		Parameters: nodelist (list) = The object containing the analysed ast
			reduced to a list of objects with text attributes.
		Returns (list) = The original list with redundant usub and uadd nodes pruned.
		"""
		isconst = False
		usub = False
		prunedlist = []
		lastconst = None
		for x in nodelist:
			# We are working on a constant, and we encountered a '-'.
			if isconst and x.opcode == 'usub':
				usub = not usub
			# We are working on a constant, and we encountered a '+'.
			elif isconst and x.opcode == 'uadd':
				pass
			# We just encountered a constant.
			elif x.opcode == 'pushconst':
				isconst = True
				lastconst = x
				prunedlist.append(x)
			# We were working on a constant, and just encountered something
			# other than a usub or uadd.
			elif isconst and x.opcode != 'pushconst':
				if usub:
					lastconst.param = -lastconst.param

				isconst = False

				prunedlist.append(x)
			# We encountered something else.
			else:
				prunedlist.append(x)


		return prunedlist


	########################################################
	def _ConvertConstants(self, nodelist):
		"""Convert the constant numeric types as required. Also check that the
		numeric constants will fit within the selected array type. 
		Parameters: nodelist (list) = The object containing the analysed ast
			reduced to a list of objects with text attributes.
		Returns (list) = The original list with any constants converted and
			range checked. An exception may be raised if a range error is
			encountered.
		"""

		# This is used to check if the values of constants are compatible with
		# the chosen array type.
		consttester = array.array(self._ArrayType)

		# Convert any constants to the correct types. This may involve 
		# converting ints to floats or floats to ints.
		for x in nodelist:
			if x.opcode == 'pushconst':
				if self._DataType in ('int', 'uint'):
					x.param = int(x.param)
				else:
					x.param = float(x.param)

				# Test if the constant will actually fit in the array type. We
				# do this by trying to actuall stick in an array. 
				# We are assuming at this point that usub and uadd operations
				# associated with constants have been removed and the appropriate 
				# signs added to the constant itself.
				try:
					consttester.append(x.param)
				except(OverflowError):
					raise OverflowError('equation constant %s is out of range for the selected array type in ACalc compile.' % x.param)

		return nodelist



	########################################################
	def _CheckOpCodes(self, nodelist):
		"""Check that the op codes are compatible with the array type specified. 
		Parameters: nodelist (list) = The object containing the analysed ast
			reduced to a list of objects with text attributes.
		Returns nothing, however an exception may be raised if invalid op codes
			for the selected array type are encountered. 
		"""
		# Select which set of operations we will check against. This depends
		# on the type of the array.
		if self._DataType == 'int':
			testset = set(_OpCodesInt.keys())
		elif self._DataType == 'uint':
			testset = set(_OpCodesUInt.keys())
		else:
			testset = set(_OpCodesFloat.keys())

		# This extracts all the operations used in the equation.
		nodeset = set([x.opcode for x in nodelist])

		# If the set is not empty, the difference is the unrecognised operations.
		invalidops = nodeset - testset

		# These operations are invalid on all platforms.
		if invalidops:
			raise ValueError('invalid operations in ACalc compile: %s.' % ', '.join(invalidops))

		# These operations are not supported by the current platform.
		unsupportedops = nodeset & set(self._UnsupportedCodes)
		if unsupportedops:
			raise ValueError('unsupported operations in ACalc compile: %s.' % ', '.join(unsupportedops))



	########################################################
	def _CheckStack(self, nodelist):
		"""Check the stack for overflow.
		Parameters: nodelist (list) = The object containing the analysed ast
			reduced to a list of objects with text attributes.
		Returns (bool, int) True if the stack is OK (does not overflow), and 
			the required stack depth.
		"""
		stackprofile = list(itertools.accumulate([_OpCodes[x.opcode].stack for x in nodelist]))

		# The largest value is the depth of stack required. We need to add 2 to
		# the calculated value because we can't effectively use the first array
		# element in the stack (the first instruction must be PUSH, which 
		# increments the stack), plus, size is max index + 1. 
		return min(stackprofile) > 0, max(stackprofile) + 2



	########################################################
	def _AssignToRegisters(self, nodelist, arrayname, paramnames):
		"""Find all the instructions relating to loading variables and constants
		and assign them to registers.
		Parameters: nodelist (list) = The object containing the analysed ast
			reduced to a list of objects with text attributes.
			arrayname (string) = The variable used to represent the array 
				elements.
			paramnames (list) = A list of strings defining the additional 
				variables used in the equation.
		Returns (list, dict) = The modified nodelist, a dictionary with
			the variable names as keys and the array index as values.
		"""
		# Check the variables used to see if they match the list of variables
		# provided.
		varsused = set([x.param for x in nodelist if x.opcode == 'pushvar'])

		varsavailable = set(paramnames)

		# Make sure the array name has not be re-used in the additional parameters.
		if arrayname in paramnames:
			raise ValueError('array name used in additional parameters in ACalc compile.')

		# A variable was used which was not defined.
		if (varsused - varsavailable):
			raise ValueError('undefined variables in ACalc compile: %s.' % ', '.join(varsused - varsavailable))

		# A variable was left unused.
		if (varsavailable - varsused):
			raise ValueError('unused variables in ACalc compile: %s.' % ', '.join(varsavailable - varsused))


		# Make sure the array parameter list does not contain duplicate names.
		if len(varsavailable) != len(paramnames):
			raise ValueError('duplicate parameter names in ACalc compile.')


		# This lets us look up parameter order by parameter name.
		paramorder = dict([(y,x) for x,y in enumerate(paramnames)])


		# Now substitute the integer values for the parameter names. These values
		# will correspond to array indices in the array used to store the
		# parameter values.
		for x in nodelist:
			if x.opcode == 'pushvar':
				x.param = paramorder[x.param]


		return nodelist, paramorder



	########################################################
	def _CompileToByteCode(self, nodelist):
		"""Compile the ast node list to executable byte code. These are
		the byte codes for the static interpreter, not Python byte codes.
		Also create the constant and varaible offset arrays.
		Parameters: nodelist (list) = The object containing the analysed ast
			reduced to a list of objects with text attributes.
		Returns (array, array, array) = The bytecodes, variable offsets, 
			constant offsets in arrays.
		"""
		# The type will be int or float.
		if self._DataType in ('int', 'uint'):
			opcodes = _OpCodesInt
		else:
			opcodes = _OpCodesFloat

		# Put these into the arrays which will be passed to the interpreter.
		codearray = array.array('I', [opcodes[x.opcode] for x in nodelist])

		varcodes = list(map(lambda x: x.param if x.opcode == 'pushvar' else 0, nodelist))
		varoffsetarray = array.array('I', varcodes)

		# The const array type needs to be the same as the data array type.
		constcodes = list(map(lambda x: x.param if x.opcode == 'pushconst' else 0, nodelist))
		constarray = array.array(self._ArrayType, constcodes)


		return codearray, varoffsetarray, constarray



	########################################################
	def comp(self, equation, arrayname, paramnames):
		"""Compile the equation. The variables used in the equation must match 
		the names used in the 'arrayname' and 'paramnames' parameters. The data 
		type of calculation will be determined by the array type.
		Parameters: equation (string) = The equation to solve.
			arrayname (string) = The name of the current array element as
				used in the equation.
			paramnames (tuple) = A tuple or list of strings specifying the 
				additional parameter names. 
		Returns: Nothing. An exceptions will be raised if an error is 
			encountered.
		"""

		self._ParamNames = paramnames

		# Make sure that we are not attempting to use any Python keywords, or
		# the names 'math' or 'abs' as a variable name. 
		badparams = self._CheckParamKeywords(arrayname, paramnames)
		if badparams:
			raise ValueError('"%s" may not be used as a variable name in ACalc compile.' % '", "'.join(badparams))



		# Do a simple parentheses count to see if there is a missing'(' or ')'.
		# This does not check actual syntax. However, this is a simple test so 
		# it pays to do a simple check first for a missing one in order to give 
		# a better one in order to give a better error message.
		if equation.count('(') != equation.count(')'):
			raise ValueError('unbalanced parentheses in ACalc compile.')


		# Check for known invalid tokens.
		invalidtokens = set(equation) & set(_InvalidTokens)
		if invalidtokens:
			raise ValueError('invalid tokens in ACalc compile: %s.' % ', '.join(invalidtokens))



		# Parse the equation into an AST tree.
		try:
			astnode = ast.parse(equation, mode='eval')
		except SyntaxError as inst:
			# inst.args[1][2] extracts the character position where an error was found,
			# and inst.args[1][3] repeats the equation itself.
			raise SyntaxError('invalid syntax in equation in ACalc compile in position %d  %s.' %(inst.args[1][2], inst.args[1][3]))



		# Check to see if all nodes are of the supported type.
		if not self._AllNodesValid(astnode):
			raise ValueError('unsupported element in equation in ACalc compile.')


		# Make sure the function calls are to valid function names.
		if not self._AllFuncCallsValid(astnode):
			raise ValueError('unsupported function call in equation in ACalc compile.')



		# Parse out the equation string. This will not find all errors.
		try:
			eqcomp = AnalyseCode(arrayname)
			eqcomp.visit(astnode)
		except SyntaxError as errcode:
			raise SyntaxError('parsing error in ACalc compile: %s' % errcode)
		except:
			raise ValueError('unknown compile error in ACalc compile.')



		# Filter out the excess component in function calls.
		opcodelist = eqcomp.GetOpCodes()


		# Convert any unary usub '-' or uadd '+' associated with a constant
		# to an actual signed number. 
		opcodelist = self._FilterUSubConst(opcodelist)

		# Convert the constants to the correct types.
		opcodelist = self._ConvertConstants(opcodelist)


		# Check that the opcodes are consistent with the types. An exception 
		# will be raised if any invalid ops are encountered.
		# All usub operations associated with constants should have been removed 
		# before this point, and the signs transferred to the constants 
		# themselves so that we don't have confusing error messages.
		self._CheckOpCodes(opcodelist)


		# Check for stack overflow.
		stackok, stackdepth = self._CheckStack(opcodelist)
		if not stackok:
			raise ValueError('stack overflow or underflow in ACalc compile.')


		# Create the stack array with the correct depth.
		self._VMStack = array.array(self._ArrayType, [0] * (stackdepth * self._VMStackSegments))


		# Assign the variables and constants to register indices.
		opcodelist, paramorder = self._AssignToRegisters(opcodelist, arrayname, self._ParamNames)

		# Compile to byte code.
		self._codearray, self._varoffsetarray, self._constarray = self._CompileToByteCode(opcodelist)



	########################################################
	def execute(self, params, disovfl=False, maxlen=0):
		"""Execute the compiled equation, and return the result.
		Parameters: params (list) = A list of the parameters in the same order
			as declared in the compile stage.
			disovfl (boolean) = If True, disable overflow checking. This is an
				optional keyword parameter.
			maxlen (integer) = The maximum length of array to use. If zero,
				the entire array will be operated on.
		Returns: (value) = The calculated value.
		"""
		# The variable array needs to be the same data type as the data array.
		vararray = array.array(self._ArrayType, params)

		arrayfunc.acalcvm(self._codearray, self._varoffsetarray, 
				vararray, self._constarray, self._VMStack, 
				self._DataArray, self._DataOutArray, self._VMStackSegments, 
				disovfl=disovfl, maxlen=maxlen)


##############################################################################

