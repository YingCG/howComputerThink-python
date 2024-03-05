# this is a username and password verification system

# initiate variable for username and password
admin = "Sesame"
secret = "secret101"

# get user input for username and password
username = input("Enter your name: ")
password = input("Enter your password: ")

# Check if entered username and password matching
if username == admin and password == secret:
    print("Sesame door is opening. All the treasures are still here!")
else:
    print("Notthing here...")
