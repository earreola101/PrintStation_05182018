#//******************************************************************************************************************************
#//  Copyright (c) 1999-2017 Logitech, Inc.  All Rights Reserved
#//
#//  This program is a trade secret of LOGITECH, and it is not to be reproduced,
#//  published, disclosed to others, copied, adapted, distributed or displayed
#//  without the prior authorization of LOGITECH.
#//
#//  Licensee agrees to attach or embbed this notice on all copies of the program,
#//  including partial copies or modified versions thereof.
#//
#//  Description:
#//
#//  Created by Eduardo Arreola
#//******************************************************************************************************************************
import subprocess
import sys
import string
import os
import random
import datetime
import time
from time import sleep
from time import gmtime, strftime
from shutil import copyfile


TDETOOLPATH=r"./tools/tdebt.exe";
class BolideLib:
	TST_PLAN_SCAN_MAC=r"C:/tstplan/ETHERNET_MACADDRESS.txt";
	#Versions
	FW_TDEBT_VERSION="1.0.66";
	FW_TVHUB_VERSION="1.0.211"
	FW_TABLEHUB_VERSION="1.0.202"
	FW_BLE_VERSION="1.0.11"
	ERROR_MESSAGE="No errors detected.";
	FW_TVHUB_PIDVID="";
	#PATHS
	DATETIME_SER=r"\\172.17.159.36\Sharing\Bolide\date.inf";

	dest_path = r"C:\TEMP"
	
	DataFilePath='./HDMIData.csv';
	outTestDataFile="./inout/Test.out";
	inTestDataFile="./inout/Test.in";
	#BT server APP will write Internet "Date" on PM 24:00 
	#Everyday into one .ini file (the file name will be fixed in "date.ini")
	#read "Date" from server ini during initial stage and compare with 
	#local PC time for correction or not.
	#will create ini file if not exist which would be 
	#occurred when P_line changed testing PC or setup new line.
	#load server path " \\172.17.159.36\Sharing\Bolide" from .TXT file
	#we can manually change path to local to resume P_line build once server shut down accidentally.

	#UID
	UID_FORMAT="PID:YYYYmmdd:<macaddress>";
	SIM_UID="{0x0889:20180508:001122334455}";

	#Flags
	m_DeviceCheckCount=10;     #The number of times that will be checked before returning printer failure mode. 
	m_UID_Present=False;       #Track the UID flag being present. 
	m_Printer_Present=False;   #Track the printer present.
	m_DeviceDUT_present=False; #Track the device DUT.
	m_UID_DUT_Readback="NULL"; #Macaddress read back value.

	#Error Codes
	ERROR_PRINTER_DUT_FAILURE=0x01;                #attempted to print again up too N times but still failed. 
	ERROR_READ_UID_TABLE=0x02;                     #return string UID validity check. failed if the validity check failed. 
	ERROR_DATE_UID_LOCALTIME_OR_BADSTR=0x03        #the local time does not match as expected.
	ERROR_PERIODIC_VISUAL_INSPECTION_FAULURE=0x04; #if the date is not a match with local date  
												   #then the station will fail dut.
												   #otherwise continue.
	ERROR_GENERAL_PRINTER_FAILURE=0x05;            #general printer failure.
	ERROR_INSTRUCTION_PHYSICAL_PLACEMENT=0x06;     # physical instruction placement error.
	ERROR_VISUAL_CHECK_FAILED=0x07                 #visual check issue.
	ERROR_BARCODE_SCANNER_FAILURE=0x08;            #scanned bar code error or failure.
	ERROR_LABEL_PLACEMENT_READ_BACK_FAILED=0x09;   #Label placement read back error. 
    	#table hub commands
	def GetTVHUB_HardwareVersion():
		#returns the hardware version for the PCB type.
		
		return;
		
	def GetTVHUB_FirmwareVersion():
		#returns the sofyware version for the firmware binary.
		return;
		
	def GetTVHUB_ValensInitStatus():
		#returns the valens chip successful initialization status.
		return;
		
	def GetTVHUB_GUID():
		#return the TVHUB GUID unique number.
		return;

	def StTVHUB_GUID():
		#writes the TV HUB GUID number.
		return;
		
	def SetTVHUB_TestTracking():
		#write the test tracking data buffer.
		return;	

	def GetTVHUB_TestTracking():
		#read the test tracking data buffer.
		return;
		
	def SetTVHUB_BluetoothMacaddress():
		#write the bluetooth macaddress.
		return;
		
	def GetTVHUB_BluetoothMacaddress():
		#read the bluetooth macaddress.
		return;	

	def SetTVHUB_DeviceName():
		#write the bluetooth macaddress.
		return;	
		
	def GetTVHUB_DeviceName():
		#read the bluetooth macaddress.
		return;
		
	def GetTVHUB_Device_Manufacturing_Name():
		#read device manufacturing name.
		return;

	def SetTVHUB_Device_Manufacturing_Name():
		#write device manufacturing name.
		return;	

	def GetTVHUB_Bluetooth_TX_Frequency():
		#read device Bluetooth_TX_Frequency.
		return;		
		
	def SetTVHUB_Bluetooth_TX_Frequency():
		#write device Bluetooth_TX_Frequency.
		return;

	def SetTVHUB_USB_HUB_Mode():
		#write device USB HUB Mode.
		return;
		
	def GetTVHUB_Speaker_HUB_Connection_Status():
		#read speaker hub connection status
		return;
		
	def GetsTVHUB_The_Hub_USB_Cable_Connection_Status():
		#read the hub usb cable connection status.
	   return;	
		
	def GetTVHUB_Valens_Connection_Status():
	  #read the tv hub valens connection status.
	  return;


