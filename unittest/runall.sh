#!/bin/sh

# Run all the unit tests associated with Arrayfunc.

# Get the command line arguments.
testname=$1
packsource=$2
fileprefix=$3

echo
echo "Running unit tests."

# Test library version.
# Find out if running on BSD. FreeBSD and OpenBSD use "pip" instead of "pip3".
# Linux uses "pip3". uname for FreeBSD and OpenBSD is their names as written here.
# Since we have to run on BSD, we can't use Bash built-ins for string comparions
# and so have to do it the hard way.
platform=$( uname )
echo "OS platform $platform detected."
if echo "$platform" | grep -q "BSD"; then
	af_version=$( pip show arrayfunc | grep Version | cut -d: -f2)
else
	af_version=$( pip3 show arrayfunc | grep Version | cut -d: -f2)
fi


# This program resets the test log file and inserts a time stamp and
# information about the test platform in the top of the file.
./unit-test-timestamp.py $testname $packsource $fileprefix $af_version


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

