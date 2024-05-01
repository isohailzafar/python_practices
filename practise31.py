# class Car:
#     brand = None
#     model = None



# #Object
# my_car = Car() #copy of class in my_car
# print(my_car)

#Real Method
#self is used to make the connection between Car class and my_car variable which contains the object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corola")
print(my_car.brand)
print(my_car.model)
my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)