#d0000_errorHandling
import sys

try:
    tasks = int(input("please provide number of tasks: "))
    people = int(input("please provide number of developers: "))
    tasksPerPerson = tasks / people

except ValueError:
    print("Sorry, you need to provide integer number")

except ZeroDivisionError:
    print("Sorry, you need to provide number greater than 0")

except:
    print("Something went wrong...", sys.exc_info()[0])

#else:
#shows result if everything worked
#finally:
#shows final result no matter if everything worked okay or not

print("Every developer has:",tasksPerPerson,"tasks")