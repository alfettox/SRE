# TUPLE IS IMMUTABLE, cannot add remove or reassign

age_range = (10, 120)
print(age_range)
print(type(age_range))

info = ("Maria", "Smith", 31, "131 Street")
print(info)
print(type(info))

filtered_info_tuple = tuple(x for x in info if x != "Smith")
filtered_info_list = list(x for x in info if x != "Smith")
print(filtered_info_list)
print(filtered_info_tuple)

print(len(filtered_info_list))
print(len(filtered_info_tuple))

#slicing tuples
myTuple = ("Jonathan", "Vance", "3434 Rue de chambly", "QC")

print(f"The name is: {myTuple[0]}")

print(f"The address is: {myTuple[2:]}")