#!/bin/bash
# This expects arrayfunc to be installed somewhere where it is visible.


# This program resets the test log file and inserts a time stamp and
# information about the test platform in the top of the file.
# The $@ parameter passes all parameters given to the shell script
# through into the Python program.
./unit-test-timestamp.py $@

# Time at which the test sequence started.
starttime=$(date '+%s')

failcount=0
for utest in `ls test_*.py`

do
	# Construct the test to run.
	CMD="./"$utest
	echo "Testing: " $CMD
	# Run the test.
	$CMD -l
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

