import os

# Create a new directory in the current folder

currDir = os.path.dirname(__file__)

newDir = input("please insert the name of the new directory")

newDirPath = os.path.join(currDir, newDir)

if not os.path.exists(newDirPath):
    os.mkdir(newDirPath)
else:
    print("already exists")

if os.path.exists(newDirPath):
    os.rmdir(newDirPath)
