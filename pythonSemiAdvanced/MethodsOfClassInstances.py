class Car:
    
    def __init__(self, brand, model, isAirBagOK, isPaintingOK,isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

    def is_damaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)
    
    def get_info(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOK))
        print("Painting - ok - {}".format(self.isPaintingOK))
        print("Mechanic - ok - {}".format(self.isMechanicOK))
        print("*" *25)


car_01 = Car('Seat','Ibiza',True, True, True)

print(car_01.is_damaged())
car_01.get_info()

car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOK' : True,
'carIsPaintingOK' : False,
'carIsMechanicOK' : True}

car_03 = Car('Opel','Ibiza',True, False, True)

print(car_03.is_damaged())
car_03.get_info()


### part 2 - classess and instances use car_01 and car_03

