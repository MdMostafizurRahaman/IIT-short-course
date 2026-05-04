def fizz_buzz(n):
    output_list = []
    
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Check if divisible by BOTH 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            output_list.append("FizzBuzz")
        # Check if divisible by 3 only
        elif i % 3 == 0:
            output_list.append("Fizz")
        # Check if divisible by 5 only
        elif i % 5 == 0:
            output_list.append("Buzz")
        # If none of the above, just add the number itself
        else:
            output_list.append(str(i))
            
    # Join all the items in the list with a comma and a space
    print(", ".join(output_list))

# Testing the function with n = 15
fizz_buzz(15)