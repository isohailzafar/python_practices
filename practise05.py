weather = input("1.Sunny\n2.Rainy\n3.Snowy\nEnter your weather type as mentioned above: ")

if weather.lower() == "sunny":
    print("Go for a walk")
elif weather.lower() == "rainy":
    print("Read a book")
elif weather.lower() == "snowy":
    print("Make a snowman")