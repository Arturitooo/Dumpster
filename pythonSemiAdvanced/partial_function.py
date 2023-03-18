import smtplib
import functools

def SendInfoEmail(user,password,mailFrom, mailTo, mailSubject,mailBody):
 
    message = '''From: {}
    Subject: {}
    
    {}
    '''.format(mailFrom, mailSubject, mailBody)
 
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user,password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
    except:
        print('error sending email')

mailFrom = "Your automation system"
mailTo = ['mail1@gmail.com','mail2@gmail.com']
mailSubject = 'test'
mailBody = 'this is python program message'
user = 'your_username@gmail.com'
password = 'your_password_here'

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password)

SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)

#if you want to hardcode part of code - in that case mailSubject
SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password, mailSubject='Alert')

SendInfoEmailFromGmail(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)


#SendInfoEmail(user,password,mailFrom, mailTo, mailSubject,mailBody)


###HOMEWORK https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14394292#overview



