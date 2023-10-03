age = input("Enter your age")



try:
    age = int(age)
    if age < 18:
        print("You are underage")
    elif age == 18:
        print("You are 18 yo")
    else:
        print("You are an adult")
except ValueError as errorType:
    print("invalid input please try again. ERROR:" + str(errorType))
