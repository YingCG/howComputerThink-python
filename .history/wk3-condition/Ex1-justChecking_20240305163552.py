# get user input for conditions
is_sunny = input("Is it sunny today? (Y for yes, N for no)")

# Check if the person is in a good mood
if is_sunny == "y":
    print("Enjoy your sunshine")
else:
    print("Don't forget to bring umbrella with you! Have a good day anyway")

# get user input for conditions
want_coffee = input("Do you like a coffee? (Y for yes, N for no)")
if want_coffee == "y" and is_sunny:
    cold = input("Would you like it hot or cold? (h / c)")
    if cold != "h":
        print("Here is your ice-coffee")
    else:
        print("Here is your coffee")
# is_weekend = input("Is it Friday Yet? (Y for yes, N for no) ")
