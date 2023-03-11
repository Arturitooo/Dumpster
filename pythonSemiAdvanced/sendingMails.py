import smtplib

mailFrom = "Art Part"

mailTo = "hello@aspect-creative.com"
mailSubject = "test python"
mailBody = "If you've received the email - my program works, thanks for being there for me to spam :)"

message = f'''From: {mailFrom}()
Subject: {mailSubject}
{mailBody}
'''

user = "arturito.python@gmail.com"
password = "Szemud!995"

try:
    print('try')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print("Something went wrong")


