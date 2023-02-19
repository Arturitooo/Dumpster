#d00_functions
"""t1
def printAnimal(animal='', *nameOfAnimal ,**sizeOfAnimal):
    #the function displays image of picked animal
    if animal == 'monkey':
        print("monkey +1")
        print('possible names are:', nameOfAnimal)
        print('and the size is: ',sizeOfAnimal)
        printed = True
    elif animal == 'dog':
        print("dog +1")
        printed = True
    elif animal == 'cat':
        print("cat +1")
        printed = True  
    else:
        print('You putted incorrect value, please provide value "cat" or "monkey" or "dog"')
        printed = False
    
    return printed

t2
from datetime import date

def daysToEndOfYear(year = date.today().year, month = date.today().month, day=date.today().day):
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days
"""

#t1 image = input('What kind of animal would you like to see? ').lower()
#t1 if printAnimal(image,"Tony","Johny","Cory", long = 15, width = 20, depth = 30) == True:
#t1     print('true')
#t1 else:
#t1     print('false')

#t2 counter = daysToEndOfYear(2017)
#t2 print('Number of days to the end of the year left: ',counter)

#t3 & t4 https://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/8299612#notes
#part1
import math

def giveGeomSeqElement(index = 10):
    a1=3
    factor = 2
    for i in range(1, index+1):
        value ={i: factor ** (i-1)*a1}
        print(factor, "^ (",i,"- 1 ) *",a1,"=",value)
    return value.get(index,'error')

print(giveGeomSeqElement(7))
