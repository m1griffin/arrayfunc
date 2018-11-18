"""The ArrayFunc module provides high speed array processing functions 
for use with the standard Python array module. These functions are 
patterned after the functions in the standard Python Itertools module 
together with some additional ones import other sources.

"""

from arrayfunc.count import count
from arrayfunc.cycle import cycle
from arrayfunc.repeat import repeat

from arrayfunc.afilter import afilter
from arrayfunc.takewhile import takewhile
from arrayfunc.dropwhile import dropwhile
from arrayfunc.compress import compress

from arrayfunc.aall import aall
from arrayfunc.aany import aany
from arrayfunc.amax import amax
from arrayfunc.amin import amin
from arrayfunc.asum import asum
from arrayfunc.findindex import findindex
from arrayfunc.findindices import findindices

from arrayfunc.convert import convert

import arrayfunc.simdsupport
import arrayfunc.arraylimits
import arrayfunc.arrayguardbands

from arrayfunc.neg import neg
from arrayfunc.abs_ import abs_
from arrayfunc.factorial import factorial
from arrayfunc.invert import invert

from arrayfunc.and_ import and_
from arrayfunc.or_ import or_
from arrayfunc.xor import xor
from arrayfunc.lshift import lshift
from arrayfunc.rshift import rshift

from arrayfunc.add import add
from arrayfunc.mul import mul
from arrayfunc.sub import sub
from arrayfunc.truediv import truediv
from arrayfunc.floordiv import floordiv
from arrayfunc.mod import mod
from arrayfunc.pow import pow

from arrayfunc.eq import eq
from arrayfunc.ne import ne
from arrayfunc.gt import gt
from arrayfunc.ge import ge
from arrayfunc.lt import lt
from arrayfunc.le import le

from arrayfunc.acos import acos
from arrayfunc.acosh import acosh
from arrayfunc.asin import asin
from arrayfunc.asinh import asinh
from arrayfunc.atan2 import atan2
from arrayfunc.atan import atan
from arrayfunc.atanh import atanh
from arrayfunc.ceil import ceil
from arrayfunc.copysign import copysign
from arrayfunc.cos import cos
from arrayfunc.cosh import cosh
from arrayfunc.degrees import degrees
from arrayfunc.erf import erf
from arrayfunc.erfc import erfc
from arrayfunc.exp import exp
from arrayfunc.expm1 import expm1
from arrayfunc.fabs import fabs
from arrayfunc.floor import floor
from arrayfunc.fmod import fmod
from arrayfunc.gamma import gamma
from arrayfunc.hypot import hypot
from arrayfunc.isfinite import isfinite
from arrayfunc.isinf import isinf
from arrayfunc.isnan import isnan
from arrayfunc.ldexp import ldexp
from arrayfunc.lgamma import lgamma
from arrayfunc.log10 import log10
from arrayfunc.log1p import log1p
from arrayfunc.log2 import log2
from arrayfunc.log import log
from arrayfunc.radians import radians
from arrayfunc.sin import sin
from arrayfunc.sinh import sinh
from arrayfunc.sqrt import sqrt
from arrayfunc.tan import tan
from arrayfunc.tanh import tanh
from arrayfunc.trunc import trunc
