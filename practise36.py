#Class Variables
#Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    track = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.track +=  1

    def full_name(self):
        return f"{self.__brand} {self.model} {self.battery_size}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

ElectricCar("Tesla", "S", "85kWh")
Car("Tata", "Safari")
print(Car.track)