s1 = 'Hello'
s2 = "World"
s3 = '''This is
a multi-line
string'''

print(type(s1))  # <class 'str'> - This tells us s1 is a string
print(s1 + " " + s2)  # Hello World - We can combine strings
print(s3)  # Prints the multi-line text exactly as written

text = "Hello World"
print(len(text))  # 11 (H-e-l-l-o-space-W-o-r-l-d = 11 characters)

word = "    Python          "
print(word.strip())          # 'Python' - Removed spaces from both sides

sentence = "\n\n\n Hello World \t"  # \n = new line, \t = tab
print(sentence.strip())      # 'Hello World' - Cleaned up the text


