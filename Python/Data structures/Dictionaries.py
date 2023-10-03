#Dictionaries are similar to Java maps
# KEY - VALUE


student_dictionary = dict()

student_dictionary ["AAAA"] = "Michel"
student_dictionary ["BBBB"] = "Second"
student_dictionary ["CCCC"] = "Third"


print(student_dictionary)

for key in student_dictionary.keys():
    print(key, end=" : ")
    print(student_dictionary[key])