from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.messages.create(
    to="+61",
    from_="+61",
    body="Welcome to the 100daysofweb Course using Twilio!"
)
