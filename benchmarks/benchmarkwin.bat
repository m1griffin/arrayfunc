REM Benchmark all the functions associated with arrayfunc.

echo off

echo "Testing amap benchmarks."

benchamap.py

REM ============================================================================

echo "Testing acalc benchmarks."

benchacalc.py

REM ============================================================================

echo "Testing other funcsions benchmarks."

REM This one does not get automatically regenerated.
benchfuncs.py

