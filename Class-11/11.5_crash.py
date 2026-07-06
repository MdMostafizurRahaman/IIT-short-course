file = open("nofile.txt", "r")
content = file.read()
print(content) 
file.close() 
print("The file does not exist.")

print("something interesting") 