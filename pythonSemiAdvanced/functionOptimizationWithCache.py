import functools
import time

#using the LRU cache - you remember last calculations, so if you go all the way from 1! to 10! - you have to make only 1 calculation
#from 1! to 10!, not go again and again all the way down so it's 3! -> 2! * 3 = 6 etc. instead of 3! -> 1! = 1, 2! = 2 , 3! = 6

#to compare result - just comment the line nr 9 ;)

@functools.lru_cache()
def Factorial(n):
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

#x = int(input("please provide any number: "))
#print(Factorial(x))

start = time.time()
for i in range(1,11):
    print("{}! = {}".format(i, Factorial(i)))

stop = time.time()
print("Execution time: ", stop - start)
print(Factorial.cache_info())

print('-'*20)

#homework - https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14393222#overview

@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 3:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result

start = time.time()
for i in range(0,11):
    print("{} Fibonacci number is = {}".format(i+1, fib(i)))

stop = time.time()
print("Execution time: ", stop - start)
print(fib.cache_info())