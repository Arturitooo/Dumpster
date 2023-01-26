listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []

for a in listA:
    for b in listB:
        product.append((a,b))

print(product)
print('-'*50)
listC = list(range(6))
listD = list(range(6))

product2 = [(c,d) for c in listC for d in listD]
print(product2)
print('-'*50)
product2 = [(c,d) for c in listC for d in listD if c % 2 == 1 and d % 2 == 0]
print(product2)
print('-'*50)
product3 = {c:d for c in listC for d in listD if c % 2 == 1 and d % 2 == 0}
print(product3)

product2 = [(c,d) for c in listC for d in listD if c % 2 == 1 and d % 2 == 0]
print(product2)
print('-'*50)
gen = ((c,d) for c in listC for d in listD if c % 2 == 1 and d % 2 == 0)
print(gen)
#generator is rather programmers thing

#prints first value in generator
print(next(gen))
#prints second value in generator
print(next(gen))
print('-'*50)
for x in gen:
    print(x)    

print('-'*50)
#this time the generator doesnt work :sadge:
for x in gen:
    print(x) 

print('try one more time')

gen = ((c,d) for c in listC for d in listD if c % 2 == 1 and d % 2 == 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("stop infinitiv loop")
        break

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14269930#overview

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen = ((starts,stops) for starts in ports for stops in ports)
counter = 0 
"""while True:
    try:
        print(next(gen))
        counter += 1
    except:
        print(counter)
        break"""

for (start, stop) in gen:
    print("{} - {}".format(start, stop))
    counter += 1
print(counter)

counter = 0 
gen = ((starts,stops) for starts in ports for stops in ports if starts != stops)
"""print(len(gen))
while True:
    try:
        print(next(gen))
        counter += 1
    except:
        print(counter)
        break"""

for (start, stop) in gen:
    print("{} - {}".format(start, stop))
    counter += 1
print(counter)

counter = 0 
gen = ((starts,stops) for starts in ports for stops in ports if starts < stops)
for (start, stop) in gen:
    print("{} - {}".format(start, stop))
    counter += 1
print(counter)
