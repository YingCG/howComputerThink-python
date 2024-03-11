current_mode = "Happy"
previous_mode = "Grumpy"
grocery_bag = ["apple", "kiwi", "lolly", "ice-cream"]

# upgrade your mode
current_mode += " and Excited"
print(f"Today, I'm feeling {current_mode}. That's is a major mood upgrade!")

mode = input("Are you feeling happy now?").lower()
if current_mode != "Happy":
    snack = input("Any snack you like?")
    if "chocolate" in grocery_bag:
        print(
            "There is no chocolate! I hope you feeeling better with other snack anyway"
        )
    else:
        print("Found chocolate in the bag! Keep smiling...")
print("I hoep you have a good day")
