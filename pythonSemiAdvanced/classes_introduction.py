car_01 = {
'carBrand' : 'Seat',
'carModel' : 'Ibisa',
'carIsAirBagOK' : True,
'carIsPaintingOK' : True,
'carIsMechanicOK' : True}

car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOK' : True,
'carIsPaintingOK' : False,
'carIsMechanicOK' : True}

def IsCarDamaged(aCar):
    return not  (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])

cars = [car_01, car_02]

for car in cars:
    print(IsCarDamaged(car))

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14364274#overview

cake1 = {
'taste' : 'vanilia',
'glaze' : 'chocolade',
'text' : 'Happy Brithday',
'weight' : 0.7
}

cake2 = {
'taste' : 'tee',
'glaze' : 'lemon',
'text' : 'Happy Python Coding',
'weight' : 1.3
}
 
 
 
def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))
 
show_cake_info(cake1)
show_cake_info(cake2)


## classes and classes atributes

class Car:
    
    def __init__(self, brand, model, isAirBagOK, isPaintingOK,isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

car_01 = Car('Seat','Ibiza',True, True, True)


car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOK' : True,
'carIsPaintingOK' : False,
'carIsMechanicOK' : True}

print(car_01)

def IsCarDamaged(aCar):
    return not  (aCar ['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])

def ClassIsCarDamaged(aCar):
    return not  (aCar.brand, aCar.model, aCar.isAirBagOK, aCar.isPaintingOK, aCar.isMechanicOK)


cars = [car_01, car_02]

print(ClassIsCarDamaged(car_01))
print(IsCarDamaged(car_02))

#class instance - element created with class

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14790372#overview

class Cake():
    def __init__(self, name, kind, taste, additives, filling = ""):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
 
bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)
 
print("Today in our offer:")
for c in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))