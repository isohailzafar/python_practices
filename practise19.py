items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) == 2:
        print(item)
        break

#Or another method to do this is
unique_set = set()

for item in items:
    if item in unique_set:
        print("Dublicate:", item)
        break
    unique_set.add(item)