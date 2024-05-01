age = int(input("Enter your age: "))
day = input("Enter the day: ")


price = 12 if age >= 18 else 8
price = price - 2 if day == "Wednesday" else price

print(price)