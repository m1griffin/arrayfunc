#!/bin/bash

# 12-Dec-2022
# Build a new version, updating the documentation.
# This assembles all the documentation files, but does not recompile
# the source or build a new package.
# The following should be present first:
# 1) The main documentation template and readme templates should be
#    updated if necessary.
# 2) The version file should be updated with the new version number.
# 3) The release history file should be updated with the new data.
# 4) An up to date vmsummary table should be present in the current 
#    directory.
# 5) An up to date version of the benchmark files should be present in 
#    the benchmarks directory.
#
# This script will:
# 1a) Update the main documentation file, 
# 1b) move it to the docs directory,
# 1c) call the script to build the PDF version,
# 1d) call the script to build the HTML version.
# 2a) Update the README file,
# 2b) and move it to the main directory.
#
# This script does not update the __init__.py file.
#
# The setup.py file imports the version number directly and so does not
# need to be changed to update the version.

# Main documenation:
./docgenmath.py

docfile="ArrayFunc.rst"

# Update the main documentation file.
if [ -e "$docfile" ]; then
	echo "Updated $docfile"
	cd ../docs
	mv "../codegen/$docfile" .
	echo "Updating PDF"
	./arrayfunc2pdf.sh
	echo "Updating HTML"
	./makehtml.sh
	cd ../codegen
else
	echo "Failure when updating $docfile"
fi

# Readme file:

readmefile="README.rst"
# Update the README file.
if [ -e "$readmefile" ]; then
	echo "Updated $readmefile"
	mv "$readmefile" ../
else
	echo "Failure when updating $readmefile"
fi


