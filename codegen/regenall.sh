#!/bin/sh
# Regenerate all the code from scripts.

# Time at which the code generation sequence started.
starttime=$(date '+%s')

filecount=0

# C code generation.
for codetarget in `ls *_codegen.py`

do
	# Skip this file. $0 is the name of the invoked script.
	if [ "./$codetarget" != $0 ]
    then
		echo "Generating: " $codetarget
		# Run the file.
		"./"$codetarget
		filecount=$(($filecount + 1))
	fi
done

# Move C source files.
for csource in `ls *.c`

do

	# Move it to the C source code directory.
	mv $csource ../src

done

# Move C source headers.
for csource in `ls *.h`

do

	# Move it to the C source code directory.
	mv $csource ../src

done



# Unit test code generation.
for codetarget in `ls *_testgen.py`

do
	# Skip this file. $0 is the name of the invoked script.
	if [ "./$codetarget" != $0 ]
    then
		echo "Generating: " $codetarget
		# Run the file.
		"./"$codetarget
		filecount=$(($filecount + 1))
	fi
done


for utest in `ls test_*.py`

do

	# Set executable bit
	chmod +x $utest

	# Move it to the unit test directory.
	mv $utest ../unittest

done


# TODO: Remove.
# Documentation and op codes.
#echo "Generating:  docsgen.py"
#./docsgen.py
#filecount=$(($filecount + 1))


# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))
echo
echo "Generated " $filecount " files in" $elapsedtime "seconds."

