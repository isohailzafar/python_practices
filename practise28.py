def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name = "Sohail Zafar", power = "Hardword")
print_kwargs(power = "Hardword")
print_kwargs(name = "Sohail Zafar")
print_kwargs(power = "Hardword",name = "Sohail Zafar",  age = 21)
