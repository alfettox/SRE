#SETS ARE LIKE hashset
# they use {}, not indexed random order, no diplicates


names = {'Gianni', 'Pinotto', 'Stanlio', 'Ollio'}

for x in range(0,5):
    print(names)


print(names)

names.add("Genoveffa")

print(names)
names.remove('Pinotto')
print(names)

names.add("Gianni")


#add multiple items

setA = {0,1,2,3,4}

setB = {5,6,7,8,9}

setA.update(setB)

print(setA)

#DISCARD NO ERROR IF ELEMENT NOT EXISTS -  REMOVE  RAISE error

# setA.remove("Merveille")
setA.discard("Marco")

setA.clear()

print(setA)

print(setB)
setB.pop()
print(setB)

print(setB)
del setB

# print(setB)


#DIFFERENCE BETWEEN SETS
shake_1 = {"kiwi", "banana", "peanut butter"}
shake_2 = {"banana", "kiwi", "spinach"}
shake_3 = shake_1.difference(shake_2)

print(shake_3)

#INTERESECT
intersectShake = shake_1.intersection(shake_2)
print(intersectShake)

#UNION
unionOfShakes = shake_1.union(shake_2)
print(unionOfShakes)