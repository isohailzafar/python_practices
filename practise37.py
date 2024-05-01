#Polymorphism

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol Diesel"
    
    @staticmethod #This is a decorator
    def general_definition():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize
    
    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("Corolla", "Safari")
print(Car.general_definition())


# tesla = ElectricCar("Tesla", "Safari", "85Kwh")
# print(tesla.fuel_type())