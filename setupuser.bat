REM MS Windows version.
REM This script will do a simple user local setup of arrayfunc. 
REM Call setup.py directly with the appropriate options if you wish to have a
REM different type of install.

REM This requires the python Windows launcher to be present.

echo off


REM This tells distutils that Visual Studio isn't installed, just the compiler.
SET DISTUTILS_USE_SDK=1

REM Set the environment variables.
call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build"\vcvarsall.bat amd64
ECHO ON

ECHO Setting path next.

REM This adds the paths to the required compiler components.
SET PATH=C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.10.25017\bin\HostX64\x64;C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.10.25017\lib\x64;C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.10.25017\include;C:\Program Files (x86)\Windows Kits\10\Include\10.0.15063.0\ucrt;%PATH%

echo Running ArrayFunc build as a local install. 
echo Compiler messages are redirected to af_compile_results.txt

ECHO Running the setup.py

setup.py install --user 2> af_compile_results.txt

echo Setup complete. Check af_compile_results.txt for errors.
