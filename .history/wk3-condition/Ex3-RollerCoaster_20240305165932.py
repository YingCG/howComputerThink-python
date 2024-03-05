# minimum height 120cm
# under 12 years old ticket price $5
# under 18 years old ticket price $7
# over 18 years old ticket price $12
# photo take $3

print("Welcome to the roller costal")
height = float(input("Let's measure your height (cm): "))

if height >= 120:
    bill = 0
    print("Child ticket are $5 \nYouth ticket are $7 \nAdult tickets are $12 \n")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    photo_taken = input("Do you want a photo taken? Y or N ")
    if photo_taken.lower() == "y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("You have to grow taller before you can take a ride ")

# a simple number guessing game
guess = int(input("Guess the number (between 1 and 100): "))

# Check if the guess is correct
if guess == secret_number:
    print(f"Congratulations! You guessed the correct number: {secret_number}")
else:
    # Provide a hint and let the user know if their guess was too high or too low
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
