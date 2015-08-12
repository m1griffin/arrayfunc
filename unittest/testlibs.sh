#!/bin/bash

# Run all the tests associated with arrayfunc.


# Get rid of the old files.
rm arrayfunc/*.so
rm arrayfunc/*.py

# Copy the module libraries here.
cp ../arrayfunc/*.so arrayfunc
cp ../arrayfunc/__init__.py arrayfunc
cp ../arrayfunc/arrayops.py arrayfunc


# Copy any new tests from the test generation directory to here.
for ufile in `ls ../codegen/test_*.py`

do
	 # Get just the file name.
	 tfile=${ufile:11}
	 # Delete the old file.
	 rm $tfile
	 # Copy in the new file.
	 mv $ufile .
	 # Set the permissions bit to execute.
	 chmod a+x $tfile 
done



# Time at which the test sequence started.
starttime=$(date '+%s')

failcount=0
for utest in `ls test_*.py`

do
	# Construct the test to run.
	CMD="./"$utest
	echo "Testing: " $CMD
	# Run the test.
	$CMD
	result=$?
	# Speak a failure message, and count up how many failures.
	if [ "$result" -ne 0 ]
	then 
		espeak -s 120 -v en  $utest" failed." 2> /dev/null
		failcount=$(($failcount + 1))
	fi

done

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

# Speak whether a test failed or not.
if [ $failcount -ne 0 ]
then 
	echo $failcount " tests failed."
	espeak -s 120 -v en $failcount" tests failed." 2> /dev/null
else
	echo "All tests passed in" $elapsedtime "seconds."
	espeak -s 120 -v en "All tests passed." 2> /dev/null
fi

