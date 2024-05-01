number = int(input("Enter a number to calculate factorial: "))
i = 1
fact = 1
while (i <= number):
    fact = fact * i
    i = i + 1

print(fact)

# OR another method is

while (number > 0):
    fact = fact * number
    number = number - 1

print(fact)