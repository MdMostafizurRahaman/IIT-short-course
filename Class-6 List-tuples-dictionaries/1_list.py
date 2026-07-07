# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]

#print list
print(fruits)

# Accessing items
print(fruits[0])             # Output: apple (first item)
print(fruits[1]) 
print(fruits[2]) 
#print(fruits[3]) 
print(fruits[-1])            # Output: cherry (last item)
print(fruits[-2]) 
print(fruits[-3]) 
#print(fruits[-4]) 

# Modifying lists (Adding and removing)
fruits[1] = "orange"         # Change banana to orange
print(fruits)

fruits.append("mango")       # Add mango at the end of the list
print(fruits)

fruits.insert(1, "grape")
print(fruits)

fruits.remove("apple")       # Remove apple from the list
print(fruits)                # Final list output

del fruits[0]
print(fruits)

for fruit in fruits:
    print(fruit)


# Build in function and slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Length: {len(numbers)}")
print(f"Summation: {sum(numbers)}")

# Slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = numbers[1:4]  #Slicing from index 1 to 3 (4 is exluded)
print(f"Sublist of specific range: {sublist}")

sublist_start = numbers[:4]
print(f"Sublist without starting: {sublist_start}")

sublist_end = numbers[4:]
print(f"Sublist without ending: {sublist_end}")

# Negative index slicing
sublist_neg = numbers[-4: -1]
print(f"Negative sublist: {sublist_neg}")

