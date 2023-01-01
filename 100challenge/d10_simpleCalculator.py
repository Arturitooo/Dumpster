#d10_simple text-based calculator

from os import system

stopCalcuation = "no"

def calculation(operator, n1, n2):
    if operator == "+":
        result = n1+n2
    elif operator == "-":
        result = n1-n2
    elif operator == "*":
        result = n1*n2
    elif operator == "/":
        result = n1/n2
    else:
        print("You didn't provide valid operation")
    return (result)

while stopCalcuation != "stop":
    if stopCalcuation == "no":
        num1 = float(input("What's the first number? "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
    elif stopCalcuation == "yes":
        print("First number equals:",num1)
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
    else:
        print("you put the wrong action, so the program turns off")
        break

    print(num1, operation, num2, "=", calculation(operation, num1, num2))

    stopCalcuation = input(f"Type 'yes' to continue calculating with {calculation(operation, num1, num2)}, type 'no' to start new calculation, type 'stop' to stop the program at all: ").lower()
    num1 = calculation(operation, num1, num2)
    system('cls')