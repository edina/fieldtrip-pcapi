netsh wlan set hostednetwork mode=allow ssid=ft-test key=qwertyui keyUsage=persistent
netsh wlan start hostednetwork
call %~dp0pcapi\Scripts\activate.bat
python %~dp0pcapi\pcapi.py
pause
