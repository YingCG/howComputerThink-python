class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, entered_password):
        if entered_password != self.password:
            raise ValueError("Incorrect password")
        print(f"Welcome, {self.username}!")
