#!/bin/sh
# This script will do a simple user local setup of arrayfunc. 
# Call setup.py directly with the appropriate options if you wish to have a
# different type of install.

echo Running ArrayFunc build as a local install. 
echo Compiler messages are redirected to af_compile_results.txt

echo `date` > af_compile_results.txt
./setup.py install --user 2>> af_compile_results.txt

echo Setup complete. Check af_compile_results.txt for errors.
