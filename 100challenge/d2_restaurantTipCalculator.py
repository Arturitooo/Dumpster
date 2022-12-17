#this is tip calculator

print("Welcome to the tip calculator")
sum = float(input("What was the total bill? $"))
tipSize = int(input("What percantage tip would you like to give? 10 / 15 / 20? "))
people = int(input("How many people are there to split the bill? "))
billPerPerson = (sum + (sum * tipSize/100))/people
print("each of you should pay: $", billPerPerson)