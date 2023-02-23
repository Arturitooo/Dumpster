#wrapper - supervise all the other functions

import datetime as dt
import functools

def CreateFunctionWithWrapper_LogToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, "a")
            file.write("-"*20 + "\n")
            file.write(f"Function {func.__name__} started at {dt.datetime.now().isoformat()}")
            file.write("\nFollowing parameters were used:")
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}".format(k,v) for k,v in kwargs.items()))
            file.write("\n")
            result = func (*args, **kwargs)
            file.write('Function returned: {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

#decorator
@CreateFunctionWithWrapper_LogToFile(r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\salary_logs.txt")
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print(f"Changing salary for {emp_name} to {new_salary} USD as bonus: {is_bonus}")
    return new_salary

@CreateFunctionWithWrapper_LogToFile(r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\position_logs.txt")
def ChangePosition(emp_name, new_position):
    print(f"{emp_name} changes his position to {new_position}")
    return new_position


ChangeSalary("Johnoson",20000, True)
ChangePosition('Anke', 'Manager')

#homework - https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14360770#overview


import os

def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with(open(log_file_path, "a")) as f:
                f.write("-"*20 + "\n")
                f.write(f"The action {logged_action} on file {path} has been taken at {dt.datetime.now().isoformat()}")
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file
 
#@CreateFunctionWithWrapper_LogToFile(r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\position_logs.txt")
@wrapper_with_log_file("FILE_CREATE", r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\homework_logs\file_create.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"a")
 
@wrapper_with_log_file("FILE_DELETE", r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\homework_logs\file_delete.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)
 
 
create_file(r'C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\homework_logs\dummy_file.txt')
delete_file(r'C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\homework_logs\dummy_file.txt')
create_file(r'C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\homework_logs\dummy_file.txt')
delete_file(r'C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\wrappers\homework_logs\dummy_file.txt')