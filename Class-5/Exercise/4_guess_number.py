secret_number = 7
guess = 0

print("Guess the secret number!")

while guess != secret_number:    # Condition: Loop continues until the guess is correct
    guess = int(input("Your guess: "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("Congratulations! You guessed it right!")