"""The ArrayFunc module provides high speed array processing functions 
for use with the standard Python array module. These functions are 
patterned after the functions in the standard Python Itertools module 
together with some additional ones from other sources.

The list of valid array operations may be found in the arrayops module 
as aops data. e.g. arrayfunc.aops.af_add
"""

from arrayfunc.arrayops import aops

from arrayfunc.count import *
from arrayfunc.cycle import *
from arrayfunc.repeat import *

from arrayfunc.afilter import *
from arrayfunc.takewhile import *
from arrayfunc.dropwhile import *
from arrayfunc.compress import *

from arrayfunc.aall import *
from arrayfunc.aany import *
from arrayfunc.amax import *
from arrayfunc.amin import *
from arrayfunc.asum import *
from arrayfunc.findindex import *
from arrayfunc.findindices import *

from arrayfunc.amap import *
from arrayfunc.amapi import *
from arrayfunc.starmap import *
from arrayfunc.starmapi import *

from arrayfunc.convert import *

from arrayfunc.arraylimits import *
from arrayfunc.arrayguardbands import *
