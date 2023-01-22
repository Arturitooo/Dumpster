#operations on files with ifs

import os

#the "r" says you don't have to put \\ two backslahes, because it doesn't interpretate it as smthg different
path = r'C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\files_operations_with_ifs\mydata.txt'
path_name = "mydata.txt"

#os.remove(path)


"""
if os.path.isfile(path):
    print("File %s already exists" % path_name)
else:
    print("Creating a file %s" % path_name)
    open(path,'x').close()
    print('File %s is created' % path_name)

result = os.path.isfile(path) or open(path,'x').close()
print(result)
"""


"""ver2

os.remove(path)

if os.path.isfile(path):
    print("File %s already exists" % path_name)
else:
    print("Creating a file %s" % path_name)
    open(path,'x').close()
    print('File %s is created' % path_name)


result = os.path.isfile(path)
print(result)
"""

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14210846#overview

#f = open(r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\files_operations_with_ifs\weather.txt", "r")
#text = f.read()
#print(text)


def words_counter(file_path):
    f = open(f"{file_path}", "r")
    text = f.read()
    list = text.split(" ")
    print(f"There are",len(list), "words in this file")

path = r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\files_operations_with_ifs\weather.txt"

if os.path.isfile(path):
    words_counter(path)
else:
    print("there's no such a file")