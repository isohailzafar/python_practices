class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corola")
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())
my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.fullname())