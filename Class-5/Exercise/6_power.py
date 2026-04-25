base = int(input("Enter a base number: "))
power = 1
result = base

while result <= 1000:            # Condition: Stop when the result exceeds 1000
    print(f"{base} to the power {power} is {result}")
    power = power + 1            # Increment the power
    result = base ** power       # Update the result using the exponentiation operator (**)