def GetTVHUB_USBPIDVID():
	#returns the PIDVID from memory in the.
    tvhubPIDVID=runCmdx(" -c tvhub -g btusbpidvid");
    return tvhubPIDVID;
	
#Table Hub APIs
#SetTableHubSecurityIC/UIDControl()
def SetTableHubSecurityIC_UIDControl():
    return;

#SetTableHubOPT_SecuirtyIC
#sets the security ID chip applied OPT permanent function.
def SetTableHubOPT_SecuirtyIC():
    success=False;
    return success;

#GetTableHubSecurityUID()
def GetTableHubSecurityUID():
    success=False;
    return success;	

#SetTableHubOPT_SecuirtyIC()
def SetTableHubOPT_SecuirtyIC():
    success=False;
    return success;
	
#generate UID
def SetgenUID():
    print("Apply OTP security setting");
    success=False;
    return success;

#tableHub_USB status
def GetUSBTableHub_Status():
    success=False;
	#-g tablehub_usbhub_status
	#-g tablehub_chrontel_status-
	#-s tde_unique_id
    return success;


#get usb pid vid directly	
def GetUSBPIDVID():
    success=False;
	#GET TableHub PID (from TDEBT tool)	
	#tdebt.exe -c tablehub -g tablehub_device_pid
    PIDVID_TableHub="046d/0886";
    return PIDVID_TableHub;
	
