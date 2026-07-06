import os

folder_name = "documents" 

if os.path.exists(folder_name):
    files = os.listdir(folder_name)
    print("Text files in documents folder:")
    for file in files:
        if file.endswith(".txt"):
            print(file)
else:
    print("The documents folder does not exist.")