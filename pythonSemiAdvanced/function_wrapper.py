#wrapper - supervise all the other functions

import datetime
import functools

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started at {datetime.datetime.now().isoformat()}")
        print("Following parameters were used:", args, kwargs)
        result = func (*args, **kwargs)
        return result
    return func_with_wrapper

#decorator
@CreateFunctionWithWrapper #functools
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print(f"Changing salary for {emp_name} to {new_salary} USD as bonus: {is_bonus}")
    return new_salary

ChangeSalary = CreateFunctionWithWrapper(ChangeSalary)

print(ChangeSalary("Johnoson",20000, True))

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14331166#overview

import time

def wrapper_time(a_function):
    def a_function_wWrapper(*args, **kwargs):
        time_start = time.time()
        result = a_function(*args, **kwargs)
        time_stop = time.time()
        time_past = time_start-time_stop
        print(f"Function {a_function.__name__} took {time_past})")
        return result
    return a_function_wWrapper

@wrapper_time
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
    
print(get_sequence(10))