#Class Method and Self
#Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_first_car = Car("Toyota", "Corola")
print(my_first_car.full_name())
my_second_car = Car("Tesla", "S")
print(my_second_car.full_name())