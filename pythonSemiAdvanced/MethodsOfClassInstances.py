brandOnSale = 'Opel'

class Car:
    
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK,isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale # You use __ only if something is "internal"
        Car.numberOfCars+=1
        Car.listOfCars.append(self)

    def is_damaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)
    
    def get_info(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOK))
        print("Painting - ok - {}".format(self.isPaintingOK))
        print("Mechanic - ok - {}".format(self.isMechanicOK))
        print("Is on sale - ok - {}".format(self.__isOnSale))
        print("*" *25)

    def GetIsOnSale(self):
        return self.__isOnSale
    
    def SetIsOnSale(self, newIsOnSale):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSale
            print("Changing status isOnSale to {}".format(newIsOnSale))

    IsOnSale = property(GetIsOnSale, SetIsOnSale, None, "If true - the car is available for sale/promo")
    #     IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, "If true - the car is available for sale/promo")



car_01 = Car('Seat','Ibiza',True, True, True, False)

print(car_01.is_damaged())
car_01.get_info()

car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOK' : True,
'carIsPaintingOK' : False,
'carIsMechanicOK' : True}

car_03 = Car('Opel','Ibiza',True, False, True, True)

print(car_03.is_damaged())

car_03.get_info()

car_03.__isOnSale = False
car_03.get_info()
print(vars(car_03))

#Now, after adding __isOnSale - we have two variables, one hidden, second available

del car_03.__isOnSale
print(vars(car_03))

setattr(car_03, "Taxi", False) #we're changing car_03 instance, adding parameter Taxi which value is False - the car wasnt used as a Taxi
print(hasattr(car_03, "Taxi")) #the hasattr is checking if the object has attribute "Taxi" in that case


print("Status of cars:", car_01.GetIsOnSale(), car_03.GetIsOnSale())
car_01.SetIsOnSale(True) #wont work cuz its opel
print("Status of cars:", car_01.GetIsOnSale(), car_03.GetIsOnSale())

car_03.SetIsOnSale(False) #should work and works
print("Status of cars:", car_01.GetIsOnSale(), car_03.GetIsOnSale())


car_03.IsOnSale = True 
car_03.IsOnSale = True #changed only for Seat 
print("Status of cars:", car_01.GetIsOnSale(), car_03.GetIsOnSale())