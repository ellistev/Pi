from twilio.rest import TwilioRestClient

def sendMessage(message):
    account_sid = "sid"
    auth_token = "token"

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=message,
                                 to="+14039217113",
                                 from_="+12898062227")

    print(message.sid)
    return



