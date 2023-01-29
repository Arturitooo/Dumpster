#function "eval()" reads text which might be considered as a code and deubgged

x = 10
password = "My super secret password:"

source = 'x+2'

result = eval(source)
print(password, result)
print("-"*20)


source = 'password'
result = eval(source)
print(result)


source = '33+3'
globals = {} #we cleaned up the environment so the user cannot user all the variables we have
result = eval(source, globals)
print(result)

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14282624#overview

import math

argument_list = []

for i in range(101):
    argument_list.append(i/10)

print(argument_list)

formula = input("please provide the formula that you want to calculate (use 'x' as an unknown): ")

for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))