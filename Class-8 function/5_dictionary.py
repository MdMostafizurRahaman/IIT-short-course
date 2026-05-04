# Function returning multiple pieces of data packed inside a dictionary
def get_user_info():
    return {
        "name": "Alice",
        "age": 22,
        "department": "BBA"
    }

# Storing and accessing the returned dictionary
user_data = get_user_info()
print("Student Name:", user_data["name"])
print("Department:", user_data["department"])