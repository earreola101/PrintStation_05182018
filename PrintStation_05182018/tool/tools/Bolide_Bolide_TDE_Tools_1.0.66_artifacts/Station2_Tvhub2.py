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
        return
		
    def test_03_SetBleCentralAdd(self):
        print("test_03_SetBleCentralAdd ")
        cmdStr=tdebt+" -c tvhub -s tvhub_ble_central_address 111234567899"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return

    def test_04_GetBleCentralAdd(self):
        print("test_04_GetBleCentralAdd ")
        cmdStr=tdebt+" -c tvhub -g tvhub_ble_central_address"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return

    def test_05Settvhub_freq(self):
        print("test_05Settvhub_freq ")
        cmdStr=tdebt+" -c tvhub -s freq 17039363"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_21TvhubBTStartTx(self):
        print("test_21TvhubBTStartTx ")
        cmdStr=tdebt+" -c tvhub -s  bt_tx_start 2402 177462 0"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_07TvhubRadioTXdata(self):
        print("test_07TvhubRadioTXdata ")
        cmdStr=tdebt+" -c tvhub -s tdebt.exe -s radiotxdata"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_08TvhubRadioRxStart(self):
        print("test_08TvhubRadioRxStart ")
        cmdStr=tdebt+" -c tvhub -s  -s radiorxstart"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_22Tvhubradiorxdata(self):
        print("test_22Tvhubradiorxdata ")
        cmdStr=tdebt+" -c tvhub -s  radiorxdata 1 2 3"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_10Settvhub_macaddress(self):
        print("test_10Settvhub_macaddress ")
        cmdStr=tdebt+" -c tvhub -s macaddress 111234567899"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_11Gettvhub_macaddress(self):
        print("test_11Gettvhub_macaddress ")
        cmdStr=tdebt+" -c tvhub -g macaddress"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        #self.assertEqual("111234567899",r)
        return
		
    def test_02Gettvhub_pskey(self):
        print("test_02Gettvhub_pskey ")
        cmdStr=tdebt+" -c tvhub -g pskey"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        self.assertEqual("12345",r)
        return
		
    def test_14Settvhub_crystal(self):
        print("test_14Settvhub_crystal ")
        cmdStr=tdebt+" -c tvhub -s crystal 12345"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_16Settvhub_freq(self):
        print("test_16Settvhub_freq ")
        cmdStr=tdebt+" -c tvhub -s freq 17039363"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_17TvhubBTStartTx(self):
        print("test_17TvhubBTStartTx ")
        cmdStr=tdebt+" -c tvhub -s  bt_tx_start 2402 177462 0"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_18TvhubRadioTXdata(self):
        print("test_18TvhubRadioTXdata ")
        cmdStr=tdebt+" -c tvhub -s tdebt.exe -s radiotxdata"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_19vhubRadioRxStart(self):
        print("test_19vhubRadioRxStart ")
        cmdStr=tdebt+" -c tvhub -s  -s radiorxstart"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_20Tvhubradiorxdata(self):
        print("test_20Tvhubradiorxdata ")
        cmdStr=tdebt+" -c tvhub -s  radiorxdata 1 2 3"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
if __name__ == '__main__':
    with open('Station2_Tvhub2.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
