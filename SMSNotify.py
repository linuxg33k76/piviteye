# SMSNotify Python Program for Raspberry Pi 3
# Author:  Ben Calvert
# Date: August 7, 2016 v1.0.0
# Revision: August 21, 2016 v1.0.1
# Revision: August 21, 2016 v1.1.0 - Added Security for TwilioSMS via /etc/piviteye/twilio.conf file

# This program sends out an SMS message for motion detected by webcam

# Import class files

import os
import sys
import glob
import json
from Classes import twclass


def main(argv):

    # Setup message from arguments passed to command
    argv.pop(0)
    msg = ''
    if argv:

        # set the message equal to the text after filename in argument
        for val in argv:
            msg = msg + ' ' + val
    else:

        # treat this like a video message
        path = '/mnt/usb/video/'
        latest_video = max(glob.iglob(os.path.join(path, '*.[Aa][Vv][Ii]')), key=os.path.getctime)
        msg = 'Motion Detected!  Recording has been made: ' + latest_video

    #  Load Twilio Configuration VALUES
    with open('/etc/piviteye/twilio.conf') as data_file:
        data = json.load(data_file)
    data_file.close()

    #  New TwilioSMS instance
    tw = twclass.TwilioSMS(data)

    # Call send_message method
    tw.send_message(msg)

if __name__ == "__main__":
    main(sys.argv)
