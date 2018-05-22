import subprocess
import sys,string,os
#import serial
import random
import unittest
import xmlrunner
from timeit import default_timer
from time import sleep

#automated TDE mode test version 0.1.0

tdebt="tdebt.exe"
if not os.path.exists(tdebt):
    raise IOError('{} not found'.format(tdebt))
       

class TDE_Modes(unittest.TestCase):
        
    def test_01GetTablehubZynqStatus(self):
        print("\n test_01GetTablehubZynqStatus ")
        cmdStr=tdebt+" -c tablehub -g tablehub_zynq_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_02GetTablehubValensStatus(self):
        print("\n test_02GetTablehubValensStatus ")
        cmdStr=tdebt+" -c tablehub -g tablehub_valens_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return

    def test_03GetTablehubUsbhubStatus(self):
        print("\n test_03GetTablehubUsbhubStatus ")
        cmdStr=tdebt+" -c tablehub -g tablehub_usbhub_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_04GetTablehubChrontelStatus(self):
        print("\n test_04GetTablehubChrontelStatus ")
        cmdStr=tdebt+" -c tablehub -g tablehub_chrontel_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_05SetTablehub_uniqueid(self):
        print("test_05SetTablehub_uniqueid ")
        cmdStr=tdebt+" -c tablehub -s tablehub_unique_id 1111222233334444 "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
				
    def test_07GetTablehubResetStatus(self):
        print("\n test_07GetTablehubResetStatus ")
        cmdStr=tdebt+" -c tablehub -g tablehub_reset"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return	

if __name__ == '__main__':
    with open('Station5_Tablehub1.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
