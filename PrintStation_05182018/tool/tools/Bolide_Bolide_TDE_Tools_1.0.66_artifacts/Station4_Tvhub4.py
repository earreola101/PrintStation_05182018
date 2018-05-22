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
      
    def test_01Gettvhub_uniqueid(self):
        print("test_01Gettvhub_uniqueid ")
        cmdStr=tdebt+" -c tvhub -g tde_unique_id"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("1234123412341234",r)
        return
		
    def test_02_GetButtonStatus(self):
        print("test_02_GetButtonStatus ")
        cmdStr=tdebt+" -c tvhub -g btn_status "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_03Gettvhub_btusbpidvid(self):
        print("test_03Gettvhub_btusbpidvid ")
        cmdStr=tdebt+" -c tvhub -g btusbpidvid "
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
if __name__ == '__main__':
    with open('Station4_Tvhub4.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
