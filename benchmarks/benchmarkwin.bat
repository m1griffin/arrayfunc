REM Benchmark all the functions associated with arrayfunc.

echo off

echo "Testing general functions benchmarks."

REM This one does not get automatically regenerated.
benchfuncs.py

REM ============================================================================

echo "Testing math functions benchmarks."

benchmath.py

REM ============================================================================

