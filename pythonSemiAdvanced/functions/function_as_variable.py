def BuyMe(what):
    print("Give me", what)

BuyMe('a new car')
StealForMe = BuyMe
print(StealForMe('an old car'))

def GoLeft(*args):
    print('PLACEHOLDER - turning left with', *args)

def GoRight(*args):
    print('PLACEHOLDER - turning right with', *args)

def GoForward(*args):
    print('PLACEHOLDER - going forward with', *args)

def GoBack(*args):
    print('PLACEHOLDER - going back with', *args)

def Start(*args):
    print('PLACEHOLDER - starting with', *args)

def Stop(*args):
    print('PLACEHOLDER - stoping with', *args)

instructions = [Start, GoForward, GoForward, GoLeft, GoForward, GoRight, Stop]

dish = 'Pizza'

for instr in instructions:
    instr(dish)

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14290374#overview

def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

number = 8

transformations = [double, square, div2, negative]

tmp_return_value = number

for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print(tmp_return_value)


transformations = [square, square, div2, double]
number = 125
tmp_return_value = number

for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print(tmp_return_value)

print("-"*25)

#function as function's argument
def Bake(what):
    print(f"Baking {what}")

def Add(what):
    print(f"Adding {what}")

def Mix(what):
    print(f"Mixing {what}")

cookbook = [(Add, 'milk'), (Add,'eggs'), (Add, 'flour'), (Add, 'sugar'), (Mix, 'ingridients'), (Bake, 'cookies')]

for activity, object in cookbook:
    activity(object)

print("-"*5)
def Cook(activity, obj):
    activity(obj)
Cook(Bake, "Brownies")
print("-"*5)

for activity, object in cookbook:
    Cook(activity,object)

#homework 2 - https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14293050#overview

def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2


def generate_values(action, table):
    print(table)
    new_list = []
    for number in table:
        new_list.append(action(number))
    return(new_list)

x_table = list(range(11))
 
print('\ndoubling')
print(generate_values(double, x_table))
print('\nsquare')
print(generate_values(square, x_table))
print('\nnegative')
print(generate_values(negative, x_table))
print('\ndivided by 2')
print(generate_values(div2, x_table))

