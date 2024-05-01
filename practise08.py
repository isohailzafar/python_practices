password = input("Enter passowrd: ")

if len(password) < 6:
    eligibility = "Weak"

elif len(password) <= 10:
    eligibility = "Medium"

else:
    eligibility = "Strong"

print(eligibility, "Password")