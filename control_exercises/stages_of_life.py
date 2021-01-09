try_again = True
while try_again:
    age = int(input("How old are you?: "))
    if age < 2:
        print(f"You are {age} year old and you are a baby")
    elif age < 4:
        print(f"You are {age} years old and you are a toddler")
    elif age < 13:
        print(f"You are {age} years old and you are a kid")
    elif age < 20:
        print(f"You are {age} years old and you are a teenager")
    elif age < 65:
        print(f"You are {age} years old and you are an adult")
    elif age >= 65:
        print(f"You are {age} years old and you are an elder")
    try_continue = input("Do you want to play again (yes/no): ")
    if try_continue.lower() == "no":
        try_again = False
