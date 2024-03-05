# a simple number guessing game
guess = int(input("Guess the number (between 1 and 100): "))
secret_number = 56

# Check if the guess is correct
if guess == secret_number:
    print(f"Congratulations! You guessed the correct number: {secret_number}")
else:
    # Provide a hint and let the user know if their guess was too high or too low
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
