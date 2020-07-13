import sendgrid
from sendgrid.helpers.mail import Mail

sg = sendgrid.SendGridAPIClient(api_key="MY_API_KEY")

from_email = "test@example.com"
subject = "Winter is coming"
to_email = "<youremail>@<domain>"
content = "So... put on a jumper!"

mail = Mail(from_email, to_email, subject, content)

response = sg.send(mail)

print(response.status_code)
print(response.body)
print(response.headers)
