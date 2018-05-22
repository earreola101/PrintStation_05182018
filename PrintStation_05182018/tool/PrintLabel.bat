@echo off
SET PATH="%~dp0";"%~dp0tool\";"%~dp0inout\";"C:\Python27\";"C:\Program Files\Kinetic\kinetic\";
echo %PATH%
echo %CD%
echo "%~dp0PrintStation\"
echo "Printing Label"
set /p Ethernet_Macaddress=<"C:\tstPlan\ETHERNET_MACADDRESS.txt"
echo -------[%Ethernet_Macaddress%]
rem /////// add print label command below ////
echo -------[START]-------
echo "run.py"
%~dp0run.py
set testErrorCode=%errorlevel%
echo "exit code[%errorlevel%]"
rem python run.py %Ethernet_Macaddress%
rem TDE_PrintLabel.exe Fireball_03.lbx "SN:1711CE0006EF,MAC:%Ethernet_Macaddress%"
rem ///////////////////////////////////////////
echo -------[END]-------
ksleep.exe 5000
exit %testErrorCode%