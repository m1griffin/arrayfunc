#!/bin/sh

# Benchmark all the functions associated with arrayfunc.


# Get rid of the old files.
rm arrayfunc/*.so
rm arrayfunc/*.py

# Copy the module libraries here.
cp ../arrayfunc/*.so arrayfunc
cp ../arrayfunc/__init__.py arrayfunc
cp ../arrayfunc/arrayops.py arrayfunc


# This is the name of the main benchmark program.
benchfile="benchmark.py"

# Check if there is a newer version of the benchmark program.
if [ -f ../codegen/$benchfile ]
	then
	echo "Copying in a new version of the benchmark program."
	# Delete the old file.
	rm $benchfile
	# Copy in the new file.
	mv ../codegen/$benchfile .
	# Set the permissions bit to execute.
	chmod a+x $benchfile 
fi


echo "Testing amap benchmarks."

# Time at which the test sequence started.
starttime=$(date '+%s')

./$benchfile

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Amap benchmarks completed in " $elapsedtime " seconds."
echo

echo "Testing other funcsions benchmarks."

# Time at which the test sequence started.
starttime=$(date '+%s')

# This one does not get automatically regenerated.
./benchfuncs.py

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

echo "Other funcsions benchmarks completed in " $elapsedtime " seconds."

