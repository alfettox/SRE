import json
import os

person = {
    'name': "John",
    'age': 30,
    'city': "Montreal"
}

person_json = json.dumps(person)  # Serialize the dictionary to a JSON string

# SAVE TO JSON FILE
currDir = os.path.abspath(os.path.dirname(__file__))
completePath = os.path.join(currDir, "new_file.txt")
with open(completePath, "w") as f:
    f.write(person_json)

print(person_json)
print(type(person_json))

decoded_person = json.loads(person_json)        #BACK TO DICTIONARY FROM STR JSON
print(decoded_person)
print(type(decoded_person))
