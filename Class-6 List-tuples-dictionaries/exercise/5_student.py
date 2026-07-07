# Create a dictionary holding dictionaries
students_db = {
    "student_1": {
        "name": "Alice", 
        "id": 101, 
        "department": "CSE"
    },
    "student_2": {
        "name": "Bob", 
        "id": 102, 
        "department": "EEE"
    }
}

# Loop through and print all information
for student_key, info in students_db.items():
    print(f"--- Info for {student_key} ---")
    print(f"Name: {info['name']}")
    print(f"ID: {info['id']}")
    print(f"Department: {info['department']}\n")

for student_key, info in students_db.items():
    print(f"--- Info for {student_key} ---")
    for key, value in info.items():
        print(f"{key} => {value}")
    print()
print(students_db)