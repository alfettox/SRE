import numpy as np

array_1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(array_1)

normalArray = [0,1,2,3,4,5,6,7,8,9]
print(normalArray)


#Multiplications
list_1 = [1,2,3]
array = np.array(list_1)
list_2 = list_1 * 4
array_4 = array * 4

print(list_2)
print(array_4)



#multidimensional arrays


arrayMulti = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

print(arrayMulti)

arrayMulti = 2 * arrayMulti

print(arrayMulti)
print(arrayMulti.shape)

print(arrayMulti.reshape(4,3))


#create empty array
arr_zeroes = np.zeros((2, 3))
print(arr_zeroes)