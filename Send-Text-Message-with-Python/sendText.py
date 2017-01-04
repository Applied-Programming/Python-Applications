#! Python 3
from twilio.rest import TwilioRestClient

# Enter the appropriate credebtials
accountSID = 'YOUR-OWN-ACCOUNT-SID'
authToken = 'YOUR-OWN-AUTHORIZATION-TOKEN'
my_TwilioNumber = 'YOUR-OWN-TWILIO-NO'
my_CellPhone = 'SEND-TEXT-TO-THIS-PHONE-NO'


def send_text(message):
    twilio_client = TwilioRestClient(accountSID, authToken)
    twilio_client.messages.create(body=message, from_ = my_TwilioNumber, to = my_CellPhone)

send_text("This message is specifically sent to you via a python script")
