#mutable_immutable

#immutable
number = 10
print(number, id(number))
number += 2
print(number, id(number))
number2 = 10
print(number2, id(number2))
number = 10
print(number, id(number))

#immutable
text = 'africa'
print(text, id(text))
text += "is great"
print(text, id(text))
text = 'africa'
print(text, id(text))

#mutable
list = [1,2,3]
print(list, id(list))
list.append(4)
print(list, id(list))
#you have to use .copy() function, because list is mutable so the approach above relates to specific space in memory
list2 = list
list2.append(5)
print(list2, id(list2))

list3 = list.copy()
list3.append(6)
print(list3, id(list3))

#lab for today https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14203810#overview

days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()

workdays.remove('sat')
workdays.remove('sun')


print(days)
print(workdays)