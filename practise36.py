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

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize
    
    def fuel_type(self):
        return "Electric Charge"
    
Car("Corolla", "Safari")
Car("Corolla", "Safari")
Car("Corolla", "Safari")
print(Car.total_car)

# tesla = ElectricCar("Tesla", "Safari", "85Kwh")
# print(tesla.fuel_type())