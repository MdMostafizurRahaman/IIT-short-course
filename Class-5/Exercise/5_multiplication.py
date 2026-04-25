import random                    # Module to generate random numbers

correct_answers = 0
keep_playing = True              # Flag to control the loop

while keep_playing:
    num1 = random.randint(1, 10) # Generate a random number between 1 and 10
    num2 = random.randint(1, 10)
    
    answer = int(input(f"What is {num1} x {num2}? "))
    
    if answer == (num1 * num2):
        print("Correct!")
        correct_answers = correct_answers + 1
    else:
        print("Wrong!")
        keep_playing = False     # Set flag to False to exit the loop

print(f"Game Over! You got {correct_answers} right.")