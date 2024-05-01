#Recursion is basically calling of function itself and the main problem is how to get out of it
#there must be a check at some point to get out the infinite loop in which the function is stucked

def factorial(n):
    #exit staraegy
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))