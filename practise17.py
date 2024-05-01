num = int(input("Enter a number: "))

if (num > 1 and num < 10):
    print("You have entered the right number!")
else:
    while (num < 1 or num > 10):
        num = int(input("Enter a number between 1 and 10 please: "))
        if (num > 1 and num < 10):
            print("You have entered the right number!")
    
# or another method is 

while True:
    number = int(input("Enter value b/w 1 and 10: "))

    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid entry!")