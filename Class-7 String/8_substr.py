text = "Hello World"

print(text.find("World"))  # 6 (the word "World" starts at position 6)
print(text.find("Python")) # -1 (not found - Python returns -1 when searching fails)

# This is useful for checking if something exists before trying to work with it.
# Confused seeing 'if'? Don't worry, we will learn it clearly in upcoming lectures
if text.find("World") != -1:
    print("Found 'World' in the text!")