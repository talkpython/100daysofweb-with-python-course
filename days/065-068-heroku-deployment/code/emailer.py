import smtplib

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login('<gmail-address>', '')

smtp_server.sendmail('<from-email>@gmail.com', '<to-email>@<domain>', 'Subject: Hello from Heroku!\nTest email from Heroku. Cheers!')

smtp_server.quit()
