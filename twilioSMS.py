from twilio.rest import Client
# Your Account Sid and Auth Token from twilio account
account_sid = 'ACd774fef6d0d94509288a891442d641bc'
auth_token = 'df9fbbb7182bcc86588aa84cf16c8c17'
# instantiating the Client
client = Client(account_sid, auth_token)


# from_=+17632251011, to=+918319578097


def sendMessage(title, desc, url):
    # sending message
    content = title + '\n' + desc + '\n' + url
    message = client.messages.create(
        body=content, from_='whatsapp:+14155238886', to='whatsapp:+917840908066')
    # printing the sid after success
    print(message.sid)
