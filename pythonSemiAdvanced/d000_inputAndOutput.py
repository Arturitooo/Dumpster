#d000_inputAndOutput
"""
#reading from file
file = open("C:\\Users\\Art\\Documents\\GitHub\\learning\\text.py","r")

content = file.read()
print(content)

file.close()

print()

with open("C:\\Users\\Art\\Documents\\GitHub\\learning\\text.py", "r") as file:
    content = file.read()
    print(content)

print()

with open("C:\\Users\\Art\\Documents\\GitHub\\learning\\text.py", "r") as file:
    for line in file:
        print(line)

"""

#saving to file

line = "europe"
cities = "szemud, gdansk"

filename = "C:\\Users\\Art\\Documents\\GitHub\\learning\\text.py"

file = open(filename, 'a')

file.write(line)
file.write(cities)

file.close()

file = open("C:\\Users\\Art\\Documents\\GitHub\\learning\\text.py","r")

content = file.read()
print(content)

file.close()

print()

