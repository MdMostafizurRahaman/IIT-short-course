# Creating a dictionary using curly braces {}
student = {
    "name": "Alice",         # "name" is Key, "Alice" is Value
    "age": 22,
    "grade": "A"
}

# Accessing values using keys
print(f"Name: {student["name"]}")       # Output: Alice
print(f"Age: {student.get("age")}")

# Accessing non existing key
# print(student["id"])
# print(f"Non existing key: {student.get("id")}")

# Adding or updating a key-value pair
student["age"] = 23          # Updates age to 23
student["email"] = "alice@test.com"  # Adds a new key called email

print("Loop using key:")
for key in student:
    print(key)

print("Loop using value:")
for value in student.values():
    print(value)

# Looping through a dictionary
for key, value in student.items():
    print(f"{key} => {value}")

del student["email"]
print("After deleting email:")
for key, value in student.items():
    print(f"{key} => {value}")