# Creating a tuple
info = ("Alice", 25, "Engineer")

# Accessing items works just like lists
print(info[0])               # Output: Alice

# Access through loop
print("List: ")
for item in info:
    print(item)

# Packing and Unpacking (Distributing tuple items into variables)
person = ("Bob", 30, "Doctor")    # Packing
name, age, job = person           # Unpacking

print(name)                  # Output: Bob
print(job)                   # Output: Doctor

dob = ("2002", "April", "26")
for item in dob:
    print(item)

year, month, date = dob

print(year)
print(month)
print(date)