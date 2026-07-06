import os

if os.path.exists("original.txt"): 
    with open("original.txt", "r") as source:
        content = source.read()
        
    with open("backup.txt", "w") as dest: 
        dest.write(content) 
    print("Backup created successfully.")
else:
    print("File not found")