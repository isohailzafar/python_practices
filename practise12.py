number = int(input("Enter a number: "))
sum = 0
for n in range(1, number + 1):
    if n % 2 == 0:
        sum = sum + n

print(sum)