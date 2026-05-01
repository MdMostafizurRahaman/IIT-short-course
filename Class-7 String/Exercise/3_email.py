email = input("Enter your email address: ")

if email.endswith("@gmail.com"):
    print("Gmail account detected")
else:
    print("Other email provider")