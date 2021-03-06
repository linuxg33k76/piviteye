# twclass Python Program for Raspberry Pi 3
# Author:  Ben Calvert
# Date: August 7, 2016 v1.0.0
# Revision: v1.0.1 - added /etc/piviteye Configuration file language

# This class was created to be utilized between multiple python programs

# Import class files

from twilio.rest import Client


# --------------Class Definitions------------------#

class TwilioSMS(object):

    '''
    Initialize the class for all TwilioSMS activities
    '''

    def __init__(self, data):
        self.tw_account = data['tw_account']
        self.tw_token = data['tw_token']
        self.tw_receiver = data['tw_receiver']
        self.tw_sender = data['tw_sender']
        self.tw_client = Client(self.tw_account, self.tw_token)

    def get_last_msg(self):
        rx = self.tw_receiver
        tx = self.tw_sender
        client = self.tw_client

        # Get last message sid number
        messages = client.messages.list(to=tx, from_=rx)

        return messages[0].sid

    def get_last_msg_body(self):
        rx = self.tw_receiver
        tx = self.tw_sender
        client = self.tw_client

        # Get last message body
        messages = client.messages.list(to=tx, from_=rx)

        return messages[0].body

    def send_message(self, message):
        rx = self.tw_receiver
        tx = self.tw_sender
        message = message

        self.tw_client.messages.create(to=rx, from_=tx, body=message)

    def get_messages(self):
        global logger
        rx = self.tw_receiver
        tx = self.tw_sender
        client = self.tw_client
        messages = client.messages.list(to=tx, from_=rx)
        return messages
