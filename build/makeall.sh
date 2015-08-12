#!/bin/sh

# Time at which the compile sequence started.
starttime=$(date '+%s')

filecount=0
failcount=0

# Copy the build and source files into the build directory.
cp ../conf/*.py .
cp ../src/*.h .
cp ../src/*.c .


# Compile the source files.
for comptarget in `ls *setup.py`
do
	echo "Compiling: " $comptarget
	# Compile the file.
	./$comptarget build_ext --inplace
	result=$?
	if [ "$result" -ne 0 ]
	then 
		espeak -s 120 -v en  $comptarget" failed." 2> /dev/null
		failcount=$(($failcount + 1))
	fi
	if [ "$result" -eq 0 ]
	then 
		filecount=$(($filecount + 1))
	fi
done


# Copy the object files into the arrayfunc directory.
mv *.so ../arrayfunc


# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))
echo
echo "Compiled " $filecount " files in" $elapsedtime "seconds."

if [ "$failcount" -ne 0 ]
then 
	echo "Errors when compiling " $failcount " files."
	espeak -s 120 -v en  "Failed to compile "$failcount" files" 2> /dev/null
fi

