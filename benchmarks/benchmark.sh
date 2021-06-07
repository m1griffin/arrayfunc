#!/bin/sh

# Benchmark all the functions associated with arrayfunc.

# ==============================================================================

echo "Testing benchmarks." $(date)

# Time at which the test sequence started.
starttime=$(date '+%s')

# This is used to run the benchmarks. Benchmark parameters can be
# altered via command line parameters.
./benchall_af.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Benchmarks completed in " $elapsedtime " seconds."
echo

# ==============================================================================
