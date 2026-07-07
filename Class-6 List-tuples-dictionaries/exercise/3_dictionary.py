# Create dictionary for a student
student = {
    "name": "John Doe",
    "id": 105,
    "marks": 65
}

# Check condition and add the "result" key
if student["marks"] >= 40:
    student["result"] = "Pass"
else:
    student["result"] = "Fail"

print(student)