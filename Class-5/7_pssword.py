correct_password = "python123"
user_password = ""               # Start with an empty password

while user_password != correct_password:  # Condition: Run until passwords match
    user_password = input("Enter the password: ")
    
    if user_password != correct_password:
        print("Wrong password! Try again.")

print("Access granted!")         # Executes only when the correct password is provided