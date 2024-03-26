class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    def login(self, entered_password):
        if entered_password != self.password:
            raise ValueError("Incorrect password")
        print(f"Welcome, {self.username}!")
