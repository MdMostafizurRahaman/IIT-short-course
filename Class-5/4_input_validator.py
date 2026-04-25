number = -1                      # Start with an invalid (negative) number

while number <= 0:               # Condition: Keep asking if the number is 0 or negative
    number = int(input("Enter a positive number: "))
    
    if number <= 0:
        print("Error: Number must be positive!")

print(f"Thank you! You entered: {number}")