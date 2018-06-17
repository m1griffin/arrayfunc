#!/bin/sh

# Benchmark all the functions associated with arrayfunc.

# ==============================================================================


echo "Testing general functions benchmarks."

# Time at which the test sequence started.
starttime=$(date '+%s')

# This one does not get automatically regenerated.
./benchfuncs.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "General functions benchmarks completed in " $elapsedtime " seconds."


# ==============================================================================


echo "Testing math functions benchmarks."

# Time at which the test sequence started.
starttime=$(date '+%s')

./benchmath.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Math functions benchmarks completed in " $elapsedtime " seconds."
echo

# ==============================================================================

