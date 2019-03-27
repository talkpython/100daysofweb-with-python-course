import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail

sg = sendgrid.SendGridAPIClient(apikey='<apikey>')

from_email = Email("test@example.com")
subject = "Winter is coming"
to_email = Email("<youremail>@<domain>")
content = Content("text/plain", "So... put on a jumper!")

mail = Mail(from_email, subject, to_email, content)

response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
