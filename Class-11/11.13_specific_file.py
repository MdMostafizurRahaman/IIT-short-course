import os

files = os.listdir(".")
python_files = []

for file in files:
    if file.endswith(".py"):
        python_files.append(file)
        print("Python file found!!!")

for file in python_files:
    print(file)

