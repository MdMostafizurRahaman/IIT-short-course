text = "Python"
#      P y t h o n
#      0 1 2 3 4 5  (forward indexing)
#     -6-5-4-3-2-1  (backward indexing)

print(text[0])    # P (first character)
print(text[3])    # h (fourth character)
print(text[-1])   # n (last character)
print(text[-3])   # h (third from the end)


# s = "Hello"
# s[0] = "J"  # This will raise - TypeError: 'str' object does not support item assignment

# # CORRECT WAY
# s = "Hello"
# s = "J" + s[1:]
# print(s)  # Output: Jello


text = "Python"
#      P y t h o n
#      0 1 2 3 4 5
#     -6-5-4-3-2-1  (backward indexing)

print(text[0:3])  # Pyt (positions 0,1,2 - stops before position 3)
print(text[2:])   # thon (from position 2 to the end)
print(text[:4])   # Pyth (from the beginning up to position 4)
print(text[-4:-1]) # tho (using negative indices)