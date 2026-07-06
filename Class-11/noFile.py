try:
    file = open("nofile.txt", "r")
    content = file.read()
    print(content) 
    file.close() 
except FileNotFoundError:
    print("The file does not exist.")
print("something interesting") 
