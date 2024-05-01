pet_specie = input("Enter pet specie: ")
age = int(input("Enter pet age: "))

if pet_specie.lower() == "dog":
    if age < 2:
        food = "Puppu food"
    else:
        food = "Adult food"

elif pet_specie.lower() == "cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Junior cat food"

else:
    print("Invalid Specie")
    exit()

print(food)