#day5 password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []
password_string = ""

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
nrOfLetters = int(input())
for nrOfLetter in range(0,nrOfLetters):
    password.append(random.choice(letters))

print("How many symbols would you like?")
nrOfSymbols = int(input())
for nrOfSymbol in range(0,nrOfSymbols):
    password.append(random.choice(symbols))

print("How many numbers would you like?")
nrOfnumbers = int(input())
for nrOfnumber in range(0,nrOfnumbers):
    password.append(random.choice(numbers))

random.shuffle(password)



print("\nHere's your password:", password_string.join(password))