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


# Documentation and op codes.
echo "Generating:  docsgen.py"
./docsgen.py
filecount=$(($filecount + 1))
echo "Generating:  opcodes.py"
./opcodes.py
filecount=$(($filecount + 1))


# Time at which the test sequence completed.
endtime=$(date '+%s')
elapsedtime=$(($endtime - $starttime))
echo
echo "Generated " $filecount " files in" $elapsedtime "seconds."

