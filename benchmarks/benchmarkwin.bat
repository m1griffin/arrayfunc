REM Benchmark all the functions associated with arrayfunc.


echo "Testing amap benchmarks."

benchmark.py

REM ============================================================================

echo "Testing acalc benchmarks."

acalcbenchmark.py

REM ============================================================================

echo "Testing other funcsions benchmarks."

REM This one does not get automatically regenerated.
benchfuncs.py

