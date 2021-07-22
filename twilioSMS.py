from twilio.rest import Client
# Your Account Sid and Auth Token from twilio account
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_ACCOUNT_TOKEN'
# instantiating the Client
client = Client(account_sid, auth_token)


def sendMessage(title, desc, url):
    # sending message
    content = title + '\n' + desc + '\n' + url
    message = client.messages.create(
        body=content, from_='whatsapp:+14155238886', to='whatsapp:+91XXXXXXXXXX')
    # printing the sid after success
    print(message.sid)
