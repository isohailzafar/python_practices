distance = int(input("Enter distance in km: "))

if distance <= 3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
else:
    mode = "Car"

print(mode)