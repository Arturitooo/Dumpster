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