echo off

REM Run all the tests associated with arrayfunc.


REM ==============================================================

SET failcount=0

FOR /R %%A IN (test_*.py) DO CALL :pytest %%A

IF failcount EQU 0 GOTO :DONE
ECHO Testing failed with %failcount% errors.
GOTO:EOF

:DONE
ECHO Done - OK
EXIT /B

REM Subroutine pytest =============================================
:pytest
%1
IF ERRORLEVEL 1 SET /A failcount += 1

EXIT /B

