total = 0
number = 1                       # Initialized with 1 just to start the loop

print("Enter numbers to add (enter 0 to stop):")

while number != 0:               # Condition: Stop the loop if user enters 0
    number = int(input("Enter a number: "))
    
    if number != 0:              # Only add if the number is not 0
        total = total + number
        print(f"Running total: {total}")

print(f"Final sum: {total}")