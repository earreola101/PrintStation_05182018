tdebt -c tvhub -g tde_unique_id 
pause
tdebt -c tvhub -s tvhub_ble_central_address 111234567899 
pause
tdebt -c tvhub -g tvhub_ble_central_address 
pause
tdebt -c tvhub -s freq 17039363 
pause
tdebt -c tvhub -s  bt_tx_start 2402 177462 0 
pause
tdebt -c tvhub -s tdebt.exe -s radiotxdata 
pause
tdebt -c tvhub -s  radiorxdata 1 2 3 
pause
tdebt -c tvhub -s macaddress 111234567899 
pause
tdebt -c tvhub -g pskey 
pause
tdebt -c tvhub -s crystal 12345 
pause
tdebt -c tvhub -s freq 17039363 
pause
tdebt -c tvhub -s  bt_tx_start 2402 177462 0 
pause
tdebt -c tvhub -s tdebt.exe -s radiotxdata 
pause
tdebt -c tvhub -s  -s radiorxstart 
pause
tdebt -c tvhub -s  radiorxdata 1 2 3 
pause