#Polymorphism
#Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

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

#Same method is accessed by both class but with different outputs
my_car = ElectricCar("Tesla", "S", "85kWh")
print(my_car.fuel_type())
my_new = Car("Tata", "Safari")
print(my_new.fuel_type())