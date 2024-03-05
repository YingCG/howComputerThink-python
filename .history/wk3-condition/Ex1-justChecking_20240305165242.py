# get user input for conditions
is_sunny = input("Is it sunny today? (Y for yes, N for no)")

# Check if the person is in a good mood
if is_sunny == "y":
    print("Enjoy your sunshine")
else:
    print("Don't forget to bring umbrella with you! Have a good day anyway")


# check if it is a weekend
is_friday = input("Is it Friday Yet? (Y for yes, N for no) ")
if is_friday and is_sunny:
    print("Let's go to the beach!")
elif is_friday:
    print("It's Friday! Plan something exciting for the weekend!")
else:
    print("Join us for a cuppa!")


# check if user want a coffee with nested if else
want_coffee = input("Do you like a coffee? (Y for yes, N for no)")
if want_coffee == "y" and is_sunny:
    cold = input("Would you like it hot or cold? (h / c)").lower()
    if cold != "h":
        print("Here is your ice-coffee")
    else:
        print("Here is your warm coffee")
else:
    print("See you soon")
