# List representing days of the week
days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# Get user input for the day
user_day = input(
    "Enter the day of the week: "
).capitalize()  # Capitalize the first letter for consistency

# Check if the entered day is within the range of Monday to Sunday
if user_day in days_of_week:
    day_index = days_of_week.index(user_day)

    if day_index < 5:  # Monday to Friday
        print(f"{user_day} is a weekday.")
    elif day_index == 5:  # Saturday
        print(f"{user_day} is a Saturday. Enjoy the weekend!")
    else:  # Sunday
        print(f"{user_day} is a Sunday. Relax and recharge for the upcoming week.")
else:
    print("Invalid day. Please enter a valid day of the week.")
