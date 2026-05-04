def factorial(n):
    # Factorial of 0 or 1 is always 1
    result = 1
    
    # Loop from 1 up to the number 'n'
    for i in range(1, n + 1):
        result = result * i  # Multiply the current result by the loop number
        
    return result

# Testing the function
print(factorial(5))  # Output: 120