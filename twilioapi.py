import os
from twilio import rest

# Declare variables and initialize them to your Account Sid and Auth Token

account_sid = os.environ.get('ACCT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

# Instantiate the client variable to a new Twilio client

# TwilioRestClient method takes two string parameters in the following order:
# accountsid, authtoken
client = rest.TwilioRestClient(account_sid, auth_token)

order_id = 123 #We should get the order id from views
seller_name = "Pablo" #Get seller's name from views
buyer_name = "Jessica" #Get buyer's name  from views
seller_phone = "+19176916498" #Get seller's phone number from views

message = "Hi %s. You have a MyGarden order from %s! The order number is %d" % (seller_name, buyer_name, order_id)

sms = client.sms.messages.create(
	body = message,
	to = seller_phone,
	from_ = "+12167778433")