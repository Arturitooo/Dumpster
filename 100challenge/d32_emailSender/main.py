import datetime as dt
import random

now = dt.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
weekday = now.weekday

date_of_birth = dt.datetime(year=1995, month = 12, day = 15)

#if tuesday = send me motivational quote

if weekday ==1:
    with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d32_emailSender\quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)
    print(quote)

'''import smtplib

my_email = "artur@aspect-creative.com"
pw = "..."

connection = smtplib.SMTP("smtppro.zoho.eu")
connection.starttls()
connection.login(user = my_email, password = pw)
connection.sendmail(from_addr=my_email, to_addrs="sklep@wood-shop.pl", msg=f"Subject: A little bit of motivation \n\n {quote}}")
connection.close()
'''
