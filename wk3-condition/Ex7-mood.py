current_mood = "Happy"
previous_mood = "Grumpy"

# Take user input to decide whether to upgrade the mood
upgrade_mood = input("Do you want to upgrade your mood? (yes/no): ").lower()

# # Conditional upgrade using if-else statement and assignment operator
if upgrade_mood == "yes":
    current_mood += " and Excited"
    print(f"Today, I'm feeling {current_mood}. That's a major mood assignment upgrade!")
else:
    print(f"Today, I'm feeling {current_mood}. No mood upgrade.")