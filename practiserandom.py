def code(num):
    def actual(x):
        return x ** num
    return actual

f = code(2)
print(f(3))
