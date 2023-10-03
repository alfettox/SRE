list_of_names = ["Kate", "Jennifer", "Mike", "Pete", "Alex", "Mike", "Kate"]
name = "Kate"

if name in list_of_names:
    print(f"{name} is in the list {list_of_names}")


for list_name in list_of_names:
    if name == list_name:
        print(f"{name} has been found")


#searching a string

myString = "Hello my name is Giovanni"

for x in myString:
    if x == "a":
        print(f"The letter {x} has been found")