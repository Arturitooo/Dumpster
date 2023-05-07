class Car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.isOnSale = isOnSale

        def IsDamaged(self):
            return not(self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

        def GetInfo(self):
            print("{} {}".format(self.Brand, self.Model).upper())
            print("Air Bag ok - {}".format(self.isAirBagOK))
            print("-"*20)
        
        def __GetIsOnSale(self):
            return self.__isOnSale
        
        def __SetIsOnSale(self, newIsOnSaleStatus):
            if self.brand == brandOnSale:
                self.__isOnSale = newIsOnSaleStatus
                print("Changing status IsOnSale to {} for {}".format(newIsOnSaleStatus, self.brand))
            else:
                print("Can't change status IsOnSale. Sale valid only for {}".format(brandOnSale))
        IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, "if set to true, the car is available in sale/promo")

        @classmethod
        def ReadfromText(cls, aText):
            aNewCar = cls(*aText.split(":"))
            return aNewCar
        
        @staticmethod
        def Convert_KM_KW(KM):
            return KM*0.735

lineOfText = "Renault:Megane:True:True;False:false"
car_03 = Car.ReadfromText(lineOfText)
car_03.GetInfo()

print(Car.Convert_KM_KW(120))


'''
There are 3 types of methods in classes:
1. Instance method - argument it takes is self 
    It can change specific instance of class
2. Class method - argument it takes is class
    It can prepare data for the class you're working on
3. Static Method - argument it takes is external
    Is not directly connected to the class it is in. 
'''


