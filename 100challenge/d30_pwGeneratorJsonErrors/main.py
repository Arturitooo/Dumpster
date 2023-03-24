#KeyError
#a_dictionary = {"key":"value"}
#value = a_dictionary['non_existing_one']

#IndexError
#fruit_list = ['apple','banana','pear']
#fruit = fruit_list[3]

#TypeError
#text="abc"
#print(text + 5)


#FileNotFound
#with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d30_pwGeneratorJsonErrors\text.txt") as f:
#    f.read()

#FileNotFound
try:
    file = open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d30_pwGeneratorJsonErrors\text.txt")
    a_dictionary = {"key":"value"}
    value = a_dictionary['key']
except FileNotFoundError:
    file = open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d30_pwGeneratorJsonErrors\text.txt", "w")
except KeyError as error_key:
    print(f"There's no such a dictionary element as {error_key}")
else:
    print("it all worked well")
    
finally:
#    raise TypeError("My own error")
#    file.close()


    height = float(input("Height: "))
    weight = int(input("Weight: "))

    if height > 3:
        raise ValueError("Human height shouldn't be over 3 meters")

    bmi = weight/height**2
    print(bmi)