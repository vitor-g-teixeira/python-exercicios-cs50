import validators

validation = validators.email(input("What is your email address? "))

if validation:
    print("Valid")
else:
    print("Invalid")
