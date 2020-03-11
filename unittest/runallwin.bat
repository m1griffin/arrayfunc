echo off

REM Run all the tests associated with arrayfunc.


REM ==============================================================

REM This program resets the test log file and inserts a time stamp and
REM information about the test platform in the top of the file.
REM Pass all parameters through to the Python program (as many as possible). 
unit-test-timestamp.py %1 %2 %3 %4 %5 %6 %7 %8 %9


SET failcount=0

FOR /R %%A IN (test_*.py) DO CALL :pytest %%A

IF %failcount% EQU 0 GOTO :DONE
ECHO Testing failed with %failcount% errors.
GOTO:EOF

:DONE
ECHO Done - OK
EXIT /B

REM Subroutine pytest =============================================
:pytest
echo "Testing: " %1
%1 -l
IF ERRORLEVEL 1 SET /A failcount += 1

EXIT /B

