num = 0

while num < 10:
    num = num + 1                # Increment first
    
    if num % 3 == 0:             # Check if the number is a multiple of 3
        print(f"Skipping {num} (multiple of 3)")
        continue                 # Skip the rest of the code and go back to the top of the loop
        
    print(f"Processing {num}")