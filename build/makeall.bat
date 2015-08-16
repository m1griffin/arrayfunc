
REM Copy the build and source files into the build directory.
COPY ..\conf\*.py .
COPY ..\src\*.h .
COPY ..\src\*.c .


SET failcount=0

FOR /R %%A IN (*setup.py) DO CALL :pybuild %%A

IF failcount EQU 0 GOTO :DONE
ECHO Compile failed with %failcount% errors.
GOTO:EOF

:DONE
# Copy the object files into the arrayfunc directory.
COPY *.pyd ..\arrayfunc
ECHO Done - OK
EXIT /B

REM Subroutine pybuild =============================================
:pybuild
\python34\python %1 build_ext --inplace
IF ERRORLEVEL 1 SET /A failcount += 1

EXIT /B

