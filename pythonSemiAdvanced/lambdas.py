def double(x):
    return x*2


x=int(input("Provide number you want to double: "))
x = double(x)
print("Doubled number: {}".format(x))

x=int(input("Provide number you want to double: "))
f = lambda x: x * 2
print(f(x))

#lambda is a simple function without a name or syntax
#lambda syntax
# ... = lambda var1, var2: INSTRUCTION
#OR
#lambda var1,var2: INSTRUCTION

list_numbers = [1, 2, 3, 4, 11, 14, 15, 20, 21]

listed_numbers = list(filter(lambda num: num % 2 != 0,list_numbers))
print("The odd numbers: ",listed_numbers)

print("The odd numbers: ", list(filter(lambda num: num % 2 != 0,list_numbers)))


#homework - https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14785554#overview

text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda text: len(text)

print(f('randomowy tekst'))

print(list(map(f, text_list)))
      
print(list(map(lambda s: len(s), text_list)))
