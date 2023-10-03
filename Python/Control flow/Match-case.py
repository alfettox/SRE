value = "Hello"

match value.lower():
    case "hello":
        print("value is hello")
    case "goodbye":
        print("value is goodbye")
    case _:
        print("I don't know")


x = 5

match x:
    case 1 | 2 | 3:
        print("The value of x is between 1 and 3")
    case 4 | 5 | 6:
        print("The value is between 4 and 6")
    case _:
        print('The value of x is something else')

y = 2

if y in (1, 2, 3):
    print("The value of y is between 1 and 3")
elif y in (4, 5, 6):
    print("The value of y is between 4 and 6")
else:
    print('The value of y is something else')

score = 22

match score:
    case s if s >= 90:
        print ("You got an A")
    case s if 80 <= s < 90:
        print ("You got a B")
    case s if 60 < s < 80:
        print("you got less than b")
    case _:
        print("Not a good score")

