@echo off
echo Starting working_all.py...
if not exist "C:\gh\oomlout_base\lock" mkdir "C:\gh\oomlout_base\lock"
echo %TIME% > "C:\gh\oomlout_base\lock\working_all.lock"
cd /d "%~dp0"
python working_all.py
python working_all.py
del "C:\gh\oomlout_base\lock\working_all.lock"
echo Done!
pause
