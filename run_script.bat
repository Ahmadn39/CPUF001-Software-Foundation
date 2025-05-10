@echo off
REM Ensure correct usage
if "%~1"=="" (
    echo Usage: run_script.bat ^<input_file^>
    exit /b 1
)

REM Run the Python processing file with input file arguments
python processing.py %1
