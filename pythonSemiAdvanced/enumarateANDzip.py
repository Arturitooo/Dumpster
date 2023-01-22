"""workDays = [19, 21, 22, 21, 20, 22]

print(workDays)

#enumarated work days
enumatedDays = enumerate(workDays)
print(enumatedDays)

#enumarated work days in list
enumatedDays2 = list(enumerate(workDays))
print(enumatedDays2)

#use enumarated list in loop
for pos, val in enumatedDays2:
    print('Position:',pos,' Value:',val)

months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = zip(months, workDays)
print(monthsDays)

monthsDays2 = list(zip(months, workDays))
print(monthsDays2)

for mon, day in monthsDays2:
    print('Month:',mon,' Working Days:',day)

for pos, (m,d) in enumerate(zip(months, workDays)):
    print("Position:",pos, " Month:", m, " Working days:",d)"""


#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14246672#overview

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for pname, lname in list(zip(projects, leaders)):
    print(f"The leader of {pname} is {lname}")

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for num, (pname, lname, date) in list(enumerate(zip(projects, leaders, dates))):
    print(f"The leader of project nr {num+1} named {pname} is {lname}, project started {date}")