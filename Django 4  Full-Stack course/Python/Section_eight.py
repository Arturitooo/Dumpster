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

