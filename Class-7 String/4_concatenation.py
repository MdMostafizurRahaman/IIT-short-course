first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe



# s = "Age: "
# n = 30
# # This would cause an error because you can't directly join text and numbers
# print(s + n)  # TypeError: can only concatenate str (not "int") to str


# s = "Age: "
# n = 30
# print(s + str(n))  # Age: 30 - n is first converted into string, 30 becomes '30',
#                    # then it is concatenated.