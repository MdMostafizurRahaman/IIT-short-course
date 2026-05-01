sentence = "Python is easy to learn"
words = sentence.split()  # Split at spaces (default behavior)
print(words)  # ['Python', 'is', 'easy', 'to', 'learn'] - Now it's a list!

# You can specify what to split on
csv = "apple,banana,cherry"
fruits = csv.split(",")  # Split at each comma
print(fruits)  # ['apple', 'banana', 'cherry']