#error handling lecture
def divider(a, b):
    try:
        result = a//b
    except ZeroDivisionError:
        print("Please do not divide by zero!")
    else:
        return result
    

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
dog1 = Dog("Hans", "German Shepherd")
dog2 = Dog("Lou", "Labrador")

print(f"{dog1.name} and {dog2.name} are friends")

class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def calculate_human_age(self):
        return self.age * 7
        
dog1 = Dog("Hans", "German Shepherd", 7)

print(dog1.calculate_human_age())

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")
    
class Cat(Animal):
    def __init__(self, name):
        self.name = name 
    def sound():
        print("ruff")
    
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def sound():
        print("meow")


class Students():
    def __init__(self, names):
        self.names = names
    
    #this is dunder - it defines what is shown to the user once he or she writes "len(Students_class_instance)"
    def __len__(self):
        return len(self.names)
    
    #this is dunder - it defines what is shown to the user once he or she writes "print(Students_class_instance)"
    def __str__(self):
        return f"We have multiple students here, such as: {self.names}"

from module import UsefulClass
from module import useful_func

useful_func()

#myInstance = UsefulClass("hello fella")
#myInstance.report()

from mypackage.submodel import sub_func

sub_func()