def Get_tablehub_system_date():
	#GET System time used by TDE BT tool to prepare the device label.
	#tdebt.exe -c tablehub -g tablehub_system_date
	#20050505
    tdebtDate=runCmdx(" -c tablehub -g tablehub_system_date");
    dt = datetime.datetime.strptime(tdebtDate, '%Y%m%d')
    datestrr=str('{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year % 100));
    return datestrr;	

#apply table hub reset function.
def ApplyTableHub_Reset():
    success=False;
    #tablehub_reset(Set/Get)
    return success;	
		
#ProgramEthernetMacaddress
def ProgramEthernetMacaddress():
    success=False;
	#send print command.
	
	#SetEthernetMacaddress
	#success=SetEthernetMacaddress(ScannedMacaddress);
	
	#GetEthernetMacaddress
	#GetEthernetMacaddress();
	
    return success;

#set Ethernet Macaddress 
def SetEthernetMacaddress(macaddressStr):
    print("BolideLib:"+macaddressStr);
	#Set Tablehub Ethernet MAC address
	#tdebt.exe -c tablehub -s tablehub_eth_mac <a1b2c3d4e5f6>
    runCmdx(" -c tablehub -s tablehub_eth_mac "+str(macaddressStr));
    return	
	
#Get Ethernet Macaddress.
def GetEthernetMacaddress():
	#GET Tablehub Ethernet MAC address
	#tdebt.exe -c tablehub -g tablehub_eth_mac
    macaddressStr=runCmdx(" -c tablehub -g tablehub_eth_mac");
    return macaddressStr;

def GetScriptMacaddress():
    #print(TST_PLAN_SCAN_MAC);
    file = open(TST_PLAN_SCAN_MAC,'r');
    scriptScanMac=file.readline();
    file.close();
    return scriptScanMac;

def SetDeviceLabel(devicelabel):
	#3. Set tablehub device label: (need to provide the mac address)
	#tdebt.exe -c tablehub -s tablehub_device_label 088500018045
	#4. Get tablehub device label: (Returns this format , PID:YYYYMMDD:MAC ADDR)
    #tdebt.exe -c tablehub -s tablehub_device_label
    devicelabelMac=runCmdx(" -c tablehub -s tablehub_device_label "+devicelabel);
    return;
	
def GetDeviceLabel():
	#4. Get tablehub device label: (Returns this format , PID:YYYYMMDD:MAC ADDR)
    #tdebt.exe -c tablehub -g tablehub_device_label
    devicelabelMac=runCmdx(" -c tablehub -g tablehub_device_label");
    return devicelabelMac;

#///
	
#Set UID Setting.	
def SetUID():
    print("setUID setting")
    UID_Success=False;
    return UID_Success;

	
#Get UID Setting.	
def GetUID():
    print("get uid security IC setting")
    UID_Success=False;
    return UID_Success;
	
	
#Check UID for errors.
def UIDValidityCheck(m_UID_DUT_Readback):
    print("UID Check");
    UIDCheck=False;
    return UIDCheck;	

def logActivity():
    #log activities for trouble shooting.
    return;
	
#Check the printer access.	
def CheckPrinterAccess():
    print("check printer access");
    checkPrinter=False;
    return checkPrinter;
	
	
#Check the device access.	
def CheckDeviceAccess():
    print("check device access");
    checkDevice=False;
    return checkDevice;


def runCmdx(cmd):
    cmdStr=TDETOOLPATH+cmd
    print(cmdStr);
    resultscmd=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
    #print("OUTPUT: "+resultscmd+"\r\n");
    return resultscmd;

def SetLocalPCDate(datestr):
    dt = datetime.datetime.strptime(datestr, '%Y-%m-%d')
    datestrr=str('{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year % 100));
    print(datestrr);
    os.system("date "+datestrr);
    return
	
def GetLocalPCTime():
    localDate=str(time.strftime("%Y-%m-%d"));
    return localDate;

def GetServerDateTime():
    print("ApplyTableHubStation_Test");
    EXITCODE=0x00;
    success=False;
    src = r'\\172.17.159.36\Sharing\Bolide\date.inf'
    dst = r'date.inf'


    found=os.path.isfile(dst);
    print("Date File Found:"+str(found));
    
    print("Copying date file from network server:"+src);       
    copyfile(src, dst);
    
    if (os.path.isfile(dst)):
       print("Copied date file found:"+dst);
    else:
       print("Copied date file NOT found:"+dst);
       EXITCODE=0x01;

       
    file = open(dst,'r');
    readFile=file.readline();
    file.close();


    if (os.path.isfile(dst)):
       print("Date File Found:"+dst);
       os.remove(dst);

    rdate=readFile.split('=');
    serverDate=str(rdate[1].replace('\n',''));
    return serverDate;


#check the tdebt version.
def CheckTDEBT_version():
    success=False;
    FW_TDEBT_VERSION="1.0.45";
	#will check the tdebt tool version. 
    return FW_TDEBT_VERSION;
	
#Check the tvHub version	
def CheckTVHub_Version():
    success=False;
    FW_TVHUB_VERSION="v.1.0.163";
    #will check the tablehub version.
    FW_TVHUB_VERSION=runCmdx(" -c tvhub -g fwversion");
    return FW_TVHUB_VERSION;


#Check the table hub version
def CheckTableHub_version():
    success=False;
    FW_TABLEHUB_VERSION="v.1.0.72";
    FW_TABLEHUB_VERSION=runCmdx(" -c tablehub -g tablehub_version_query");
    return FW_TABLEHUB_VERSION;  

def CheckBLE_HubVersion():
    FW_BLE_VERSION="1.0.11";
    return FW_BLE_VERSION;
    