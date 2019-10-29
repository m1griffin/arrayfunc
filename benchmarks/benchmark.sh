#!/bin/sh

# Benchmark all the functions associated with arrayfunc.

# ==============================================================================

# Get the command line arguments.
argsvals=$( echo $@ )

echo "Testing benchmarks." $(date)

# Time at which the test sequence started.
starttime=$(date '+%s')

# The benchmarks.
./benchmarks.py $argsvals

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Benchmarks completed in " $elapsedtime " seconds."
echo

# ==============================================================================

