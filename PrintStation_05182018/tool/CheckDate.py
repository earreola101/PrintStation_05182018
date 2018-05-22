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
from tdelib import BolideLib
from tdelib import TdePrinter

EXITCODE=0;
ERROR_MESSAGE="";
serverDate=BolideLib.GetServerDateTime();
localDate=BolideLib.GetLocalPCTime();
print("==================Checking Date by Network===========================");
print("ServerDate: ["+serverDate+"]");
print("LocalPCDate:["+localDate+"]");
if(serverDate==localDate):
  print("Server and local PC date match.");
  print("[PASSED]-->ServerDate["+serverDate+"]LocalPCDate["+localDate+"]");
  EXITCODE=0;
else:
  MSG=("Server and local PC date DONOT match.\n[FAILED]-->ServerDate["+serverDate+"]LocalPCDate["+localDate+"]\r\n");
  print(MSG);
  BolideLib.SetLocalPCDate(serverDate);
  ERROR_MESSAGE=ERROR_MESSAGE+MSG;
  EXITCODE=EXITCODE+1;
print("====================================================\r\n");
print("The TEST EXIT CODE IS:["+str(hex(EXITCODE))+"]");
sys.exit(EXITCODE);
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
