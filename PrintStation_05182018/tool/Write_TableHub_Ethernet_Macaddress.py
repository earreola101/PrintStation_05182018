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
from tdelib import TdePrinter
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
EXITCODE=2;

	
macWrite=str(sys.argv[1]);


print("Programming Macaddress! ["+macWrite+"]");
#Set Ethernet Macaddress.
BolideLib.SetEthernetMacaddress(macWrite);
sys.exit(0);

time.sleep(10);

#Get Ethernet Macaddress
macRead=BolideLib.GetEthernetMacaddress();
#print(mac);
if(macWrite==macRead):
	EXITCODE=0;
	print("PASS macaddress match pass device.Write["+macWrite+"]Read["+macRead+"]"+	str(EXITCODE));
	sys.exit(0);
else:
	EXITCODE=1;
	print("FAIL macaddress does not match fail device..Write["+macWrite+"]Read["+macRead+"]"+	str(EXITCODE));
	sys.exit(0);



