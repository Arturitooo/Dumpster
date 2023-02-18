#day 26
#lists
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

print(numbers)
print(new_numbers)

name = "Artur"
new_list = [letter for letter in name]

print(new_list)

numberz = range(1,5)
new_numberz = [n*2 for n in numberz]

print(new_numberz)

#dictionaries

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score>=50}
print(passed_students)

student_dict = {"student":["Angela","James", "Lily"], "score":[56,76,98]}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through a data frame
for (key,value) in student_data_frame.items():
    print(value)

#loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)