@echo off
set current_dir=%~dp0
set python_dir=%current_dir%
set seven_zip_dir=%current_dir%7-Zip Extra

:: Check if the Python-3.12.4 directory exists
if not exist "%python_dir%python-3.12.4" (
    echo Python-3.12.4 directory does not exist, extracting...
    "%seven_zip_dir%\7za.exe" x "%current_dir%python-3.12.4.7z" -o"%python_dir%"
    if errorlevel 1 (
        echo Extraction failed.
        pause
        exit /b 1
    )
    echo Extraction completed.
)

:: Ensure paths are correctly formatted
set "python_exe=%python_dir%\python-3.12.4\python.exe"

:: Run pip_upgrade.bat to upgrade pip
call "%current_dir%pip_upgrade.bat"

:: Run the Python script
if exist "%python_exe%" (
    "%python_exe%" "%current_dir%main.py"
) else (
    echo Python executable not found at "%python_exe%".
)
pause
