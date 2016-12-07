from twilio.rest import TwilioRestClient

def sendMessage(message):
    account_sid = "ACe8362809f80f4bae57310e689d9e04f0"
    auth_token = "d8f0d0459d99e5e42884bcd29ad48337"

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=message,
                                 to="+14039217113",
                                 from_="+12898062227")

    print(message.sid)
    return



