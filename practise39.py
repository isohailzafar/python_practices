#Class Inheritance and isinstance() Function
#Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    track = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.track +=  1

    def full_name(self):
        return f"{self.__brand} {self.__model} {self.battery_size}"
    
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

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S", "85kWh")
print(isinstance(my_tesla, Car))



