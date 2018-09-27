#!/bin/sh

# Benchmark all the functions associated with arrayfunc.

# ==============================================================================


echo "Testing benchmarks." $(date)

# Time at which the test sequence started.
starttime=$(date '+%s')

./benchmarks.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Benchmarks completed in " $elapsedtime " seconds."
echo

# ==============================================================================

