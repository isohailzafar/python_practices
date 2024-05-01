import math

def calc(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi *radius
    return [area, circumference]

(area, circum) = calc(5)

#Precision upto to two decimal points
print("Area: {:.{}f}".format(area, 2))
print("Circumference: {:.{}f}".format(circum, 2))
