number = 1

while number <= 20:
    square = number * number
    print(f"{number} squared is {square}")
    
    if square > 100:             # Check if the square value exceeds 100
        print("Found first square greater than 100!")
        break                    # Instantly exit the loop
        
    number = number + 1