tdebt -c micpod -s micpod_led_control 1 
pause
tdebt -c micpod -s micpod_led_control 2 
pause
tdebt -c micpod -s micpod_led_control 3 
pause
tdebt -c micpod -s micpod_led_control 4 
pause
tdebt -c micpod -s micpod_led_control 5 
pause
tdebt -c micpod -s micpod_led_control 6 
pause
tdebt -c micpod -s micpod_led_control 7 
pause
tdebt -c micpod -s micpod_led_control 0 
pause
tdebt -c micpod -s micpod_reset 1 
pause
tdebt -c micpod -g micpod_version_query 
pause
tdebt -c micpod -g micpod_button_status 
pause
tdebt -c micpod -s micpod_set_mic_channel 1 21 1 
pause
tdebt -c micpod -s micpod_set_mic_channel 1 21 2 
pause
tdebt -c micpod -s micpod_set_mic_channel 1 21 3 
pause
tdebt -c micpod -s micpod_set_mic_channel 1 21 4 
pause
tdebt -c micpod -s micpod_set_mic_channel 1 21 0 
pause
tdebt -c micpod -s micpod_loopback 1 
pause
tdebt -c micpod -s micpod_loopback 0 
pause
tdebt -c tablehub -g tablehub_num_of_dev 
pause