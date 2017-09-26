echo off

REM Run all the tests associated with arrayfunc.


REM ==============================================================

REM This program resets the test log file and inserts a time stamp and
REM information about the test platform in the top of the file.
unit-test-timestamp.py


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

