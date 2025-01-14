#!/bin/sh

# Run all the unit tests associated with Arrayfunc.

# Get the command line arguments.
# The first must be the package name for what is being tested (e.g. arrayfunc).
# This first parameter will be used in looking up package data so it must
# be correct.
# The second is the source of the package (e.g. 'local', 'pypi', etc.).
# It is simpy inserted into the report.
# The third is a name used to describe the platform OS (e.g. Ubuntu2404).
# It is simply inserted into the report.
# If these are not specified, some default values will be used instead.
#
testname=$1
packsource=$2
fileprefix=$3

# This is the file the unit test data is written into.
utfilename="af_unittest.txt"

# Provide some defaults for the arguments in the event they were
# not specified.
if [ -z $testname ]; then
	testname='arrayfunc'
fi

if [ -z $packsource ]; then
	packsource='unspecified'
fi

if [ -z $fileprefix ]; then
	fileprefix='unspecified'
fi

# ======================================================================

echo
echo "Running unit tests."


# Delete any existing version as otherwise the new version will append onto it.
if [ -e "$utfilename" ]; then
	rm "$utfilename"
fi

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
	# Count up how many failures.
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

# ======================================================================

# The unit tests have been run, but now we will collect some data about
# the test evironment and summarize the pass / fall to put into a report.

# Test library version.
# This checks if this version of Python as the importlib.metadata library.
hasimpmd=$( ./reportdatacheck.py )
# If not, then we need to do a bit of a work-around in order to find out
# which library version is installed.
if [ $hasimpmd!='OK' ]; then
	# Find out if running on BSD. FreeBSD and OpenBSD use "pip" instead of "pip3".
	# Linux uses "pip3". uname for FreeBSD and OpenBSD is their names as written here.
	# Since we have to run on BSD, we can't use Bash built-ins for string comparions
	# and so have to do it the hard way.
	platform=$( uname )
	echo "OS platform $platform detected."
	if echo "$platform" | grep -q "BSD"; then
		af_version=$( pip show "$testname" | grep Version | cut -d: -f2)
	else
		af_version=$( pip3 show "$testname" | grep Version | cut -d: -f2)
	fi
else
	# If importlib.metadata is available then unittestdata.py can find the
	# library version for itself and we don't need to supply it.
	af_version=''
fi


# This will collect information about the test environment and then
# summarize the pass / fail criteria.
./reportunittest.py $testname $packsource $fileprefix $utfilename $af_version > reportunittestresult.txt

cat $utfilename >> reportunittestresult.txt
mv reportunittestresult.txt $utfilename
