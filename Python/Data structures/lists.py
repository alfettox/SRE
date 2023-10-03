list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_of_numbers)

print(type(list_of_numbers))

print(list_of_numbers[:-1])

print(f"Length: {len(list_of_numbers)}")


# addint to the list of numbers

list_of_numbers.append(99)
print(list_of_numbers)

# insert in  a specific position, it replace the current element

list_of_numbers[0] = 55
print(list_of_numbers)


# push forward when a new item is inserted
list_of_numbers.insert(0, 777)
print(list_of_numbers)

# remove items from the list, shifts everything
list_of_numbers.remove(777)
print(list_of_numbers)

input_list = ["Haythem", "Mike", 1, "Layla", "Livia",
              "Layla", 2, 1, 2, 3, "Mike", "Jesse", "Haythem"]

# removes just the first item with the specified name
# input_list.remove("Layla")
# print(input_list)

# remove all the occurencies of Layla

input_list = [x for x in input_list if x != "Layla"]
print(input_list)
