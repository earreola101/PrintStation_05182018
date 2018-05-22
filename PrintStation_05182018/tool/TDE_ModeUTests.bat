@echo off
SET PATH="%~dp0";".\inout\";"C:\Python27\";"C:\Program Files\Kinetic\kinetic\";
echo %PATH%
echo %CD%
ksleep 1000
echo "checking date...."
%~dp0TDE_ModeUTests.py
set testErrorCode=%errorlevel%
echo "[%testErrorCode%]"
ksleep.exe 5000
pause
exit %testErrorCode%