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
        
    def test_01Gettvhub_valens_status(self):
        print("test_01Gettvhub_valens_status ")
        cmdStr=tdebt+" -c tvhub -g tvhub_valens_status "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_02TvhubUSBhubMode(self):
        print("test_02TvhubUSBhubMode ")
        cmdStr=tdebt+" -c tvhub -g tvhub_usbhub_mode"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_03TvhubBLE_status(self):
        print("test_03TvhubBLE_status ")
        cmdStr=tdebt+" -c tvhub -g tvhub_ble_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_04TvhubCEC_status(self):
        print("test_04TvhubCEC_status ")
        cmdStr=tdebt+" -c tvhub -g tvhub_cec_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_05TvhubChrontel_status(self):
        print("test_05TvhubChrontel_status ")
        cmdStr=tdebt+" -c tvhub -g tvhub_chrontel_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_06Settvhub_uniqueid(self):
        print("test_06Settvhub_uniqueid ")
        cmdStr=tdebt+" -c tvhub -s tde_unique_id 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
		
if __name__ == '__main__':
    with open('Station1_Tvhub1.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
