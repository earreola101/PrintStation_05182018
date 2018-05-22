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

class kineticIO:
    ver="";    
CLKp_Val1HighLimit="";
CLKn_Val1HighLimit="";
H01_HDMI_POWER_LOW_LIMIT_mV="";
H03_HDMI_LINK_LOW_LIMIT_mV="";
H05_HDMI_HPD_ZERO_LOW_LIMIT_mV="";
H07_HDMI_HPD_ONE_LOW_LIMIT_mV="";
H09_HDMI_DDC_LOW_LIMIT_mV="";
H11_HDMI_CEC_ZERO_LOW_LIMIT_mV="";
H13_HDMI_CEC_ONE_LOW_LIMIT_mV="";
CLKp_Val2LowLimit="";
CLKn_Val1HighLimit="";
H02_HDMI_POWER_HIGH_LIMIT_mV="";
H04_HDMI_LINK_HIGH_LIMIT_mV="";
H06_HDMI_HPD_ZERO_HIGH_LIMIT_mV="";
H08_HDMI_HPD_ONE_HIGHT_LIMIT_mV="";
H10_HDMI_DDC_HIGH_LIMIT_mV="";
H12_HDMI_CEC_ZERO_HIGH_LIMIT_mV="";
H14_HDMI_CEC_ONE_HIGH_LIMIT_mV="";
CLKp_Val1_TARGET_Limit="";
CLKp_Val2_TARGET_Limit="";
CLKn_Val1_TARGET_Limit="";
CLKn_Val2_TARGET_Limit="";
H02_HDMI_POWER_TARGET_LIMIT_mV="";
H04_HDMI_LINK_TARGET_LIMIT_mV="";
H06_HDMI_HPD_ZERO_TARGET_LIMIT_mV="";
H08_HDMI_HPD_ONE_TARGET_LIMIT_mV="";
H10_HDMI_DDC_TARGET_LIMIT_mV="";
H12_HDMI_CEC_ZERO_TARGET_LIMIT_mV="";
H14_HDMI_CEC_ONE_TARGET_LIMIT_mV="";


#[Outputs]
#Status=1
#ReturnCode=1
#Message=FAILED!
#Headers=HDMI_VoltageLineTest
#Values=3.289,3.302,3.289,3.302,3.289,3.302,3.289,0
#LowLimit=0,0,4700,2900,0,2400,4500,0,2500
#UpLimit=0,0,5300,3100,400,5300,5500,600,3600
#TargetLimit=0,0,0,0,0,0,0,0,0,00
#VarResultSummary=FAILED!



def processOutData(outdir,testName,status,returncode,message,
					h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,
					v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,
					l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,
					u0,u1,u2,u3,u4,u5,u6,u7,u8,u9,
					t0,t1,t2,t3,t4,t5,t6,t7,t8,t9):
	
	#safety clean
	testName=testName.replace('\n','');
	
	message=message.replace('\n','');
	message=message.replace('\r','');
	message=message.replace('[',' ');
	message=message.replace(']',' ');
	message=message.replace('.',' ');
	message=message.replace(',',' ');
	
    #generate header	
	outheader=(str(h0)+","+str(h1)+","+str(h2)+","+str(h3)+","+str(h4)+","+
	str(h5)+","+str(h6)+","+str(h7)+","+str(h8)+","+str(h9)+"\n");
	outvalues=(str(v0)+","+str(v1)+","+str(v2)+","+str(v3)+","+str(v4)+","+
	str(v5)+","+str(v6)+","+str(v7)+","+str(v8)+","+str(v9)+"\n");
	outllimits=(str(l0)+","+str(l1)+","+str(l2)+","+str(l3)+","+str(l4)+","+
	str(l5)+","+str(l6)+","+str(l7)+","+str(l8)+","+str(l9)+"\n");
	outulimits=(str(u0)+","+str(u1)+","+str(u2)+","+str(u3)+","+str(u4)+","+
	str(u5)+","+str(u6)+","+str(u7)+","+str(u8)+","+str(u9)+"\n");
	outtargets=(str(t0)+","+str(t1)+","+str(t2)+","+str(t3)+","+str(t4)+","+
	str(t5)+","+str(t6)+","+str(t7)+","+str(t8)+","+str(t9)+"\n");
	
	
	if(os.path.isfile(outdir)):
	 print("found out file:"+outdir);
	 os.remove(outdir);
	 print("removed out file:"+outdir);

	
	f = open(outdir,'a');
	f.write("[Outputs]\n");
	f.write("Status="+str(status)+"\n");
	f.write("ReturnCode="+str(returncode)+"\n");
	f.write("Message="+message+"\n");
	f.write("Headers="+outheader);							
	f.write("Values="+outvalues);							
	f.write("LowLimit="+outllimits);						
	f.write("UpLimit="+outulimits);						
	f.write("TargetLimit="+outtargets);		   
	f.write("VarResultSummary="+message+"\n");
	f.close();
	return