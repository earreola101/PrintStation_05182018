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

class TdePrinter:

	def runCmdx(cmd):
		cmdStr=TDETOOLPATH+cmd;
		resultscmd=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT);
		print("OUTPUT: "+resultscmd+"\r\n");
		return resultscmd;
		
def printLabel(label):
		print("printing...");
		return;