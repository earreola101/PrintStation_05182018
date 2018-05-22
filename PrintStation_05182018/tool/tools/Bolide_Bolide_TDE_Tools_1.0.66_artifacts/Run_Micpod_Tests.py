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
        
    def test_01SetMicpodLEDcontrol(self):
        print("\n test_01SetMicpodLEDcontrol ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 1"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_02SetMicpodLEDcontrol(self):
        print("\n test_02SetMicpodLEDcontrol ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 2"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_03SetMicpodLEDcontrol(self):
        print("\n test_03SetMicpodLEDcontrol ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 3"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_04SetMicpodLEDcontrol(self):
        print("\n test_04SetMicpodLEDcontrol ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 4"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_05SetMicpodLEDcontrol(self):
        print("\n test_05SetMicpodLEDcontrol ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 5"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_06SetMicpodLEDcontrol(self):
        print("\n test_06SetMicpodLEDcontrol ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 6"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_07SetMicpodLEDcontrol(self):
        print("\n test_07SetMicpodLEDcontrol ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 7"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
    def test_08SetMicpodLEDcontrolOFF(self):
        print("\n test_08SetMicpodLEDcontrolOFF ")
        cmdStr=tdebt+" -c micpod -s micpod_led_control 0"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
    def test_09SetMicpodReset(self):
        print("\n test_09SetMicpodReset ")
        cmdStr=tdebt+" -c micpod -s micpod_reset 1"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_10GetMicpodVersionQuery(self):
        print("\n test_10GetMicpodVersionQuery ")
        cmdStr=tdebt+" -c micpod -g micpod_version_query"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_11GetMicpodTouchStatus(self):
        print("\n test_11GetMicpodTouchStatus ")
        cmdStr=tdebt+" -c micpod -g micpod_button_status"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_12SetMicpodChannelMic1(self):
        print("\n test_12SetMicpodChannelMic1 ")
        cmdStr=tdebt+" -c micpod -s micpod_set_mic_channel 1 21 1"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return

    def test_13SetMicpodChannelMic2(self):
        print("\n test_12SetMicpodChannelMic1 ")
        cmdStr=tdebt+" -c micpod -s micpod_set_mic_channel 1 21 2"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_14SetMicpodChannelMic3(self):
        print("\n test_12SetMicpodChannelMic1 ")
        cmdStr=tdebt+" -c micpod -s micpod_set_mic_channel 1 21 3"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_15SetMicpodChannelMic4(self):
        print("\n test_12SetMicpodChannelMic1 ")
        cmdStr=tdebt+" -c micpod -s micpod_set_mic_channel 1 21 4"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_16SetMicpodResetChannel(self):
        print("\n test_16SetMicpodResetChannel ")
        cmdStr=tdebt+" -c micpod -s micpod_set_mic_channel 1 21 0"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_17SetMicpodLoopbackEnable(self):
        print("\n test_17SetMicpodLoopbackEnable ")
        cmdStr=tdebt+" -c micpod -s micpod_loopback 1"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_18SetMicpodLoopbackDisable(self):
        print("\n test_18SetMicpodLoopbackDisable ")
        cmdStr=tdebt+" -c micpod -s micpod_loopback 0"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
    def test_19MicpodsSplitterConnected(self):
        print("\n test_19MicpodsSplitterConnected ")
        cmdStr=tdebt+" -c tablehub -g tablehub_num_of_dev"
        r=subprocess.check_output(cmdStr,stderr=subprocess.STDOUT)
        r = r.replace("\r\n", " ")
        r = r.replace(" ", " ")
        print("OUTPUT: "+r+"\r\n")
        return
		
if __name__ == '__main__':
    with open('results_Micpod_tests.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
