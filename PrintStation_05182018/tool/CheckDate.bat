@echo off
SET PATH="%~dp0";".\inout\";"C:\Python27\";"C:\Program Files\Kinetic\kinetic\";
echo %PATH%
echo %CD%
ksleep 1000
echo "checking date...."
%~dp0checkdate.py
set testErrorCode=%errorlevel%
echo "checking date....[%testErrorCode%]"
ksleep.exe 5000
exit %testErrorCode%