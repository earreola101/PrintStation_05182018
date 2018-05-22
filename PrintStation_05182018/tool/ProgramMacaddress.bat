@echo off
SET PATH="%~dp0";".\inout\";"C:\Python27\";"C:\Program Files\Kinetic\kinetic\";
echo %PATH%
echo %CD%
ksleep 1000
set /p Ethernet_Macaddress=<"C:\tstPlan\ETHERNET_MACADDRESS.txt"
echo "Program Macaddress"

rem batch file way
%~dp0tools\tdebt.exe "-c tablehub -s tablehub_eth_mac "%Ethernet_Macaddress%

rem python way
rem %~dp0Write_TableHub_Ethernet_Macaddress.py %Ethernet_Macaddress%
echo %errorlevel%
set testErrorCode=%errorlevel%

echo "Program Macaddress [%testErrorCode%]"

ksleep.exe 5000

exit %testErrorCode%