#!/usr/bin/env python3

# 6-Oct-2024
# M. Griffin
# 
# This is a simple test to see if importlib.metadata is present.
# This is needed for working with older versions of Python in some distros.
#

try:
	import importlib.metadata
	print('OK')
except:
	print('error')
