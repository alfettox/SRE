import os

currDir = os.path.abspath(os.path.dirname(__file__))

for file_name in os.listdir(currDir):
    print(file_name)

with open("new_file.txt", "w") as f:
    f.write("This is a line of text")
    f.write("This is another line of text")