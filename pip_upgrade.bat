@echo off
set current_dir=%~dp0
"%current_dir%\Python-3.12.4\python.exe" -m pip install --upgrade pip
"%current_dir%\Python-3.12.4\python.exe" -m pip install requests
"%current_dir%\Python-3.12.4\python.exe" -m pip install pyinstaller
"%current_dir%\Python-3.12.4\python.exe" -m pip install beautifulsoup4
pause