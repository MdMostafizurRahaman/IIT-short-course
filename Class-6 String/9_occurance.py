text = "banana"

print(text.count("a"))   # 3 (the letter 'a' appears 3 times)
print(text.count("na"))  # 2 (the sequence 'na' appears 2 times)

# This is useful for analysis or validation
password = "password123"
if password.count("1") > 0:
    print("Password contains at least one '1'")