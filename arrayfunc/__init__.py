"""The ArrayFunc module provides high speed array processing functions 
for use with the standard Python array module. These functions are 
patterned after the functions in the standard Python Itertools module 
together with some additional ones import other sources.

The list of valid array operations may be found in the arrayops module 
as aops data. e.g. arrayfunc.aops.af_add
"""

from arrayfunc.arrayops import aops

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

from arrayfunc.amap import amap
from arrayfunc.amapi import amapi
from arrayfunc.starmap import starmap
from arrayfunc.starmapi import starmapi

from arrayfunc.convert import convert

import arrayfunc.acalc
from arrayfunc.acalcvm import acalcvm

import arrayfunc.arraylimits
import arrayfunc.arrayguardbands
