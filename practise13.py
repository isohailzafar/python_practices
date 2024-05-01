number = int(input("Enter a number: "))

for i in range(1, 11):  
    if i == 5:
        continue
    else:
        mul = number * i
        print(number, "x" , i, "=", mul)