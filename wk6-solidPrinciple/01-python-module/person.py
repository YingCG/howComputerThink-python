class Person:
    def __init__(self, name, password=None):
        self.name = name
        self.password = password

    def greet(self):
        print(f"Hello, {self.name}!")

    def login(self):
        try:
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
                print("Nothing here...")
        except ValueError as e:
            print(f"Login failed: {e}")
