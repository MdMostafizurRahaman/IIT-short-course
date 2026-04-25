total = 0
user_input = 0

while user_input != -1:          # Condition: Stop if the user inputs -1
    user_input = int(input("Enter a positive number (or -1 to stop): "))
    
    if user_input > 0:           # Only add the number if it is positive
        total = total + user_input

print(f"Final sum is: {total}")