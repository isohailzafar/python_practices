# def generator(num):
#     for i in range(2, num + 1,2):
#             print("Even:", i)

# # Return ends after returning one time
# def generator(num):
#     for i in range(2, num + 1,2):
#             return i


# def generator(num):
#     li = []
#     for i in range(2, num + 1,2):
#             li.append(i)
#     return li


#yeild means not returning
def generator(num):
    for i in range(2, num + 1,2):
            yield i #HOLD smething in the memory and then start after the first one an can be accessed by loop

for i in generator(10):
    print(i)
