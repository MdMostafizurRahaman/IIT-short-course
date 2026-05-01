password = input("Enter a password: ")

# Creating tuples with all letters and digits to use as options in startswith/endswith
letters = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = tuple("0123456789")

# Checking conditions
valid_start = password.startswith(letters)
valid_end = password.endswith(numbers)

if valid_start and valid_end:
    print("Valid password")
elif valid_start and not valid_end:
    print("Valid start but invalid end")
elif not valid_start and valid_end:
    print("Valid end but invalid start")
else:
    print("Invalid password")

# letters_list = ['a', 'b', 'c']
# print("apple".startswith(letters_list))