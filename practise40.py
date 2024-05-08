#Multiple Inheritance
#Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    track = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.track +=  1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are beautiful"
    
    @property 
    def model(self):
        return self.__brand
class Engine:
    def engine_info(self):
        return "Petrol"
class Battery:
    def battery_size(self):
        return "Dry battery"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"
class ElectricCartwo(Engine, Battery, Car):
    pass
my_tesla = ElectricCartwo("Tesla", "Model S")
print(my_tesla.battery_size())
print(my_tesla.engine_info())
print(my_tesla.model)
print(my_tesla.full_name())


