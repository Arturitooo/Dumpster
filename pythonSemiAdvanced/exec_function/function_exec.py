#function_exec()

x = 10

source = """
for i in range(x):
    print('_'*i)
"""

result = exec(source)
print(result)
print(x)

source = input("enter your expression: ")
print(eval(source))

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14283674#overview

import os

files_to_process = [
    r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\exec_function\file1.py",
    r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\exec_function\file2.py"
    ]

#os.path.basename

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print("File {} is going to be opened!".format(os.path.basename(file_path)))
        result = f.read()
        exec(result)

