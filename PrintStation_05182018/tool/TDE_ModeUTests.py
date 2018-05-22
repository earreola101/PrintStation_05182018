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
import sys
import time
from tdelib import BolideLib

BolideLib.SetDeviceLabel("443e24d9f245");
time.sleep(10);
getdevicelabel=BolideLib.GetDeviceLabel();
print(getdevicelabel);
time.sleep(10);
tablehub_device_label=BolideLib.GetDeviceLabel();
print(tablehub_device_label);
time.sleep(10);
tdebtSystemDate=BolideLib.Get_tablehub_system_date(); 
print(tdebtSystemDate);

tvhubversion=BolideLib.CheckTVHub_Version();
print(tvhubversion);

tvhubPIDVID=BolideLib.GetTVHUB_USBPIDVID();
print(tvhubPIDVID);

tablehubVer=BolideLib.CheckTableHub_version();
print(tablehubVer);

time.sleep(15);
mac=BolideLib.GetEthernetMacaddress();
print(mac);


#Get Ethernet Macaddress.
BolideLib.SetEthernetMacaddress("554433221100");
time.sleep(15);
mac=BolideLib.GetEthernetMacaddress();
print(mac);

#GetTVHUB_HardwareVersion
#BolideLib.GetTVHUB_HardwareVersion();

#Sets the security ID chip applied OPT permanent function.
#BolideLib.SetTableHubOPT_SecuirtyIC();

#GetTableHubSecurityUID()
#BolideLib.GetTableHubSecurityUID();

#SetTableHubOPT_SecuirtyIC()
#BolideLib.SetTableHubOPT_SecuirtyIC();

#Generate UID
#BolideLib.SetgenUID():

#tableHub_USB status
#BolideLib.GetUSBTableHub_Status();

#get usb pid vid directly	
#BolideLib.GetUSBPIDVID();
#BolideLib.Get_tablehub_system_date();

#apply table hub reset function.
#BolideLib.ApplyTableHub_Reset();
	


#set Ethernet Macaddress 
#BolideLib.SetEthernetMacaddress();

#Device Label
#devicelabel="";
#BolideLib.SetDeviceLabel(devicelabel);
#BolideLib.GetDeviceLabel();

#Set UID Setting.	
#BolideLib.SetUID();

#Get UID Setting.	
#BolideLib.GetUID();

#Check UID for errors.
#m_UID_DUT_Readback="";
#BolideLib.UIDValidityCheck(m_UID_DUT_Readback);

#Check the device access.	
#BolideLib.CheckDeviceAccess();

sys.exit(0);
