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

#Reference Document
#https://docs.google.com/document/d/1HRe-uBYe5Cwu3H_l01xYswmnSSiYoz5otMA6hG7DHRs/edit#
import sys
from tdelib import BolideLib
from tdelib import TdePrinter
from tdelib import kineticIO



#directories
BolideLib.DATA_FILE_PATH=r"./Data.csv";
BolideLib.OUT_TEST_DATA_FILE=r"../inout/label_test.out";
BolideLib.IN_TEST_DATA_FILE=r"../inout/label_test.in";
BolideLib.TST_PLAN_SCAN_MAC=r"C:/tstplan/ETHERNET_MACADDRESS.txt"

#error code
EXITCODE=0x00;


#expected versions
BolideLib.FW_TDEBT_VERSION="1.0.45";
BolideLib.FW_TVHUB_VERSION="v.1.0.163";
BolideLib.FW_TABLEHUB_VERSION="v.1.0.72"
BolideLib.FW_BLE_VERSION="1.0.11"
BolideLib.FW_TVHUB_PIDVID="[M]:VID=15, PID=27908"

#get all versions
serverDate=BolideLib.GetServerDateTime();

#getlocal pc time.
localDate=BolideLib.GetLocalPCTime();

#check tde bt version
tdebtVer=BolideLib.CheckTDEBT_version();

#check tde table hub version
tablehubVer=BolideLib.CheckTableHub_version();

#check tv hub version 
tvhubVer=BolideLib.CheckTVHub_Version(); 
#get pid vid 
tablehubPIDVID=BolideLib.GetUSBPIDVID();

#get the tde system time
tablehub_system_date=BolideLib.Get_tablehub_system_date();

#get ethernet macaddress
tablehub_eth_mac=BolideLib.GetEthernetMacaddress();

#get device label
tablehub_device_label=BolideLib.GetDeviceLabel();

#get scanned macaddress
script_Scan_Eth_Mac=BolideLib.GetScriptMacaddress();
ERROR_MESSAGE="";

#
print("==================TDETool==========================");
print("TDE_bt_Ver: ["+tdebtVer+"]");
print("===================================================\r\n");

print("==================TableHub=========================");
print("TablehubVer: ["+tablehubVer+"]");
print("TVHubVer: ["+tvhubVer+"]");
print("TableHubPIDVID:["+tablehubPIDVID+"]");
print("Tablehub_system_date:["+tablehub_system_date+"]");
print("Tablehub_eth_mac:["+tablehub_eth_mac+"]");
print("Tablehub_device_label:["+tablehub_device_label+"]");
print("====================================================\r\n");

print("==================Network===========================");
print("ServerDate: ["+serverDate+"]");
print("LocalPCDate:["+localDate+"]");
if(serverDate==localDate):
  print("Server and local PC date match.");
  print("[PASSED]-->ServerDate["+serverDate+"]LocalPCDate["+localDate+"]");
else:
  MSG=("Server and local PC date DONOT match.\n[FAILED]-->ServerDate["+serverDate+"]LocalPCDate["+localDate+"]\r\n");
  print(MSG);
  ERROR_MESSAGE=ERROR_MESSAGE+MSG;
  EXITCODE=EXITCODE+0x01;
print("====================================================\r\n");


print("====================Label===========================");
print("Script_Scan_Eth_Mac: ["+script_Scan_Eth_Mac+"]");
print("Tablehub_device_label:["+tablehub_device_label+"]");
print("Tablehub_eth_mac:["+tablehub_eth_mac+"]");
print("scanned label...");
if(script_Scan_Eth_Mac==tablehub_eth_mac):
    print("[PASSED] Scanned label mac and TvHubMac are a match.");
    print("--->Scanned["+script_Scan_Eth_Mac+"]Device["+tablehub_eth_mac+"]");
else:
    MSG=("Scanned label mac and TvHubMac are NOT a match.\n[FAILED]--->Scanned["+script_Scan_Eth_Mac+"]Device["+tablehub_eth_mac+"]\r\n");
    print(MSG);
    ERROR_MESSAGE=ERROR_MESSAGE+MSG;
    EXITCODE=EXITCODE+0x01;
  
print("write label...");
BolideLib.SetDeviceLabel(tablehub_eth_mac);

read_TableHub_Label=BolideLib.GetDeviceLabel();
print("Read_TableHub_Label:["+read_TableHub_Label+"]");
print("===================================================\r\n");

print("================Printer============================\r\n");
print("sending to printer");
TdePrinter.printLabel(read_TableHub_Label);

print("===================================================\r\n");

print("================ProcessData============================\r\n");
print("processing data");
TestName="LabelTest";
h0=h1=h2=h3=h4=h5=h6=h7=h8=h9="NA";
v0=v1=v2=v3=v4=v5=v6=v7=v8=v9="NA";
l0=l1=l2=l3=l4=l5=l6=l7=l8=l9="NA";
u0=u1=u2=u3=u4=u5=u6=u7=u8=u9="NA";
t0=t1=t2=t3=t4=t5=t6=t7=t8=t9="NA";
#kineticIO.processOutData(BolideLib.OUT_TEST_DATA_FILE,TestName,EXITCODE,EXITCODE,ERROR_MESSAGE,
#					h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,
#					v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,
#					l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,
#					u0,u1,u2,u3,u4,u5,u6,u7,u8,u9,
 #                   t0,t1,t2,t3,t4,t5,t6,t7,t8,t9);
print("===================================================\r\n");


print("================ErrorMessageSummary================\r\n");
print(ERROR_MESSAGE);
print("===================================================\r\n");
print("The TEST EXIT CODE IS:["+str(hex(EXITCODE))+"]");
sys.exit(EXITCODE);
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
