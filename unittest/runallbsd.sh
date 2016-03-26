#!/bin/sh

# Run all the tests associated with arrayfunc.

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
		failcount=$(($failcount + 1))
	fi

done

# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))

# Indicate whether a test failed or not.
if [ $failcount -ne 0 ]
then 
	echo $failcount " tests failed."
else
	echo "All tests passed in" $elapsedtime "seconds."
fi

