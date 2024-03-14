import time

my_timer = int(input("Entere the time in seconds:"))


# Define function
def countdown_timer(seconds):
    for sec in range(my_timer, 0, -1):
        remaining_seconds = sec % 60
        remaining_minutes = int(sec / 60) % 60
        remaining_hours = int(sec / 3600)
        print(f"{remaining_hours:02}:{remaining_minutes:02}:{remaining_seconds:02}")
        time.sleep(1)
        print("Show Start!")
        
# # Get user input for time
user_time = int(input("Enter the time in seconds: "))
# # Call the function with user input
countdown_timer(user_time)