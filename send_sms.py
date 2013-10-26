#with Jessica Mong, Cassie Dixon, Aimee Morgan, Melanie Warrick
#LinkedIn DevelopHer hack day 10/25/13

# git checkout -b twilio
# to get back, git checkout master
# to get to twilio, git checkout git
# go back to master, git pull origin
# in master, git merge twilio
# if there's a conflict, get help

""" This is a module of the MyGarden app. This program takes in the following
information: phone number and message and sends an SMS to the phone number. 
The SMS message will contain:
MyGarden Order <order ID> Confirmation. Pickup <date> <time>.
"""
import os
from twilio import rest

######## hard coded for testing purposes #########
order_id="123"
seller_phone="+16509964810"
seller_name = "Gowri"
pickup = "10/25/13 at 5:00pm PDT"
###################################################
message="Hi %s!  You have a MyGarden Order. ID %s. Pickup %s" % (seller_name, order_id, pickup)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = rest.TwilioRestClient(account_sid, auth_token)
sms = client.sms.messages.create(body=message,
to=seller_phone, # Replace with seller's phone number
from_="+180543GOWRI") # This is Gowri's Twilio ID
