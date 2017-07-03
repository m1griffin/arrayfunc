#!/bin/sh

# Benchmark all the functions associated with arrayfunc.


echo "Testing amap benchmarks."

# Time at which the test sequence started.
starttime=$(date '+%s')

./benchamap.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Amap benchmarks completed in " $elapsedtime " seconds."
echo

# ==============================================================================

echo "Testing acalc benchmarks."

# Time at which the test sequence started.
starttime=$(date '+%s')

./benchacalc.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Acalc benchmarks completed in " $elapsedtime " seconds."
echo

# ==============================================================================


echo "Testing other functions benchmarks."

# Time at which the test sequence started.
starttime=$(date '+%s')

# This one does not get automatically regenerated.
./benchfuncs.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Other functions benchmarks completed in " $elapsedtime " seconds."

