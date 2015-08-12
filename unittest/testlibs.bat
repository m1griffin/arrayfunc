echo off

REM Run all the tests associated with arrayfunc.

del arrayfunc\*.pyd
del arrayfunc\__init__.py
del arrayfunc\arrayops.py

copy ..\arrayfunc\*.pyd arrayfunc
copy ..\arrayfunc\__init__.py arrayfunc
copy ..\arrayfunc\arrayops.py arrayfunc

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
\python34\python %1
IF ERRORLEVEL 1 SET /A failcount += 1

EXIT /B

