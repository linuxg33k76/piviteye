# piviteye
Raspberry Pi Home Monitor &amp; Utility Project

Still pending licensing decision.

Software created by Ben Calvert (linuxg33k76@gmail.com)

This software requires:

1.  TwilioSMS for Python (pip3 install twilio) & your own Twilio account/token
    - Twilio's SMS API is a paid for service, Just FYI.
2.  /etc/piviteye/twilio.conf file in JSON format
3.  sudo apt-get install motion - configure via /etc/motion/motion.conf (autostart is your option)
4.  sudo apt-get install tshark (packet capture functions)
4.  Hardware:  Raspberry Pi 3

Installation:

1.  I installed to /opt/piviteye
2.  Make sure you have python3 and the all necessary pip packages installed
3.  Add /etc/piviteye directory and include a JSON fomatted text file as shown below (replace CAPS text with correct data).  Filename should be twilio.conf.

     ``` 
     {
        "tw_account":"ACCOUNT NUMBER",
        "tw_token":"TWILIO TOKEN",
        "tw_receiver":"YOUR SMS PHONE NUMBER",
        "tw_sender":"TWILIO SMS NUMBER"
     }
     ```
4.  Add a file named openweather.conf to /etc/piviteye/ with the following format:
     ```
     {
         "openweatherapikey":"<API KEY GOES HERE>"
     }
     ```
5.  Make symbolic links for piviteye/webapp/static for short cuts to /mnt/usb/video and /mnt/usb/pcap
    - ln -s /mnt/usb/video piviteye/webapp/static/video
    - ln -s /mnt/usb/pcap piviteye/webapp/static/pcap
6.  Add following entries to /etc/crontab using vim or nano (tweak as desired)
    
    @reboot 	root	sleep 60; python3 /opt/piviteye/piviteye.py
    @reboot 	root	sleep 60; python3 /opt/piviteye/webapp/app.py

    59 23 	* * * 	root	/opt/piviteye/SupportFiles/motion_jpg_cleanup.sh
    59 23   * * *   root    /opt/piviteye/SupportFiles/log_rotation.sh



