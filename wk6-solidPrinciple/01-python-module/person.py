class Person:
    def __init__(self, name, password=None):
        self.name = name
        self.password = password

    def greet(self):
        print(f"Hello, {self.name}!")

    def login(self):
        try:
            if self.password is not None:
                entered_password = input(f"{self.name}, please enter your password: ")
                if entered_password != self.password:
                    print("Incorrect password")
                    return
            print(f"Welcome, {self.name}!")
        except ValueError as e:
            print(f"Login failed: {e}")
