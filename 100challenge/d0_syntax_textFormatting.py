
"""
part 1
message1 = 'File %s is deleted'
print(message1 % ("letter.xdd"))


message2 = 'File %s has size %d KB'
print(message2 % ("letter.xdd",100))


message3 = 'File {1:s} has size {0:d} KB'
print(message3.format(150, 'text.txt'))
#

def giveWorkingDay():
    #the function prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    day = date.today()

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for', day, 'is', workingday)

giveWorkingDay()
#

#homework https://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/11772954#announcements
#how many days to new year (xd - today is new year)

def dayLeftThisYear():
    #the function counts how many days are left to the last day of this year
    from datetime import date
    counter = (date(date.today().year, 12, 31)) - date.today()
    print(F"To the end of this year there are {counter.days} days")

dayLeftThisYear()
"""
