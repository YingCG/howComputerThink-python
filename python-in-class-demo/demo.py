"""
name = "who"
dowhat = "eating"
# print(name + dowhat)
print(name + "is blablalb" + dowhat)
print(f"{name} is blablalb {dowhat} ")

"""

# check if sunny
is_sunny = input("Is that raining? (Y or N)").lower()

# check if user in good mode
current_mode = input("Are you happy? (Y or N)").lower()

if is_sunny != "y":
    print("Enjoy your sunshine")

    # check if it is a weekend
    is_friday = input("Is it Friday Yet? (Y for yes, N for no)").upper()
    if is_friday and is_sunny:
        print("Let go to the beach!")

    elif is_friday or current_mode:
        print("It's is Friday! Plan something exciting for the weekedn!")
    else:
        print("Join us for a cuppa!")
print("Keep smiling anyway")
